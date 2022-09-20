import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config

class TelaPrincipal(GridLayout):
    fem = ObjectProperty(None)
    mas = ObjectProperty(None)
    other = ObjectProperty(None)
    h_games = ObjectProperty(None)
    h_ler = ObjectProperty(None)
    h_sport = ObjectProperty(None)
    h_desen = ObjectProperty(None)
    btt = ObjectProperty(None)
    corpref = ObjectProperty(None)
    mensagem = ObjectProperty(None)

    def verificarEscolhas(self):
        self.mensagem.text = ''
        sexos = [self.fem, self.mas, self.other]
        self.mensagem.text = 'Sexo: '
        for s in sexos:
            if s.active:
                self.mensagem.text += s.text

        hobbies = [self.h_ler, self.h_games, self.h_sport,self.h_desen]
        self.mensagem.text += '\n' + '='*112 + '\n' + 'Hobbies: ' + '\n'
        for h in hobbies:
            if h.active:
                self.mensagem.text += h.text +'\n'
        self.mensagem.text +=  '='*112 + '\n'


    def escolhaSpinner(self):
        popup = Popup(title = 'Cor Escolhida',
                        content = Label(text = f'Sua cor preferida é: {self.corpref.text}'),
                        auto_dismiss = True)
        popup.size_hint = .75, 0.3
        popup.open()

class SegundoApp(App):

    def build(self):
        Config.set('graphics', 'resizable', False)
        tela = TelaPrincipal()
        self.title = 'Outros Componentes Kivy'
        tela.size = 200, 210
        return tela

if __name__ == "__main__":
    SegundoApp().run()

