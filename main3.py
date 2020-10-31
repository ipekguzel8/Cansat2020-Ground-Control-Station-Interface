import serial
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtCore, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import pyqtgraph.exporters
import numpy as np
import sys
import vtk
from qtpy.QtGui import QPainter, QColor, QPen, QBrush, QPixmap
from qtpy.QtWidgets import QMainWindow, QGraphicsView, QGraphicsItem, QGraphicsSimpleTextItem, QApplication
from pytilemap import MapGraphicsView, MapTileSourceHere, MapTileSourceOSM
misst=list()
giris=0
from random import randint
strnsx=[]
import glob
from PyQt5.QtCore import Qt,QThread, pyqtSignal
import requests
import json
from PyQt5.QtWidgets import (QApplication, QDialog,
                             QProgressBar, QPushButton)
from tkinter import *
from tkinter import filedialog
misst=list()
ser = serial.Serial()
class Pencere(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stopflag =False
        self.resize(1926, 1006)
        self.frame_gl=QFrame()    
        opengl=QOpenGLWidget(parent=self.frame_gl)
        self.setWindowIcon(QIcon("logo1.png"))
        self.setAutoFillBackground(True)      
        oImage=QImage("ekran8.png")
        sImage=oImage.scaled(QSize(1926, 1020))
        palette=QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        self.bosluk=QLabel("    ")
        self.genelhbox=QHBoxLayout()
        self.firstvb=QVBoxLayout()
        self.kamera=QLabel()
        self.kamera.setFixedHeight(400)
        self.kamera.setFixedWidth(350)
        self.kamera.setStyleSheet("border:1px solid #000000")
        self.kamera.setPixmap(QPixmap("kamera.jpg"))
        self.logo=QLabel()
        self.logo.setFixedHeight(150)
        self.logo.setFixedWidth(260)
        self.logo.setPixmap(QPixmap("logo4.PNG"))
        self.logo.setAlignment(Qt.AlignTop)
        gpslatitude=[41.4528,41.4522,41.4519,41.4517,41.4516,41.4514,41.4510,41.4506,41.4502,41.4498,41.4493,41.4492,41.4490,41.4483,41.4485]
        gpslongitude=[31.7587,31.7595,31.7601,31.7605,31.7611,31.7616,31.7620,31.7624,31.7629,31.7636,31.7639,31.7650,31.7649,31.7645,31.7652]
        
        view = MapGraphicsView(tileSource=MapTileSourceHere()) #tileSource=MapTileSourceOSM("map.osm")
        view.scene().setCenter(gpslongitude[0], gpslatitude[0])
        view.setOptimizationFlag(QGraphicsView.DontSavePainterState, True)
        view.setRenderHint(QPainter.Antialiasing, True)
        view.setRenderHint(QPainter.SmoothPixmapTransform, True)
        #pointItem = view.scene().addCircle(gpslongitude[0], gpslatitude[0], 3.0)
        #pointItem2 = view.scene().addCircle(gpslongitude[14], gpslatitude[14], 5.0)
        #pointItem2.setFlag(QGraphicsItem.ItemIsSelectable, True)
        #pointItem2.setBrush(Qt.red)
        #pointItem2.setPen(QPen(Qt.NoPen))
        #pointItem2.setToolTip('%f, %f' % (gpslongitude[14], gpslatitude[14]))
        #pointItem.setToolTip('%f, %f' % (gpslongitude[0], gpslatitude[0]))
        #pointItem.setBrush(Qt.black)
        #pointItem.setToolTip('31.789339, 41.450508')
        #pointItem = view.scene().addCircle(gpslongitude[0], gpslatitude[0], 5.0)
        #pointItem.setBrush(Qt.green)
        #pointItem.setPen(QPen(Qt.NoPen))
        #for i in range(1,14):
        #    pointItem3 = view.scene().addCircle(gpslongitude[i], gpslatitude[i], 5.0)
        #    pointItem3.setBrush(Qt.blue)
        #    pointItem3.setPen(QPen(Qt.NoPen))
        #    pointItem3.setToolTip('%f, %f' % (gpslongitude[i], gpslatitude[i]))
        #    pointItem3.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.z=0
        self.resize(1926, 1006)
        #view.setStyleSheet("border:4px solid #F5BB47")
        view.setFixedWidth(350)
        view.setFixedHeight(400)
        self.twovb=QVBoxLayout()
        view.setStyleSheet("border:1px solid #000000")
        self.threevb=QVBoxLayout()
        self.firstvb.addWidget(self.logo)
        self.firstvb.addWidget(self.bosluk)
        self.firstvb.addWidget(self.kamera)
        self.firstvb.addWidget(self.bosluk)
        self.firstvb.addWidget(view)
        self.twovbhb1=QHBoxLayout()
        self.twovbhb12=QHBoxLayout()
        self.twovbhb13=QHBoxLayout()
        self.twovbhb14=QHBoxLayout()
        self.twovbhb15=QHBoxLayout()
        self.twovbvb1=QVBoxLayout()
        self.twovbhb2=QHBoxLayout()
        self.twovbhb3=QHBoxLayout()
        self.port=QLabel("Ports:       ")
        self.port.setFixedWidth(100)
        self.port.setFont(QFont("Helvetica",12,QFont.Bold))
        self.ports=QComboBox()
        self.ports.setFixedWidth(100)
        self.ports.addItems([''])
        self.ports.addItems(self.portlar())
        self.ports.setStyleSheet("font: bold 15px;")
        self.groupbox2 = QGroupBox("Seri Port Yapılandırması")
        self.start=QPushButton("BAŞLA")
        self.start.setFont(QFont("Helvetica",10,))
        self.start.clicked.connect(self.Start)
        self.start.setInputMethodHints(Qt.ImhNone)
        #self.start.clicked.connect(self.Start)
        self.baudrates=QLabel("Baudrate:     ")
        self.baudrates.setFont(QFont("Helvetica",12,QFont.Bold))
        self.baudrate=QComboBox()
        self.baudrate.setFixedWidth(100)
        self.baudrate.addItems(["","9600","19200"])
        self.baudrate.setStyleSheet("font: bold 15px;")
        self.baudrates.setFixedWidth(100)
        
        self.gerial=QPushButton("GERİ AL")
        self.twovbhb15.addWidget(self.gerial)
        
        self.ayırma=QPushButton("AYIR")
        self.ayırma.setFixedWidth(113)
        self.gerial.setFixedWidth(113)
        self.groupbox4 = QGroupBox("Ayrılma Komutu")
        self.groupbox3 = QGroupBox("Arşivlenen Verileri Arayüze Geri Alma Komutu")
        self.groupbox3.setLayout(self.twovbhb15)
        self.twovbhb14.addWidget(self.ayırma)
        self.groupbox4.setLayout(self.twovbhb14)
        self.ayırma.setFont(QFont("Helvetica",10))
        self.packetcount=QLabel("Paket Numarası:")
        self.packetcount2=QLabel()
        self.packetcount.setFont(QFont("Helvetica",12,QFont.Bold))
        self.packetcount2.setFont(QFont("Helvetica",12,QFont.Bold))
        self.packetcount.setFixedWidth(137)
        self.missiontime=QLabel("Gönderme Saati:")
        self.missiontime2=QLabel()
        self.missiontime2.setFont(QFont("Helvetica",12,QFont.Bold))
        self.missiontime.setFont(QFont("Helvetica",12,QFont.Bold))
        self.missiontime.setFixedWidth(157)
        self.start.setInputMethodHints(Qt.ImhNone)
        self.dosyasecs=QLabel("Dosya Seç:")
        self.dosyasecs.setFixedHeight(20)
        self.dosyasecs.setFixedWidth(90)
        self.dosyasecs.setFont(QFont("Helvetica",12,QFont.Bold))
        self.dosyasec=QPushButton("...")
        self.stop=QPushButton("DUR")
        self.stop.setInputMethodHints(Qt.ImhNone)
        self.stop.clicked.connect(self.Stop)
        self.stop.setFont(QFont("Helvetica",10,))
        self.dosyasec.setFixedHeight(20)
        self.dosyasec.setFixedWidth(20)
        self.gonder=QPushButton("GÖNDER")
        self.gonder.setFixedWidth(110)
        self.gonder.setFont(QFont("Helvetica",10,))
        self.groupbox = QGroupBox("Video Aktarımı")
        self.gbx=QHBoxLayout()
        self.gbx.addWidget(self.dosyasecs)
        self.gbx.addWidget(self.dosyasec)
        self.gbx.addWidget(self.gonder)
        self.groupbox.setLayout(self.gbx)
        self.twovbhb13.addWidget(self.port)
        self.twovbhb13.addWidget(self.ports)
        self.twovbhb13.addWidget(self.bosluk)
        self.twovbhb13.addWidget(self.baudrates)
        self.twovbhb13.addWidget(self.baudrate)
        self.twovbhb12.addWidget(self.start)
        self.twovbhb12.addWidget(self.stop)
        self.twovbvb1.addLayout(self.twovbhb13)
        self.twovbvb1.addLayout(self.twovbhb12)
        self.groupbox2.setLayout(self.twovbvb1)
        self.twovbhb1.addWidget(self.groupbox2)        
        self.twovbhb1.addWidget(self.bosluk)
        self.twovbhb1.addWidget(self.groupbox4)
        self.twovbhb1.addWidget(self.bosluk)
        self.twovbhb1.addWidget(self.groupbox3)
        self.twovbhb1.addWidget(self.bosluk)
        self.twovbhb1.addWidget(self.groupbox)
        
        
        self.temp=[]
        self.pressure=list()
        self.voltage=list()
        self.altitude=list()
        self.inishiz=list()
        self.gpsaltitude=list()
        self.timer=list()
        self.tableWidget2=QTableWidget()
        self.tableWidget2.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget2.setColumnCount(17)   
        self.tableWidget2.setHorizontalHeaderLabels(str("TAKIM NO;PAKET NUMARASI;GÖNDERME SAATİ;BASINÇ;YÜKSEKLİK;İNİŞ HIZI;SICAKLIK;PİL GERİLİMİ;GPS LATITUDE;GPS LONGITUDE;GPS ALTITUDE;UYDU STATÜSÜ;PITCH;ROLL;YAW;DÖNÜŞ SAYISI;VİDEO AKTARIM BİLGİSİ").split(";"))
        self.tableWidget2.verticalHeader().hide()
        self.tableWidget2.horizontalHeader().setStyleSheet("font: bold 7px;")
        self.tableWidget2.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.tableWidget2.horizontalScrollBar().hide()
        self.tableWidget2.setStyleSheet("font:12px;")
        self.tableWidget2.setColumnWidth(0,57)
        self.tableWidget2.setColumnWidth(1,97)
        self.tableWidget2.setColumnWidth(2,96)
        self.tableWidget2.setColumnWidth(3,47)
        self.tableWidget2.setColumnWidth(4,60)
        self.tableWidget2.setColumnWidth(5,53)
        self.tableWidget2.setColumnWidth(6,51)
        self.tableWidget2.setColumnWidth(7,70)
        self.tableWidget2.setColumnWidth(8,78)
        self.tableWidget2.setColumnWidth(9,88)
        self.tableWidget2.setColumnWidth(10,77)
        self.tableWidget2.setColumnWidth(11,83)
        self.tableWidget2.setColumnWidth(12,38)
        self.tableWidget2.setColumnWidth(13,34)
        self.tableWidget2.setColumnWidth(14,33)
        self.tableWidget2.setColumnWidth(15,81)
        self.tableWidget2.setColumnWidth(16,130)
        self.tableWidget2.horizontalHeader().setStyleSheet("font: bold 10px;")
        self.tableWidget2.setFixedHeight(195)
        self.tableWidget=QTableWidget()
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setColumnCount(17)
        self.tableWidget.setHorizontalHeaderLabels(str("TAKIM NO;PAKET NUMARASI;GÖNDERME SAATİ;BASINÇ;YÜKSEKLİK;İNİŞ HIZI;SICAKLIK;PİL GERİLİMİ;GPS LATITUDE;GPS LONGITUDE;GPS ALTITUDE;UYDU STATÜSÜ;PITCH;ROLL;YAW;DÖNÜŞ SAYISI;VİDEO AKTARIM BİLGİSİ").split(";"))
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().setStyleSheet("font: bold 13px;")
        self.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
        self.tableWidget.horizontalScrollBar().hide()
        self.tableWidget.setStyleSheet("font:12px;")
        self.tableWidget.setColumnWidth(0,59)
        self.tableWidget.setColumnWidth(1,98)
        self.tableWidget.setColumnWidth(2,97)
        self.tableWidget.setColumnWidth(3,47)
        self.tableWidget.setColumnWidth(4,61)
        self.tableWidget.setColumnWidth(5,56)
        self.tableWidget.setColumnWidth(6,55)
        self.tableWidget.setColumnWidth(7,72)
        self.tableWidget.setColumnWidth(8,75)
        self.tableWidget.setColumnWidth(9,89)
        self.tableWidget.setColumnWidth(10,77)
        self.tableWidget.setColumnWidth(11,86)
        self.tableWidget.setColumnWidth(12,38)
        self.tableWidget.setColumnWidth(13,34)
        self.tableWidget.setColumnWidth(14,33)
        self.tableWidget.setColumnWidth(15,81)
        self.tableWidget.setColumnWidth(16,130)
        self.tableWidget.horizontalHeader().setStyleSheet("font: bold 10px;")
        self.splitter1 = QSplitter()
        self.splitter1.setOrientation(Qt.Vertical)
        self.splitter2 = QSplitter()
        self.splitter2.setOrientation(Qt.Horizontal)
        self.splitter3 = QSplitter()
        self.splitter3.setOrientation(Qt.Horizontal)
        self.splitter4 = QSplitter()
        self.splitter4.setOrientation(Qt.Horizontal)
        self.dates2=[]
        self.axis = DateAxis(orientation='bottom')
        self.axis2 = DateAxis(orientation='bottom')
        self.axis3 = DateAxis(orientation='bottom')
        self.axis4 = DateAxis(orientation='bottom')
        self.axis5 = DateAxis(orientation='bottom')
        self.axis6 = DateAxis(orientation='bottom')
        self.pw = pg.PlotWidget(axisItems={'bottom': self.axis},  title="PlotItem")
        self.pw2 = pg.PlotWidget(axisItems={'bottom': self.axis2},  title="PlotItem")
        self.pw3 = pg.PlotWidget(axisItems={'bottom': self.axis3}, title="PlotItem")
        self.pw4 = pg.PlotWidget(axisItems={'bottom': self.axis4}, title="PlotItem")
        self.pw5 = pg.PlotWidget(axisItems={'bottom': self.axis5},  title="PlotItem")
        self.pw6 = pg.PlotWidget(axisItems={'bottom': self.axis6},  title="PlotItem")
        self.pen = pg.mkPen(color=(0, 0, 0))
        self.pw.setBackground('w')
        self.pw.setTitle('<span style=\"color:black;font-size:17px\">YÜKSEKLİK(m)</span>')
        self.pw.setLabel('left', '<span style=\"color:black;font-size:17px\">m</span>')
        self.pw.setLabel('bottom', '<span style=\"color:black;font-size:17px\">Gönderme Saati(sa:dk:sn)</span>')
        self.data_line =  self.pw.plot(self.dates2, self.altitude,pen=self.pen,symbol='o', symbolSize=10, symbolBrush=('r'))
        self.pw2.setBackground('w')
        self.pw2.setTitle('<span style=\"color:black;font-size:17px\">SICAKLIK(°C)</span>')
        self.pw2.setLabel('left', '<span style=\"color:black;font-size:17px\">°C</span>')
        self.pw2.setLabel('bottom', '<span style=\"color:black;font-size:17px\">Gönderme Saati(sa:dk:sn)</span>')
        self.data_line2 =  self.pw2.plot(self.dates2, self.temp,pen=self.pen,symbol='o', symbolSize=10, symbolBrush=('r'))
        self.pw3.setBackground('w')
        self.pw3.setTitle('<span style=\"color:black;font-size:17px\">BASINÇ(Pa)</span>')
        self.pw3.setLabel('left', '<span style=\"color:black;font-size:17px\">Pa</span>')
        self.pw3.setLabel('bottom', '<span style=\"color:black;font-size:17px\">Gönderme Saati(sa:dk:sn)</span>')
        self.data_line3 =  self.pw3.plot(self.dates2, self.pressure,pen=self.pen,symbol='o', symbolSize=10, symbolBrush=('r'))
        self.pw4.setBackground('w')
        self.pw4.setTitle('<span style=\"color:black;font-size:17px\">PİL GERİLİMİ(V)</span>')
        self.pw4.setLabel('left', '<span style=\"color:black;font-size:17px\">V</span>')
        self.pw4.setLabel('bottom', '<span style=\"color:black;font-size:17px\">Gönderme Saati(sa:dk:sn)</span>')
        self.data_line4 =  self.pw4.plot(self.dates2, self.voltage,pen=self.pen,symbol='o', symbolSize=10, symbolBrush=('r'))
        self.pw5.setBackground('w')
        self.pw5.setTitle('<span style=\"color:black;font-size:17px\">İNİŞ HIZI(m/s)</span>')
        self.pw5.setLabel('left', '<span style=\"color:black;font-size:17px\">m/s</span>')
        self.pw5.setLabel('bottom', '<span style=\"color:black;font-size:17px\">Gönderme Saati(sa:dk:sn)</span>')
        self.data_line5 =  self.pw5.plot(self.dates2, self.gpsaltitude,pen=self.pen,symbol='o', symbolSize=10, symbolBrush=('r'))
        self.pw6.setBackground('w')
        self.pw6.setTitle('<span style=\"color:black;font-size:17px\">GPS ALTİTUDE(m)</span>')
        self.pw6.setLabel('left','<span style=\"color:black;font-size:17px\">m</span>')
        self.pw6.setLabel('bottom', '<span style=\"color:black;font-size:17px\">Gönderme Saati(sa:dk:sn)</span>')
        self.data_line6 =  self.pw6.plot(self.dates2, self.inishiz,pen=self.pen,symbol='o', symbolSize=10, symbolBrush=('r'))
        self.splitter3.addWidget(self.pw)
        self.splitter3.addWidget(self.pw2)
        self.splitter3.addWidget(self.pw3)
        self.splitter2.addWidget(self.pw4)
        self.splitter2.addWidget(self.pw5)
        self.splitter2.addWidget(self.pw6)
        self.splitter1.addWidget(self.splitter3)
        self.splitter1.addWidget(self.splitter2)
        self.splitter4.addWidget(self.tableWidget2)
        self.splitter1.addWidget(self.splitter4)
        layout = QGridLayout()
        view2 = MapGraphicsView(tileSource=MapTileSourceHere()) #tileSource=MapTileSourceOSM("map.osm")
        view2.scene().setCenter(gpslongitude[0], gpslatitude[0])
        view2.setOptimizationFlag(QGraphicsView.DontSavePainterState, True)
        view2.setRenderHint(QPainter.Antialiasing, True)
        view2.setRenderHint(QPainter.SmoothPixmapTransform, True)
        #pointItem3 = view2.scene().addCircle(gpslongitude[0], gpslatitude[0], 3.0)
        #pointItem4 = view2.scene().addCircle(gpslongitude[14], gpslatitude[14], 5.0)
        #pointItem4.setFlag(QGraphicsItem.ItemIsSelectable, True)
        #pointItem4.setBrush(Qt.red)
        #pointItem4.setPen(QPen(Qt.NoPen))
        #pointItem4.setToolTip('%f, %f' % (gpslongitude[14], gpslatitude[14]))
        #pointItem3.setToolTip('%f, %f' % (gpslongitude[0], gpslatitude[0]))
        #pointItem3.setBrush(Qt.black)
        #pointItem3.setToolTip('31.789339, 41.450508')
        #pointItem3 = view2.scene().addCircle(gpslongitude[0], gpslatitude[0], 5.0)
        #pointItem3.setBrush(Qt.green)
        #pointItem3.setPen(QPen(Qt.NoPen))
        #for i in range(1,14):
        #    pointItem5 = view2.scene().addCircle(gpslongitude[i], gpslatitude[i], 5.0)
        #    pointItem5.setBrush(Qt.blue)
        #    pointItem5.setPen(QPen(Qt.NoPen))
        #    pointItem5.setToolTip('%f, %f' % (gpslongitude[i], gpslatitude[i]))
        #    pointItem5.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.kamera2=QLabel()
        self.kamera2.setPixmap(QPixmap("kamera.jpg"))
        tabwidget = QTabWidget()
        tabwidget.addTab(self.splitter1, "GRAFİKLER")
        tabwidget.addTab(self.tableWidget, "TELEMETRİ VERİLERİ")
        tabwidget.addTab(view2, "HARİTA")
        tabwidget.addTab(self.kamera2, "KAMERA KAYDI")
        tabwidget.setStyleSheet("font: bold 18px;")
        layout.addWidget(tabwidget, 0, 0) 
        
        self.twovbhb3.addWidget(self.packetcount)
        self.twovbhb3.addWidget(self.packetcount2)
        self.twovbhb3.addWidget(self.missiontime)
        self.twovbhb3.addWidget(self.missiontime2)
        self.twovb.addLayout(self.twovbhb1)
        self.twovb.addLayout(self.twovbhb3)
        self.twovb.addWidget(self.bosluk)
        self.twovb.addLayout(layout)
        
        self.prog=QProgressBar(self)
        self.prog.setMaximum(100)
        self.prog.setUpdatesEnabled(True)
        self.prog.setValue(0)
        self.prog.setAlignment(Qt.AlignCenter)
        self.prog.setStyleSheet("QProgressBar{border: 2px solid grey; border-radius: 5px;}")
        self.prog.setStyleSheet("::chunk{background-color: #42C9EB; width: 10px; margin:1.2px; align:center}")
        self.prog.setFixedWidth(350)
        self.prog.setFixedHeight(54)
        self.prog.setFont(QFont("Helvetica",13,QFont.Bold))
        self.listem=QListWidget()
        self.addg=QBrush(QColor(0,255,127))#(156, 239, 130)
        self.listem.setStyleSheet("font:bold 13px rgb(4, 199, 234)")
        self.listem.setFixedHeight(242)
        self.listem.setFixedWidth(350)
        self.listem.setSelectionMode(QListWidget.MultiSelection)
        self.listem.setAutoFillBackground(True)
        self.softws=QLabel("          UYDU STATÜSÜ")
        self.listemitem=["Görev Başladı","Uçuş Bekleniyor","Uydu(Taşıyıcı+Yük) Yükselmekte","Uydu(Taşıyıcı+Yük) İnişte","Yük Taşıyıcıdan Ayrıldı","Yük Kurtarılmayı Bekliyor","Görev Tamamlandı"]
        for i in self.listemitem:
            self.listem.addItem(i)
        self.softws.setFixedWidth(352)
        self.softws.setFixedHeight(62)
        self.softws.setStyleSheet("font:bold 24px #E0E0E0; background-color: #e6e6e6; border:1px solid #000000")
        self.listem.setStyleSheet("font:24px;background-color: #e6e6e6")
        filename = "ipek.STL"
        self.frame =QFrame()
        self.frame.resize(100,100)
        reader = vtk.vtkSTLReader()
        reader.SetFileName(filename)
        self.vl =QVBoxLayout()
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.vl.addWidget(self.vtkWidget)
        self.iren =self.vtkWidget.GetRenderWindow().GetInteractor()
        self.transform = vtk.vtkTransform()
        self.transformFilter=vtk.vtkTransformPolyDataFilter()
        self.transformFilter.SetTransform(self.transform)
        self.transformFilter.SetInputConnection(reader.GetOutputPort())
        self.transformFilter.Update()
        self.mapper = vtk.vtkPolyDataMapper()
        if vtk.VTK_MAJOR_VERSION <= 5:
            self.mapper.SetInput(self.transformFilter.GetOutput())
        else:
            self.mapper.SetInputConnection(self.transformFilter.GetOutputPort())
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(self.mapper)
        self.actor.SetScale(0.0107, 0.0107, 0.0107)
        self.actor.GetProperty().SetColor(0.5,0.5,0.5)
        self.actor.GetProperty().SetOpacity(0.5)
        self.ren = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.ren.AddActor(self.actor)
        self.ren.SetBackground(0.496,0.832,0.996)
        self.ren.ResetCamera()
        self.frame.setLineWidth(0.6)
        self.frame.setLayout(self.vl)
        self.iren.Initialize()
        self.frame.setFixedWidth(350)
        self.frame.setFixedHeight(423)
        self.frame.setStyleSheet("border:1px solid #000000; background-color:#7FD5FF")
        self.koordinat=QLabel("PITCH:                    ROLL:                    YAW:")
        self.koordinat.setFixedHeight(72)
        self.koordinat.setFixedWidth(350)
        self.koordinat.setStyleSheet("font:bold 15px; background-color: #e6e6e6; border:1px solid #000000")
        self.stated=QLabel("Uydu Statüsü:")
        self.stated.setFont(QFont("Helvetica",12,QFont.Bold))
        self.kaynak=QLabel("Görev Tamamlanma Yüzdesi:")
        self.kaynak.setFont(QFont("Helvetica",12,QFont.Bold))
        self.kaynak.setFixedHeight(25)
        self.threevb.addWidget(self.kaynak) 
        self.threevb.addWidget(self.prog)  
        self.threevb.addWidget(self.stated)
        self.threevb.addWidget(self.bosluk)
        self.threevb.addWidget(self.softws)
        self.threevb.addWidget(self.listem)
        
        self.threevb.addWidget(self.frame)
        self.threevb.addWidget(self.koordinat)
        self.genelhbox.addLayout(self.firstvb)
        self.genelhbox.addLayout(self.twovb)
        self.genelhbox.addLayout(self.threevb)
        self.setLayout(self.genelhbox)
        self.setWindowTitle("Grizu-263 Uzay Takımı| Yer İstasyonu")
        self.show()
    def Start(self):
        self.start.setDisabled(True)
        if str(self.ports.currentText())== str(''):
            print("Port Seçmediniz!!") 
        else:
            ser.port=str(self.ports.currentText())
            ser.baudrate=int(self.baudrate.currentText())
            ser.timeout=0.5
            ser.open()
            self.runnable = Runnable(self)
            QtCore.QThreadPool.globalInstance().start(self.runnable)
    def Stop(self):
        self.stop.setDisabled(True)
        self.stopflag = True
    def portlar(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result
    def dosyasec():
        dosyaal=askopenfilename()
        if dosyaal:
            yazi2.config(text=dosyaal)
        else:
            yazi2.config(text="Seçilen Dosya: Dosya Seçilmedi")
class Runnable(QtCore.QRunnable,Pencere,QtCore.QThread):
    def __init__(self, w, *args, **kwargs):
        QtCore.QRunnable.__init__(self, *args, **kwargs)
        self.w = w
    def run(self):
        while True:
            if (self.w.stopflag): 
                self.w.stopflag = False
                break
            else:
                reading = ser.readline()
                if len(str(reading))>3:
                    z=reading.decode('utf-8')
                    t=z.split(',')
                    if len(t)!=17:
                        continue
                    misst.append(str(t[2]))
                    self.w.timer.append(str(t[2]))
                    self.w.altitude.append(float(t[4]))
                    self.w.temp.append(float(t[6])) 
                    self.w.pressure.append(float(t[3])) 
                    self.w.voltage.append(float(t[7])) 
                    self.w.gpsaltitude.append(float(t[10])) 
                    self.w.inishiz.append(float(t[5])) 
                    self.w.packetcount2.setText(t[1])
                    self.w.missiontime2.setText(t[2])
                    self.w.transform.Identity()
                    self.w.transform.RotateX(int(t[12]))
                    self.w.transform.RotateY(int(t[13]))
                    self.w.transform.RotateZ(int(t[14]))
                    self.w.transformFilter.SetTransform(self.w.transform)
                    self.w.transform.Update()
                    self.w.mapper.StaticOn()
                    self.w.transformFilter.Update()
                    self.w.ren.RemoveCuller(self.w.ren.GetCullers().GetLastItem())
                    self.w.actor.SetUserTransform(self.w.transform)
                    self.w.mapper.SetInputConnection(self.w.transformFilter.GetOutputPort())
                    self.w.vtkWidget.update()
                    self.w.koordinat.setText("PITCH:"+str(t[12])+"               ROLL:"+str(t[13])+"               YAW:"+str(t[14]))
                    if (len(t[11])==12 and self.w.z==0):
                        self.w.listem.addItem(t[11])
                        self.w.listem.setCurrentRow(self.w.z)
                        self.w.listem.item(self.w.z).setBackground(self.w.addg)
                        self.w.z+=1
                        self.prev=t[11]
                        self.w.stated.setText("Uydu Statüsü:"+str(t[11]))
                        QtCore.QMetaObject.invokeMethod(self.w.prog, "setValue", QtCore.Qt.QueuedConnection,QtCore.Q_ARG(int, self.w.z*20))
                    else:
                        if self.prev!=t[11]:
                            self.w.listem.addItem(t[11])
                            self.w.listem.item(self.w.z-1).setForeground(Qt.gray)
                            self.w.listem.setCurrentRow(self.w.z)
                            self.w.listem.item(self.w.z).setBackground(self.w.addg)
                            self.w.z+=1
                            self.w.stated.setText("Uydu Statüsü:"+str(t[11]))
                            QtCore.QMetaObject.invokeMethod(self.w.prog, "setValue",QtCore.Qt.QueuedConnection,QtCore.Q_ARG(int, self.w.z*20))
                            self.prev=t[11]
                    if len(misst)<6:
                        self.w.dates2.append(len(misst)-1)
                        self.w.data_line.setData(x=self.w.dates2, y=self.w.altitude,clear = True)
                        self.w.data_line2.setData(x=self.w.dates2, y=self.w.temp,clear = True)
                        self.w.data_line3.setData(x=self.w.dates2, y=self.w.pressure,clear = True)
                        self.w.data_line4.setData(x=self.w.dates2, y=self.w.voltage,clear = True)
                        self.w.data_line5.setData(x=self.w.dates2, y=self.w.gpsaltitude,clear = True)
                        self.w.data_line6.setData(x=self.w.dates2, y=self.w.inishiz,clear = True)
                    else:
                        del misst[0]
                        self.w.temp = self.w.temp[1:]
                        self.w.timer= self.w.timer[1:]  
                        self.w.altitude = self.w.altitude[1:]
                        self.w.pressure = self.w.pressure[1:]
                        self.w.voltage = self.w.voltage[1:]
                        self.w.gpsaltitude = self.w.gpsaltitude[1:]
                        self.w.inishiz = self.w.inishiz[1:]
                        self.w.data_line.setData(x=self.w.dates2, y=self.w.altitude,clear = True)
                        self.w.data_line2.setData(x=self.w.dates2, y=self.w.temp,clear = True)
                        self.w.data_line3.setData(x=self.w.dates2, y=self.w.pressure,clear = True)
                        self.w.data_line4.setData(x=self.w.dates2, y=self.w.voltage,clear = True)
                        self.w.data_line5.setData(x=self.w.dates2, y=self.w.gpsaltitude,clear = True)
                        self.w.data_line6.setData(x=self.w.dates2, y=self.w.inishiz,clear = True)
                        self.w.pw.plotItem.updateLogMode()
                        self.w.pw2.plotItem.updateLogMode()
                        self.w.pw3.plotItem.updateLogMode()
                        self.w.pw4.plotItem.updateLogMode()
                        self.w.pw5.plotItem.updateLogMode()
                        self.w.pw6.plotItem.updateLogMode()
                    try:
                        for sayi3 in range(0,17):
                            self.w.tableWidget2.item(0,sayi3).setData(Qt.BackgroundRole,Qt.blue)
                            self.w.tableWidget.item(0,sayi3).setData(Qt.BackgroundRole,Qt.blue)
                    except AttributeError:
                        print('START')
                    self.w.tableWidget2.insertRow(0)
                    self.w.tableWidget.insertRow(0)
                    for i in range(17):
                        self.w.tableWidget2.setItem(0,i,QTableWidgetItem(str(t[i])))
                        self.w.tableWidget.setItem(0,i,QTableWidgetItem(str(t[i])))
                    for sayi in range(0,17):
                        self.w.tableWidget2.item(0,sayi).setData(Qt.BackgroundRole, QColor (2, 232, 253))   
                        self.w.tableWidget.item(0,sayi).setData(Qt.BackgroundRole, QColor (2, 232, 253))   
        ser.close()
class DateAxis(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        strns = []
        if len(misst)==0:
            return strns
        for x in values:
            strns.append(misst[int(x)])
        return strns
if __name__=="__main__":
    app=QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())
class DateAxis(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        strns = []
        if len(misst)==0:
            return strns
        for x in values:
            strns.append(misst[int(x)])
        return strns
if __name__=="__main__":
    app=QApplication(sys.argv)
    pencere=Pencere()
    sys.exit(app.exec())