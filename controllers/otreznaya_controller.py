from ui_autoinput import Ui_MainWindow
from views.pages.page_otreznaya import PageOtreznaya
from controllers.base_controller import BaseOperationController
from logic.operation_otreznaya import OperationOtreznaya
from logic.automation import TechnoproAutomation


class OtreznayaController(BaseOperationController):
    """Контроллер операции ОТРЕЗНАЯ (каркас, по образцу остальных операций)."""

    def __init__(self, ui, parent=None):
        super().__init__(ui, OperationOtreznaya(), TechnoproAutomation(), parent)
        self.ui: Ui_MainWindow = ui
        self.model: OperationOtreznaya = OperationOtreznaya()
        self.automation: TechnoproAutomation = TechnoproAutomation()
        self._connect_signals()

    def _connect_signals(self):
        self.ui.page_otreznaya.btn_home_clicked.connect(self._go_to_main_page)
        self.ui.page_otreznaya.btn_save_clicked.connect(self._save_result)
        self.ui.page_otreznaya.btn_click_delete.connect(self.delete_row)
        self.ui.page_otreznaya.btn_clear_clicked.connect(self.clear_all)

    # ================= ОБЯЗАТЕЛЬНЫЕ МЕТОДЫ =================
    def get_operation_name(self) -> str:
        return 'Отрезная'

    def get_target_page(self):
        return self.ui.page_otreznaya

    def go_to_main_page(self):
        # Возврат на страницу выбора операции (page_select_operation) —
        # индекс вычисляется динамически, чтобы не ломаться при добавлении новых страниц.
        idx = self.ui.stackedWidget.indexOf(self.ui.page_select_operation)
        self.ui.stackedWidget.setCurrentIndex(idx)

    def _go_to_main_page(self):
        self.exit_to_main_menu_requested.emit()

    def clear_all(self):
        """Очистка всех данных операции."""
        self.model.clear_all()
        self.model.all_instrument.clear()
        self.ui.page_otreznaya.clear_table()
        self.ui.page_otreznaya.show_label('Записанные данные в таблицу успешно удалены!')

    def delete_row(self, r):
        """Удаляет строку из таблицы и модели."""
        item = self.model.operations[r]['описание']
        if self.model.operations[r]['инструмент'].text() != '':
            item_instrument = self.model.operations[r]['инструмент'].text()
            self.model.find_and_delete_from_all_instrument(item_instrument.split('\n'))
        row_index = self.ui.page_otreznaya.get_index_row(item)
        self.ui.page_otreznaya.show_label(f'Строка №{row_index + 1} успешно удалена!')
        self.ui.page_otreznaya.delete_row(row_index)
        del self.model.operations[r]

    # ================= СПЕЦИФИЧНЫЕ МЕТОДЫ =================
    def _save_result(self):
        """Сохранение результата операции.

        TODO: заполни по образку MarkirovanieController._save_result /
        других контроллеров, когда напишешь логику в OperationOtreznaya.
        Пример:
            self.clear_all()
            d = self.ui.page_otreznaya.get_result()
            result = self.model.<твоя_метод_логики>(d)
            self._process_and_save_result(result)
        """
        pass
