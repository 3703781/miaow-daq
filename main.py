"""
BY: Miaow, Wanderson M.Pimenta
PROJECT MADE WITH: Qt Designer and PySide6
V: 1.0.0

This project can be used freely for all uses, as long as they maintain the
respective credits only in the Python scripts, any information in the visual
interface (GUI) can be modified without any implication.

There are limitations on Qt licenses if you want to use your products
commercially, I recommend reading them on the official website:
https://doc.qt.io/qtforpython/licenses.html
"""

import sys
import os
import time
from threading import Thread, Event

import numpy as np
import pyqtgraph
import pyqtgraph.exporters as exporters

from modules import *
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QHeaderView, QMessageBox, QCheckBox
from PySide6.QtCore import Qt, Signal, QTimer
from PySide6.QtGui import QIcon, QIntValidator, QPen, QColor
from daq.DataAcquisition import DataAcquisitionDevice
from modules.ui_main import Ui_MainWindow
import json

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%


class MainWindow(QMainWindow):
    daq_connect_signal = Signal()
    daq_stop_signal = Signal(bool)  # True为手动停止，False为出错停止
    daq_start_signal = Signal()

    range_dict = {"-10V ~ +10V": "+10v~-10v", "-5V ~ +5V": "+5v~-5v"}
    os_dict = {"None - 1x": 1, "Up - 2x": 2, "Up - 4x": 4, "Up - 8x": 8, "Up - 16x": 16, "Up - 32x": 32, "Up -64x": 64}
    trig_dir_dict = {"Rising Edge": "rising", "Falling Edge": "falling", "Both": "both"}
    trig_mode_dict = {"Internal": "internal", "Switch & Internal": "both"}

    range_dict_rev = {"+10v~-10v": "-10V ~ +10V", "+5v~-5v": "-5V ~ +5V"}
    os_dict_rev = {1: "None - 1x", 2: "Up - 2x", 4: "Up - 4x", 8: "Up - 8x", 16: "Up - 16x", 32: "Up - 32x", 64: "Up -64x"}
    trig_dir_dict_rev = {"rising": "Rising Edge", "falling": "Falling Edge", "both": "Both"}
    trig_mode_dict_rev = {"internal": "Internal", "both": "Switch & Internal"}

    def __init__(self):
        super().__init__()
        # ===prepare data===
        self.channels = 8  # channel count of self.daq
        self.need_close_event = Event()  # before exit the app, set this event to stop acquisition and disconnect from daq device
        self.daq = DataAcquisitionDevice()  # wrap the daq device
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        UIFunctions.uiDefinitions(self)  # set ui, e.g. title bar, grip & resize, min/max/close
        self.channel_select_list = [1, 2, 3, 4, 5, 6, 7, 8]  # channels that need to be show when first plotting, depends on the performance of your computer
        self.total_sample_data = np.zeros((10, 8))  # placeholder data
        self.total_sample_count = 10  # placeholder data
        self.data_timer = QTimer()  # read fifo in daq driver during acquisition at regular intervals

        # ===buttons on left menu bar===
        self.ui.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        self.ui.btn_home.clicked.connect(self.menu_btn_clicked)
        self.ui.btn_settings.clicked.connect(self.menu_btn_clicked)
        self.ui.btn_chart.clicked.connect(self.menu_btn_clicked)
        self.ui.btn_table.clicked.connect(self.menu_btn_clicked)
        self.ui.settingsTopBtn.clicked.connect(lambda: UIFunctions.toggleRightBox(self, True))
        self.ui.btn_start.clicked.connect(self.btn_start_clicked)
        self.ui.btn_start.is_started = False

        # ===plot page===
        self.ui.glw_detail.setBackground("#282c34")
        self.ui.glw_detail.ci.setContentsMargins(0, 0, 0, 0)
        self.ui.glw_overall.setBackground("#282c34")
        self.ui.glw_overall.ci.setContentsMargins(0, 0, 0, 0)

        self.plot_item_detail = self.ui.glw_detail.addPlot()
        self.plot_item_detail.setMenuEnabled(False)
        self.plot_item_detail.showGrid(x=True, y=True)
        self.plot_item_detail.addLegend(horSpacing=20, offset=(1, 1), colCount=4, labelTextSize="7pt")
        self.plot_item_overall = self.ui.glw_overall.addPlot()
        self.plot_item_overall.setMenuEnabled(False)
        self.plot_item_overall.showAxes(False, showValues=False)
        self.plot_item_overall.setMouseEnabled(x=False, y=False)

        self.pen_list = [pyqtgraph.mkPen(color=QColor.fromHsv(int(i), 50, 255), width=1) for i in np.linspace(0, 360, self.channels + 1)][:-1]
        self.curve_detail_list, self.curve_overall_list = [], []
        self.curve_detail_list = [self.plot_item_detail.plot(name=f"Channel {i + 1}", pen=pen) for i, pen in enumerate(self.pen_list)]
        self.curve_overall_list = [self.plot_item_overall.plot(name=f"Channel {i + 1}", pen=pen) for i, pen in enumerate(self.pen_list)]
        self.pg_region = pyqtgraph.LinearRegionItem()
        self.pg_region.setZValue(10)
        self.plot_item_overall.addItem(self.pg_region, ignoreBounds=True)

        self.pg_region.sigRegionChanged.connect(lambda: self.plot_item_detail.setXRange(*self.pg_region.getRegion(), padding=0))
        self.plot_item_detail.sigRangeChanged.connect(lambda window, viewRange: self.pg_region.setRegion(viewRange[0]))
        self.ui.cb_ch1.stateChanged.connect(self.cb_ch_state_changed)
        self.ui.cb_ch2.stateChanged.connect(self.cb_ch_state_changed)
        self.ui.cb_ch3.stateChanged.connect(self.cb_ch_state_changed)
        self.ui.cb_ch4.stateChanged.connect(self.cb_ch_state_changed)
        self.ui.cb_ch5.stateChanged.connect(self.cb_ch_state_changed)
        self.ui.cb_ch6.stateChanged.connect(self.cb_ch_state_changed)
        self.ui.cb_ch7.stateChanged.connect(self.cb_ch_state_changed)
        self.ui.cb_ch8.stateChanged.connect(self.cb_ch_state_changed)

        # ===settings page===
        self.ui.le_period.textChanged.connect(self.le_period_text_changed)
        self.ui.le_frequency.textChanged.connect(self.le_frequency_text_changed)
        self.ui.slider_period.valueChanged.connect(self.slider_period_value_changed)
        self.ui.le_cycles.textChanged.connect(self.le_cycles_text_changed)
        self.ui.slider_cycles.valueChanged.connect(self.slider_cycles_value_changed)
        self.ui.pb_load_profile.clicked.connect(self.pb_load_profile_clicked)
        self.ui.pb_save_profile.clicked.connect(self.pb_save_profile_clicked)
        self.ui.pb_save_plot.clicked.connect(self.pb_save_plot_clicked)

        self.ui.le_period.setValidator(QIntValidator(10, 5000, self))
        self.ui.le_period.setValidator(QIntValidator(200, 100000, self))
        self.ui.le_cycles.setValidator(QIntValidator(10, 2097152, self))

        # ===table page===
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.pb_export_table.clicked.connect(self.pb_export_table_clicked)

        # connect signals for self.daq
        self.daq_connect_signal.connect(self.daq_connected_action)  # emit at connecting to the daq device
        self.daq_stop_signal.connect(self.daq_stopped_action)  # emit at btn_start clicked when acquisiting
        self.daq_start_signal.connect(self.daq_started_action)  # emit at btn_start clicked while not acquisiting
        self.data_timer.timeout.connect(self.daq_data_timer_action)


        # set custom theme
        # UIFunctions.theme(self, "themes\py_dracula_light.qss", True)
        # AppFunctions.setThemeHack(self)

        # ===show main window, start at home page with stopped status===
        self.show()
        self.ui.btn_home.click()
        self.daq_stopped_action(False)
        self.load_profile()

    def load_profile(self):
        profile_path = self.ui.le_profile_file.text().strip()
        if profile_path == "":
            profile_path = "./profile.json"
        try:
            with open(profile_path) as f:
                profile = json.load(f)
                profile = profile["daq"]
            self.ui.cb_range.setCurrentText(self.range_dict_rev[profile["range_"]])
            self.ui.cb_trig_mode.setCurrentText(self.trig_mode_dict_rev[profile["trig_mode"]])
            self.ui.cb_trig_dir.setCurrentText(self.trig_dir_dict_rev[profile["trig_dir"]])
            self.ui.cb_os.setCurrentText(self.os_dict_rev[profile["os_"]])
            self.ui.slider_period.setFocus()
            self.ui.slider_period.setValue(profile["period"])
            self.slider_period_value_changed(profile["period"])
            self.ui.slider_cycles.setFocus()
            self.ui.slider_cycles.setValue(profile["cycles"])
            self.slider_cycles_value_changed(profile["cycles"])
        except:
            self.ui.le_profile_file.setText("Load failed. Try again!")

    def save_profile(self):
        profile_path = self.ui.le_profile_file.text().strip()
        if profile_path == "":
            profile_path = "./profile.json"
        profile = {}
        profile["range_"] = self.range_dict[self.ui.cb_range.currentText()]
        profile["trig_mode"] = self.trig_mode_dict[self.ui.cb_trig_mode.currentText()]
        profile["trig_dir"] = self.trig_dir_dict[self.ui.cb_trig_dir.currentText()]
        profile["os_"] = self.os_dict[self.ui.cb_os.currentText()]
        profile["period"] = self.ui.slider_period.value()
        profile["cycles"] = self.ui.slider_cycles.value()
        try:
            with open(profile_path, "w") as f:
                json.dump({"daq": profile}, f, indent=4)
        except:
            self.ui.le_profile_file.setText("Save failed. Try again!")


    def menu_btn_clicked(self):
        btn = self.sender()
        btnName = btn.objectName()

        # show home page
        if btnName == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # show settings page
        if btnName == "btn_settings":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_setting)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # show chart page
        if btnName == "btn_chart":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_plot)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        # show table page
        if btnName == "btn_table":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_table)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

    def cb_ch_state_changed(self):
        cb: QCheckBox = self.sender()
        cb_name = cb.objectName()
        cb_index = int(cb_name[5:])
        d = self.total_sample_data[:, cb_index - 1]
        if cb.isChecked():
            self.channel_select_list.append(cb_index)
            self.curve_detail_list[cb_index - 1].setData(d)
            self.curve_overall_list[cb_index - 1].setData(d)
        else:
            self.curve_detail_list[cb_index - 1].setData([])
            self.curve_overall_list[cb_index - 1].setData([])
            self.channel_select_list.remove(cb_index)

    def closeEvent(self, event):
        self.need_close_event.set()
        self.data_timer.stop()
        self.save_profile()
        time.sleep(0.5)
        self.daq.disconnect()

    def le_period_text_changed(self, text):
        if self.ui.le_period.hasFocus():
            self.ui.le_frequency.setText(str(1000000 // int(text)))
            self.ui.slider_period.setValue(int(text))

    def le_frequency_text_changed(self, text):
        if self.ui.le_frequency.hasFocus():
            self.ui.le_period.setText(str(1000000 // int(text)))
            self.ui.slider_period.setValue(1000000 // int(text))

    def slider_period_value_changed(self, pos):
        if self.ui.slider_period.hasFocus():
            self.ui.le_period.setText(str(pos))
            self.ui.le_frequency.setText(str(1000000 // int(pos)))
        self.ui.time_status_label.setText(f"0 / {pos * self.ui.slider_cycles.value() / 1000:,.1f}ms")

    def le_cycles_text_changed(self, text):
        if self.ui.le_cycles.hasFocus():
            self.ui.slider_cycles.setValue(int(text))

    def slider_cycles_value_changed(self, pos):
        if self.ui.slider_cycles.hasFocus():
            self.ui.le_cycles.setText(str(pos))
        self.ui.time_status_label.setText(f"0 / {pos * self.ui.slider_period.value() / 1000:,.1f}ms")

    def daq_connect_in_new_thread(self):
        def daq_connect_thread():
            while not self.daq.connected and not self.need_close_event.isSet():
                try:
                    time.sleep(1)
                    self.daq.connect()
                except BaseException as e:
                    print(e)
            self.daq_connect_signal.emit()

        thread = Thread(target=daq_connect_thread)
        thread.start()

    def pb_load_profile_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Load profile", ".", "*.json")
        if not filename == "":
            self.ui.le_profile_file.setText(filename)
            self.load_profile()

    def pb_save_profile_clicked(self):
        filename, ok = QFileDialog.getSaveFileName(self, "Save profile", ".", "*.json")
        if not filename == "":
            self.ui.le_profile_file.setText(filename)
            self.save_profile()

    def pb_export_table_clicked(self):
        filename, filter = QFileDialog.getSaveFileName(self, "Export data", ".", "CSV File (*.csv);;Numpy File (*.npy)")
        try:
            if filter == "CSV File (*.csv)":
                np.savetxt(filename, self.total_sample_data, delimiter=",")
                with open(filename, "r+") as f:
                    old = f.read()
                    f.seek(0)
                    f.write(",".join([f"Channel {i}" for i in range(self.total_sample_data.shape[1])]) + "\n")
                    f.write(old)
            elif filter == "Numpy File (*.npy)":
                np.save(filename, self.total_sample_data)
        except BaseException as e:
            QMessageBox.warning(self, "Warning", f"Export failed, try again.\n\n{e}", buttons=QMessageBox.StandardButton.Yes)

    def btn_start_clicked(self):
        if self.ui.btn_start.is_started:
            self.data_timer.stop()
            self.daq.adc_stop()
            self.daq_stop_signal.emit(True)
        else:

            self.daq.set_config(range_=self.range_dict[self.ui.cb_range.currentText()],
                                os_=self.os_dict[self.ui.cb_os.currentText()],
                                trig_dir=self.trig_dir_dict[self.ui.cb_trig_dir.currentText()],
                                trig_mode=self.trig_mode_dict[self.ui.cb_trig_mode.currentText()],
                                period=self.ui.slider_period.value(),
                                cycles=self.ui.slider_cycles.value())
            self.index = 0
            self.total_sample_count = self.ui.slider_cycles.value()
            self.total_sample_data = np.zeros((self.total_sample_count, 8), dtype=np.float32)
            self.total_sample_time_ms_str = f"{self.ui.slider_period.value() * self.ui.slider_cycles.value() / 1000:,.1f}"
            self.daq.adc_start()
            self.data_timer.start(200)
            self.daq_start_signal.emit()

    def pb_save_plot_clicked(self):
        filename, filter = QFileDialog.getSaveFileName(self, "Export data", ".", "Portable Network Graphics File (*.png);;Scalable Vector Graphics File (*.svg);;CSV File of current scene (*.csv)")

        try:
            if filter == "Portable Network Graphics File (*.png)":
                ex = exporters.ImageExporter(self.ui.glw_detail.scene())
            elif filter == "Scalable Vector Graphics File (*.svg)":
                ex = exporters.SVGExporter(self.ui.glw_detail.scene())
            elif filter == "CSV File of current scene (*.csv)":
                ex = exporters.CSVExporter(self.ui.glw_detail.scene())
            ex.export(fileName=filename)
        except BaseException as e:
            QMessageBox.warning(self, "Warning", f"Export failed, try again.\n\n{e}", buttons=QMessageBox.StandardButton.Yes)

    def daq_connected_action(self):
        self.ui.btn_settings.setEnabled(True)
        self.ui.btn_start.setEnabled(True)
        self.ui.btn_settings.click()
        self.ui.connection_status_label.setText("Connected")

    def daq_stopped_action(self, status: bool):
        self.ui.btn_start.is_started = False
        self.ui.btn_start.setText("Start Sampling")
        self.ui.btn_start.setStyleSheet("background-image: url(:/icons/images/icons/cil-media-play.png);")
        self.ui.running_status_label.setText("Not running...")

        if status:
            # menu
            self.ui.btn_settings.setEnabled(True)
            self.ui.btn_chart.setEnabled(True)
            self.ui.btn_table.setEnabled(True)
            # plot
            self.ui.glw_overall.setEnabled(True)
            for i in self.channel_select_list:
                d = self.total_sample_data[:, i - 1]
                self.curve_detail_list[i - 1].setData(d)
                self.curve_overall_list[i - 1].setData(d)
            self.pg_region.setBounds([0, self.total_sample_count])
            self.pg_region.setRegion([self.total_sample_count * 0.9, self.total_sample_count])
            # table
            self.ui.tableView.setModel(TableModel(self.total_sample_data))
        else:
            self.ui.btn_home.click()
            self.ui.connection_status_label.setText("Connecting device...")
            self.ui.btn_settings.setEnabled(False)
            self.ui.btn_chart.setEnabled(False)
            self.ui.btn_table.setEnabled(False)
            self.daq_connect_in_new_thread()

    def daq_data_timer_action(self):
        try:
            # sampling
            data = self.daq.read_fifo()
            if data is None:
                return
            sample_count = data.shape[0]
            self.total_sample_data[self.index:self.index + sample_count, :] = data.astype(np.float32) / 65536 * 20
            self.index += sample_count

            # display
            self.ui.time_status_label.setText(
                f"{self.index * self.daq.sample_period / 1000:,.1f} / {self.total_sample_time_ms_str}ms")

            left = max(self.index - self.total_sample_count // 10, 0)
            for i in self.channel_select_list:
                d = self.total_sample_data[:self.index, i - 1]
                self.curve_detail_list[i - 1].setData(d)
                self.curve_overall_list[i - 1].setData(d)
            self.plot_item_detail.setXRange(left, self.index)

            # end
            if self.index == self.total_sample_count:
                self.data_timer.stop()
                self.daq_stop_signal.emit(True)
        except BaseException as e:
            print(e)
            self.data_timer.stop()
            # self.daq.adc_stop()
            self.daq_stop_signal.emit(False)

    def daq_started_action(self):
        self.plot_item_overall.setXRange(0, self.total_sample_count)
        self.pg_region.setBounds([0, self.total_sample_count])
        self.pg_region.setRegion([0, self.total_sample_count])
        self.ui.glw_overall.setEnabled(False)
        self.ui.btn_table.setEnabled(False)
        self.ui.btn_settings.setEnabled(False)
        self.ui.btn_start.setText("Stop - sampling...")
        self.ui.btn_start.setStyleSheet("background-image: url(:/icons/images/icons/cil-media-stop.png);")
        self.ui.btn_chart.setEnabled(True)
        self.ui.btn_chart.click()
        self.ui.btn_start.is_started = True
        self.ui.running_status_label.setText("Running")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
