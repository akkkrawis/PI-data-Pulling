from PyQt5 import QtGui, QtCore,QtChart
from PyQt5.QtWidgets import *
from mydesignV3 import Ui_MainWindow

from popup import Ui_PreviewWindow

import pandas as pd
import datetime

#pyuic5 mydesignV3.ui -o mydesignV3.py
#pyuic5 mydesignV3_Popup.ui -o popup.py
#cd C:\Users\akkrawis\Desktop\Python\Mysql\ptong
#python gui.py

import sys
import clr   
import time

import subprocess

#from playsound import playsound

sys.path.append(r'C:\Program Files (x86)\PIPC\AF\PublicAssemblies\4.0')    
clr.AddReference('OSIsoft.AFSDK')  

from OSIsoft.AF import *  
from OSIsoft.AF.PI import *  
from OSIsoft.AF.Asset import *  
from OSIsoft.AF.Data import *  
from OSIsoft.AF.Time import *  
#from OSIsoft.AF.UnitsOfMeasure import *  
  
import numpy as np

print("Program Start")  
# PI Data Archive  
piServers = PIServers()    

df_read = pd.DataFrame()
df_inter = pd.DataFrame()
df_Try = pd.DataFrame()
trys = []
machinelist = []
serverlist = ["SKIC-PIserver","SKICWSPIDB01"]
Criteria = ["Equal","Greater than","Less than","Between","Greater or Equal","Less than or Equal","Not Equal"]
    
error = ['No Data','OFF','Sample Bad','Comm Fail','Bad','Cal Failed',\
         'Error','I/O Timeout','Not Connect','Scan Timeout'\
         ,'Configure','Intf Shut','Out of Serv','[-11059] No Good Data For Calculation']


spanlist = ['1m','10m','30m','1h','Other']
VariableSelect = ''

class Mypopup(QMainWindow):
    
    def __init__(self):
        super().__init__()
        global VariableSelect
        
        self.setWindowTitle("PreviewGraph: "+VariableSelect)
        self.setGeometry(100,100, 680,500)
 
        self.create_linechart()
 
    def create_linechart(self):
 
        series = QtChart.QLineSeries(self)
        for i in range(0,df_inter.shape[0]):
            dataadd = df_inter.loc[df_inter.index[i],VariableSelect]
            series.append(i,dataadd)
            
        chart =  QtChart.QChart()
 
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)
        chart.setTitle("Line Chart Example")
 
        chart.legend().setVisible(True)
        chart.legend().setAlignment(QtCore.Qt.AlignBottom)
 
 
        chartview = QtChart.QChartView(chart)
        chartview.setRenderHint(QtGui.QPainter.Antialiasing)
 
        self.setCentralWidget(chartview)

        self.show()
class MypopupFilter(QMainWindow):

    def __init__(self,row,datashow):
        super().__init__()
 
        self.datashow = datashow
        self.row = row
        self.setWindowTitle("PyQtChart Line")
        self.setGeometry(100,100, 680,500)
 
        self.create_linechart()
 
    def create_linechart(self):
 
        series = QtChart.QLineSeries(self)
        for i in range(0,self.datashow.shape[0]):
            dataadd = self.datashow.loc[self.datashow.index[i],self.datashow.columns[self.row]]
            series.append(i,dataadd)
            
        chart =  QtChart.QChart()
 
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)
        chart.setTitle("Line Chart Example")
 
        chart.legend().setVisible(True)
        chart.legend().setAlignment(QtCore.Qt.AlignBottom)
 
 
        chartview = QtChart.QChartView(chart)
        chartview.setRenderHint(QtGui.QPainter.Antialiasing)
 
        self.setCentralWidget(chartview)

        self.show()

class Previewdata(QMainWindow):

    def __init__(self,df_preview):
        super(Previewdata, self).__init__()

        self.preview = Ui_PreviewWindow()
        self.preview.setupUi(self)
        
        self.initWindow(df_preview)

    def initWindow(self,df_preview):

        self.preview.ExitButton.clicked.connect(self.ok)
        self.preview.Savebutton.clicked.connect(self.Saving)

        self.preview.PreviewTable.setRowCount(df_preview.shape[0])
        self.preview.PreviewTable.setColumnCount(df_preview.shape[1])
        self.preview.PreviewTable.setHorizontalHeaderLabels(df_preview.columns)  
        
        for row in range(0,df_preview.shape[0]): 
            for col in range(0,df_preview.shape[1]):
                item = str(df_preview.loc[df_preview.index[row],df_preview.columns[col]])
                cellinfo1=QTableWidgetItem(item) 
                self.preview.PreviewTable.setItem(row, col, cellinfo1) 
        label = []
        for i in df_preview.index:
            label.append(str(i))
        self.preview.PreviewTable.setVerticalHeaderLabels(label)
        self.preview.PreviewTable.resizeColumnsToContents()
        
        self.preview.Savebutton.clicked.connect(self.Saving)
        
        self.show()

    def ok(self):
        
        self.close()
 
    def Saving(self):
        print("Saving Button Click!")
        global df_inter
        
        filename, _  = QFileDialog.getSaveFileName(self, 
                                               'Single File',
                                               '*.xlsx')
        
        new_row = {}
        for i in range (0, df_read.shape[0]):
            new_row[df_filter.columns[i]] = df_read.index[i]
        
        df_new = pd.DataFrame(new_row, index =['Name'])
        df_new = df_new.append(df_filter, ignore_index=False)

        df_new.to_excel(filename)
        self.ui.label_4.setText("Save Complete")   
        
        msg = QMessageBox()
        msg.setText("Save File Complete!")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
        
