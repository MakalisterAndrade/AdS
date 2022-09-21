import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config

class Tela(GridLayout):
    pass


class ScriptApp(App):

    def build(self):
        Config.set('graphics', 'resizable', False)
        Config.set('graphics', 'width', '380')
        Config.set('graphics', 'height', '300')
        tela = Tela()
        self.title = 'App de leitura e cálculo de gastos de energia'
        #tela.size = 50, 50
        return tela

if __name__ == "__main__":
    ScriptApp().run()
