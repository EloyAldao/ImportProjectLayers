# coding=utf-8
import os

from PyQt5 import QtWidgets
from qgis.core import *
from .ImportLayerTree_dialog import ImportLayerTreeDialog


class ILT_Manager:
    def __init__(self):
        self.dialog = ImportLayerTreeDialog()
        # self.dialog.tree_widget = QgsLayerTreeView()
        # self.dialog.tree_widget.setMinimumSize(QtCore.QSize(200, 200))
        self.wid = self.dialog.tree_widget
        self.dialog.open()

        self.curr_project = QgsProject.instance()
        self.signals_slots()

    def signals_slots(self):
        self.dialog.pushButtonPrj.clicked.connect(self.load_project)
        self.dialog.button_box.accepted.connect(self.set_widget)

    def load_project(self):
        dlg = QtWidgets.QFileDialog()
        project_file = dlg.getOpenFileName(None, "Select Project", 'D:/', "QGis Projects (*.qgz *.qgs);;*.*")
        if project_file is not None:
            self.dialog.lineEditPrj.setText(project_file[0])
            # self.set_widget()
            # print(project_file)
            # self.current_dir = os.path.dirname(project_file)
        # else:
        #     self.lineEditGPS.clear()

    def set_widget(self):
        read_project = QgsProject()
        read_project.read(self.dialog.lineEditPrj.text())

        tree_root = read_project.layerTreeRoot()

        tree_model = QgsLayerTreeModel(tree_root)
        self.wid.setModel(tree_model)
        # self.dialog.tree_widget.selectedNodes()