class mywindow(QMainWindow):

    def __init__(self):
    
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)       


        self.ui.dateTimeEdit.setCalendarPopup(True)
        self.ui.dateTimeEdit_2.setCalendarPopup(True)
        
        YTD = datetime.date.today()+datetime.timedelta(-1)      
        self.YTD = QtCore.QDateTime(YTD)
        self.ui.dateTimeEdit.setDateTime(QtCore.QDateTime(YTD))
        
        self.ui.dateTimeEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.dateTimeEdit.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.ui.dateTimeEdit_2.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        
        
        self.ui.pushButton.setEnabled(False)
        self.ui.Try.setEnabled(False)
        self.ui.Try.setVisible(False)
        
        self.ui.Savebutton.setEnabled(False)
        
        self.ui.Value1.setEnabled(True)
        self.ui.Value2.setEnabled(False)
        self.ui.VariableBox.setEnabled(False)
        self.ui.CriteriaBox.setEnabled(False)
        
        self.ui.FilterCheck.setEnabled(False)
        self.ui.AvgCheck.setEnabled(False)
        self.ui.SDCheck.setEnabled(False)
        
        self.progress = self.ui.progressBar
        self.progress.setValue(0)
        
        
        for i in serverlist:
            self.ui.Server.addItem(i)
        
        for i in spanlist:
            self.ui.Spanlist.addItem(i)  
        
        for j in Criteria:
            self.ui.CriteriaBox.addItem(j)  
        
        self.ui.CriteriaBox.currentTextChanged.connect(self.criteriachange)
        
        self.ui.Spanlist.currentTextChanged.connect(self.SpanChange)
        
        self.ui.lineEdit.textEdited.connect(self.SpanOtherChange)
        
        self.ui.dateTimeEdit.dateTimeChanged.connect(self.dataChange)
        self.ui.dateTimeEdit_2.dateTimeChanged.connect(self.dataChange)
        self.ui.Server.currentTextChanged.connect(self.SpanChange)
        self.ui.Machine.currentTextChanged.connect(self.SpanChange)
        
        button = self.ui.pushButton
        button.clicked.connect(self.running)
        
        button2 = self.ui.pushButton2
        button2.clicked.connect(self.buttonexit)
        button2.clicked.connect(self.close)
        
        button3 = self.ui.Try
        button3.clicked.connect(self.trying)
        
        button4 = self.ui.Try_2
        button4.clicked.connect(self.checking)        

        button5 = self.ui.Savebutton
        button5.clicked.connect(self.Saving)
        
        button6 = self.ui.GraphShow
        button6.clicked.connect(self.showgraph)
        
        button7 = self.ui.FilRun
        button7.clicked.connect(self.filterrun)
        
        button8 =self.ui.BrownFile
        button8.clicked.connect(self.openfile)

        button9 =self.ui.MulFilRun
        button9.clicked.connect(self.FilterSave)

        button10 =self.ui.GenGraph
        button10.clicked.connect(self.GenGraphh)


        self.ui.Outlier.stateChanged.connect(self.outlierCheck) 
       
        self.ui.FilterCheck.stateChanged.connect(self.filterchange)
        self.ui.VariableBox.currentTextChanged.connect(self.VariableChange)
        
        self.ui.AvgCheck.stateChanged.connect(self.VariableChange)
        self.ui.SDCheck.stateChanged.connect(self.VariableChange)
        
        self.ui.label_4.setText("")
        self.ui.label_4.setFont(QtGui.QFont('SansSerif', 14))
        
        self.ui.lineEdit.setEnabled(False)
        
        self.ui.Try_2.setEnabled(False)
        
        self.ui.tabWidget.setTabEnabled(1,False)
        self.ui.tabWidget.setTabEnabled(2,False)
        self.spantime = str(self.ui.Spanlist.currentText())
        
    def openfile(self):
        global df_read
        
        self.machinelist = []
        
        filename, _  = QFileDialog.getOpenFileName(self, 
                                               'Single File',
                                               '*.xlsx')
                
        df_read = pd.DataFrame()
        df_read = pd.read_excel(filename,index_col=0,sheet_name='Sheet1',header=0)
        
        for i in df_read.columns:
            self.machinelist.append(i)
            
        self.ui.Machine.clear()
        for j in self.machinelist:
            self.ui.Machine.addItem(j)
        self.ui.Machine.addItem("All")
        
        self.ui.fliepath.setText(filename)
            
        self.ui.Try_2.setEnabled(True)
    def dataChange(self):
        self.ui.pushButton.setEnabled(False)
        
    def SpanChange(self):
        if str(self.ui.Spanlist.currentText()) == "Other":
            self.ui.lineEdit.setEnabled(True)
            self.spantime = str(self.ui.lineEdit.text())
        else:
            self.ui.lineEdit.setEnabled(False)
            self.spantime = str(self.ui.Spanlist.currentText())      
        self.ui.pushButton.setEnabled(False)
    def SpanOtherChange(self):
        self.spantime = str(self.ui.lineEdit.text())
        self.ui.pushButton.setEnabled(False)
    def criteriachange(self):
        
        self.criteriaText =  str(self.ui.CriteriaBox.currentText())
        
        if self.criteriaText == "Equal":
            self.ui.Value1.setEnabled(True)
            self.ui.Value2.setEnabled(False)
            self.ui.label_12.setText("Value = ")
        elif self.criteriaText == "Greater than":
            self.ui.Value1.setEnabled(True)
            self.ui.Value2.setEnabled(False)
            self.ui.label_12.setText("Value > ")
        elif self.criteriaText == "Less than":
            self.ui.Value1.setEnabled(True)
            self.ui.Value2.setEnabled(False)
            self.ui.label_12.setText("Value < ")
        elif self.criteriaText == "Between":
            self.ui.Value1.setEnabled(True)
            self.ui.Value2.setEnabled(True)
            self.ui.label_12.setText("Value <-> ")
        elif self.criteriaText == "Greater or Equal":
            self.ui.Value1.setEnabled(True)
            self.ui.Value2.setEnabled(False)
            self.ui.label_12.setText("Value >= ")
        elif self.criteriaText == "Less than or Equal":            
            self.ui.Value1.setEnabled(True)
            self.ui.Value2.setEnabled(False)
            self.ui.label_12.setText("Value <= ")
        elif self.criteriaText == "Not Equal":            
            self.ui.Value1.setEnabled(True)
            self.ui.Value2.setEnabled(False)
            self.ui.label_12.setText("Value != ")
