from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from ui_page_select_operation import Ui_PageSelectOperation
from dialogs.dialog_predlog import DialogPredlog


class PageSelectOperation(QWidget):
    btn_tokarnaya_clicked = Signal()
    btn_razmetka_clicked = Signal()
    btn_sverlilnaya_clicked = Signal()
    btn_tehno_iot_clicked = Signal()
    btn_sborka_clicked = Signal()
    btn_normirovanie_clicked = Signal()
    btn_kontrol_otk = Signal()
    btn_markirovanie = Signal()
    btn_shlifovanie = Signal()
    btn_otreznaya = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageSelectOperation()
        self.ui.setupUi(self)
        self.dialog = DialogPredlog()

        self.ui.btn_tokarnaya.clicked.connect(self._on_btn_tokarnaya_clicked)
        self.ui.btn_razmetka.clicked.connect(self._on_button_razmetka_clicked)
        self.ui.btn_sverlilnaya.clicked.connect(self._on_button_sverlilnaya_clicked)
        self.ui.btn_tehno_iot.clicked.connect(self._on_button_tehno_iot_clicked)
        self.ui.btn_sborka.clicked.connect(self._on_button_sborka_clicked)
        self.ui.btn_normirovanie.clicked.connect(self._on_button_normirovanie_clicked)
        self.ui.btn_kontrol_otk.clicked.connect(self._on_button_kontrol_otk_clicked)
        self.ui.btn_predlog.clicked.connect(self._on_btn_predlog_clicked)
        self.ui.btn_markirovanie.clicked.connect(self._on_btn_markirovanie_clicked)
        self.ui.btn_shlifovanie.clicked.connect(self._on_btn_shlifovanie_clicked)
        # Кнопка "ОТРЕЗНАЯ" в Designer имеет objectName btn_kontrol_otk_13
        self.ui.btn_kontrol_otk_13.clicked.connect(self._on_btn_otreznaya_clicked)

    def _on_btn_otreznaya_clicked(self):
        self.btn_otreznaya.emit()

    def _on_btn_shlifovanie_clicked(self):
        self.btn_shlifovanie.emit()

    def _on_btn_predlog_clicked(self):
        self.dialog.show()

    def _on_button_kontrol_otk_clicked(self):
        self.btn_kontrol_otk.emit()

    def _on_button_normirovanie_clicked(self):
        self.btn_normirovanie_clicked.emit()

    def _on_button_tehno_iot_clicked(self):
        self.btn_tehno_iot_clicked.emit()

    def _on_button_razmetka_clicked(self):
        self.btn_razmetka_clicked.emit()

    def _on_btn_tokarnaya_clicked(self):
        self.btn_tokarnaya_clicked.emit()

    def _on_button_sverlilnaya_clicked(self):
        self.btn_sverlilnaya_clicked.emit()

    def _on_button_sborka_clicked(self):
        self.btn_sborka_clicked.emit()

    def _on_btn_markirovanie_clicked(self):
        self.btn_markirovanie.emit()