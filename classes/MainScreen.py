from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder


class MainScreen(ScreenManager):
    Builder.load_file('gui/screen/main.kv')        # Загрузка файлов разметки ".kv"
    pass
