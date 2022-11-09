from TodosOsRegistros import TodosRegistros  # Importado automaticamente pelo PyCharm
import tkinter as tk
import tkinter.messagebox
import crud as crud
from outros import calc_acrescimo


class PrincipalBD:
    def __init__(self, win, porcentagem_acrescimo):
        self.connection = None
        self.objBD = crud.AppBD()
        self.win = win
        self.acrescimo = porcentagem_acrescimo
        # componentes
        self.lbCodigo = tk.Label(win, text='Código do Produto:')
        self.lblNome = tk.Label(win, text='Nome do Produto')
        self.lblPreco = tk.Label(win, text='Preço')
        self.lblAcrescimo = tk.Label(win, text=f'Preço Acrésc. (10%)')
        self.txtCodigo = tk.Entry(bd=3)
        self.txtNome = tk.Entry()
        self.txtPreco = tk.Entry()
        self.txtAcrescimo = tk.Entry(win)
        self.txtAcrescimo.insert(0, 'R$ 0,00')
        # Fonte de pesquisa do método 'bind':
        # https://stackoverflow.com/questions/46567324/tkinter-window-focus-loss-event
        self.txtPreco.bind("<FocusOut>", self.fDefinePorcentagem)
        self.btnPesquisar = tk.Button(win, text='Pesquisar', command=self.fPesquisarProduto)
        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)
        self.btnAtualizar = tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)
        self.btnExcluir = tk.Button(win, text='Excluir', command=self.fExcluirProduto)
        self.btnLimpar = tk.Button(win, text='Limpar', command=self.fLimparTela)
        self.btnTudo = tk.Button(win, text='Mostrar Todos os Produtos', command=self.fExibirTudo)
        # Posicionamentos
        self.lbCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)
        self.lblNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)
        self.lblPreco.place(x=100, y=150)
        self.txtPreco.place(x=250, y=150)
        self.lblAcrescimo.place(x=100, y=200)
        self.txtAcrescimo.place(x=250, y=200)

        posicionamentoBotoes = 250
        self.btnPesquisar.place(x=450, y=50)
        self.btnCadastrar.place(x=100, y=posicionamentoBotoes)
        self.btnAtualizar.place(x=200, y=posicionamentoBotoes)
        self.btnExcluir.place(x=300, y=posicionamentoBotoes)
        self.btnLimpar.place(x=400, y=posicionamentoBotoes)
        self.btnTudo.place(x=200, y=posicionamentoBotoes + 50)

    def fCadastrarProduto(self):  # Cadastra o produto no banco de dados
        try:
            (codigo, nome, preco, _) = self.fLerCampos()
            print('inserindo produto')
            self.objBD.inserirDados(codigo, nome, preco)
            self.fLimparTela()
            tkinter.messagebox.showinfo(title=None, message='Produto Cadastrado com Sucesso!')
        except:
            tkinter.messagebox.showerror(title="Erro", message='Não foi possível fazer o cadastro.')

    def fPesquisarProduto(self):  # Pesquisa um determinado produto pelo código e preenche os campos...
        try:
            (codigo, _, _, _) = self.fLerCampos()
            (codigo, nome, preco, acrescimo) = self.objBD.obterUmDado(codigo)

            self.txtNome.delete(0, tk.END)
            self.txtNome.insert(0, nome)

            self.txtPreco.delete(0, tk.END)
            self.txtPreco.insert(0, f'{preco}')

            self.txtAcrescimo.delete(0, tk.END)
            self.txtAcrescimo.insert(0, f'R$ {acrescimo:,.2f}')
        except Exception as error:
            tkinter.messagebox.showerror(title="Erro", message="""
                Não foi possível realizar a busca do produto.\nOu o produto não existe!
            """.strip())
            print(error)

    def fLimparTela(self):  # Limpa todos os campos
        try:
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            self.txtAcrescimo.delete(0, tk.END)
        except:
            tkinter.messagebox.showerror(title="Erro", message='Não foi possível limpar os campos.')

    def fLerCampos(self):  # Obtém cada um dos campos...
        codigo = f'{self.txtCodigo.get()}'
        nome = f'{self.txtNome.get()}'
        preco = f'{self.txtPreco.get()}'
        acrescimo = f'{self.acrescimo}'
        return codigo, nome, preco, acrescimo

    def fAtualizarProduto(self): #Atualiza um determinado produto
        try:
            (codigo, nome, preco, _) = self.fLerCampos()
            print('atualizando produto')
            self.objBD.atualizarDados(codigo, nome, preco)
            self.fLimparTela()
            tkinter.messagebox.showinfo(title=None, message='Produto Atualizado com Sucesso!')
        except:
            tkinter.messagebox.showerror(title="Erro", message='Não foi possível fazer a atualização.')

    def fExcluirProduto(self): #Remove um determinado produto pelo código e limpa os campos.
        try:
            (codigo, nome, preco, _) = self.fLerCampos()
            print('excluindo produto')
            self.objBD.excluirDados(codigo)
            self.fLimparTela()
            tkinter.messagebox.showinfo(title=None, message='Produto Excluído com Sucesso!')
        except:
            tkinter.messagebox.showerror(title="Erro", message='Não foi possível fazer a exclusão do produto.')

    def fExibirTudo(self): #Exibe todos os produtos cadastrados no banco de dados
        janelaExibirTudo = tk.Tk()
        dados = []
        try:
            for (codigo, nome, preco, precoAcresc) in self.objBD.obterTodosOsDados():
                # Adicionando um a um, para formatar o preço, colocando o R$...
                dados.append((codigo, nome, f'R$ {preco:,.2f}', f'R$ {precoAcresc:,.2f}'))
            print(dados)
        except:
            tk.messagebox.showerror(title='Erro',
                                    message='Não foi possível obter os dados.\nSerá exibido dados de exemplo!')
        TodosRegistros(janelaExibirTudo, dados)
        janelaExibirTudo.title('Todos os registros')
        janelaExibirTudo.mainloop()

    def fDefinePorcentagem(self, args): #Calcula automaticamente a porcentagem e preenche o campo...
        try:
            if self.txtPreco.get() == '': return
            (_, _, preco, _) = self.fLerCampos()
            preco = float(preco.replace(',', '.'))
            self.acrescimo = calc_acrescimo(preco, 10 / 100)
            self.txtAcrescimo.delete(0, tk.END)
            self.txtAcrescimo.insert(0, f'R$ {self.acrescimo:,.2f}')
        except:
            print('Erro ao definir porcentagem!')


# -------------------------------------
# Programa Principal
# -------------------------------------
janela = tk.Tk()
principal = PrincipalBD(janela, 10 / 100)
janela.title('Bem Vindo a JJ4Tech')
janela.geometry("600x500")
janela.mainloop()
