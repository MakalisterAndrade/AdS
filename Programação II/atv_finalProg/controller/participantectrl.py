from kivy.uix.button import Button
from kivy.uix.label import Label
from peewee import ModelSelect

from model.models import Participante, Atividade

class ParticipanteCtrl:

    def salvar_atualizar_participante(self, nome,instituicao,endereco,
                                      telefone,email,categoria,
                                      atividade, id=None):
        try:
            if id:
                participante = Participante.get_by_id(id)
                participante.nome = nome
                participante.instituicao = instituicao
                participante.endereco = endereco
                participante.telefone = telefone
                participante.email = email
                participante.categoria = categoria
                participante.atividade = atividade
            else:
                participante = Participante(nome=nome,instituicao=instituicao,endereco=endereco,
                                      telefone=telefone,email=email,categoria=categoria,
                                      atividade=atividade)
            participante.save()
            return 'Operação concluida com sucesso!'
        except Exception as e:
            print(e)
            return "Não foi possivel realizar a operação!"

    def excluir_participante(self, id):
        try:
            Participante.delete_by_id(id)
            return 'Participante deletado com sucesso'
        except Exception as e:
            print(e)
            return 'Não foi possível deletar o participante'
    def buscar_participante(self, id=None, nome = None):
        try:
            if id:
                participante = Participante.get_by_id(id)
            elif nome:
                participante = Participante.select().where(Participante.nome%f'%{nome}%')
            else:
                participante = Participante.select()
        except Exception as e:
            print(e)
            return None
        itens = []
        if type(participante) is Participante:
            itens.append(self._montar_participante(participante.id, participante.nome,
                                                   participante.instituicao, participante.endereco,
                                                   participante.telefone, participante.email,participante.categoria,
                                                   participante.atividade))
        elif type (participante) is ModelSelect:
            for p in participante:
                itens.append(self._montar_participante(
                    p.id, p.nome, p.instituicao, p.endereco, p.telefone,
                    p.email, p.categoria, p.atividade
                ))
        return itens
    def _montar_participante(self, id,nome,intituicao,endereco,telefone, email,categoria, atividade):
        meuparticipante = {
        'lblId': self._criarLabel(id, 0.1),
        'lblNome': self._criarLabel(nome, 0.4),
        'lblInst': self._criarLabel(intituicao, 0.3),
        'lblEnd': self._criarLabel(endereco, 0.3),
        'lblTel': self._criarLabel(telefone,0.4),
        'lblEmail': self._criarLabel(email, 0.3),
        'lblCat': self._criarLabel(categoria, 0.3),
        'lblAtv': self._criarLabel(atividade, 0.3),
        'btAtualizar': self._criarBotao("Atualizar"),
        'btEscluir': self._criarBotao("Exluir")
        }

    def _criarLabel(self, texto, tam):
        label = Label()
        label.text = str(texto)
        label.size_hint_y = None
        label.size_hint_x = tam
        label.height = '30dp'
        return label

    def _criarBotao(self, texto):
        botao = Button(text=texto,
                       font_size='10sp',
                       size_hint_y = None,
                       height='30dp',
                       size_hint_x = .1)
        return botao

    def buscarAtividades(self):
        Atividadebanco = Atividade.select()
        atividades = []
        for atividade in Atividadebanco:
            atividade.append({"id": atividade.id, "descricao": atividade.descricao})
        return atividades