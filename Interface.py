from tkinter import*
from tkinter import ttk
import sqlite3
import pandas as pd
import time
import datetime
from threading import Timer
### INSERIR SCROOLL BAR NAS TREE VIEW#####
###BOTÃO UPDATE ATUALIZAR VLOR ATUAL#####
path = (r'C:\Users\win\Carteira-Acoes')
conn = sqlite3.connect(path + r'\teste_Acoes.db')
c = conn.cursor()


def criar_tabela():
    c.execute('CREATE TABLE IF NOT EXISTS Acoes (nome text, valor_de_compra real, quantidade integer ,data text)')
    c.execute('CREATE TABLE IF NOT EXISTS AcoesCompleta(nome text, valor_de_compra real, quantidade integer, data text, valor_atual real)')
    c.execute('CREATE TABLE IF NOT EXISTS taxaNome (nome text, valor_taxa real)')
    c.execute('CREATE TABLE IF NOT EXISTS valorAtual (valor real, Lucro real, lucro_porcentagem real)')

criar_tabela()

class Pagina_Principal():

    def __init__(self, janela):
        self.janela1 = janela
        self.janela1.title('Carteira de Ações')
        self.janela1.geometry('380x590+100+70')
        self.cor_pagina = '#4d5d53'
        self.fonte = 'Century Gothic'
        self.cor_fonte = '#dbdace'

        #CENTER FRAME
        self.center = Frame(self.janela1, bg=self.cor_pagina, width = 310, height = 310)
        self.center.grid(row=1, sticky = W + E)

        #TOP FRAME
        self.top = Frame(self.janela1, bg='#403f3f', width = 310, height = 60)
        self.top.grid(row=0, sticky = W + E)

        #BOT FRAME
        self.bot = Frame(self.janela1, bg='white', width = 310, height = 250)
        self.bot.grid(row=2, sticky = W + E)

        # LABELS FRAME
        #LABEL FRAME CORRETORA
        self.frame = LabelFrame(self.center, text = 'Informações de Corretagem', bg=self.cor_pagina,
                                relief = 'sunken', labelanchor = 'n',bd=3,font=(self.fonte,11,'bold'),fg=self.cor_fonte)
        self.frame.grid(row=1,columnspan=2, pady=5,padx = 15)

        #LABEL FRAME AÇÕES
        self.frame1 = LabelFrame(self.center, text='Informações Sobre O papel',bg=self.cor_pagina,
                                 relief = 'sunken', labelanchor = 'n',bd=3, font=(self.fonte,11,'bold'),fg=self.cor_fonte)
        self.frame1.grid(row=2, columnspan=2, pady=5)

        # ADICIONAR LABELS
        #LABELS TOP FRAME
        self.carteira_completa = Label(self.top, text = 'Carteira', fg='white',
                                       bg='#403f3f', font = ('Rockwell',8,'bold'))
        self.carteira_completa.place(x=8, y = 44)

        self.graficos = Label(self.top, text = 'Graficos', fg='white',
                                       bg='#403f3f', font = ('Rockwell',8,'bold'))
        self.graficos.place(x=66, y = 44)

        self.graficos = Label(self.top, text = 'Simulador', fg='white',
                                       bg='#403f3f', font = ('Rockwell',8,'bold'))
        self.graficos.place(x=126, y = 44)

        #LABELS FRAME CORRETORA
        self.n_corretora = Label(self.frame, text='Nome da Corretora', bg=self.cor_pagina,
                                 font=(self.fonte,10),fg=self.cor_fonte)
        self.n_corretora.grid(row=0, column=0, pady=3)

        self.taxa = Label(self.frame, text='Valor da Taxa de Corretagem',bg=self.cor_pagina,
                          font=(self.fonte,10),fg=self.cor_fonte)
        self.taxa.grid(row=1, column=0)

        self.nome_corretora_lb = Label(self.frame, text='', bg=self.cor_pagina,
                                       fg='yellow')
        self.nome_corretora_lb.grid(row=3, column=0, sticky=E)
        self.valor_taxa_lb = Label(self.frame, text='', bg=self.cor_pagina,
                                   fg='yellow')
        self.valor_taxa_lb.grid(row=4, column=0, sticky=W)


        #LABELS FRAME AÇÕES
        self.nome = Label(self.frame1, text='Nome do Papel',bg=self.cor_pagina,
                          font = (self.fonte,10),fg=self.cor_fonte)
        self.nome.grid(row=1, column=0)

        self.valor_de_compra = Label(self.frame1, text='Valor de Compra',bg=self.cor_pagina,
                                     font=(self.fonte,10),fg=self.cor_fonte)
        self.valor_de_compra.grid(row=2, column=0)

        self.quantidade = Label(self.frame1, text='Quantidade de Papéis',bg=self.cor_pagina,
                                font=(self.fonte,10),fg=self.cor_fonte)
        self.quantidade.grid(row=3, column=0)

        self.data = Label(self.frame1, text='Data de Compra',bg=self.cor_pagina,
                          font=(self.fonte,10),fg=self.cor_fonte)
        self.data.grid(row=4, column=0)

        # ADICIONAR ENTRYS
        ####### ENTRY DADOS CORRETORA #######
        self.n_corretora_entry = Entry(self.frame)
        self.n_corretora_entry.grid(row=0, column=1,pady=3,padx=10)

        self.taxa_entry = Entry(self.frame)
        self.taxa_entry.grid(row=1, column=1)

        ###### ENTRY DADOS AÇÕES ########
        self.nome_entry = Entry(self.frame1)
        self.nome_entry.grid(row=1, column=1, pady=5, padx=10)

        self.valor_entry = Entry(self.frame1)
        self.valor_entry.grid(row=2, column=1, pady=5)

        self.quantidade_entry = Entry(self.frame1)
        self.quantidade_entry.grid(row=3, column =1, pady=5)

        self.data_entry = Entry(self.frame1)
        self.data_entry.grid(row=4, column=1, pady=5)

        ###### BOTÕES PARA TROCA DE PÁGINA #######
        self.carteira_imagem = PhotoImage(file ='C:\\Users\\win\\PycharmProjects\\Carteira_Acoes\\icons\\wallet.png')
        button_carteira = Button(self.top, image = self.carteira_imagem, command = self.go_to_carteira, bg='#403f3f')
        button_carteira.place(x=15, y=5)

        self.grafico_imagem = PhotoImage(file = 'C:\\Users\\win\\PycharmProjects\\Carteira_Acoes\\icons\\graph.png')
        button_grafico = Button(self.top, image = self.grafico_imagem, bg='#403f3f')
        button_grafico.place(x = 75, y=5)

        self.simulador_imagem = PhotoImage(file = 'C:\\Users\\win\\PycharmProjects\\Carteira_Acoes\\icons\\target.png')
        button_simulador = Button(self.top, image = self.simulador_imagem, bg='#403f3f',command = self.go_to_simulador)
        button_simulador.place(x=135, y = 5)


        ###### BOTÕES PARA DADOS CORRETORA######
        button_add_corretora = ttk.Button(self.frame, text='Salvar', command = self.salvar_corretora)
        button_add_corretora.grid(row=2, columnspan =3, pady=8)

        ####### BOTÕES PARA DADOS AÇÕES ########
        button_add_acoes = ttk.Button(self.frame1, text='Adicionar',command = self.inserir_dados)
        button_add_acoes.grid(row=5, columnspan=3, pady=5)


        # ESTILO DA MESA
        self.estilo = ttk.Style()
        self.estilo.configure("TreeView",background ="green",foreground="white", relief = "flat")

        # ADICIONAR MESA
        self.tree = ttk.Treeview(self.bot)
        self.tree['columns'] = ('One', 'Two','Three')
        self.tree.grid(row=1,column= 0)
        self.tree.column('#0', width=100)
        self.tree.heading('#0', text='Nome do Papel', anchor=CENTER)
        self.tree.column('One', width=90)
        self.tree.heading('One', text='Preço Compra', anchor=CENTER)
        self.tree.column('Two', width=90)
        self.tree.heading('Two', text='Quantidade', anchor=CENTER)
        self.tree.column('Three',width= 80)
        self.tree.heading('Three', text = 'Data Compra', anchor = CENTER)
        self.style = ttk.Style()
        self.style.configure('Treeview',rowheight= 15)
        self.style.configure('Treeview.Heading',font=('arial',9,'bold'))


        #AICIONAR SCROLLBAR
        self.vsb = ttk.Scrollbar(self.bot, orient = 'vertical', command= self.tree.yview)
        self.vsb.grid(row=1, column=1, sticky = 'NSE')

        self.tree.configure(yscrollcommand = self.vsb.set)
        self.vsb.configure(command = self.tree.yview)

        ##### CHAMAR FUNÇOES ####
        self.add_na_tabela()
        self.mostrar_dados_corretora()
        #self.nome_corretora_lb = Label(frame, text='')
        #self.nome_corretora_lb.grid(row=3, column=0)

    def validacao(self):
        return len(self.nome_entry.get()) !=0 and len(self.valor_entry.get()) !=0 and (self.data_entry.get()) !=0

    '''def valorAtual(self):
        self.nome_papel = str(self.nome_entry.get())
        self.data = pd.read_html('https://markets.ft.com/data/equities/tearsheet/summary?s='+self.nome_papel+':SAO')
        self.dados_resumidos = (self.data[0].head())
        self.valorAtual = self.dados_resumidos[1][4]
        print(self.valorAtual)
        return self.valorAtual
'''


    def inserir_dados(self):
        #### BUSCANDO TAXA #####
        self.pegar_valor_atual()
        c.execute("SELECT * FROM taxaNome ORDER BY nome ASC LIMIT 1")
        self.result = c.fetchone()
        if self.result is not None:
            self.taxa_corretagem = self.result[1]
            self.nome1 = self.nome_entry.get()
            self.valor1 = self.valor_entry.get()
            self.data1 = self.data_entry.get()
            self.quantidade1 = self.quantidade_entry.get()
            print(self.nome1, self.valor1, self.data1)
            if self.validacao():
                #c.execute("INSERT INTO valorAtual VALUES(?)",(self.valor_float,))
                c.execute("INSERT INTO Acoes VALUES (?,?,?,?)", (self.nome1, self.valor1, self.quantidade1, self.data1))
                c.execute("INSERT INTO AcoesCompleta VALUES (?,?,?,?,?)",(self.nome1, self.valor1, self.quantidade1, self.data1,self.valorAtual))
                conn.commit()
                self.nome_entry.delete(0, END)
                self.valor_entry.delete(0, END)
                self.data_entry.delete(0, END)
                self.quantidade_entry.delete(0, END)
            else:
                print('Faltam dados a serem preenchidos')
        else:
            self.taxa_corretagem = 0
            self.erro_corretora()

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
            self.tree.insert('',0, text = row[0], values = (row[1],row[2],row[3]),tag = ('teste',))
            self.tree.tag_configure('teste', foreground='yellow',background='red', font = ('',9))


    def salvar_corretora(self):
        self.nome_corretora = self.n_corretora_entry.get()
        self.valor_taxa = self.taxa_entry.get()
        self.nomes = [self.nome[0] for self.nome in c.execute("SELECT nome from taxaNome")]
        if (len(self.n_corretora_entry.get())!=0 and len(self.taxa_entry.get())!=0 and (len(self.nomes))==0):
            c.execute("INSERT INTO taxaNome VALUES(?,?)",(self.nome_corretora,self.valor_taxa))
            conn.commit()
            c.execute("SELECT * FROM taxaNome WHERE nome = ?",(self.n_corretora_entry.get(),))
            for row in c.fetchall():
                self.dado_nome = row[0]
                self.dado_taxa = row[1]
            self.dado_nome_str = str(self.dado_nome)
            self.dado_taxa_str = str(self.dado_taxa)
            self.nome_corretora_lb = Label(self.frame, text= 'Corretora: '+self.dado_nome_str, bg = self.cor_pagina, fg='yellow')
            self.nome_corretora_lb.grid(row=3, column=0, sticky = W)
            self.valor_taxa_lb = Label(self.frame, text = 'Taxa de corretagem: '+self.dado_taxa_str, bg = self.cor_pagina, fg='yellow')
            self.valor_taxa_lb.grid(row=4, column=0, sticky=W)
        else:
            c.execute("UPDATE taxaNome SET nome = ?, valor_taxa = ?",(self.nome_corretora,self.valor_taxa))
            conn.commit()
            c.execute("SELECT * FROM taxaNome")
            for row in c.fetchall():
                self.dado_nome = row[0]
                self.dado_taxa = row[1]
            self.dado_nome_str = str(self.dado_nome)
            self.dado_taxa_str = str(self.dado_taxa)
            self.nome_corretora_lb = Label(self.frame, text= 'Corretora: '+self.dado_nome_str, bg = self.cor_pagina, fg='yellow')
            self.nome_corretora_lb.grid(row=3, column=0, sticky = W)
            self.valor_taxa_lb = Label(self.frame, text = 'Taxa de corretagem: '+self.dado_taxa_str, bg = self.cor_pagina, fg='yellow')
            self.valor_taxa_lb.grid(row=4, column=0, sticky=W)

    def pegar_valor_atual(self):
        self.nome_papel = str(self.nome_entry.get())
        self.data = pd.read_html('https://markets.ft.com/data/equities/tearsheet/summary?s=' + self.nome_papel + ':SAO')
        self.dados_resumidos = (self.data[0].head())
        self.valorAtual = self.dados_resumidos[1][4]
        self.valor_float = float(self.valorAtual)
        return self.valorAtual


    def mostrar_dados_corretora(self):
        c.execute("SELECT * FROM taxaNome ORDER BY nome ASC LIMIT 1")
        self.result = c.fetchone()
        if self.result is not None:
            self.label_nome = self.result[0]
            self.label_taxa = self.result[1]
            self.label_taxa_str = str(self.label_taxa)
            print(self.label_nome)
            print(self.label_taxa)
            self.result_corretora = Label(self.frame, text = 'Corretora: '+self.label_nome, bg = self.cor_pagina, fg='yellow')
            self.result_corretora.grid(row=3, column=0, sticky=W)
            self.result_nome = Label(self.frame, text = 'Taxa de Corretagem: '+self.label_taxa_str, bg =self.cor_pagina, fg='yellow')
            self.result_nome.grid(row=4,column=0,sticky =W)
        else:
            print('vazio')

    def erro_corretora(self):
        self.messagebox = Toplevel(bg='white')
        self.messagebox.title('Erro')
        self.messagebox.geometry("200x100")
        self.messagebox.focus_set()
        self.messagebox.grab_set()

        self.mensagem = Label(self.messagebox, text='Preencha os dados \nda sua corretora', fg='red', bg='white',
                              font=('Arial', 8, 'bold')).place(x=50, y=10)
        self.button = Button(self.messagebox, text="OK", width=10, command=lambda: self.messagebox.destroy())
        self.button.place(x=60, y=50)




    def go_to_carteira(self):
        janela2 = Toplevel(self.janela1)
        pagina_escolhida = carteiraCompleta(janela2)
        if 'normal' == janela2.state():
        #janela2.transient(self.janela1)
            janela2.focus_set()
            janela2.grab_set()



    def go_to_simulador(self):
        janela3 = Toplevel(self.janela1)
        pagina_escolhida = Simulador(janela3)

