# main_window.py
from PySide6.QtWidgets import QMainWindow
from controllers.razmetka_controller import RazmetkaController
from controllers.tokarnaya_controller import TokarnayaController
from controllers.sverlilnaya_controller import SverlilnayaController
from controllers.tehno_iot_controller import TehnoIotController
from controllers.sborka_controller import SborkaController
from controllers.normirovanie_controller import NormirovanieController
from controllers.kontrol_otk_controller import KontrolOtkController
from controllers.SlesarnieControllers.markirovanie_controller import MarkirovanieController
from controllers.shlifovanie_controller import ShlifovanieController
from controllers.otreznaya_controller import OtreznayaController
from ui_autoinput import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        # Инициализируем контроллеры
        self.tokarnaya_ctrl = TokarnayaController(self.ui)
        self.razmetka_ctrl = RazmetkaController(self.ui)
        self.sverlilnaya_ctrl = SverlilnayaController(self.ui)
        self.tehno_iot_ctrl = TehnoIotController(self.ui)
        self.sborka_ctrl = SborkaController(self.ui)
        self.normirovanie_ctrl = NormirovanieController(self.ui)
        self.kotrol_otk_ctrl = KontrolOtkController(self.ui)
        self.markirovanie = MarkirovanieController(self.ui)
        self.shlifovanie_ctrl = ShlifovanieController(self.ui)
        self.otreznaya_ctrl = OtreznayaController(self.ui)


        # Активный контроллер (тот, из которого перешли в Technopro)
        self.active_controller = None


        self._connect_global_signals()

    def _connect_global_signals(self):
        # 1. Переход из главного меню в операцию
        self.ui.page_select_operation.btn_tokarnaya_clicked.connect(
            lambda: self._activate_controller(self.tokarnaya_ctrl)
        )
        self.ui.page_select_operation.btn_razmetka_clicked.connect(
            lambda: self._activate_controller(self.razmetka_ctrl)
        )
        self.ui.page_select_operation.btn_sverlilnaya_clicked.connect(
            lambda: self._activate_controller(self.sverlilnaya_ctrl)
        )
        # 1.1 Переход из главного меню в заполнение оборудования
        self.ui.page_select_operation.btn_tehno_iot_clicked.connect(
            lambda: self._activate_controller(self.tehno_iot_ctrl)
        )
        self.ui.page_select_operation.btn_sborka_clicked.connect(
            lambda: self._activate_controller(self.sborka_ctrl)
        )
        self.ui.page_select_operation.btn_normirovanie_clicked.connect(
            lambda: self._activate_controller(self.normirovanie_ctrl)
        )
        self.ui.page_select_operation.btn_kontrol_otk.connect(
            lambda: self._activate_controller(self.kotrol_otk_ctrl)
        )
        self.ui.page_select_operation.btn_markirovanie.connect(
            lambda: self._activate_controller(self.markirovanie)
        )
        self.ui.page_select_operation.btn_shlifovanie.connect(
            lambda: self._activate_controller(self.shlifovanie_ctrl)
        )
        self.ui.page_select_operation.btn_otreznaya.connect(
            lambda: self._activate_controller(self.otreznaya_ctrl)
        )


        # 2. Возврат в главное меню
        self.tokarnaya_ctrl.exit_to_main_menu_requested.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0)
        )
        self.razmetka_ctrl.exit_to_main_menu_requested.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0)
        )
        self.sverlilnaya_ctrl.exit_to_main_menu_requested.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0)
        )
        self.tehno_iot_ctrl.exit_to_main_menu_requested.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0)
        )
        self.sborka_ctrl.exit_to_main_menu_requested.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0)
        )
        self.normirovanie_ctrl.exit_to_main_menu_requested.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0)
        )
        self.kotrol_otk_ctrl.exit_to_main_menu_requested.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0)
        )
        self.markirovanie.exit_to_main_menu_requested.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0)
        )
        self.shlifovanie_ctrl.exit_to_main_menu_requested.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0)
        )
        self.otreznaya_ctrl.exit_to_main_menu_requested.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0)
        )


        # 3. Technopro — подключаем ОДИН РАЗ, делегируем активному контроллеру
        self.ui.page_input_technopro.btn_clicked_start.connect(self._on_technopro_start)
        self.ui.page_input_technopro.btn_clicked_tokarnaya.connect(self._on_technopro_back)
        self.ui.page_input_technopro.btn_clicked_update.connect(self._on_technopro_update)

    def _activate_controller(self, controller):
        """Активирует контроллер и переходит на его главную страницу."""
        self.active_controller = controller
        controller.go_to_main_page()

    def _on_technopro_start(self, value, result_clear):
        """Вызывает process_technopro_start у активного контроллера."""
        if self.active_controller:
            self.active_controller.process_technopro_start(value, result_clear)
        else:
            self.ui.page_input_technopro.error_start('Ошибка: не выбрана операция!')

    def _on_technopro_back(self):
        """Возврат из Technopro к активному контроллеру."""
        if self.active_controller:
            self.active_controller.go_to_main_page()

    def _on_technopro_update(self):
        """Обновление Technopro через активный контроллер."""
        if self.active_controller:
            self.active_controller.go_to_technopro()
