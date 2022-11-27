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
