from functools import partial

from kivy.uix.label import Label
from kivy.uix.popup import Popup

from controller.participantectrl import ParticipanteCtrl

class ViewParticipante:
    def __int__(self, gerenc_tela):
        self._gt = gerenc_tela # para gerenciar facilmente a tela
        self._telacad = self._gt.get_screen("CadastroParticipante")
        self._telalistar = self._gt.get_screen("ListarParticipantes")

    def cad_atual_participante(self):
        control = ParticipanteCtrl()
        try:
            id_participante = self._telacad.lblidpart.text
            nome_participante = self._telacad.lblnome.text
            inst_participante = self._telacad.lblinst.text
            endere_participante = self._telacad.lblend.text
            tel_participante = self._telacad.lbltele.text
            email_participante = self._telacad.lblemail.text
            categ_participante = self._telacad.lblcateg.text
            ativi_participante = self._telacad.lblativ.text
            if self._telacad.bt_cad_atual.text =="Excluir":
                result = control.excluir_participante(id_participante)
                self.busca_participantes()
                self._gt.current = "ListarParticipantes"
            else:
                result = control.salvar_atualizar_participante(id=id_participante,
                                                               nome=nome_participante, instituicao=inst_participante,
                                                               endereco=endere_participante, telefone=tel_participante, email = email_participante,
                                                               categoria= categ_participante, atividade=ativi_participante)
            self._popJanela(result)
            self._limpar_tela()
            self._telacad.lblnome.focus = True
        except Exception as e:
            print(str(e))
            self._popJanela(f'Não foi possível {self._telacad.bt_cad_atual.text} o participante')

    def _limpar_tela_listar(self):
        self._telalistar.txi_pesq_id.text=""
        self._telalistar.txi_pesq_nome.text=""
        cabecalho=[
            self._telalistar.ids.col_id,
            self._telalistar.ids.col_nome,
            self._telalistar.ids.col_ins,
            self._telalistar.ids.col_endere,
            self._telalistar.ids.col_tel,
            self._telalistar.ids.col_email,
            self._telalistar.ids.col_cate,
            self._telalistar.ids.col_atv,
            self._telalistar.ids.lbl_atual,
            self._telalistar.ids.lbl_excluir
        ]
        self._telalistar.layout_lista_participante.clear_widgets()
        for c in cabecalho:
            self._telalistar.layout_lista_participante.add_widget(c)

    def busca_participantes(self, nome=""):
        try:
            control = ParticipanteCtrl()
            id_pesq = self._telalistar.txi_pesq_id.text
            resultado = control.buscar_participante(id=id_pesq, nome=nome)
            self._limpar_tela_listar()
            for res in resultado:
                res['btAtualizar'].bind(on_release=partial(self._gt.tela_cadastro_participante, res['lblidpart'].text))
                res['btExcluir'].bind(on_release=partial(self._gt.tela_cadastro_participante, res['lblidpart'].text))
                self._telalistar.layout_lista_participante.add_widget(res['lblidpart'])
                self._telalistar.layout_lista_participante.add_widget(res['lblnome'])
                self._telalistar.layout_lista_participante.add_widget(res['lblinst'])
                self._telalistar.layout_lista_participante.add_widget(res['lblend'])
                self._telalistar.layout_lista_participante.add_widget(res['lbltele'])
                self._telalistar.layout_lista_participante.add_widget(res['lblemail'])
                self._telalistar.layout_lista_participante.add_widget(res['lblcateg'])
                self._telalistar.layout_lista_participante.add_widget(res['lblativ'])
                self._telalistar.layout_lista_participante.add_widget(res['btAtualizar'])
                self._telalistar.layout_lista_participante.add_widget(res['btExcluir'])

        except Exception as e:
            print(e)

    def montar_tela_at(self, id_participante="", botao=None):
        control = ParticipanteCtrl()
        self._montar_spinner()
        participantes = []
        if id_participante:
            participantes = control.buscar_participante(id=id_participante)
        if participantes:
            for p in participantes:
                self._telacad.lblidpart.text = p['lblidpart'].text

                self._telacad.bt_cad_atual.text = botao.text

    def _montar_spinner(self):
        lista_valores = self.busca_atividades_tela()
        self._telacad.sp_atividade.values = lista_valores

    def _buscar_atividades_tela(self):
        control = ParticipanteCtrl
        atividades = control.buscarAtividades()
        descricaoAtividades = []
        for atividade in atividades:
            descricaoAtividades.append(atividade['descricao'])
        return tuple(descricaoAtividades)


    def _limpar_tela(self):
        self._telacad.lblidpart.text = ""
        self._telacad.lblnome.text = ""
        self._telacad.lblinst.text = ""
        self._telacad.lblend.text = ""
        self._telacad.bt_cad_atual.text = "Cadastrar"

    def _popJanela(self, texto=""):
        popup = Popup(title='Informação', content=Label(text=texto), auto_dismiss=True)
        popup.size_hint = (0.98, 0.4)
        popup.open()