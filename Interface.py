from tkinter import*
from tkinter import ttk
import sqlite3
import pandas as pd

path = (r'C:\Users\win\PycharmProjects\Carteira_Acoes')
conn = sqlite3.connect(path + r'\teste_Acoes.db')
c = conn.cursor()


def criar_tabela():
    c.execute('CREATE TABLE IF NOT EXISTS Acoes (nome text, valor_de_compra real, quantidade integer ,data text)')
    c.execute('CREATE TABLE IF NOT EXISTS AcoesCompleta(nome text, valor_de_compra real, quantidade integer, data text, valor_atual real, lucro_dinheiro real)')

criar_tabela()

class Pagina_Principal():

    def __init__(self, janela):
        self.janela1 = janela
        self.janela1.title('Carteira de Ações')
        self.janela1.geometry('350x560+100+70')

        #CENTER FRAME
        self.center = Frame(self.janela1, bg='#696969', width = 300, height = 510)
        self.center.grid(row=1, sticky = W + E)

        #TOP FRAME
        self.top = Frame(self.janela1, bg='#403f3f', width = 300, height = 50)
        self.top.grid(row=0, sticky = W + E)

        # LABELS FRAME
        #LABEL FRAME CORRETORA
        frame = LabelFrame(self.center, text = 'Informações de Corretagem', bg='#696969')
        frame.grid(row=1,column=-0, pady=3)

        #LABEL FRAME AÇÕES
        frame1 = LabelFrame(self.center, text='Informações Sobre O papel',bg='#696969')
        frame1.grid(row=2, column=0, pady=5)

        # ADICIONAR LABELS
        #LABELS FRAME CORRETORA
        self.n_corretora = Label(frame, text='Nome da corretora', bg='#696969')
        self.n_corretora.grid(row=0, column=0, pady=3)

        self.taxa = Label(frame, text='Valor da taxa de corretagem',bg='#696969')
        self.taxa.grid(row=1, column=0)

        #LABELS FRAME AÇÕES
        self.nome = Label(frame1, text='Digite o nome do papel',bg='#696969')
        self.nome.grid(row=1, column=0)

        self.valor_de_compra = Label(frame1, text='Digite o valor de Compra',bg='#696969')
        self.valor_de_compra.grid(row=2, column=0)

        self.quantidade = Label(frame1, text='Quantidade de Papéis',bg='#696969')
        self.quantidade.grid(row=3, column=0)

        self.data = Label(frame1, text='Digite a Data de Compra',bg='#696969')
        self.data.grid(row=4, column=0)

        # ADICIONAR ENTRYS
        ####### ENTRY DADOS CORRETORA #######
        self.n_corretora_entry = Entry(frame)
        self.n_corretora_entry.grid(row=0, column=1,pady=3)

        self.taxa_entry = Entry(frame)
        self.taxa_entry.grid(row=1, column=1)

        ###### ENTRY DADOS AÇÕES ########
        self.nome_entry = Entry(frame1)
        self.nome_entry.grid(row=1, column=1, pady=5)

        self.valor_entry = Entry(frame1)
        self.valor_entry.grid(row=2, column=1, pady=5)

        self.quantidade_entry = Entry(frame1)
        self.quantidade_entry.grid(row=3, column =1, pady=5)

        self.data_entry = Entry(frame1)
        self.data_entry.grid(row=4, column=1, pady=5)

        ###### BOTÕES PARA TROCA DE PÁGINA #######
        self.carteira_imagem = PhotoImage(file ='C:\\Users\\win\\PycharmProjects\\Carteira_Acoes\\icons\\wallet.png')
        button_carteira = Button(self.top, image = self.carteira_imagem, command = self.go_to_carteira, bg='#403f3f')
        button_carteira.place(x=15, y=5)

        self.grafico_imagem = PhotoImage(file = 'C:\\Users\\win\\PycharmProjects\\Carteira_Acoes\\icons\\graph.png')
        button_grafico = Button(self.top, image = self.grafico_imagem, bg='#403f3f')
        button_grafico.place(x = 65, y=5)

        self.simulador_imagem = PhotoImage(file = 'C:\\Users\\win\\PycharmProjects\\Carteira_Acoes\\icons\\target.png')
        button_simulador = Button(self.top, image = self.simulador_imagem, bg='#403f3f')
        button_simulador.place(x=115, y = 5)


        ###### BOTÕES PARA DADOS CORRETORA######
        button_add_corretora = ttk.Button(frame, text='Adicionar')
        button_add_corretora.grid(row=2, columnspan =3, pady=3)

        ####### BOTÕES PARA DADOS AÇÕES ########
        button_add_acoes = ttk.Button(frame1, text='Adicionar',command = self.inserir_dados)
        button_add_acoes.grid(row=5, columnspan=3, pady=5)

        # ADICIONAR MESA
        self.tree = ttk.Treeview(self.janela1,)
        self.tree['columns'] = ('One', 'Two','Three')
        self.tree.column('#0', width=90)
        self.tree.heading('#0', text='Nome do Papel', anchor=CENTER)
        self.tree.column('One', width=100)
        self.tree.heading('One', text='Preço de Compra', anchor=CENTER)
        self.tree.column('Two', width=80)
        self.tree.heading('Two', text='Quantidade', anchor=CENTER)
        self.tree.column('Three',width= 80)
        self.tree.heading('Three', text = 'Data Compra', anchor = CENTER)
        self.tree.grid(row=6)

        # ESTILO DA MESA
        self.estilo = ttk.Style(self.janela1)
        self.estilo.theme_use("clam")
        self.estilo.configure("TreeView", background='#403f3f', fieldbackground='#403f3f',foreground='#403f3f')


        self.add_na_tabela()


    def validacao(self):
        return len(self.nome_entry.get()) !=0 and len(self.valor_entry.get()) !=0 and (self.data_entry.get()) !=0

    def valorAtual(self):
        self.nome_papel = str(self.nome_entry.get())
        self.data = pd.read_html('https://markets.ft.com/data/equities/tearsheet/summary?s='+self.nome_papel+':SAO')
        self.dados_resumidos = (self.data[0].head())
        self.valorAtual = self.dados_resumidos[1][4]
        return self.valorAtual

    def inserir_dados(self):
        self.valorAtual()
        self.valor_atual = self.valorAtual
        self.nome1 = self.nome_entry.get()
        self.valor1 = self.valor_entry.get()
        self.data1 = self.data_entry.get()
        self.quantidade1 = self.quantidade_entry.get()
        self.quantidade_atual = (int(self.quantidade1)*float(self.valor_atual))
        self.quantidade_compra = (int(self.quantidade1)*float(self.valor1))
        self.lucro = (self.quantidade_atual - self.quantidade_compra)
        print(self.nome1,self.valor1,self.data1)
        if self.validacao():
            c.execute("INSERT INTO Acoes VALUES (?,?,?,?)", (self.nome1, self.valor1, self.quantidade1, self.data1))
            c.execute("INSERT INTO AcoesCompleta VALUES (?,?,?,?,?,?)", (self.nome1, self.valor1, self.quantidade1, self.data1,self.valorAtual,self.lucro))
            conn.commit()
            self.nome_entry.delete(0,END)
            self.valor_entry.delete(0, END)
            self.data_entry.delete(0, END)
        else:
            print('Faltam dados a serem preenchidos')

        self.limpar_tabela()

    def limpar_tabela(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        c.execute("SELECT * FROM Acoes")
        for row in c.fetchall():
            print(row)
            self.tree.insert('', 0, text=row[0], values=(row[1], row[2],row[3]))

    def add_na_tabela(self):
        c.execute("SELECT * FROM Acoes")
        for row in c.fetchall():
            print(row)
            self.tree.insert('',0, text = row[0], values = (row[1],row[2],row[3]))

    def go_to_carteira(self):
        janela2 = Toplevel(self.janela1)
        pagina_escolhida = carteiraCompleta(janela2)

class carteiraCompleta():
    def __init__(self,janela):
        self.janela = janela
        self.janela.geometry('700x200+450+70')

        #ADICIONAR MESA
        self.tree = ttk.Treeview(self.janela)
        self.tree['columns'] = ('One', 'Two','Three','Four','Five','Six')
        self.tree.column('#0', width=100)
        self.tree.heading('#0', text='Nome do Papel', anchor=CENTER)
        self.tree.column('One', width=100)
        self.tree.heading('One', text='Preço de Compra', anchor=CENTER)
        self.tree.column('Two', width=100)
        self.tree.heading('Two', text='Quantidade', anchor=CENTER)
        self.tree.column('Three', width=100)
        self.tree.heading('Three', text = 'Data Compra', anchor = CENTER)
        self.tree.column('Four', width=100)
        self.tree.heading('Four', text = 'Valor Atual', anchor = CENTER)
        self.tree.column('Five', width=100)
        self.tree.heading('Five', text = 'LUCRO R$', anchor = CENTER)
        self.tree.column('Six', width = 100)
        self.tree.heading('Six', text = 'LUCRO %')
        self.tree.grid(row=1)

        self.add_na_tabela2()

        self.limpar_tabela2()
    def limpar_tabela2(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        c.execute("SELECT * FROM AcoesCompleta")
        for row in c.fetchall():
            self.tree.insert('', 0, text=row[0], values=(row[1], row[2], row[3], row[4],row[5]))

    def add_na_tabela2(self):
        c.execute("SELECT * FROM AcoesCompleta")
        for row in c.fetchall():
            self.tree.insert('', 0, text=row[0], values=(row[1], row[2], row[3], row[4],row[5]))







if __name__ == '__main__':
    janela = Tk()
    janela.geometry()
    acoes = Pagina_Principal(janela)
    janela.mainloop()
