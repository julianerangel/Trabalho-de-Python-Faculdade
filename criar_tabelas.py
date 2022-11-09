import psycopg2


def tabelas_db():
    # Criando banco de dados jj4tech (banco de dados deste programa)
    print('ATENÇÃO IMPORTANTÍSSIMA: O banco de dados "jj4tech" DEVERÁ estar devidamente criado com antecedência!')
    input("Aperte qualquer tecla para continuar....")
    print('Criando as tabelas do banco de dados "jj4tech", que é o bando de dados que será trabalhado neste programa.')
    print('Abrindo conexão para realizar a criação das tabelas...')
    conn = psycopg2.connect(host="localhost", database="jj4tech", user="postgres", password="1234", port="5432")
    comando = conn.cursor()
    print("Conexão com o Banco de Dados aberta com sucesso!")
    # Código utilizado pela professora
    print('criando tabela "agenda", do código direto da professora...')
    comando.execute(""" 
        CREATE TABLE Agenda (
            id INT PRIMARY KEY NOT NULL,
            Nome TEXT NOT NULL,
            Telefone CHAR(12)
        );
    """)
    print('tabela "agenda" criada com sucesso!')
    print('criando a tabela produto, seguindo dos artigos lidos na internet...')
    # Parte da Fonte abaixo: https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-serial/
    comando.execute("""
        CREATE TABLE Produto (
            codigo SERIAL PRIMARY KEY NOT NULL,
            Nome TEXT NOT NULL,
            Preco DECIMAL NOT NULL,
            PrecoAcrescido DECIMAL
        );
    """)
    comando.execute("""
       INSERT INTO Produto (codigo, Nome, Preco, PrecoAcrescido) VALUES (1,'Apple iPhone 13s Pro Max', 5998.98, 6598.88);
       INSERT INTO Produto (codigo, Nome, Preco, PrecoAcrescido) VALUES (2,'Dell XPS 13 Plus', 13247.97, 14572.77);
       INSERT INTO Produto (codigo, Nome, Preco, PrecoAcrescido) VALUES (3,'JetBrains All Product Pack', 1792.46, 1971.71);
       INSERT INTO Produto (codigo, Nome, Preco, PrecoAcrescido) VALUES (4,'Alexa Echo Show', 1804.05, 1984.45);
    """)
    conn.commit()
    print('tabela produto criada com sucesso!')
    print('fechando conexão...')
    conn.close()
    print('conexão fechada!')
    print("Tabelas criadas com sucesso no BD!!!")

if __name__ == '__main__':
    tabelas_db()
