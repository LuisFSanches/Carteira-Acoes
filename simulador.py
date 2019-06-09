from tkinter import*
class Simulador():
    def __init__(self,janela):
        self.janela = janela
        self.janela.geometry('700x300')

        self.janela_simu = Frame(self.janela, bg='#696969', width = 700, height = 300)
        self.janela_simu.grid(row = 0, sticky = W + E)

        ##### CRIAR LABELS #####
        self.nome_acao = Label(self.janela, text = 'Nome da Ação', fg= 'black')
        self.nome_acao.place(x=10, y = 10)

        self.valor_acao = Label(self.janela, text = 'Valor Da Ação', fg='black')
        self.valor_acao.place(x = 120, y= 10)

        self.quantidade_acao = Label(self.janela, text = 'Quantidade', fg = 'black')
        self.quantidade_acao.place(x=230,y=10)

        self.valor_venda= Label(self.janela, text = 'Valor de Venda', fg = 'black')
        self.valor_venda.place(x=330, y=10)

        ##### CRIAR ENTRYS #####
        self.na_entry = Entry(self.janela, width = 10)
        self.na_entry.place(x=18, y=35)

        self.va_entry = Entry(self.janela, width = 10)
        self.va_entry.place(x = 126, y = 35)

        self.qa_entry = Entry(self.janela, width = 10)
        self.qa_entry.place(x=232, y =35)

        self.va_entry = Entry(self.janela, width =10)
        self.va_entry.place(x=340, y =35)

        ##### CRIAR BOTÕES ######
        self.b_calcular = Button(self.janela, text='Calcular', width =10)
        self.b_calcular.place(x=425, y = 33)

        self.apagar = Button(self.janela, text = 'Apagar', width =10)
        self.apagar.place(x=510, y = 33)

        ##### CRIAR IMAGENS ######

        self.foto_nome= PhotoImage(file='C:\\Users\\win\\PycharmProjects\\Carteira_Acoes\\icons\\investment.png')
        self.foto_nome_lab = Label(self.janela,image = self.foto_nome,bg='#696969')
        self.foto_nome_lab.place(x=300, y=150)

        self.foto_valor= PhotoImage(file='C:\\Users\\win\\PycharmProjects\\Carteira_Acoes\\icons\\money_bag_menor.png')
        self.foto_valor_lab = Label(self.janela,image = self.foto_valor,bg='#696969')
        self.foto_valor_lab.place(x=10, y=150)

        self.foto_quantidade= PhotoImage(file='C:\\Users\\win\\PycharmProjects\\Carteira_Acoes\\icons\\overflow.png')
        self.foto_quantidade_lab = Label(self.janela,image = self.foto_quantidade,bg='#696969')
        self.foto_quantidade_lab.place(x=100, y=150)

        self.foto_venda= PhotoImage(file='C:\\Users\\win\\PycharmProjects\\Carteira_Acoes\\icons\\bank.png')
        self.foto_venda_lab = Label(self.janela,image = self.foto_venda,bg='#696969')
        self.foto_venda_lab.place(x=200, y=150)



if __name__ == '__main__':
    janela = Tk()
    janela.geometry()
    simu = Simulador(janela)
    janela.mainloop()