# In[5]:  
    def buttonexit(self):
        QApplication.instance().quit()
# In[5]:      
    def checking(self):
        print("Checking Button Click!")
        self.progress.setValue(0)
        global trys,df_inter,Group
        
        trys = []
        
        self.ui.label_4.setText("Checking")
        
        Server = str(self.ui.Server.currentText())
        Machine =  str(self.ui.Machine.currentText())       
        
        ServerBP = ['PB11','PB12','PB16','PB19','PB17','TG11','TG12','TG16','TG19','TG17']
        ServerWS = ['PB14','PB18','TG5','TG6','TG14']
        ["SKIC-PIserver","SKICWSPIDB01"]
        
        if Server == 'SKIC-PIserver':
            for MachineOne in machinelist:
                if not MachineOne.rstrip() in ServerBP:
                    self.ui.label_4.setText("Wrong Server")
                    print('1')
                    return "Error"  
        elif Server == 'SKICWSPIDB01':
            for MachineOne in machinelist:
                print(MachineOne)
                if not MachineOne.rstrip() in ServerWS:
                    self.ui.label_4.setText("Wrong Server")
                    print('2')
                    return "Error"   
                
        preGroup = df_read.dropna()
        preGroup = preGroup.reset_index()
        
        Group = pd.DataFrame()
        Group['Name'] = ""
        Group['PI Tag'] = ""
    
        
        if Machine == 'All':
            for com in range(0,len(machinelist)):
                MachineOne = machinelist[0]
                for ind in range(0,df_read.shape[0]):
                    nameNew = MachineOne+' '+preGroup.loc[preGroup.index[ind],'Name']
                    PitagNew = preGroup.loc[preGroup.index[ind],MachineOne]
                    new_row = {'Name':nameNew,'PI Tag':PitagNew}
                    Group = Group.append(new_row, ignore_index=True)
        else:
            for ind in range(0,df_read.shape[0]):
                nameNew = Machine+' '+preGroup.loc[preGroup.index[ind],'Name']
                PitagNew = preGroup.loc[preGroup.index[ind],Machine]
                new_row = {'Name':nameNew,'PI Tag':PitagNew}
                Group = Group.append(new_row, ignore_index=True)
            
        Group['Status'] = "Waiting"
        Group['Enable'] = ""    
        
        self.ui.tableWidget.setRowCount(Group.shape[0])
        self.ui.tableWidget.setColumnCount(Group.shape[1])
        self.ui.tableWidget.setHorizontalHeaderLabels(Group.columns)        
        
        label = []
        
        for i in Group.index:
            label.append(str(i))
        self.ui.tableWidget.setVerticalHeaderLabels(label)
            
        for row in range(0,Group.shape[0]): 
            for col in range(0,Group.shape[1]):
                item = str(Group.loc[Group.index[row],Group.columns[col]])
                cellinfo=QTableWidgetItem(item) 
                self.ui.tableWidget.setItem(row, col, cellinfo)        
        
        for row in range(0,Group.shape[0]):
            item = QTableWidgetItem('Enable')
            item.setFlags(QtCore.Qt.ItemIsUserCheckable |QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Checked)        
            self.ui.tableWidget.setItem(row, 3, item)
      
       
        self.ui.tableWidget.setColumnWidth(2, 140)
        
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
#        header.setSectionResizeMode(2, 5)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        
        self.ui.tableWidget.itemClicked.connect(self.handleItemClicked)
        layout = QVBoxLayout(self)
        layout.addWidget(self.ui.tableWidget)
        self._list = []
        
        start_time = '"'+str(self.ui.dateTimeEdit.text())+'"'
        end_time = '"'+str(self.ui.dateTimeEdit_2.text())+'"'
        print(start_time)
        print(end_time)

        date_time_obj = datetime.datetime.strptime(self.ui.dateTimeEdit_2.text(), '%Y-%m-%d %H:%M:%S')


        
        wifitest = str(subprocess.check_output("netsh wlan show interfaces"))
        namewifi = "SCGconnect"
        
        if not namewifi in wifitest:
            self.ui.label_4.setText("Wrong WIFI Server")
            return "Error"
        
        if self.ui.dateTimeEdit_2.text()== self.ui.dateTimeEdit.text():
            self.ui.label_4.setText("DateTime Error Please Try Again")
            return "Error"
        else:
            self.ui.label_4.setText("Okay")
            if date_time_obj>datetime.datetime.now():
                dt = datetime.datetime.now()
                dt = dt.strftime('%Y-%m-%d %H:%M:%S')
                end_time = '"'+str(dt)+'"'
        
        if self.spantime == "":
            self.ui.label_4.setText("Span Time Error Please Try Again")
            return "Error"        
        
        self.start_time = start_time
        self.end_time = end_time
                
        self.ui.pushButton.setEnabled(True)

