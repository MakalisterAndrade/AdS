import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config

class TelaPrincipal(GridLayout):
    pass


class SegundoApp(App):

    def build(self):
        Config.set('graphics', 'resizable', False)
        tela = TelaPrincipal()
        tela.size = 200, 210
        return tela

if __name__ == "__main__":
    SegundoApp().run()