class carteiraCompleta():
    def __init__(self,janela):
        self.janela = janela
        self.janela.geometry('721x210+480+70')
        ## ADICIONAR FRAMES
        self.top= Frame(self.janela, height = 30, width = 720, bg='white')
        self.top.grid(row=0,sticky =  W+E)

        self.centro = Frame(self.janela, height = 170, width  = 705, bg='white')
        self.centro.grid(row=1,sticky = W)

        self.style = ttk.Style()
        self.style.configure("")

        #ADICIONAR MESA UM
        self.tree = ttk.Treeview(self.centro)
        self.tree['columns'] = ('One', 'Two','Three')
        self.tree.column('#0', width=100)
        self.tree.heading('#0', text='Nome do Papel', anchor=CENTER)
        self.tree.column('One', width=100)
        self.tree.heading('One', text='Preço de Compra', anchor=CENTER)
        self.tree.column('Two', width=100)
        self.tree.heading('Two', text='Quantidade', anchor=CENTER)
        self.tree.column('Three', width=100)
        self.tree.heading('Three', text = 'Data Compra', anchor = CENTER)
        self.tree.grid(row=1, column= 0)

        #ADICIONAR MESA 2


        self.tree2 = ttk.Treeview(self.centro,style = "Custom.Treeview")
        self.tree2['columns'] = ('primeira','segunda')
        self.tree2.column('#0',width=100)
        self.tree2.heading('#0', text = 'Valor Atual', anchor = CENTER)
        self.tree2.column('primeira', width = 90)
        self.tree2.heading('primeira',text = 'Lucro R$', anchor = CENTER)
        self.tree2.column('segunda', width = 115)
        self.tree2.heading('segunda',text = 'Valorização %', anchor = CENTER)
        self.tree2.grid(row=1, column = 1)
        self.tree2.tag_configure("teste",background = 'black')

        #AICIONAR SCROLLBAR
        self.vsb = ttk.Scrollbar(self.centro, orient = 'vertical', command= self.tree.yview)
        self.vsb.grid(row=1, column=1, sticky = 'NSE')

        self.tree.configure(yscrollcommand = self.vsb.set)
        self.vsb.configure(command = self.tree.yview)

        ### BOTÃO DE UPDATE ####
        self.bt_update = Button(self.top, width = 10, text = 'Editar')
        self.bt_update.place(x=10, y=0)

        self.bt_vender = Button(self.top, width = 10, text = 'Ação Vendida')
        self.bt_vender.place(x=120, y=0)

        #self.add_na_tabela()
        self.atualizando_no_tempo()
        self.add_na_tabela()
        self.limpar_tabela_Completa()

    def valor_atual(self):
        self.nomes = [self.nome[0] for self.nome in c.execute("SELECT nome from AcoesCompleta")]
        self.valor_compra = [self.compra[0] for self.compra in c.execute("SELECT valor_de_compra from AcoesCompleta")]
        self.quant_compra= [self.quant[0] for self.quant in c.execute("SELECT quantidade from AcoesCompleta")]
        self.valor_atual_lista = [self.valor01[0] for self.valor01 in c.execute("SELECT valor from valorAtual")]
        self.taxas = [self.taxa01[0] for self.taxa01 in c.execute("SELECT valor_taxa FROM taxaNome")]
        self.nomes_quantidade = len(self.nomes)
        self.quantidade_acoes = len([self.valor for self.valor in c.execute("SELECT valor from valorAtual")])
        self.valoresAtuais = []
        self.indice = 0
        self.contador = 1
        self.i = 0
        while self.contador<=(len(self.nomes)):
            self.nome_papel = self.nomes[self.indice]
            self.data = pd.read_html('https://markets.ft.com/data/equities/tearsheet/summary?s=' + self.nome_papel + ':SAO')
            self.dados_resumidos = (self.data[0].head())
            self.valorAtual = self.dados_resumidos[1][4]
            self.valoresAtuais.append(self.valorAtual)

            self.lucro = ((self.valorAtual*self.quant_compra[self.indice]) - (self.valor_compra[self.indice]*self.quant_compra[self.indice])-2*self.taxas[0])
            self.decimal_lucro = ("%.2f" % self.lucro)
            self.valorizacao = (((self.valorAtual)/(self.valor_compra[self.indice]))-1)*100
            self.decimal_valorizacao = ("%.2f" % self.valorizacao)

            if self.quantidade_acoes!=self.nomes_quantidade and self.quantidade_acoes<self.nomes_quantidade:
                c.execute("INSERT INTO valorAtual VALUES(?,?,?)", (self.valorAtual,self.decimal_lucro,self.decimal_valorizacao))
                conn.commit()
            else:
                records = self.tree2.get_children()
                for element in records:
                    self.tree2.delete(element)
                c.execute("DELETE FROM valorAtual")
                conn.commit()

            self.indice += 1
            self.contador += 1

        c.execute('SELECT * FROM valorAtual')
        for linhas in c.fetchall():
            self.tree2.insert('',0,text=linhas[0], values= (linhas[1],str(linhas[2])+'%'),tags="teste")

        if self.quantidade_acoes == self.nomes_quantidade:
            records = self.tree2.get_children()
            for element in records:
                self.tree2.delete(element)



    def atualizando_no_tempo(self):
        contador = True
        def callback():
            nonlocal contador
            self.valor_atual()
            self.janela.after(2000, lambda: contador == False)
            if contador == False:
                 self.janela.update()
            else:
                self.janela.after(4000, callback)
            #contador-=1
            #if not contador:
                #self.janela.update()
            #else:
                #self.janela.after(1000, callback)
        self.janela.after(2000, callback)

    def limpar_tabela_Completa(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        c.execute("SELECT * FROM acoesCompleta")
        for row in c.fetchall():
            self.nome = row[0]
            self.valor = row[1]
            self.quantidade = row[2]
            self.data = row[3]
            self.tree.insert('', 0, text=self.nome, values=(self.valor, self.quantidade, self.data))
        return self.quantidade

    def add_na_tabela(self):
        c.execute("SELECT * FROM AcoesCompleta")
        for row in c.fetchall():
            self.tree.insert('', 'end', text=row[0], values=(row[1], row[2], row[3]), tags = ('teste1',))
            self.tree.tag_configure('teste1',background = 'orange')


################# PAGINA PARA SIMULAÇÃO ##############
class Simulador():
    def __init__(self,janela):
        self.janela = janela
        self.janela.geometry('700x180+480+325')
        self.janela_cor = '#4d5d53'  #'#2c3b54'
        self.fonte = 'Century Gothic'
        self.cor_fonte = '#dbdace'
        self.janela_simu = Frame(self.janela, bg=self.janela_cor, width = 700, height = 300)
        self.janela_simu.grid(row = 0, sticky = W + E)


        self.soma= 0
        while (self.soma<=81):
            self.layout(self.soma)
            self.soma+=27

        self.entries()
        self.botoes()
    def entries(self):
        ##### CRIAR ENTRYS PRIMEIRA FILA#####
        self.na_entry1 = Entry(self.janela, width=15)
        self.na_entry1.place(x=40, y=37)

        self.va_entry1 = Entry(self.janela, width=15)
        self.va_entry1.place(x=162, y=37)

        self.qa_entry1 = Entry(self.janela, width=10)
        self.qa_entry1.place(x=290, y=37)

        self.vd_entry1 = Entry(self.janela, width=10)
        self.vd_entry1.place(x=397, y=37)

        ##### CRIAR ENTRYS SEGUNDA FILA#####
        self.na_entry2 = Entry(self.janela, width=15)
        self.na_entry2.place(x=40, y=64)

        self.va_entry2 = Entry(self.janela, width=15)
        self.va_entry2.place(x=162, y=64)

        self.qa_entry2 = Entry(self.janela, width=10)
        self.qa_entry2.place(x=290, y=64)

        self.vd_entry2 = Entry(self.janela, width=10)
        self.vd_entry2.place(x=397, y= 64)

        ##### CRIAR ENTRYS TERCEIRA FILA#####
        self.na_entry3 = Entry(self.janela, width=15)
        self.na_entry3.place(x=40, y=90)

        self.va_entry3 = Entry(self.janela, width=15)
        self.va_entry3.place(x=162, y=90)

        self.qa_entry3 = Entry(self.janela, width=10)
        self.qa_entry3.place(x=290, y=90)

        self.vd_entry3 = Entry(self.janela, width=10)
        self.vd_entry3.place(x=397, y=90)

        ##### CRIAR ENTRYS QUARTA FILA#####
        self.na_entry4 = Entry(self.janela, width=15)
        self.na_entry4.place(x=40, y=115)

        self.va_entry4 = Entry(self.janela, width=15)
        self.va_entry4.place(x=162, y = 115)

        self.qa_entry4 = Entry(self.janela, width=10)
        self.qa_entry4.place(x=290, y=115)

        self.vd_entry4 = Entry(self.janela, width=10)
        self.vd_entry4.place(x=397, y= 115)

    def botoes(self):
        ##### CRIAR BOTÕES PRIMEIRA FILA ######
        self.cor_botao = '#e6e6fa'
        self.b_calcular1 = Button(self.janela, text='Calcular', width =10, bg=self.cor_botao, command = self.calcular_linha1)
        self.b_calcular1.place(x=540, y = 33)

        self.b_deletar1 = Button(self.janela, text = 'Apagar', width =10,bg=self.cor_botao, command = self.deletar_linha1)
        self.b_deletar1.place(x=620, y = 33)

        ##### CRIAR BOTÕES SEGUNDA FILA ######
        self.b_calcular2 = Button(self.janela, text='Calcular', width =10,bg=self.cor_botao, command = self.calcular_linha2)
        self.b_calcular2.place(x=540, y = 60)

        self.b_deletar2 = Button(self.janela, text = 'Apagar', width =10,bg=self.cor_botao, command = self.deletar_linha2)
        self.b_deletar2.place(x=620, y = 60)

        ##### CRIAR BOTÕES TERCEIRA FILA ######
        self.b_calcular3 = Button(self.janela, text='Calcular', width =10,bg=self.cor_botao, command = self.calcular_linha3)
        self.b_calcular3.place(x=540, y = 87)

        self.b_deletar3 = Button(self.janela, text = 'Apagar', width =10,bg=self.cor_botao, command = self.deletar_linha3)
        self.b_deletar3.place(x=620, y = 87)

        ##### CRIAR BOTÕES QUARTA FILA ######
        self.b_calcular4 = Button(self.janela, text='Calcular', width =10,bg=self.cor_botao, command = self.calcular_linha4)
        self.b_calcular4.place(x=540, y = 114)

        self.b_deletar4 = Button(self.janela, text = 'Apagar', width =10,bg=self.cor_botao, command =self.deletar_linha4)
        self.b_deletar4.place(x=620, y = 114)


    def layout(self,soma):
        self.lista_na = [0,1,2,3]

        #### CRIAR LABELS #####
        #RELIEFS = flat, groove, raised, ridge, solid, sunken
        self.nome_acao = Label(self.janela, text = 'Nome da Ação', fg= self.cor_fonte, bg=self.janela_cor,
                               font=(self.fonte,10,'bold'),relief = 'groove')
        self.nome_acao.place(x=40, y = 8)

        self.valor_acao = Label(self.janela, text = 'Valor Da Ação', fg=self.cor_fonte, bg=self.janela_cor,
                                font = (self.fonte,10,'bold'),relief = 'groove')
        self.valor_acao.place(x = 156, y= 8)

        self.quantidade_acao = Label(self.janela, text = 'Quantidade', fg = self.cor_fonte,bg=self.janela_cor,
                                     font=(self.fonte,10,'bold'),relief = 'groove')
        self.quantidade_acao.place(x=267,y=8)

        self.valor_venda= Label(self.janela, text = 'Valor de Venda', fg =self.cor_fonte,bg=self.janela_cor,
                                font=(self.fonte,10,'bold'),relief = 'groove')
        self.valor_venda.place(x=362, y= 8)

        self.lucro = Label(self.janela, text = 'Lucro', fg = '#34a31b', bg = self.janela_cor,
                           font=(self.fonte,10,'bold'),relief = 'groove')
        self.lucro.place(x=480,y=8)

        ######## CRIAR IMAGENS #########
        self.foto_nome= PhotoImage(file='C:\\Users\win\\Carteira-Acoes\\icons\\investment.png')
        self.foto_nome_lab = Label(self.janela,image = self.foto_nome,bg=self.janela_cor)
        self.foto_nome_lab.image = self.foto_nome
        self.foto_nome_lab.place(x=3, y=(30+soma))

        self.foto_valor= PhotoImage(file='C:\\Users\win\\Carteira-Acoes\\icons\\money_bag_menor.png')
        self.foto_valor_lab = Label(self.janela,image = self.foto_valor,bg=self.janela_cor)
        self.foto_valor_lab.image = self.foto_valor
        self.foto_valor_lab.place(x=133, y=(30+soma))

        self.foto_quantidade= PhotoImage(file='C:\\Users\win\\Carteira-Acoes\\icons\\overflow.png')
        self.foto_quantidade_lab = Label(self.janela,image = self.foto_quantidade,bg=self.janela_cor)
        self.foto_quantidade_lab.image = self.foto_quantidade
        self.foto_quantidade_lab.place(x=255, y=(29+soma))

        self.foto_venda= PhotoImage(file='C:\\Users\win\\Carteira-Acoes\\icons\\money.png')
        self.foto_venda_lab = Label(self.janela,image = self.foto_venda,bg=self.janela_cor)
        self.foto_venda_lab.image = self.foto_venda
        self.foto_venda_lab.place(x=360, y=(35+soma))

########### FUNÇÕES DOS BOTÕES ##############
        ########## LINHA 1 ###########
    def calcular_linha1(self):
        nome_acao = str(self.na_entry1.get())
        valor_compra = float(self.va_entry1.get())
        valor_quantidade = int(self.qa_entry1.get())
        valor_venda = float(self.vd_entry1.get())
        lucro = (valor_venda*valor_quantidade)-(valor_compra*valor_quantidade)
        lucro_str = 'RS'+str(lucro)
        if lucro>0:
            self.lucro_lb1 = Label(self.janela, text = lucro_str, fg = 'green',bg='yellow', width = 8)
            self.lucro_lb1.place(x=470,y=36)
            self.mensagem_positiva = Label(self.janela, text=('O seu lucro com a venda de '+nome_acao+' seria de '+lucro_str),fg='yellow',
                                           bg=self.janela_cor, font=('Rockwell',10,'bold'))
            self.mensagem_positiva.place(x=5, y=155)
            self.mensagem_positiva.after(3000, lambda : self.mensagem_positiva.destroy())

        else:
            self.lucro_lb1 = Label(self.janela, text=lucro_str, fg='white', bg='red', width=8)
            self.lucro_lb1.place(x=470, y=36)
    def deletar_linha1(self):
        self.va_entry1.delete(0, END)
        self.qa_entry1.delete(0, END)
        self.vd_entry1.delete(0, END)
        self.lucro_lb1.destroy()

    ########## LINHA 2 ###########
    def calcular_linha2(self):
        nome_acao = str(self.na_entry2.get())
        valor_compra = float(self.va_entry2.get())
        valor_quantidade = int(self.qa_entry2.get())
        valor_venda = float(self.vd_entry2.get())
        lucro = (valor_venda*valor_quantidade)-(valor_compra*valor_quantidade)
        lucro_str = 'RS'+str(lucro)
        if lucro>0:
            self.lucro_lb2 = Label(self.janela, text = lucro_str, fg = 'green',bg='yellow', width = 8)
            self.lucro_lb2.place(x=470,y=63)
            self.mensagem_positiva = Label(self.janela, text=('O seu lucro com a venda de '+nome_acao+' seria de '+lucro_str),fg='yellow',
                                        bg=self.janela_cor, font=('Rockwell',10,'bold'))
            self.mensagem_positiva.place(x=5, y=155)
            self.mensagem_positiva.after(3000, lambda : self.mensagem_positiva.destroy())

        else:
            self.lucro_lb2 = Label(self.janela, text=lucro_str, fg='white', bg='red', width=8)
            self.lucro_lb2.place(x=470, y=63)
    def deletar_linha2(self):
        self.va_entry2.delete(0, END)
        self.qa_entry2.delete(0, END)
        self.vd_entry2.delete(0, END)
        self.lucro_lb2.destroy()

    ########## LINHA 3 ###########

    def calcular_linha3(self):
        nome_acao = str(self.na_entry3.get())
        valor_compra = float(self.va_entry3.get())
        valor_quantidade = int(self.qa_entry3.get())
        valor_venda = float(self.vd_entry3.get())
        lucro = (valor_venda*valor_quantidade)-(valor_compra*valor_quantidade)
        lucro_str = 'RS'+str(lucro)
        if lucro>0:
            self.lucro_lb3 = Label(self.janela, text = lucro_str, fg = 'green',bg='yellow', width = 8)
            self.lucro_lb3.place(x=470,y=90)
            self.mensagem_positiva = Label(self.janela, text=('O seu lucro com a venda de '+nome_acao+' seria de '+lucro_str),fg='yellow',
                                           bg=self.janela_cor, font=('Rockwell',10,'bold'))
            self.mensagem_positiva.place(x=5, y=155)
            self.mensagem_positiva.after(3000, lambda : self.mensagem_positiva.destroy())

        else:
            self.lucro_lb3 = Label(self.janela, text=lucro_str, fg='white', bg='red', width=8)
            self.lucro_lb3.place(x=470, y=90)
    def deletar_linha3(self):
        self.va_entry3.delete(0, END)
        self.qa_entry3.delete(0, END)
        self.vd_entry3.delete(0, END)
        self.lucro_lb3.destroy()

    ########## LINHA 4 ###########
    def calcular_linha4(self):
        nome_acao = str(self.na_entry4.get())
        valor_compra = float(self.va_entry4.get())
        valor_quantidade = int(self.qa_entry4.get())
        valor_venda = float(self.vd_entry4.get())
        lucro = (valor_venda*valor_quantidade)-(valor_compra*valor_quantidade)
        lucro_str = 'RS'+str(lucro)
        if lucro>0:
            self.lucro_lb4 = Label(self.janela, text = lucro_str, fg = 'green',bg='yellow', width = 8)
            self.lucro_lb4.place(x=470,y=117)
            self.mensagem_positiva = Label(self.janela, text=('O seu lucro com a venda de '+nome_acao+' seria de '+lucro_str),fg='yellow',
                                           bg=self.janela_cor,font=('Rockwell',10,'bold'))
            self.mensagem_positiva.place(x=5, y=155)
            self.mensagem_positiva.after(3000, lambda : self.mensagem_positiva.destroy())

        else:
            self.lucro_lb4 = Label(self.janela, text=lucro_str, fg='white', bg='red', width=8)
            self.lucro_lb4.place(x=470, y=117)
    def deletar_linha4(self):
        self.va_entry4.delete(0, END)
        self.qa_entry4.delete(0, END)
        self.vd_entry4.delete(0, END)
        self.lucro_lb4.destroy()


if __name__ == '__main__':
    janela = Tk()
    janela.geometry()
    acoes = Pagina_Principal(janela)
    janela.mainloop()
