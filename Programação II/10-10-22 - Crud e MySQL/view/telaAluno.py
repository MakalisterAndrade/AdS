from kivy.uix.label import Label
from kivy.uix.popup import Popup

from control.alunoCtrl import AlunoCtrl


class ViewAluno:

    def __init__(self, gerencTela):
        self._gerencTela = gerencTela

    def cadAtualAluno(self):
        result = ""
        try:
            tela = self._gerencTela.get_screen("CadastroAluno")
            idAluno = tela.ids.lblId.text
            nome = tela.ids.inputNome.text
            turno = self._verTurno(tela)
            control = AlunoCtrl()
            if tela.ids.btCadAtual.text == "Excluir":
                result = control.excluirAluno(idAluno)
            else:
                result = control.salvarAtualizarAluno(id=idAluno, nome=nome, dt_nasc=dt_nasc, renda_familiar=renda_familiar, turma=turma)

            self._popJanela(result)
            self._limparTela(tela)
        except Exception as e:
            print(e)
            self._popJanela(f"Não foi possível {tela.ids.btCadAtual.text} a turma!!!")

    def _limparTelaListar(self, tela):
        cabecalho = [
            tela.colid,
            tela.colnome,
            tela.colturno,
            tela.colatual,
            tela.colexcluir
        ]
        tela.gridlistar.clear_widgets()
        for c in cabecalho:
            tela.gridlistar.add_widget(c)

    def buscaTurmas(self):
        control = AlunoCtrl()
        tela = self._gerencTela.get_screen("ListarTurmas")
        idPesq = tela.inputid.text
        resultado = control.buscarTurma(id=idPesq)
        self._limparTelaListar(tela)
        for res in resultado:
            for r in res:
                if r.text == "Atualizar" or r.text == "Excluir":
                    r.bind(on_release=self.montarTelaAt)
                tela.gridlistar.add_widget(r)

    def montarTelaAt(self, botao):
        turma = []
        if hasattr(botao, 'id'):
            id = str(botao.id).replace("bt", "")
            control = AlunoCtrl()
            turma = control.buscarTurma(id=id)
        telaCad = self._gerencTela.get_screen("CadastroTurma")
        for t in turma:
            telaCad.ids.lblId.text = t[0].text
            telaCad.ids.inputNome.text = t[1].text
            if t[2] != "":
                self._marcarTurno(t[2].text, telaCad)
        telaCad.ids.btCadAtual.text = botao.text
        self._limparTelaListar(self._gerencTela.get_screen("ListarTurmas"))
        self._gerencTela.telaCadastroTurma()

    def _limparTela(self, tela):
        tela.ids.lblId.text = ""
        tela.ids.inputNome.text = ""
        tela.ids.chkMatutino.active = False
        tela.ids.chkVespertino.active = False
        tela.ids.chkNoturno.active = False
        tela.ids.chkIntegral.active = False
        tela.ids.btCadAtual.text = "Cadastrar"

    def _popJanela(self, texto=''):
        popup = Popup(title='Informação', content=Label(text=texto), auto_dismiss=True)
        popup.size_hint = (0.98, 0.4)
        popup.open()

    def _verTurno(self, tela):
        turno = ""
        if tela.ids.chkMatutino.active:
            turno = tela.ids.chkMatutino.value
        elif tela.ids.chkVespertino.active:
            turno = tela.ids.chkVespertino.value
        elif tela.ids.chkNoturno.active:
            turno = tela.ids.chkNoturno.value
        elif tela.ids.chkIntegral.active:
            turno = tela.ids.chkIntegral.value
        return turno

    def _marcarTurno(self, texto, tela):
        if tela.ids.chkMatutino.value == texto:
            tela.ids.chkMatutino.active = True
        elif tela.ids.chkVespertino.value == texto:
            tela.ids.chkVespertino.active = True
        elif tela.ids.chkNoturno.value == texto:
            tela.ids.chkNoturno.active = True
        elif tela.ids.chkIntegral.value == texto:
            tela.ids.chkIntegral.active = True
