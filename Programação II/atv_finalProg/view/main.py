import kivy
from kivy.app import App
from GerenciadorTelas import GerenciaTelas

class TelaKV(App):
    def build(self):
        self.root = GerenciaTelas()
        return self.root


if __name__ == '__main__':
    TelaKV().run()