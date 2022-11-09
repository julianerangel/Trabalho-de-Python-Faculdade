import tkinter as tk

from outros import calc_acrescimo # Gerado automaticamente pelo PyCharm


# base da fonte do código abaixo: https://www.geeksforgeeks.org/create-table-using-tkinter/
class TodosRegistros:
    def __init__(self, win, data):
        # code for creating table

        # Coluna 'Código'
        self.e = tk.Entry(win, width=20, fg='blue',
                          font=('Arial', 16, 'bold'))
        self.e.grid(row=0, column=0)
        self.e.insert(tk.END, 'Código')

        # Coluna 'Nome'
        self.e = tk.Entry(win, width=20, fg='blue',
                          font=('Arial', 16, 'bold'))
        self.e.grid(row=0, column=1)
        self.e.insert(tk.END, 'Nome')

        # Coluna 'Preco'
        self.e = tk.Entry(win, width=20, fg='blue',
                          font=('Arial', 16, 'bold'))
        self.e.grid(row=0, column=2)
        self.e.insert(tk.END, 'Preco')

        # Coluna 'Acréscimo'
        self.e = tk.Entry(win, width=20, fg='blue',
                          font=('Arial', 16, 'bold'))
        self.e.grid(row=0, column=3)
        self.e.insert(tk.END, 'Preço c/ acréscimo')

        # fonte de informação da função 'type':
        # https://dicasdepython.com.br/python-como-descobrir-o-tipo-de-uma-variavel-ou-objeto/
        self.data = data

        for i in range(1, len(self.data)+1): #Linhas
            for j in range(0, len(self.data[0])): #Colunas
                #Adicionando uma entrada...
                self.e = tk.Entry(win, width=20, fg='blue',
                                  font=('Arial', 10))
                #Adicionando uma célula da tabela
                self.e.grid(row=i, column=j)
                #Preenchendo as informações do banco de dados nesta célula...
                self.e.insert(tk.END, self.data[i-1][j])

    def dados_fakes(self): #Dados fakes apenas para exemplificar a tela.
        return [
                (1, 'Apple iPhone 13s Pro Max', f'R$ {5998.98:,.2f}', f'R$ {calc_acrescimo(5998.98, 10/100):,.2f}'),
                (2, 'Dell XPS 13 Plus', f'R$ {13247.97:,.2f}', f'R$ {calc_acrescimo(13247.97, 10/100):,.2f}'),
                (3, 'JetBrains All Product Pack', f'R$ {1792.46:,.2f}', f'R$ {calc_acrescimo(1792.46, 10/100):,.2f}'),
                (4, 'Alexa Echo Show', f'R$ {1804.05:,.2f}', f'R$ {calc_acrescimo(1804.05, 10/100):,.2f}'),
                (5, 'Microsoft XBox Series S', f'R$ {2649.55:,.2f}', f'R$ {calc_acrescimo(2649.55, 10/100):,.2f}')
            ]