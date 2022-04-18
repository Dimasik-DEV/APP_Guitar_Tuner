#########################################
# Мобильное приложение "Гитарный Тюнер" #
#########################################

from kivymd.app import MDApp
from kivy.core.window import Window  # Размер окна под Windows

from classes.CreateApp import CreateApp

Window.size = (270, 585)


class MainApp(MDApp):

    def build(self):

        app = CreateApp()
        return app.get_top_screen()


if __name__ == '__main__':
    MainApp().run()
