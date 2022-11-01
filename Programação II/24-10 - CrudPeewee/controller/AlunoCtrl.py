import locale

from kivy.uix.button import Button
from kivy.uix.label import Label
from peewee import ModelSelect

from controller.utils import Util
from model.models import Aluno, Turma


class AlunoCtrl:

    def salvar_atualizar_aluno(self, id=None, nome=None, dt_nasc=None, renda_fam=None, turma=None):
        try:
            t = Turma.get(nome=turma)
            dn = self._dt_nasc_tela_banco(dt_nasc) # "aaa-mm-dd"
            rf = self._renda_tela_banco(renda_fam)
            if id:
                aluno = Aluno.get_by_id(id)
                aluno.nome = nome
                aluno.dt_nasc = dn
                aluno.renda_fam = rf
                aluno.turma = t
            else:
                aluno = Aluno(nome=nome, dt_nasc=dn, renda_fam=rf, turma = t)
            aluno.save()
            return "Operação realizada com sucesso"
        except Exception as e:
            print(e)
            return "Não foi possível salvar ou atualizar"

    def excluir_aluno(self, id):
        try:
            aluno = Aluno.get_by_id(id)
            aluno.delete_instance()
            return "Aluno excluído com sucesso!!!"
        except Exception as e:
            print(e)
            return "Não foi possível exluir o Aluno!!!"
    def _montar_aluno(self, aluno):
        return {
            "id": aluno.id,
            "nome": aluno.nome,
            "data_nasc": aluno.dt_nasc,
            "renda_fam": aluno.renda_fam,
            "turma": aluno.turma}

    def _dt_nasc_tela_banco(self, dt_nasc):
        """
        Converte a data no formato "dd/mm/aaaa" para "aaaa-mm-dd"
        :param dt_nasc: a data de nascimento que vem na tela
        :return: a data de nascimento no formato sql Date
        """
        if Util.valida_data(dt_nasc):
            d = dt_nasc.split('/') #converte a string em lista
            databanco = f"{d[2]}-{d[1]}-{d[0]}" # monta uma string no formato "aaaa-mm-dd"
            return databanco

    def _renda_tela_banco(self, renda):
        """
        Converte a renda no formato "9.999,99" para "9999.99"
        :param renda:
        :return:
        """
        try:
            r = renda.replace(".","") # remove o ponto da renda
            r = r.replace(",", ".") # troca a virgula por ponto
            return float(r)
        except Exception as e:
            print(e)

    def buscar_aluno(self, id=None, nome=None):
        aluno = None
        try:
            if id:
                aluno = Aluno.get_by_id(id)
            elif nome:
                aluno = Aluno.select().where(Aluno.nome % (f'%{nome}%'))
            else:
                aluno = Aluno.select()
        except Exception as e:
            print(e)
            return None
        itens = []
        if type(aluno) is Aluno:
            itens.append(self._montar_aluno(aluno.id, aluno.nome, aluno.dt_nasc, aluno.renda_fam, aluno.turma))
        elif type(aluno) is ModelSelect:
            for a in aluno:
                itens.append(self._montar_aluno(a.id, a.nome, a.dt_nasc, a.renda_fam, a.turma))
        return itens

    def buscar_aluno_nome(self, nome):
        """
        Método que busca aluno pelo nome passado
        :param nome: Str com nome do aluno a ser procurada
        :return: Dict com os dados do aluno ou com erro
        """
        try:
            aluno = Aluno.get(nome=nome)
            return self._montar_aluno(aluno)
        except Exception as e:
            print(str(e))
            return {"erro": "Aluno não encontrado!"}

    def buscarTodosAlunos(self):
        """
        busca todos os alunos do banco
        :return: List com dicts de dados dos alunos
        """
        alunolist = []
        try:
            alunos = Aluno.select()
            for aluno in alunos:
                alunolist.append(self._montar_aluno(aluno))
            return alunolist
        except Exception as e:
            print(str(e))
            return [{"Erro": "Não foi possível realizar a busca!"}]
