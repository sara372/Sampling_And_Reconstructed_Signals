# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sampling_signal.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import numpy as np
from pyqtgraph import PlotWidget, PlotItem, plot
import pyqtgraph as pg
import pandas as pd
from PyQt5 import QtWidgets, uic, QtGui
import sys
import numpy as np
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene, QTextEdit, QLabel, QApplication
from pyqtgraph import PlotWidget, PlotItem
import pyqtgraph as pg
import os
import img_rc
from scipy import signal
import pyqtgraph.exporters
import statistics
from matplotlib.ticker import ScalarFormatter
from math import sin, pi
import numpy.fft as fft


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1976, 945)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_5 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.sinosoidal_signal = PlotWidget(self.splitter)
        self.sinosoidal_signal.setObjectName("sinosoidal_signal")
        self.summation_signal = PlotWidget(self.splitter)
        self.summation_signal.setObjectName("summation_signal")
        self.verticalLayout_2.addWidget(self.splitter)
        self.confirm_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_button.setFont(font)
        self.confirm_button.setObjectName("confirm_button")
        self.verticalLayout_2.addWidget(self.confirm_button)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.freq_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.freq_label.setFont(font)
        self.freq_label.setObjectName("freq_label")
        self.verticalLayout.addWidget(self.freq_label)
        self.frequency_value = QtWidgets.QTextEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.frequency_value.setFont(font)
        self.frequency_value.setObjectName("frequency_value")
        self.verticalLayout.addWidget(self.frequency_value)
        self.magnitude_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.magnitude_label.setFont(font)
        self.magnitude_label.setObjectName("magnitude_label")
        self.verticalLayout.addWidget(self.magnitude_label)
        self.magnitude_value = QtWidgets.QTextEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.magnitude_value.setFont(font)
        self.magnitude_value.setObjectName("magnitude_value")
        self.verticalLayout.addWidget(self.magnitude_value)
        self.phaseshift_label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.phaseshift_label.setFont(font)
        self.phaseshift_label.setObjectName("phaseshift_label")
        self.verticalLayout.addWidget(self.phaseshift_label)
        self.pahseshift_value = QtWidgets.QTextEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pahseshift_value.setFont(font)
        self.pahseshift_value.setObjectName("pahseshift_value")
        self.verticalLayout.addWidget(self.pahseshift_value)
        self.draw_button = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.draw_button.setFont(font)
        self.draw_button.setObjectName("draw_button")
        self.verticalLayout.addWidget(self.draw_button)
        self.save_button = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.verticalLayout.addWidget(self.save_button)
        self.signals_box = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.signals_box.setFont(font)
        self.signals_box.setObjectName("signals_box")
        self.signals_box.addItem("")
        self.signals_box.addItem("")
        self.signals_box.addItem("")
        self.signals_box.setItemText(2, "")
        self.signals_box.addItem("")
        self.signals_box.setItemText(3, "")
        self.verticalLayout.addWidget(self.signals_box)
        self.delete_signal = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.delete_signal.setFont(font)
        self.delete_signal.setObjectName("delete_signal")
        self.verticalLayout.addWidget(self.delete_signal)
        self.composed_box = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.composed_box.setFont(font)
        self.composed_box.setObjectName("composed_box")
        self.composed_box.addItem("")
        self.composed_box.addItem("")
        self.composed_box.addItem("")
        self.composed_box.addItem("")
        self.composed_box.addItem("")
        self.verticalLayout.addWidget(self.composed_box)
        self.draw_precomposed = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.draw_precomposed.setFont(font)
        self.draw_precomposed.setObjectName("draw_precomposed")
        self.verticalLayout.addWidget(self.draw_precomposed)
        self.show_summation_signal = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.show_summation_signal.setFont(font)
        self.show_summation_signal.setObjectName("show_summation_signal")
        self.verticalLayout.addWidget(self.show_summation_signal)
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter_2 = QtWidgets.QSplitter(self.layoutWidget2)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.original_signal = PlotWidget(self.splitter_2)
        self.original_signal.setObjectName("original_signal")
        self.sampling_signal = PlotWidget(self.splitter_2)
        self.sampling_signal.setObjectName("sampling_signal")
        self.verticalLayout_3.addWidget(self.splitter_2)
        self.sampling_rate_sliderll = QtWidgets.QSlider(self.layoutWidget2)
        self.sampling_rate_sliderll.setOrientation(QtCore.Qt.Horizontal)
        self.sampling_rate_sliderll.setObjectName("sampling_rate_sliderll")
        self.verticalLayout_3.addWidget(self.sampling_rate_sliderll)
        self.sampling_rate = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.sampling_rate.setFont(font)
        self.sampling_rate.setObjectName("sampling_rate")
        self.verticalLayout_3.addWidget(self.sampling_rate)
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.sampling_button = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.sampling_button.setFont(font)
        self.sampling_button.setObjectName("sampling_button")
        self.verticalLayout_4.addWidget(self.sampling_button)
        self.reconstrac_button = QtWidgets.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.reconstrac_button.setFont(font)
        self.reconstrac_button.setObjectName("reconstrac_button")
        self.verticalLayout_4.addWidget(self.reconstrac_button)
        self.hide_sampling_signal = QtWidgets.QCheckBox(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.hide_sampling_signal.setFont(font)
        self.hide_sampling_signal.setObjectName("hide_sampling_signal")
        self.verticalLayout_4.addWidget(self.hide_sampling_signal)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.gridLayout.addWidget(self.splitter_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1976, 26))
        self.menubar.setObjectName("menubar")
        self.menutaps = QtWidgets.QMenu(self.menubar)
        self.menutaps.setObjectName("menutaps")
        self.menuWindows = QtWidgets.QMenu(self.menubar)
        self.menuWindows.setObjectName("menuWindows")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionComposers = QtWidgets.QAction(MainWindow)
        self.actionComposers.setObjectName("actionComposers")
        self.actionsampling = QtWidgets.QAction(MainWindow)
        self.actionsampling.setObjectName("actionsampling")
        self.actionopen_signal = QtWidgets.QAction(MainWindow)
        self.actionopen_signal.setObjectName("actionopen_signal")
        self.menutaps.addAction(self.actionopen_signal)
        self.menuWindows.addAction(self.actionComposers)
        self.menuWindows.addAction(self.actionsampling)
        self.menubar.addAction(self.menutaps.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())

        #slider
        self.sampling_rate_sliderll.setMinimum((0))
        self.sampling_rate_sliderll.setMaximum(3)
        self.sampling_rate_sliderll.setSingleStep((1))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.confirm_button.setText(_translate("MainWindow", "Confirm"))
        self.freq_label.setText(_translate("MainWindow", " Frequency:"))
        self.magnitude_label.setText(_translate("MainWindow", "Magnitude:"))
        self.phaseshift_label.setText(_translate("MainWindow", "phase shift:"))
        self.draw_button.setText(_translate("MainWindow", "Draw"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.signals_box.setItemText(0, _translate("MainWindow", "choose signal"))
        self.signals_box.setItemText(1, _translate("MainWindow", "delete all"))
        self.delete_signal.setText(_translate("MainWindow", "Delete"))
        self.composed_box.setItemText(0, _translate("MainWindow", "Choose pre-composed signal"))
        self.composed_box.setItemText(1, _translate("MainWindow", "signal1"))
        self.composed_box.setItemText(2, _translate("MainWindow", "signal2"))
        self.composed_box.setItemText(3, _translate("MainWindow", "signal3"))
        self.composed_box.setItemText(4, _translate("MainWindow", "signal4"))
        self.draw_precomposed.setText(_translate("MainWindow", "draw pre-composed"))
        self.show_summation_signal.setText(_translate("MainWindow", "Show the final signal"))
        self.sampling_rate.setText(_translate("MainWindow", "sampling_rate"))
        self.sampling_button.setText(_translate("MainWindow", "plot the samples"))
        self.reconstrac_button.setText(_translate("MainWindow", "Reconstract the Signal"))
        self.hide_sampling_signal.setText(_translate("MainWindow", "Hide the signal"))
        self.menutaps.setTitle(_translate("MainWindow", "File"))
        self.menuWindows.setTitle(_translate("MainWindow", "Windows"))
        self.actionComposers.setText(_translate("MainWindow", "Composers"))
        self.actionsampling.setText(_translate("MainWindow", "sampling"))
        self.actionopen_signal.setText(_translate("MainWindow", "open signal"))

#------------------------------------------------------------------------
#                         setting:
        self.draw_button.clicked.connect(lambda: self.generate_sinusoidal())
        self.actionopen_signal.triggered.connect(lambda: self.open_signal())
        self.save_button.clicked.connect(lambda: self.save_sinusoidal())
        self.delete_signal.clicked.connect(lambda: self.delete_sinusoidal())
        self.show_summation_signal.clicked.connect(lambda: self.show_summed_signal())
        self.confirm_button.clicked.connect(lambda :self.confirm())
        self.draw_precomposed.clicked.connect(lambda :self.DrawPrecomposed())
        self.sampling_button.clicked.connect(lambda: self.sampling())
        #self.sampling_rate_sliderll.valueChanged.connect(lambda:self.sampling())
        self.hide_sampling_signal.clicked.connect(lambda: self.hide_view())
        self.reconstrac_button.clicked.connect(lambda: self.reconstruct())
#------------------------------------------------------------------------
#                         functions:

    def get_freq_mag_shift(self):
        self.freq=self.frequency_value.toPlainText()
        self.magnitude=self.magnitude_value.toPlainText()
        self.phase_shift= self.pahseshift_value.toPlainText()
        return float(self.freq),float(self.magnitude),float(self.phase_shift)

    time_signal = np.linspace(0,10,1000)
    def generate_sinusoidal(self):
        self.sinosoidal_signal.clear()
        self.f_freq,self.f_magnitude,self.f_phase_shift=self.get_freq_mag_shift()
        self.amp_signal =self.f_magnitude*np.sin(2*np.pi*self.f_freq*self.time_signal+self.f_phase_shift*np.pi/180)
        self.data_line1 = self.sinosoidal_signal.plot(self.time_signal, self.amp_signal)

    signals_to_be_summed=[]
    combo_box_idx=2
    def save_sinusoidal(self):
        self.f_freq,self.f_magnitude,self.f_phase_shift=self.get_freq_mag_shift()
        self.signals_to_be_summed.append({"frequency":self.f_freq,"magnitude":self.f_magnitude,'phase shift':self.f_phase_shift})
        self.text_combobox=str(self.f_freq)+','+str(self.f_magnitude)+','+str(self.f_phase_shift)
        self.signals_box.addItem("")
        self.signals_box.setItemText(self.combo_box_idx,self.text_combobox)
        self.combo_box_idx=self.combo_box_idx+1

    def delete_sinusoidal(self):

        if self.signals_box.currentText()=='delete all':
            self.signals_to_be_summed.clear()
            self.signals_box.clear()
            self.signals_box.addItem("")
            self.signals_box.setItemText(0,"choose signal")
            self.signals_box.addItem("")
            self.signals_box.setItemText(1,"delete all")
            self.combo_box_idx=2

        else:
            self.current_signal=self.signals_box.currentText()
            self.current_values=self.current_signal.split(',')

            self.current_freq=float(self.current_values[0])
            self.current_mag=float(self.current_values[1])
            self.current_shift=float(self.current_values[2])
            for self.signal in self.signals_to_be_summed:
                if (self.signal['frequency']==self.current_freq) & (self.signal['magnitude']==self.current_mag )& (self.signal['phase shift']==self.current_shift):
                    self.signals_to_be_summed.remove(self.signal)
            self.current_idx=self.signals_box.currentIndex()
            self.signals_box.removeItem(self.current_idx)
            self.combo_box_idx=self.combo_box_idx-1


    def show_summed_signal(self):
        self.summation_signal.clear()
        self.sum=0
        for self.signal in self.signals_to_be_summed:
             self.sum=self.sum+self.signal['magnitude']*np.sin(2*np.pi*self.signal['frequency']*self.time_signal+self.signal['phase shift']*np.pi/180)
        self.data_line2 = self.summation_signal.plot(self.time_signal,self.sum)

    flag=0

    def DrawPrecomposed(self):
        self.original_signal.clear()
        self.composed_signals=[]
        self.composed_signals.append(np.sin(2*np.pi*2*self.time_signal)+np.sin(2*np.pi*6*self.time_signal))
        self.flag =2

        if self.composed_box.currentText()=='signal1':
            self.data_line3=self.original_signal.plot(self.time_signal,self.composed_signals[0])
            return(self.time_signal,self.composed_signals[0])
        elif self.composed_box.currentText()=='signal2':
            self.data_line3=self.original_signal.plot(self.time_signal,self.composed_signals[1])
            return(self.time_signal,self.composed_signals[1])
        elif self.composed_box.currentText()=='signal3':
            self.data_line3=self.original_signal.plot(self.time_signal,self.composed_signals[2])
            return(self.time_signal,self.composed_signals[2])
        elif self.composed_box.currentText()=='signal4':
            self.data_line3 = self.original_signal.plot(self.time_signal,self.composed_signals[3])
            return(self.time_signal,self.composed_signals[3])

    def confirm(self):
        self.original_signal.clear()
        self.data_line3 = self.original_signal.plot(self.time_signal,self.sum)
        self.data_line3 = self.original_signal.plot(self.time_signal, self.sum)
        self.flag=1
        return self.time_signal,self.sum
#----------------SAMPLING--------------


    def open_signal(self):
        self.original_signal.clear()
        self.file_name1 = QtWidgets.QFileDialog.getOpenFileNames(
            self, 'Open only txt or CSV or xls', os.getenv('HOME'))
        self.read_file1(self.file_name1[0][0])

    x_original_signal = []
    y_original_signal = []

    def read_file1(self, file_path):
        self.path1 = file_path
        data1 = pd.read_csv(self.path1)
        self.y_original_signal = data1.values[:, 1]
        self.x_original_signal = data1.values[:, 0]
        self.data_line3 = self.original_signal.plot(self.x_original_signal, self.y_original_signal)
        self.flag=0

    def sampling(self):
        self.original_signal.clear()

        if self.flag==0:
            self.x_signal = self.x_original_signal
            self.y_signal = self.y_original_signal
            spectrum = fft.fft(self.y_signal)
            freq = fft.fftfreq(len(spectrum))
            threshold = 0.5 * max(abs(spectrum))
            mask = abs(spectrum) > threshold
            peaks = freq[mask]
            peaks = abs(peaks)
            F_max = max(peaks)*1000

        elif self.flag ==1 :
            self.x_signal = self.confirm()[0]
            self.y_signal = self.confirm()[1]
            spectrum = fft.fft(self.y_signal)
            freq = fft.fftfreq(len(spectrum))
            threshold = 0.5 * max(abs(spectrum))
            mask = abs(spectrum) > threshold
            peaks = freq[mask]
            peaks = abs(peaks)
            F_max = max(peaks)*100

        elif self.flag == 2 :
            self.x_signal = self.DrawPrecomposed()[0]
            self.y_signal = self.DrawPrecomposed()[1]
            spectrum = fft.fft(self.y_signal)
            freq = fft.fftfreq(len(spectrum))
            threshold = 0.5 * max(abs(spectrum))
            mask = abs(spectrum) > threshold
            peaks = freq[mask]
            peaks = abs(peaks)
            F_max = max(peaks)*100

        self.data_line3 = self.original_signal.plot(self.x_signal, self.y_signal)


        #slider ----->
        self.F_sampling = (F_max*self.sampling_rate_sliderll.value())
        self.T_sampling = 1/self.F_sampling

        self.Samples_values = []
        self.Time_sampling = []

        if( self.F_sampling != 0):
            self.Step_in_index = int(len(self.x_signal) / (max(self.x_signal)*self.F_sampling))
            print(self.F_sampling)
            print(self.T_sampling)
            print(self.Step_in_index)
            print(len(self.x_signal))
            print(max(self.x_signal))

            for index in range(0, len(self.x_signal), self.Step_in_index):
                    self.Samples_values.append(self.y_signal[index])
                    self.Time_sampling.append(self.x_signal[index])

        # I will plot the pints{Time_Values,self.Samples } in the same main graph as a points
        scatter = pg.ScatterPlotItem(size=8, brush=pg.mkBrush(255, 0, 0, 255))
        scatter.setData(self.Time_sampling, self.Samples_values)
        self.original_signal.addItem(scatter)
        return (self.x_signal, self.Samples_values, self.T_sampling, self.y_signal, self.Step_in_index)

        #reconstract (interpolation)
    def reconstruct(self):
        self.sampling_signal.clear()
        self.x_signal = self.sampling()[0]
        self.Samples_values = self.sampling()[1]
        self.T_sampling = self.sampling()[2]
        self.y_signal = self.sampling()[3]
        self.Step_in_index = self.sampling()[4]
        self.y_interpolated_f = 0  # class Variable                                                                                                                                                            for index in range(0,  len(Time_Values)):  # interpolation with sinc function
        for index in range(0,  len(self.Time_sampling)):
            self.y_interpolated_f += self.Samples_values[index] * np.sinc((np.array(self.x_signal) - self.T_sampling * index) / self.T_sampling)
            #    x_reconstructed += calculate_signal(k/fs) * np.sinc(k - fs * t)
        pen = pg.mkPen(color=(255, 0, 0), width=2, style=QtCore.Qt.DotLine)
        self.data_line3 = self.original_signal.plot(self.x_signal, self.y_interpolated_f, pen = pen)
        self.data_line4 = self.sampling_signal.plot(self.x_signal, self.y_interpolated_f)

    def hide_view (self):
        if self.hide_sampling_signal.checkState():
            self.sampling_signal.hide()
        else:
            self.sampling_signal.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
