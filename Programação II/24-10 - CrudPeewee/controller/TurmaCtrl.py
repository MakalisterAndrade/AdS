from model.models import Turma

class TurmaCtrl:

    def salvar_atualizar(self, nome, turno, id=None):
        """
        Método para salvar/atualizar uma turma. Passar o Id da Turma para atualizar
        :param nome: espera str com nome da turma
        :param turno: espera choices com turno da turma, já definiidos em model.models.Turma
        :param id: Integer: o id da turma para atualizar
        :return: String com o resultado
        """

        try:
            turma = Turma()
            if id:
                turma = Turma.get_by_id(id)
            turma.nome = nome
            turma.turno = turno
            turma.save()
            return 'Turma salva com sucesso!!!'
        except Exception as e:
            print(str(e))
            return 'Não foi dessa vez, meu nobre.'

    def excluirTurma(self, id):
        """
        Método para excluir uma turma
        :param id: Integer com id da turma a ser excluída
        :return: String com o resultado
        """
        try:
            Turma.delete_by_id(id)
            return 'Turma excuída com sucesso!!!'
        except Exception as e:
            print(str(e))
            return 'Não foi possível excuir a turma, parceiro.'

    def buscarTurmaId(self, id):
        """
        Método que busca turma pelo id passado
        :param id: Integer com id da turma a ser procurada
        :return: Dict com os dados da turma ou com erro
        """
        try:
            turma = Turma.get_by_id(id)
            turmadict = {
                "id": turma.id,
                "nome": turma.nome,
                "turno": turma.turno
            }
            return turmadict
        except Exception as e:
            print(str(e))
            return {"erro": "Turma não encontrada!"}

    def buscarTurmaNome(self, nome):
        """
        Método que busca turma pelo nome passado
        :param nome: Str com nome da turma a ser procurada
        :return: Dict com os dados da turma ou com erro
        """
        try:
            turma = Turma.get(nome=nome)
            turmadict = {
                "id": turma.id,
                "nome": turma.nome,
                "turno": turma.turno
            }
            return turmadict
        except Exception as e:
            print(str(e))
            return {"erro": "Turma não encontrada!"}