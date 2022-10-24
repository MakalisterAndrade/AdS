import kivy
from kivy.app import App
from view.gerencTelas import GerenciaTelas
from view.telaTurma import ViewTurma

kivy.require('2.1.0')

__version__ = '0.1'


class exemplo(App):
    def build(self):
        kivy.config.Config.set('graphics', 'resizable', False)
        self.root = GerenciaTelas()
        self.root.size = 480, 240
        return self.root


if __name__ == '__main__':
    exemplo().run()