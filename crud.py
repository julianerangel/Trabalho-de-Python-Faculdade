import psycopg2
from decimal import Decimal  # Importado pelo PyCharm

from outros import calc_acrescimo  # Importado automaticamente pelo PyCharm


class AppBD:
    def __init__(self, acrescimo=(10/100)):
        self.connection = None
        self.acrescimo = acrescimo
        print('Método Construtor')

    def abrir_conexao(self): #Inicia a conexão com o banco de dados
        try:
            self.connection = psycopg2.connect(user="postgres", password="1234", host="127.0.0.1", port="5432",
                                               database="jj4tech")
            print('conectado com sucesso ao banco de dados')
        except (Exception, psycopg2.Error) as error:
            print("Falha ao se conectar ao Banco de Dados", error)

    def inserirDados(self, codigo, nome, preco):  # Create
        try:
            self.abrir_conexao()
            cursor = self.connection.cursor()
            print('inserindo registro...')
            postgres_insert_query = """
                INSERT INTO Produto (codigo, Nome, Preco, PrecoAcrescido) VALUES (%s,%s,%s,%s)
            """
            codigo = int(codigo)
            preco = float(preco)
            precoAcrescido = float(f'{calc_acrescimo(preco, self.acrescimo)}')
            cursor.execute(postgres_insert_query, (codigo, nome, preco, precoAcrescido))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com successo na tabela PRODUTO")
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao inserir registro na tabela PRODUTO", error)
        finally:
            # closing database connection.
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

    def obterUmDado(self, codigo):  # Read (Somente 1)
        try:
            self.abrir_conexao()
            cursor = self.connection.cursor()
            sql_select_query = "SELECT * FROM Produto WHERE codigo = %s"
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            return record
        except (Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)
        finally:
            if self.connection:
                cursor.close()
            self.connection.close()
            print("A conexão com o PostgreSQL foi fechada.")

    def obterTodosOsDados(self):  # Read (Tudo)
        try:
            self.abrir_conexao()
            cursor = self.connection.cursor()
            # Obtendo todos os produtos, começando pelo último criado
            sql_select_query = "SELECT * FROM Produto ORDER BY codigo DESC;"
            cursor.execute(sql_select_query)
            record = cursor.fetchall()
            return record
        except (Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)
        finally:
            if self.connection:
                cursor.close()
            self.connection.close()
            print("A conexão com o PostgreSQL foi fechada.")

    def atualizarDados(self, codigo, nome, preco):  # Update
        try:
            self.abrir_conexao()
            cursor = self.connection.cursor()
            print('atualizando...')
            sql_update_query = """
                UPDATE Produto
                SET Nome = %s, Preco = %s, PrecoAcrescido = %s 
                WHERE codigo = %s
            """
            codigo = int(codigo)
            preco = float(preco)
            precoAcrescido = float(f'{calc_acrescimo(preco, self.acrescimo)}')
            cursor.execute(sql_update_query, (nome, preco, precoAcrescido, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso! ")
            print("Registro Depois da Atualização ")
            sql_select_query = "SELECT * FROM Produto WHERE codigo = %s"
            cursor.execute(sql_select_query, (codigo,))
            record = cursor.fetchone()
            print(record)
        except (Exception, psycopg2.Error) as error:
            print("Erro na Atualização", error)
        finally:
            if self.connection:
                cursor.close()
            self.connection.close()
            print("A conexão com o PostgreSQL foi fechada.")

    def excluirDados(self, codigo):  # Delete
        try:
            self.abrir_conexao()
            cursor = self.connection.cursor()
            sql_delete_query = "DELETE FROM Produto WHERE codigo = %s"
            cursor.execute(sql_delete_query, (codigo,))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso! ")
        except (Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)
        finally:
            # closing database connection.
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")
