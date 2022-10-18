from model.conexaoDB import Conexaodb
from model.alunoModel import Aluno


class AlunoDAO:
    __slots__ = (
        '_con'
    )

    def __init__(self):
        self._con = Conexaodb.conectar()

    def inserirAluno(self, aluno): # ok
        """
        Adiciona um aluno ao banco de dados
        :param aluno: Espera um objeto do tipo aluno
        :return: True caso a aluno seja adicionado e False caso contrario
        """
        sql = "INSERT INTO Aluno(nome,matricula, cpf, dataNasc, turma) VALUES (?,?,?,?,?);"
        valores = (aluno.nome, aluno.matricula, aluno.cpf, aluno.dataNasc, aluno.turma)
        res = Conexaodb.executarSql(sql, valores)
        return res == 1

    def atualizarAluno(self, aluno):
        """
        Atualiza um Aluno no banco de dados
        :param aluno: Espera um objeto do tipo aluno
        :return: True caso a aluno seja atualizada e False caso contrario
        """
        sql = "UPDATE Aluno SET nome=?, turno=?, matricula=?, cpf=?, dataNasc=?, turma=? WHERE id=?;"
        valores = (aluno.nome, aluno.matricula, aluno.cpf, aluno.dataNasc, aluno.turma.id)
        res = Conexaodb.executarSql(sql, valores)
        return res == 1

    def excluirAluno(self, id):
        """
        Exclui uma turma do banco de dados
        :param id: Espera o id(string) da turma a ser excluída
        :return: True caso a turma seja excluída e False caso contrario
        """
        sql = "DELETE FROM aluno WHERE id = " + str(id)
        cursor = self._con.cursor()
        cursor.execute(sql)
        self._con.commit()
        res = cursor.rowcount
        return res == 1

    def buscarAluno(self, id):
        """
        Busca um aluno no banco de dados
        :param id: Espera o id do aluno a ser buscada
        :return: A aluno de acordo com o id informado
        """

        try:
            sql = "SELECT id,nome,matricula,cpf,dataNasc,turma FROM aluno WHERE id =" + str(id) + ";"
            cursor = self._con.cursor()
            cursor.execute(sql)
            res = cursor.fetchone()
            aluno = Aluno(res[0], res[1], res[2], res[3], res[4], res[5])
            return aluno
        except Exception as e:
            print(str(e))
            return None

    def buscarTurmaPorNome(self, nome):
        """
        Busca uma turma no banco de dados pelo seu nome
        :param nome: Espera o nome da turma a ser buscada
        :return: A turma de acordo com o nome informado
        """
        try:
            sql = "SELECT id,nome,matricula,cpf,dataNasc,turma FROM aluno WHERE nome = '" + nome + "';"
            cursor = self._con.cursor()
            cursor.execute(sql)
            res = cursor.fetchone()
            aluno = Aluno(res[0], res[1], res[2], res[3], res[4], res[5])
            return aluno
        except Exception as e:
            print(str(e))
            return None

    def buscarAlunos(self, inicio=0, quant=100):
        """
        Busca as alunos do banco de dados
        :param quant: Espera a quantidade de alunos a serem buscadas
        :return: diversas alunos de acordo com a quantidade informada
        """

        alunos = []
        try:
            sql = "SELECT id,nome,matricula,cpf,dataNasc,turma FROM aluno"
            cursor = self._con.cursor()
            cursor.execute(sql)
            res = cursor.fetchmany(quant)
            alunos = self._montarResultado(res)
            return alunos
        except Exception as e:
            print(str(e))
            return alunos

    def _montarResultado(self, res):
        alunos = []

        for linha in res:
            aluno = Aluno(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5])
            alunos.append(aluno)
        return alunos
