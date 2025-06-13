''' criar um sistema de controle de estoque para uma loja de eletrônicos

Criação da base do sistema:
a) Implemente um menu de opções para o usuário, permitindo que ele selecione
diferentes funcionalidades do sistema.
b) Inclua as opções de adicionar produto, atualizar produto, excluir produto, visualizar
estoque e sair do sistema.

Adicionar produto:
a) Ao selecionar a opção de adicionar produto, o sistema deve solicitar as seguintes
informações:
- Nome do produto
- Preço do produto
- Quantidade em estoque

Atualizar produto:
a) Ao selecionar a opção de atualizar produto, o sistema deve pedir o nome do produto
para atualizar e solicitar as seguintes informações para atualizar
- Preço do produto
- Quantidade em estoque

Excluir produto:
a) Ao selecionar a opção de excluir produto, o sistema deve pedir o nome para excluir o
produto

Visualizar estoque:
a) Ao selecionar a opção de visualizar estoque, o sistema deverá mostrar a lista de
produtos, com as seguinte informações:
- Nome do produto
- Preço do produto
- Quantidade em estoque
'''
import tkinter as tk
from tkinter import messagebox

class Loja:

    def __init__(self):
        self.produtos = []

    def adicionar_produto(self):
        janela = tk.Toplevel()
        janela.title("Adicionar Produto")
        janela.geometry("300x200")
        janela.resizable(False, False)

        tk.Label(janela, text="Nome do produto:").pack()
        nome_entry = tk.Entry(janela)
        nome_entry.pack()

        tk.Label(janela, text="Preço do produto:").pack()
        preco_entry = tk.Entry(janela)
        preco_entry.pack()

        tk.Label(janela, text="Quantidade em estoque:").pack()
        quantidade_entry = tk.Entry(janela)
        quantidade_entry.pack()

        def confirmar():
            nome = nome_entry.get()
            preco_txt = preco_entry.get().replace(",", ".")
            qtd_txt = quantidade_entry.get()

            if not nome or not any(char.isalpha() for char in nome):
                messagebox.showerror("Erro", "Nome inválido!")
                return
            try:
                preco = float(preco_txt)
                if preco <= 0:
                    raise ValueError
            except:
                messagebox.showerror("Erro", "Preço inválido!")
                return
            try:
                quantidade = int(qtd_txt)
                if quantidade < 1 or quantidade > 999:
                    raise ValueError
            except:
                messagebox.showerror("Erro", "Quantidade inválida!")
                return

            self.produtos.append({'nome': nome, 'preco': preco, 'quantidade': quantidade})
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
            janela.destroy()

        tk.Button(janela, text="Confirmar", command=confirmar).pack(pady=10)

    def atualizar_produto(self):
        if not self.produtos:
            messagebox.showinfo("Info", "Estoque vazio!")
            return

        janela = tk.Toplevel()
        janela.title("Atualizar Produto")
        janela.geometry("300x200")
        janela.resizable(False, False)

        tk.Label(janela, text="Nome do produto a atualizar:").pack()
        nome_entry = tk.Entry(janela)
        nome_entry.pack()

        tk.Label(janela, text="Novo preço:").pack()
        preco_entry = tk.Entry(janela)
        preco_entry.pack()

        tk.Label(janela, text="Nova quantidade:").pack()
        quantidade_entry = tk.Entry(janela)
        quantidade_entry.pack()

        def confirmar():
            nome = nome_entry.get()
            preco_txt = preco_entry.get().replace(",", ".")
            qtd_txt = quantidade_entry.get()

            for p in self.produtos:
                if p['nome'].lower() == nome.lower():
                    try:
                        preco = float(preco_txt)
                        if preco <= 0:
                            raise ValueError
                    except:
                        messagebox.showerror("Erro", "Preço inválido!")
                        return
                    try:
                        quantidade = int(qtd_txt)
                        if quantidade < 1 or quantidade > 999:
                            raise ValueError
                    except:
                        messagebox.showerror("Erro", "Quantidade inválida!")
                        return

                    p['preco'] = preco
                    p['quantidade'] = quantidade
                    messagebox.showinfo("Sucesso", "Produto atualizado!")
                    janela.destroy()
                    return

            messagebox.showerror("Erro", "Produto não encontrado!")

        tk.Button(janela, text="Confirmar", command=confirmar).pack(pady=10)

    def excluir_produto(self):
        if not self.produtos:
            messagebox.showinfo("Info", "Estoque vazio!")
            return

        janela = tk.Toplevel()
        janela.title("Excluir Produto")
        janela.geometry("300x150")
        janela.resizable(False, False)

        tk.Label(janela, text="Nome do produto a excluir:").pack(pady=10)
        nome_entry = tk.Entry(janela)
        nome_entry.pack()

        def confirmar():
            nome = nome_entry.get()
            for p in self.produtos:
                if p['nome'].lower() == nome.lower():
                    self.produtos.remove(p)
                    messagebox.showinfo("Sucesso", "Produto excluído!")
                    janela.destroy()
                    return
            messagebox.showerror("Erro", "Produto não encontrado!")

        tk.Button(janela, text="Excluir", command=confirmar).pack(pady=10)

    def visualizar_estoque(self):
        janela = tk.Toplevel()
        janela.title("Estoque")
        janela.geometry("400x300")
        janela.resizable(True, True)

        texto = tk.Text(janela, wrap="word")
        texto.pack(expand=True, fill="both")

        if not self.produtos:
            texto.insert("1.0", "Estoque vazio!")
        else:
            for i, produto in enumerate(self.produtos, 1):
                texto.insert("end", f"Produto {i}:\n")
                texto.insert("end", f"  Nome: {produto['nome']}\n")
                texto.insert("end", f"  Preço: {produto['preco']:.2f}\n")
                texto.insert("end", f"  Quantidade: {produto['quantidade']}\n\n")

        texto.config(state="disabled")

def main():
    loja = Loja()
    root = tk.Tk()
    root.title("Loja de Produtos Eletrônicos")
    root.geometry("400x300")
    root.resizable(False, False)

    tk.Label(root, text="Selecione uma opção:").pack(pady=10)

    tk.Button(root, text="Adicionar Produto", command=loja.adicionar_produto).pack(pady=5)
    tk.Button(root, text="Atualizar Produto", command=loja.atualizar_produto).pack(pady=5)
    tk.Button(root, text="Excluir Produto", command=loja.excluir_produto).pack(pady=5)
    tk.Button(root, text="Visualizar Estoque", command=loja.visualizar_estoque).pack(pady=5)
    tk.Button(root, text="Sair", command=root.destroy).pack(pady=10)

    root.mainloop()
main()