from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDFloatingActionButtonSpeedDial

###
from classes.MainScreen import MainScreen
from classes.TunerScreen import TunerScreen
from classes.ChordScreen import ChordScreen
from classes.MetronomeScreen import MetronomeScreen
from classes.SettingScreen import SettingScreen
###


class CreateApp:

    _data = {
        "Тюнер": "icons/mode/tuner.png",
        "Аккорды": "icons/mode/chord.png",
        "Метроном": "icons/mode/metronome.png",
        "Настройки": "icons/mode/setting.png",
    }

    _mode = None                   # Содержит экземпляр объекта "MDFloatingActionButtonSpeedDial" (Режим работы)
    _manager_screen = None         # Управление переключением окон (режимов работы)
    _top_screen = None

    def get_top_screen(self):
        return self._top_screen

    ### Определение нажатия кнопки для переключения экранов ###
    def _callback(self, instance):

        self._mode.close_stack()

        if self._data.get("Тюнер") == instance.icon:
            self._manager_screen.current = "tuner"

        elif self._data.get("Аккорды") == instance.icon:
            self._manager_screen.current = "chord"

        elif self._data.get("Метроном") == instance.icon:
            self._manager_screen.current = "metronome"

        else:
            self._manager_screen.current = "setting"

        return

    ### ### ###

    def __init__(self):

        _top_screen = Screen()                       # Основа всего "gui"
        _manager_screen = MainScreen()               # Включает в себя все окна для переключения
        _mode = MDFloatingActionButtonSpeedDial()    # Кнопка для переключения окон (режимов работы)

        ### Создание экземпляров классов ###

        _tuner = TunerScreen()
        _chord = ChordScreen()
        _metronome = MetronomeScreen()
        _setting = SettingScreen()

        ### ### ###

        ### Создание структуры интерфейса ###

        _top_screen.add_widget(_manager_screen)
        _top_screen.add_widget(_mode)

        _manager_screen.add_widget(_tuner)
        _manager_screen.add_widget(_chord)
        _manager_screen.add_widget(_metronome)
        _manager_screen.add_widget(_setting)

        ### ### ###

        _mode.data = self._data                      # Добавление кнопок для виджета
        _mode.callback = self._callback               # Обратный вызов при нажатии кнопок виджета

        self._manager_screen = _manager_screen       # Необходим для переключения окон
        self._mode = _mode                           # Необходим для управления закрытием виджета после нажатия
        self._top_screen = _top_screen

    pass
