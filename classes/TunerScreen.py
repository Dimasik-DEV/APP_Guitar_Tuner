from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class TunerScreen(Screen):
    Builder.load_file('gui/screen/tuner.kv')            # Загрузка файлов разметки ".kv"
    pass
