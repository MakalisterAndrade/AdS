import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config

class Tela(GridLayout):
    atual = ObjectProperty(None)
    ant = ObjectProperty(None)
    cons = ObjectProperty(None)
    check = ObjectProperty(None)
    bt1 = ObjectProperty(None)
    bt2 = ObjectProperty(None)

    def Calcular(self):
        try:
            check = self.check
            valor1 = int(self.atual.text)
            valor2 = int(self.ant.text)
            if check.active:
                soma = valor1 + valor2 * 0.37
                self.cons.text = "R$ {:.2f}".format(soma).replace('.', ',')
            else:
                soma = valor1 + valor2 * 0.62
                self.cons.text = "R$ {:.2f}".format(soma).replace('.', ',')

        except (TypeError, ValueError):
            lblErro = Label(text='Verifique os valores')
            popup = Popup(title='ERRO 404', content=lblErro, auto_dismiss = True)
            popup.size_hint = (0.75, 0.4)
            popup.open()

    def Novo(self):
        self.atual.text, self.ant.text, self.cons.text = '', '', ''
        self.check.active = False
        return Tela()

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
