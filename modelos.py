from conexao import conectar

class Aluno:
    def __init__(self, nome_aluno, sobrenome_aluno, media_aluno, id_aluno=None, criado_em=None):
        self.id_aluno = id_aluno
        self.nome_aluno = nome_aluno
        self.sobrenome_aluno = sobrenome_aluno
        self.media_aluno = media_aluno
        self.criado_em = criado_em

    def exibir(self):
        texto = f"""
        Código aluno: {self.id_aluno}
        Nome do aluno: {self.nome_aluno}
        Sobrenome do aluno: {self.sobrenome_aluno} 
        Média aluno: {self.media_aluno}
        Criado em: {self.criado_em}
"""
        print(texto)

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()
                
        sql = "INSERT INTO produto (nome_aluno, sobrenome_aluno, media_aluno) VALUES (%s, %s, %s)"
        cursor.execute(sql, (self.nome_aluno, self.sobrenome_aluno, self.media_aluno))
        conexao.commit()
        conexao.close()

def listar_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM aluno"
    cursor.execute(sql)

    alunos = []

    for id, nome_aluno, sobrenome_aluno, media_aluno, criado_em in cursor.fetchall():
        aluno = Aluno(nome_aluno, sobrenome_aluno, media_aluno, id, criado_em)
        alunos.append(aluno)

    conexao.close()
    return alunos