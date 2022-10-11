import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Tela1(Widget):

    def somar(self):
        try:
            valor1 = int(self.ids.txt1.text)
            valor2 = int(self.ids.txt2.text)
            soma = valor1 + valor2
            self.ids.lbResult.text = str(soma)
        except (TypeError, ValueError):
            lblErro = Label(text='Verifique os valores')
            popup = Popup(title='ERRO 404', content=lblErro, auto_dismiss = True)
            popup.size_hint = (0.75, 0.4)
            popup.open()

class SomaApp(App):

    def build(self):
        return Tela1()

if __name__=="__main__":
    SomaApp().run()