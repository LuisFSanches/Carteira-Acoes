from tkinter import*
from tkinter import ttk
import sqlite3

class carteiraCompleta():
    def __init__(self,janela):
        self.janela = janela
        self.janela.geometry('600x200')

        #ADICIONAR MESA
        self.tree = ttk.Treeview(self.janela)
        self.tree['columns'] = ('One', 'Two','Three','Four','Five')
        self.tree.column('#0', width=100)
        self.tree.heading('#0', text='Nome do Papel', anchor=CENTER)
        self.tree.column('One', width=100)
        self.tree.heading('One', text='Preço de Compra', anchor=CENTER)
        self.tree.column('Two', width=100)
        self.tree.heading('Two', text='Data da Compra', anchor=CENTER)
        self.tree.column('Three', width=100)
        self.tree.heading('Three', text = 'Valor Atual', anchor = CENTER)
        self.tree.column('Four', width=100)
        self.tree.heading('Four', text = 'LUCRO R$', anchor = CENTER)
        self.tree.column('Five', width=100)
        self.tree.heading('Five', text = 'LUCRO %', anchor = CENTER)
        self.tree.grid(row=1)

    def add_na_tabela2(self):
        c.execute("SELECT * FROM Acoes")
        for row in c.fetchall():
            print(row)
            self.tree.insert('', 0, text=row[0], values=(row[1], row[2]))

    def valorAtual(self):
        data = pd.read_html('https://markets.ft.com/data/equities/tearsheet/summary?s=BEEF3F:SAO')
        self.dados_resumidos = (data[0].head())
        self.valorAtual = self.dados_resumidos[1][4]

        def pegar_valores_tabela1(self):
            c.execute('SELECT * FROM Acoes')
            for row in c.fetchall():
                n = row[0]
                v = row[1]
                d = row[2]
            c.execute('INSERT INTO AcoesCompleta VALUES(?,?,?)', (n, v, d))
            conn.commit()


if __name__ == '__main__':
    janela = Tk()
    janela.geometry()
    acoes = carteiraCompleta(janela)
    janela.mainloop()
