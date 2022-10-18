from kivy.uix.button import Button
from kivy.uix.label import Label
from model.alunoModel import Aluno
from model.alunoDAO import AlunoDAO


class AlunoCtrl:

    def salvarAtualizarAluno(self, id=None, nome="", dt_nasc="", renda_familiar="", turma=""): #ok
        if len(nome) > 3:
            inseriuAtualizou = False
            aluno = Aluno(nome=nome, dt_nasc=dt_nasc, renda_familiar=renda_familiar, turma=turma);
            dao = AlunoDAO()
            if id:
                aluno.id = id
                inseriuAtualizou = dao.atualizarAluno(aluno)
            else:
                inseriuAtualizou = dao.inserirAluno(aluno)
            if inseriuAtualizou:
                return "Aluno inserido ou atualizado com sucesso!!!"
            else:
                return "O aluno não pode ser inserido ou atualizado!"
        else:
            return "O nome deve ter mais de 3 caracteres"

    def excluirAluno(self, id): #
        dao = AlunoDAO()
        excluiu = dao.excluirAluno(str(id))
        if excluiu:
            return "Aluno excluído com sucesso!!!"
        else:
            return "O aluno não pôde ser excluído!"

    def buscarAluno(self, id="", inicio=0, quant=10):
        dao = AlunoDAO()
        res = ""
        if id != "":
            res = dao.buscarAluno(id)
        else:
            res = dao.buscarAlunos(inicio=inicio, quant=quant)
        itens = []

        if type(res) is Aluno:
            meusalunos = []
            meusalunos.append(self._criarLabel(res.id, 0.2))
            meusalunos.append(self._criarLabel(res.nome, 0.6))
            meusalunos.append(self._criarLabel(res.dt_nasc, 0.2))
            meusalunos.append(self._criarLabel(res.renda_familiar, 0.2))
            meusalunos.append(self._criarLabel(res.turma, 0.2))
            meusalunos.append(self._criarBotao("Atualizar", res.id))
            meusalunos.append(self._criarBotao("Excluir", res.id))
            itens.append(meusalunos)

        if type(res) is list:
            for aluno in res:
                meusalunos = []
                meusalunos.append(self._criarLabel(aluno.id, 0.2))
                meusalunos.append(self._criarLabel(aluno.nome, 0.6))
                meusalunos.append(self._criarLabel(aluno.dt_nasc, 0.2))
                meusalunos.append(self._criarLabel(aluno.renda_familiar, 0.2))
                meusalunos.append(self._criarLabel(aluno.turma, 0.2))
                meusalunos.append(self._criarBotao("Atualizar", aluno.id))
                meusalunos.append(self._criarBotao("Excluir", aluno.id))
                itens.append(meusalunos)
        return itens

    def _criarLabel(self, texto, tam):
        label = Label()
        label.text = str(texto)
        label.size_hint_y = None
        label.size_hint_x = tam
        label.height = '30dp'
        return label

    def _criarBotao(self, texto, id):
        botao = Button()
        botao.text = texto
        botao.id = "bt" + str(id)
        botao.font_size = '10sp'
        botao.size_hint_y = None
        botao.height = '30dp'
        botao.size_hint_x = .1
        return botao