import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Tela(Widget):

    def calculo(self):
        tempo = 0
        cont = 0
        try:
            valor1 = int(self.ids.txt1.text)
            while valor1 >= 200:
                tempo += 30
                valor1 -= 10
                cont += 1
                self.ids.lbResult.text = str(cont)
        except(TypeError, ValueError):
            lblErro = Label(text='Verifique o valor digitado\nPs: Deve ser maior que 200g')
            popup = Popup(title='ERRO :(', content=lblErro, auto_dismiss=True)
            popup.size_hint = (0.75, 0.4)
            popup.open()

class CalcApp(App):

    def build(self):
        return Tela()

if __name__=="__main__":
    CalcApp().run()