# In[5]:          
    def handleItemClicked(self, item):
        if item.checkState() == QtCore.Qt.Checked:
            print('"%s" Checked' % item.text())
            self._list.append(item.row())
            print(self._list)
        else:
            print('"%s" Clicked' % item.text())
            
# In[5]:              

    def GenGraphh(self):
        global df_filter
        self.popupwindow = testpychart(df_filter)  
    def running(self):
        print("Running Button Click!")
        global trys,df_inter,Group
        
        trys = []
        

        
        span = AFTimeSpan.Parse(self.spantime) 
        timerange = AFTimeRange(self.start_time, self.end_time) 
        
        
        Server = str(application.ui.Server.currentText())
        Machine =  str(application.ui.Machine.currentText())
        print(Server)
        print(Machine)
        
        self.serveruse1 = piServers[Server]
        
        self.Groupuse = []
        for i in range(0,Group.shape[0]):
            if self.ui.tableWidget.item(i,3).checkState()== QtCore.Qt.Checked:
                self.Groupuse.append(i)
        print(self.Groupuse)
        rnd = 0
        self.completed = 0
        self.updatecompleted = 100/len(self.Groupuse)
        
        while rnd < Group.shape[0]:
            
            if not rnd in self.Groupuse:
                rnd +=1
                continue
            
            status = '' 
            tagname = Group.loc[Group.index[rnd],Group.columns[1]]
            name = Group.loc[Group.index[rnd],Group.columns[0]] 
            listname = []
            listname.append(tagname)
            try:
                pt1 = PIPoint.FindPIPoint(self.serveruse1, tagname)
            except:
                status = "PI POINT NOT FOUND"
                Group.loc[Group.index[rnd],"Status"] =status
                cellinfo=QTableWidgetItem(status) 
                self.ui.tableWidget.setItem(rnd, 2, cellinfo)
                trys.append(rnd)
                rnd += 1
#                self.ui.tableWidget.resizeColumnsToContents()
                continue
            try:
                interpolated1 = pt1.InterpolatedValues(timerange, span, "", False)
            except:
                status = "Network Error"
                Group.loc[Group.index[rnd],"Status"] =status
                cellinfo=QTableWidgetItem(status) 
                self.ui.tableWidget.setItem(rnd, 2, cellinfo)
                trys.append(rnd)
                rnd += 1
#                self.ui.tableWidget.resizeColumnsToContents()
                continue
            print("Pulling...")
            
            times = []
            vals =[]
            datapi = {}
            
            for event in interpolated1 :
                if (str(event.Value) in error):
                    datapi[str(event.Timestamp.LocalTime)] = np.nan
                    print(str(event.Value))
                else:
                    try:
                        datapi[str(event.Timestamp.LocalTime)] = float(event.Value)
                    except:
                        datapi[str(event.Timestamp.LocalTime)] = str(event.Value)
                        print(event.Value)
                        
                times.append(str(event.Timestamp.LocalTime))
                vals.append(event.Value)
            
            if rnd == 0:
                df_inter = pd.DataFrame.from_dict(datapi, orient='index',columns=listname)
            else:
                df_inter.insert(df_inter.shape[1],tagname,datapi.values())
            
            status = "COMPLETE"
            Group.loc[Group.index[rnd],"Status"] =status
            cellinfo = QTableWidgetItem(status) 
            self.ui.tableWidget.setItem(rnd, 2, cellinfo)
            time.sleep(0.2)
            rnd += 1
            
            self.completed = self.completed + self.updatecompleted
            self.progress.setValue(self.completed)
