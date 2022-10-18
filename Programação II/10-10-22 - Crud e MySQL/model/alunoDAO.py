from model.conexaoDB import Conexaodb
from model.alunoModel import Aluno


class AlunoDAO:
    __slots__ = (
        '_con'
    )

    def __init__(self):
        self._con = Conexaodb.conectar()

    def inserirAluno(self, aluno): #ok
        """
        Adiciona um aluno ao banco de dados
        :param aluno: Espera um objeto do tipo aluno
        :return: True caso o aluno seja adicionada e False caso contrario
        """
        sql = "INSERT INTO Aluno(nome,dt_nasc,renda_familiar,turma) VALUES (?,?,?,?);"
        valores = (aluno.nome, aluno.dt_nasc, aluno.renda_familiar, aluno.turma.id) #Informar o número da turma
        res = Conexaodb.executarSql(sql, valores)
        return res == 1

    def atualizarAluno(self, aluno): #ok
        """
        Atualiza um aluno no banco de dados
        :param aluno: Espera um objeto do tipo aluno
        :return: True caso o aluno seja atualizado e False caso contrario
        """
        sql = "UPDATE Aluno SET nome=?, dt_nasc=?, renda_familiar=?, turma=? WHERE id=?;"
        valores = (aluno.nome, aluno.dt_nasc, aluno.renda_familiar, aluno.turma, aluno.turma.id)
        res = Conexaodb.executarSql(sql, valores)
        return res == 1

    def excluirAluno(self, id): #ok
        """
        Exclui um aluno do banco de dados
        :param id: Espera o id(string) do aluno a ser excluído
        :return: True caso o aluno seja excluído e False caso contrario
        """
        sql = "DELETE FROM aluno WHERE id = " + str(id)
        cursor = self._con.cursor()
        cursor.execute(sql)
        self._con.commit()
        res = cursor.rowcount
        return res == 1

    def buscarAluno(self, id): #ok
        """
        Busca um aluno no banco de dados
        :param id: Espera o id do aluno a ser buscado
        :return: O aluno de acordo com o id informado
        """

        try:
            sql = "SELECT id,nome,dt_nasc,renda_familiar,turma FROM aluno WHERE id =" + str(id) + ";"
            cursor = self._con.cursor()
            cursor.execute(sql)
            res = cursor.fetchone()
            aluno = Aluno(res[0], res[1], res[2], res[3], res[4])
            return aluno
        except Exception as e:
            print(str(e))
            return None

    def buscarAlunoPorNome(self, nome): #ok
        """
        Busca um aluno no banco de dados pelo seu nome
        :param nome: Espera o nome do aluno a ser buscado
        :return: O aluno de acordo com o nome informado
        """
        try:
            sql = "SELECT id,nome,dt_nasc,renda_familiar,turma FROM aluno WHERE nome = '" + nome + "';"
            cursor = self._con.cursor()
            cursor.execute(sql)
            res = cursor.fetchone()
            aluno = Aluno(res[0], res[1], res[2], res[3], res[4])
            return aluno
        except Exception as e:
            print(str(e))
            return None

    def buscarAlunos(self, inicio=0, quant=100): #ok
        """
        Busca os alunos do banco de dados
        :param quant: Espera a quantidade de alunos a serem buscadas
        :return: diversos Alunos de acordo com a quantidade informada
        """

        alunos = []
        try:
            sql = "SELECT id,nome,dt_nasc,renda_familiar,turma FROM aluno"
            cursor = self._con.cursor()
            cursor.execute(sql)
            res = cursor.fetchmany(quant)
            alunos = self._montarResultado(res)
            return alunos
        except Exception as e:
            return alunos

    def _montarResultado(self, res): #ok
        alunos = []

        for linha in res:
            aluno = Aluno(linha[0], linha[1], linha[2], linha[3], linha[4])
            alunos.append(aluno)
        return alunos