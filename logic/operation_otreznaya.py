from logic.operation_base import OperationBase
from logic.instrument_manager import InstrumentManager


class OperationOtreznaya(OperationBase):
    """Модель (логика) операции ОТРЕЗНАЯ.

    Каркас: наследуется от OperationBase, как остальные операции.
    TODO: напиши здесь методы формирования описаний операций,
          например: def otrezka(self, d: dict) -> dict: ...
    """

    def __init__(self):
        super().__init__()
        # PNG-шаблон для поиска строки операции в Technopro
        self.image = 'logic/find_operations/otreznaya_find.PNG'  # TODO: положи свой шаблон сюда
        self.instrument_manager = InstrumentManager()
        self.operations = {}

    @property
    def all_instrument(self):
        return self.instrument_manager.all_instrument

    def find_and_delete_from_all_instrument(self, instruments: list):
        self.instrument_manager.remove(instruments)

    def take_value_matches(self) -> int:
        return self.automation.take_value_matches(self.image)

    # =====================================================================
    # TODO: Логика операции ОТРЕЗНАЯ — напиши сам по образку других операций
    # Пример сигнатуры:
    # def otrezka(self, d: dict) -> dict:
    #     result = {'описание': '', 'инструмент': []}
    #     ...
    #     return result
    # =====================================================================