#            self.ui.tableWidget.resizeColumnsToContents()
        msg = QMessageBox()
        if len(trys) == 0:
            self.finished()
            msg.setWindowTitle("Popup")
            msg.setText("Pulling Successfully!")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
            
        else:
            msg.setWindowTitle("Popup")
            msg.setText("Some Parameter Error")
            msg.setInformativeText("Please Try Again!")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
            
            self.ui.Try.setEnabled(True)
            self.ui.Try.setVisible(True)
            self.ui.label_4.setText("Try Again")
        self.ui.pushButton.setEnabled(False)
        print("Finish Pulling")
        
# In[3]:    
    def finished(self):
        global df_filter,df_inter
        
        df_filter = df_inter
        #playsound('soundtest.mp3')
        
        self.ui.tabWidget.setTabEnabled(1,True)
        self.ui.tabWidget.setTabEnabled(2,True)
        
        self.ui.Savebutton.setEnabled(True)
        self.ui.label_4.setText("Complete")
            
        self.ui.VariableBox.setEnabled(True)
        self.ui.CriteriaBox.setEnabled(True)
        
        self.ui.FilterCheck.setEnabled(True)
        self.ui.AvgCheck.setEnabled(True)
        self.ui.SDCheck.setEnabled(True)
        
        self.ui.tableWidget_2.setRowCount(10)
        self.ui.tableWidget_2.setColumnCount(df_inter.shape[1])
        self.ui.tableWidget_2.setHorizontalHeaderLabels(df_inter.columns)  
        
        
        for j in df_inter.columns:
            self.ui.VariableBox.addItem(j) 
        for row in range(0,10): 
            for col in range(0,df_inter.shape[1]):

                item = str(df_inter.loc[df_inter.index[row],df_inter.columns[col]])
                cellinfo1=QTableWidgetItem(item) 
                self.ui.tableWidget_2.setItem(row, col, cellinfo1) 
        self.ui.tableWidget_2.resizeColumnsToContents()
        label2 = []
        for i in df_inter.index:
            label2.append(str(i))
        self.ui.tableWidget_2.setVerticalHeaderLabels(label2)
        
        test = self.multifilterpage()
# In[3]:       
    def trying(self):
        print("Trying Button Click!")
        global trys,df_inter,Group
        
        span = AFTimeSpan.Parse(self.spantime)        
        timerange = AFTimeRange(self.start_time, self.end_time) 
                                          
        for rnd in trys:
            status = 0
            tagname = Group.loc[Group.index[rnd],Group.columns[1]]
            name = Group.loc[Group.index[rnd],Group.columns[0]] 
            
            try:
                pt1 = PIPoint.FindPIPoint(self.serveruse1, tagname)
            except:
                status = "PI POINT NOT FOUND"
                Group.loc[Group.index[rnd],"Status"] =status
                cellinfo=QTableWidgetItem(status) 
                self.ui.tableWidget.setItem(rnd, 2, cellinfo)
                continue
            try:
                interpolated1 = pt1.InterpolatedValues(timerange, span, "", False)
            except:
                status = "Network Error"
                Group.loc[Group.index[rnd],"Status"] =status
                cellinfo=QTableWidgetItem(status) 
                self.ui.tableWidget.setItem(rnd, 2, cellinfo)
                continue
            print("Pulling...")
            
            times = []
            vals =[]
            datapi = {}
            
            for event in interpolated1 :
                if (str(event.Value) in error):
                    datapi[str(event.Timestamp.LocalTime)] = np.nan
                else:
                    try:
                        datapi[str(event.Timestamp.LocalTime)] = float(event.Value)
                    except:
                        datapi[str(event.Timestamp.LocalTime)] = str(event.Value)
                        print(event.Value)
                times.append(str(event.Timestamp.LocalTime))
                vals.append(event.Value)
                        
            if rnd == 0:
                df_Try = pd.DataFrame.from_dict(datapi, orient='index',columns=[tagname])
            else:
                df_Try.insert(df_Try.shape[1],tagname,datapi.values())
            
            df_inter.insert(df_inter.shape[1],tagname,df_Try[df_Try.columns[rnd]])
            
            status = "COMPLETE"
            Group.loc[Group.index[rnd],"Status"] =status
            cellinfo = QTableWidgetItem(status) 
            self.ui.tableWidget.setItem(rnd, 2, cellinfo)
            
            self.completed = self.completed + self.updatecompleted
            self.progress.setValue(self.completed)
            
        
        
        trys2 = []
        for row in trys:
            status = Group.loc[Group.index[rnd],"Status"]
            if not status == "COMPLETE":
                  trys2.append(row) 
        trys.clear()
        trys = trys2
        if len(trys)==0:
            self.finished()
