# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImportLayerTree_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from qgis.gui import QgsLayerTreeView


class Ui_ImportLayerTreeDialogBase(object):
    def setupUi(self, ImportLayerTreeDialogBase):
        ImportLayerTreeDialogBase.setObjectName("ImportLayerTreeDialogBase")
        ImportLayerTreeDialogBase.resize(373, 548)
        self.vert_lay_global = QtWidgets.QVBoxLayout(ImportLayerTreeDialogBase)
        self.vert_lay_global.setObjectName("vert_lay_global")
        self.groupBox = QtWidgets.QGroupBox(ImportLayerTreeDialogBase)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox.setObjectName("groupBox")
        self.vert_lay_file = QtWidgets.QVBoxLayout(self.groupBox)
        self.vert_lay_file.setObjectName("vert_lay_file")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditPrj = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditPrj.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditPrj.setObjectName("lineEditPrj")
        self.horizontalLayout.addWidget(self.lineEditPrj)
        self.pushButtonPrj = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonPrj.setMinimumSize(QtCore.QSize(0, 23))
        self.pushButtonPrj.setMaximumSize(QtCore.QSize(31, 23))
        self.pushButtonPrj.setObjectName("pushButtonPrj")
        self.horizontalLayout.addWidget(self.pushButtonPrj)
        self.vert_lay_file.addLayout(self.horizontalLayout)
        self.vert_lay_global.addWidget(self.groupBox)

        ################################################################################################################
        # Aquí inserto QgsLayerTreeView. Con QgsProjectionSelectionTreeWidget() por ejemplo funciona bien
        self.tree_widget = QgsLayerTreeView(ImportLayerTreeDialogBase)
        self.vert_lay_global.addWidget(self.tree_widget)
        ################################################################################################################

        self.button_box = QtWidgets.QDialogButtonBox(ImportLayerTreeDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.vert_lay_global.addWidget(self.button_box)

        self.retranslateUi(ImportLayerTreeDialogBase)
        # self.button_box.accepted.connect(ImportLayerTreeDialogBase.accept)
        self.button_box.rejected.connect(ImportLayerTreeDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(ImportLayerTreeDialogBase)

    def retranslateUi(self, ImportLayerTreeDialogBase):
        _translate = QtCore.QCoreApplication.translate
        ImportLayerTreeDialogBase.setWindowTitle(_translate("ImportLayerTreeDialogBase", "Import Layer Tree"))
        self.groupBox.setTitle(_translate("ImportLayerTreeDialogBase", "Select Project File"))
        self.pushButtonPrj.setToolTip(_translate("ImportLayerTreeDialogBase", "Open project file"))
        self.pushButtonPrj.setText(_translate("ImportLayerTreeDialogBase", "..."))
