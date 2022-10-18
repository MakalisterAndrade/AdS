from kivy.uix.button import Button
from kivy.uix.label import Label
from model.alunoModel import Aluno
from model.alunoDAO import AlunoDAO


class AlunoCtrl:

    def salvarAtualizarTurma(self, id=None, nome="", matricula=str, cpf=str, dataNasc=str, turma=''):
        if len(nome) > 3:
            inseriuatualizou = False
            aluno = Aluno(nome=nome, matricula=matricula, cpf=cpf, dataNasc=dataNasc, turma=turma);
            dao = AlunoDAO()
            if id:
                turma.id = id
                inseriuatualizou = dao.atualizarAluno(aluno)
            else:
                inseriuAtualizou = dao.inserirAluno(aluno)
            if inseriuatualizou:
                return "Aluno inserido ou atualizado com sucesso!!!"
            else:
                return "O aluno não pode ser inserido ou atualizado!"
        else:
            return "O nome deve ter mais de 3 caracteres"

    def excluirAluno(self, id):
        dao = AlunoDAO()
        excluiu = dao.excluirAluno(str(id))
        if excluiu:
            return "Aluno excluido com sucesso!!!"
        else:
            return "O Aluno não pôde ser excluído!"

    def buscarAluno(self, id="", inicio=0, quant=10):
        dao = AlunoDAO()
        res = ""
        if id != "":
            res = dao.buscarAluno(id)
        else:
            res = dao.buscarAlunos(inicio=inicio, quant=quant)
        itens = []

        if type(res) is Turma:
            minhaturma = []
            minhaturma.append(self._criarLabel(res.id, 0.2))
            minhaturma.append(self._criarLabel(res.nome, 0.6))
            minhaturma.append(self._criarLabel(res.turno, 0.2))
            minhaturma.append(self._criarBotao("Atualizar", res.id))
            minhaturma.append(self._criarBotao("Excluir", res.id))
            itens.append(minhaturma)

        if type(res) is list:
            for turma in res:
                minhaturma = []
                minhaturma.append(self._criarLabel(turma.id, 0.2))
                minhaturma.append(self._criarLabel(turma.nome, 0.6))
                minhaturma.append(self._criarLabel(turma.turno, 0.2))
                minhaturma.append(self._criarBotao("Atualizar", turma.id))
                minhaturma.append(self._criarBotao("Excluir", turma.id))
                itens.append(minhaturma)
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