# In[5]:  
    def Saving(self):
        print("Saving Button Click!")
        global df_inter
        
        filename, _  = QFileDialog.getSaveFileName(self, 
                                               'Single File',
                                               '*.xlsx')
        
        new_row = {}
        for i in range (0, df_read.shape[0]):
            new_row[df_inter.columns[i]] = df_read.index[i]
        
        df_new = pd.DataFrame(new_row, index =['Name'])
        df_new = df_new.append(df_inter, ignore_index=False)

        df_new.to_excel(filename)
        self.ui.label_4.setText("Save Complete")
        
        msg = QMessageBox()
        msg.setText("Save File Complete!")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
        
    def filterchange(self):
        if self.ui.FilterCheck.isChecked():
            print("Filter Checked")
        else:
            print("Filter UnChecked")
    def VariableChange(self):
        global VariableSelect
        print("Variable Change")
        VariableSelect = str(self.ui.VariableBox.currentText())
        if self.ui.AvgCheck.isChecked():              
            meanVariable = df_inter[VariableSelect].mean()       
            self.ui.AvgNum.setProperty("value", meanVariable)
        else:
            self.ui.AvgNum.setProperty("value", 0.0)
        
        if self.ui.SDCheck.isChecked():  
            SDVariable = df_inter[VariableSelect].std()       
            self.ui.SDNum.setProperty("value", SDVariable)
        else:
            self.ui.SDNum.setProperty("value", 0.0)
    def showgraph(self):
        
        self.popupwindow = Mypopup()
        

    def showgraph2(self):
        global df_filter
        
        combo = self.sender()
        row = combo.property('row')
        
        self.popupwindow = MypopupFilter(row,df_filter)    
        
    def filterrun(self):
        
        global df_filter
        df_filter = pd.DataFrame()
        df_filter = df_inter
        print("Filter Running")
        
        Value1 = (self.ui.Value1.text())
        Value2 = (self.ui.Value2.text())  
        
        self.ValueFilter1 = float(Value1)
        self.ValueFilter2 = float(Value2)
        
        print(self.ValueFilter1,self.ValueFilter2)
        
        self.criteriaText =  str(self.ui.CriteriaBox.currentText())
        
        if self.criteriaText == "Equal":
            df_filter = df_inter[df_inter[VariableSelect]==self.ValueFilter1]

        elif self.criteriaText == "Greater than":
            df_filter = df_inter[df_inter[VariableSelect]>self.ValueFilter1]

        elif self.criteriaText == "Less than":
            df_filter = df_inter[df_inter[VariableSelect]<self.ValueFilter1]
            
        elif self.criteriaText == "Between":
            df_filter = df_inter[(df_inter[VariableSelect]>self.ValueFilter1) & (df_inter[VariableSelect]<self.ValueFilter2)]
        elif self.criteriaText == "Greater or Equal":
            df_filter = df_inter[df_inter[VariableSelect]>=self.ValueFilter1]

        elif self.criteriaText == "Less than or Equal":  
            df_filter = df_inter[df_inter[VariableSelect]<=self.ValueFilter1]

        elif self.criteriaText == "Not Equal":   
            df_filter = df_inter[df_inter[VariableSelect]!=self.ValueFilter1]

        self.Previewwindow = Previewdata(df_filter)
        
    def multifilterpage(self):
        
        self.ui.tableWidget_3.setRowCount(len(self.Groupuse))
        
        rnd = 0      
        for row in range(0,Group.shape[0]): 
            
            if not row in self.Groupuse:
                continue
            
            item = QTableWidgetItem('Enable')
            item.setFlags(QtCore.Qt.ItemIsUserCheckable |QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Unchecked)        
            self.ui.tableWidget_3.setItem(rnd, 0, item)    

            item = str(Group.loc[Group.index[row],'Name'])
            cellinfo1=QTableWidgetItem(item) 
            cellinfo1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
            self.ui.tableWidget_3.setItem(rnd, 1, cellinfo1) 
        
            item = str(Group.loc[Group.index[row],'PI Tag'])
            cellinfo=QTableWidgetItem(item) 
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
            self.ui.tableWidget_3.setItem(rnd, 2, cellinfo)       
            
           
            self.combo = QComboBox()      
            
            for t in Criteria:
                self.combo.addItem(t)
            self.combo.setProperty('row', rnd)
            self.combo.currentIndexChanged.connect(self.CriteriaMultiChange)
            
            self.ui.tableWidget_3.setCellWidget(rnd, 3, self.combo)        
        
            itemsign = '='
            cellinfo=QTableWidgetItem(itemsign) 
            cellinfo.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
            self.ui.tableWidget_3.setItem(rnd, 4, cellinfo)
            
            itemEn = QTableWidgetItem('0')
            brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
            brush.setStyle(QtCore.Qt.SolidPattern)
            itemEn.setBackground(brush)
            self.ui.tableWidget_3.setItem(rnd, 5, itemEn)
            
            itemEn = QTableWidgetItem('100')
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
            brush.setStyle(QtCore.Qt.SolidPattern)
            itemEn.setBackground(brush)
            itemEn.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
            self.ui.tableWidget_3.setItem(rnd, 6, itemEn)

            meanValue = df_inter[df_inter.columns[rnd]].mean()
            itemEn = QTableWidgetItem(str(round(meanValue,3)))
            itemEn.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
            self.ui.tableWidget_3.setItem(rnd, 7, itemEn)
            
            stdValue = df_inter[df_inter.columns[rnd]].std()
            itemEn = QTableWidgetItem(str(round(stdValue,3)))
            itemEn.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
            self.ui.tableWidget_3.setItem(rnd, 8, itemEn)
            
            self.Push = QPushButton()
            self.Push.setText("Show Graph")
            self.Push.setProperty('row', row)
            self.Push.clicked.connect(self.showgraph2)
            self.ui.tableWidget_3.setCellWidget(rnd, 9, self.Push)       
            
            rnd +=1
            
        self.ui.tableWidget_3.resizeColumnsToContents()
    
        #self.ui.tableWidget_3.cellWidget(0, 3).currentTextChanged.connect(self.CriteriaMultiChange)
        #self.ui.tableWidget_3.cellWidget(0, 3).currentTextChanged.emit(item)
        
        self.ui.tableWidget_3.itemChanged.connect(self.CriteriaValueChangeV2)
                
        
    def CriteriaMultiChange(self,item):
        print("Change Criteria of MultiFilter")
        combo = self.sender()
        row = combo.property('row')
        index = combo.currentIndex()
        criteriaselect = combo.currentText()
                        
        if criteriaselect == "Equal":
            itemsign = '='
            self.Colortable(0,row)
            
        elif criteriaselect == "Greater than":
            itemsign = '>'            
            self.Colortable(0,row)
            
        elif criteriaselect == "Less than":
            itemsign = '<'
            self.Colortable(0,row)
            
        elif criteriaselect == "Between":
            itemsign = '<->'                        
            self.Colortable(1,row)      
            
        elif criteriaselect == "Greater or Equal":
            itemsign = '>='            
            self.Colortable(0,row)
            
        elif criteriaselect == "Less than or Equal":   
            itemsign = '<='            
            self.Colortable(0,row)
            
        elif criteriaselect == "Not Equal":            
            itemsign = '!='            
            self.Colortable(0,row)

        cellinfo=QTableWidgetItem(itemsign) 
        cellinfo.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
        self.ui.tableWidget_3.setItem(row, 4, cellinfo)  

    def Colortable(self,boolean,row):
               
        itemEn = QTableWidgetItem()
        
        if boolean == 1:
            brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
            brush.setStyle(QtCore.Qt.SolidPattern)
            itemEn.setBackground(brush)
            itemEn.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        else:
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
            brush.setStyle(QtCore.Qt.SolidPattern)
            itemEn.setBackground(brush)
            itemEn.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        
        self.ui.tableWidget_3.setItem(row, 6, itemEn)
    
    def outlierCheck(self):
        global Inlier
        row = 4
        q1 = df_inter[df_inter.columns[row]].quantile(0.25)
        q3 = df_inter[df_inter.columns[row]].quantile(0.75)
        IQR = q3 - q1
        print('IQR:',IQR)
        print(df_inter.shape)
        #print(df_inter[df_inter.columns[5]] < (q1 - 1.5 * IQR)) |(df_inter[df_inter.columns[5]] > (q3 + 1.5 * IQR))
        self.Inlier = df_inter[(df_inter[df_inter.columns[row]] > (q1 - (1.5 * IQR))) & (df_inter[df_inter.columns[row]] < (q3 + (1.5 * IQR)))]
        Inlier = self.Inlier
        print(self.Inlier.shape)
        
        self.popupwindow = MypopupFilter(4,self.Inlier)
    def FilterSave(self):
        
        print("Saving Button Click!")
        global df_filter
        
        df_filter_Save = pd.DataFrame()

        if self.ui.DropNa.isChecked():
            print("Drop Text")
            df_filter_Save = df_filter.dropna()
        else:
            df_filter_Save = df_filter

        if self.ui.Outlier.isChecked():
            print("Drop Outlier")
            df_filter_Save = df_filter_Save.dropna()
        else:
            df_filter_Save = df_filter_Save
            
        filename, _  = QFileDialog.getSaveFileName(self, 
                                               'Single File',
                                               '*.xlsx')
        
        new_row = {}
        for i in range (0, df_read.shape[0]):
            new_row[df_filter_Save.columns[i]] = df_read.index[i]
        
        df_new = pd.DataFrame(new_row, index =['Name'])
        df_new = df_new.append(df_filter_Save, ignore_index=False)

        df_new.to_excel(filename)
        self.ui.label_4.setText("Save Complete")
        
        msg = QMessageBox()
        msg.setText("Save File Complete!")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
        
    def CriteriaValueChange(self,item):
        global df_filter
        
        if (item.column() == 5 or item.column() == 6):
            print("Criteria Value Changed")
            
            row = item.row()
            multicriteriaText = self.ui.tableWidget_3.cellWidget(row, 3).currentText()
      
            Cvalue1_txt = self.ui.tableWidget_3.item(row,5).text()
            Cvalue2_txt = self.ui.tableWidget_3.item(row,6).text()
            
            Cvalue1 = float(Cvalue1_txt)
            try:        
                Cvalue2 = float(Cvalue2_txt)
            except:
                Cvalue2 = 0
            
            
            if multicriteriaText == "Equal":
                df_filter = df_inter[df_inter[df_inter.columns[row]]==Cvalue1][df_inter.columns[row]]
    
            elif multicriteriaText == "Greater than":
                df_filter = df_inter[df_inter[df_inter.columns[row]]>Cvalue1][df_inter.columns[row]]
    
            elif multicriteriaText == "Less than":
                df_filter = df_inter[df_inter[df_inter.columns[row]]<Cvalue1][df_inter.columns[row]]
                
            elif multicriteriaText == "Between":
                df_filter = df_inter[(df_inter[df_inter.columns[row]]>Cvalue1) & (df_inter[df_inter.columns[row]]<Cvalue2)][df_inter.columns[row]]
    
            elif multicriteriaText == "Greater or Equal":
                df_filter = df_inter[df_inter[df_inter.columns[row]]>=Cvalue1][df_inter.columns[row]]
    
            elif multicriteriaText == "Less than or Equal":  
                df_filter = df_inter[df_inter[df_inter.columns[row]]<=Cvalue1][df_inter.columns[row]]
    
            elif multicriteriaText == "Not Equal":   
                df_filter = df_inter[df_inter[df_inter.columns[row]]!=Cvalue1][df_inter.columns[row]]
            
            itemEn = QTableWidgetItem(str(round(df_filter.mean(),3)))
            itemEn.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
            self.ui.tableWidget_3.setItem(row, 7, itemEn)       
    
            itemEn = QTableWidgetItem(str(round(df_filter.std(),3)))
            itemEn.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
            self.ui.tableWidget_3.setItem(row, 8, itemEn)         
    
    def CriteriaValueChangeV2(self,item):
        global df_filter
        if (item.column() == 5 or item.column() == 6):
            df_filter = df_inter
            for row in range(0,df_filter.shape[1]):
                enables = self.ui.tableWidget_3.item(row, 0).checkState()
                if enables == QtCore.Qt.Checked:
                    print("Filter Start")
                    multicriteriaText = self.ui.tableWidget_3.cellWidget(row, 3).currentText()

                    Cvalue1_txt = self.ui.tableWidget_3.item(row,5).text()
                    Cvalue2_txt = self.ui.tableWidget_3.item(row,6).text()
                    
                    Cvalue1 = float(Cvalue1_txt)
                    try:        
                        Cvalue2 = float(Cvalue2_txt)
                    except:
                        Cvalue2 = 0
            
                    if multicriteriaText == "Equal":
                        df_filter = df_filter[df_filter[df_filter.columns[row]]==Cvalue1]
                    
                    elif multicriteriaText == "Greater than":
                        df_filter = df_filter[df_filter[df_filter.columns[row]]>Cvalue1]
                    
                    elif multicriteriaText == "Less than":
                        df_filter = df_filter[df_filter[df_filter.columns[row]]<Cvalue1]
                        
                    elif multicriteriaText == "Between":
                        df_filter = df_filter[(df_filter[df_filter.columns[row]]>Cvalue1) & (df_filter[df_filter.columns[row]]<Cvalue2)]
                    
                    elif multicriteriaText == "Greater or Equal":
                        df_filter = df_filter[df_filter[df_filter.columns[row]]>=Cvalue1]
                    
                    elif multicriteriaText == "Less than or Equal":  
                        df_filter = df_filter[df_filter[df_filter.columns[row]]<=Cvalue1]
                    
                    elif multicriteriaText == "Not Equal":   
                        df_filter = df_filter[df_filter[df_filter.columns[row]]!=Cvalue1]
            
            for row in range(0,df_filter.shape[1]):
                filtershow_mean = df_filter[df_filter.columns[row]].mean()
                filtershow_sd = df_filter[df_filter.columns[row]].std()
                
                itemEn = QTableWidgetItem(str(round(filtershow_mean,3)))
                itemEn.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                self.ui.tableWidget_3.setItem(row, 7, itemEn)       
        
                itemEn = QTableWidgetItem(str(round(filtershow_sd,3)))
                itemEn.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                self.ui.tableWidget_3.setItem(row, 8, itemEn)      
# In[4]:  
def main():
    global application
    app = QApplication(sys.argv)
    application = mywindow()
    application.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
    
