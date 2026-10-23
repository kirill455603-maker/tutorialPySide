from ui_page_otreznaya import Ui_PageOtreznaya  # Поменять на своё имя класса из ui_page_otreznaya.py
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QPushButton, QHeaderView


class PageOtreznaya(QWidget):
    """Страница операции ОТРЕЗНАЯ. Наследуется от ui_page_otreznaya.Ui_PageOtreznaya."""
    btn_home_clicked = Signal()
    btn_save_clicked = Signal()
    btn_click_delete = Signal(int)
    btn_clear_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PageOtreznaya()
        self.ui.setupUi(self)

        # ===== НАСТРОЙКА ТАБЛИЦЫ (как в остальных страницах) =====
        self.ui.table_widget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.ui.table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.ui.table_widget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.ui.table_widget.horizontalHeader().resizeSection(0, 400)
        self.ui.table_widget.horizontalHeader().resizeSection(1, 600)
        self.ui.table_widget.setWordWrap(True)
        # =========================================================

        # ВАЖНО: храним ссылки на кнопки удаления, чтобы их не удалил сборщик мусора
        self._delete_buttons = []

        self.ui.btn_home.clicked.connect(self._on_button_home_clicked)
        self.ui.pushButton_save.clicked.connect(self._on_button_save_clicked)
        self.ui.btn_clear_table.clicked.connect(self._on_button_clear_clicked)

    # ---------- обработчики кнопок ----------
    def _on_button_home_clicked(self):
        self.btn_home_clicked.emit()

    def _on_button_save_clicked(self):
        self.btn_save_clicked.emit()

    def _on_button_clear_clicked(self):
        self.btn_clear_clicked.emit()

    # ---------- методы таблицы (использует контроллер) ----------
    def show_result(self, text, instrument, key_count):
        """Добавляет строку в таблицу."""
        self.ui.table_widget.setRowCount(self.ui.table_widget.rowCount() + 1)
        row = self.ui.table_widget.rowCount() - 1

        self.ui.table_widget.setItem(row, 0, instrument)
        self.ui.table_widget.setItem(row, 1, text)

        btn_delete = QPushButton('Удалить')
        btn_delete.clicked.connect(
            lambda checked, r=key_count: self.on_delete_clicked(r)
        )
        self._delete_buttons.append(btn_delete)
        btn_delete.resize(50, 20)
        self.ui.table_widget.setCellWidget(row, 2, btn_delete)

    def on_delete_clicked(self, r):
        self.btn_click_delete.emit(r)

    def get_index_row(self, item):
        return self.ui.table_widget.row(item)

    def delete_row(self, r):
        self.ui.table_widget.removeRow(r)

    def clear_table(self):
        """Очистка таблицы. ОБЯЗАТЕЛЬНЫЙ метод."""
        self.ui.table_widget.clear()
        self.ui.table_widget.setRowCount(0)
        self.ui.table_widget.setHorizontalHeaderLabels(
            ['Инструмент', 'Описание [Можно изменять]', '']
        )
        self._delete_buttons.clear()

    def show_label(self, text):
        """Вывод сообщения/ошибки на странице."""
        # TODO: подставь имя своего label из дизайна, если он отличается
        self.ui.label_error.setText(text)

    def error_style_sheet(self):
        # TODO: стиль ошибки, как на других страницах (по желанию)
        pass
