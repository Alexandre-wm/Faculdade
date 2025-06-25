""" 
Portifólio - Computational Logic Using Python - Gestão de Eventos

Você foi contratado para desenvolver um sistema de gerenciamento de eventos para a
UniFECAF. Esse sistema será utilizado por alunos e coordenadores para organizar e
controlar eventos como workshops, palestras, e até a "Tech Week". O sistema deverá
permitir que novos eventos sejam cadastrados, os detalhes do evento sejam atualizados e
que os usuários possam se inscrever nos eventos. Além disso, o sistema deve exibir a lista
de eventos disponíveis e os participantes registrados.

REQUISITOS
1. Cadastro de Eventos: O sistema deve permitir que o organizador crie novos
eventos, incluindo o nome do evento, a data, a descrição e o número máximo de participantes.

2. Atualização de Eventos: Deve ser possível atualizar informações sobre eventos já
cadastrados, como alterar a data ou o número de vagas disponíveis.

3. Visualização de Eventos Disponíveis: Os usuários poderão visualizar os eventos
disponíveis com as informações detalhadas (nome, data, descrição e vagas
restantes).

4. Inscrição em Eventos: Os alunos podem se inscrever nos eventos que estão
disponíveis e dentro do limite de vagas.

5. Visualizar Inscrições: O organizador poderá visualizar a lista de inscritos para cada
evento.

6. Exclusão de Eventos: Deve ser possível remover eventos que foram cancelados.

Exemplo de Fluxo:
● O coordenador adiciona um evento chamado “Workshop de Programação em
Python” com data e número de vagas.
● Um aluno visualiza os eventos disponíveis e se inscreve no workshop.
● O coordenador verifica a lista de inscritos para o evento.
● Caso haja uma mudança de data, o coordenador pode atualizar a informação do
evento.
● Se o evento for cancelado, o coordenador poderá excluí-lo do sistema.
Funcionalidades Específicas:
● Utilize estruturas condicionais para garantir que o número de vagas não seja
excedido.
● Utilize loops para exibir a lista de eventos e participantes.
● Estruture as informações usando listas e dicionários para armazenar dados dos
eventos e inscrições.
Este portfólio permitirá que você aplique os conhecimentos de lógica computacional,
controle de fluxo e estrutura de dados, além de exercitar sua habilidade de comunicação e
apresentação com um vídeo de mais de 5 minutos explicando o desenvolvimento do projeto e suas funcionalidades.
Boa sorte no desenvolvimento e lembre-se de aplicar as boas práticas aprendidas!
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class SistemaEventos:
    def __init__(self):
        self.eventos = []

    # Normaliza o nome removendo espaços e deixando minúsculo
    def normalizar_nome(self, nome):
        return nome.strip().replace(" ", "").lower()

    # Trata datas no formato 01012025 para 01/01/2025
    def tratar_data(self, data_str):

        if len(data_str) == 8 and data_str.isdigit():
            return f"{data_str[:2]}/{data_str[2:4]}/{data_str[4:]}"
        
        return data_str

    # Validação de data
    def validar_data(self, data_str):
        data_str = self.tratar_data(data_str)

        # Verifica se a data está no formato correto conforme o padrão DD/MM/AAAA do datetime
        try:
            data = datetime.strptime(data_str, "%d/%m/%Y")
            if data < datetime.now():
                messagebox.showerror("Erro", "A data não pode estar no passado.")
                return None
            
            if data.year < 2025 or data.year > 2100:
                messagebox.showerror("Erro", "Ano deve estar entre 2025 e 2100.")
                return None
            
            return data
        
        except ValueError:
            messagebox.showerror("Erro", "Data inválida! Use o formato Dia/Mês/Ano.")
            return None

    # Criar Evento
    def criar_evento(self, coordenador, nome_evento, data, descricao, vagas_max):
        if not (coordenador and nome_evento and data and descricao):
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios.")
            return

        data_valida = self.validar_data(data)
        if not data_valida:
            return

        if not vagas_max.isdigit() or int(vagas_max) <= 0:
            messagebox.showwarning("Atenção", "Número de vagas deve ser um inteiro positivo.")
            return

        # Verifica se o evento já existe
        nome_evento_normalizado = self.normalizar_nome(nome_evento)
        for evento in self.eventos:
            if self.normalizar_nome(evento['nome_evento']) == nome_evento_normalizado:
                messagebox.showerror("Erro", f"O evento '{nome_evento}' já existe.")
                return

        # Adiciona o evento à lista
        self.eventos.append({
            'coordenador': coordenador.strip().title(),
            'nome_evento': nome_evento.strip().title(),
            'data': data_valida,
            'descricao': descricao.strip(),
            'vagas_max': int(vagas_max),
            'inscritos': []
        })
        messagebox.showinfo("Sucesso", f"Evento '{nome_evento.strip().title()}' criado com sucesso!")

    # Visualizar Eventos (ordenado por vagas restantes)
    def visualizar_eventos(self):
        if not self.eventos:
            messagebox.showinfo("Eventos", "Nenhum evento cadastrado.")
            return

        # Ordenar os eventos por quantidade de inscritos (do menor para maior)
        eventos_ordenados = sorted(
            self.eventos, key=lambda e: len(e['inscritos'])
        )

        eventos_info = ""
        for evento in eventos_ordenados:
            inscritos = len(evento['inscritos'])
            data_formatada = evento['data'].strftime("%d/%m/%Y")
            eventos_info += (
                f"Evento: {evento['nome_evento'].upper()}\n"
                f"Data do Evento: {data_formatada}\n"
                f"Descrição: {evento['descricao']}\n"
                f"Inscritos: {inscritos}/{evento['vagas_max']}\n"
                f"Coordenador: {evento['coordenador']}\n"
                "--------------------------------------\n"
            )
        messagebox.showinfo("Eventos Disponíveis", eventos_info)

    # Inscrever aluno no Evento
    def inscrever_evento(self, nome_evento, aluno):
        nome_evento_normalizado = self.normalizar_nome(nome_evento)

        for evento in self.eventos:
            # Verifica se o evento existe e se o nome normalizado bate com o nome do evento
            if self.normalizar_nome(evento['nome_evento']) == nome_evento_normalizado:
                aluno_formatado = aluno.strip().title()

                if aluno_formatado in evento['inscritos']:
                    messagebox.showwarning("Atenção", f"{aluno_formatado} já está inscrito.")
                    return

                if len(evento['inscritos']) >= evento['vagas_max']:
                    messagebox.showerror("Erro", "Não há vagas disponíveis.")
                    return

                evento['inscritos'].append(aluno_formatado)
                messagebox.showinfo("Sucesso", f"{aluno_formatado} inscrito no evento '{evento['nome_evento']}'.")
                return
            
        messagebox.showerror("Erro", "Evento não encontrado.")

    # Visualizar Inscritos
    def visualizar_inscritos(self, nome_evento):
        nome_evento_normalizado = self.normalizar_nome(nome_evento)

        # Verifica se o evento existe e busca os inscritos
        for evento in self.eventos:
            if self.normalizar_nome(evento['nome_evento']) == nome_evento_normalizado:

                # Se o evento tiver inscritos, formata a lista trazendo os nomes
                if evento['inscritos']:
                    inscritos = "\n".join([f"{aluno}" for aluno in evento['inscritos']])
                else:
                    inscritos = "Nenhum inscrito ainda."

                # Formata a data do evento
                data_formatada = evento['data'].strftime("%d/%m/%Y") # Formata a data para Dia/Mês/Ano
                info = (
                    f"Evento: {evento['nome_evento']}\n"
                    f"Data do Evento: {data_formatada}\n"
                    f"Descrição: {evento['descricao']}\n"
                    f"\nLista de Inscritos:\n{inscritos}"
                )
                messagebox.showinfo(f"Inscritos em {evento['nome_evento']}", info)
                return
            
        messagebox.showerror("Erro", "Evento não encontrado.")

    # Atualizar Evento
    def atualizar_evento(self, nome_evento, nova_data, novas_vagas):
        nome_evento_normalizado = self.normalizar_nome(nome_evento)

        # Verifica se o evento existe
        for evento in self.eventos:
            if self.normalizar_nome(evento['nome_evento']) == nome_evento_normalizado:
                data_valida = self.validar_data(nova_data)

                # faz o tratamento da nova data
                if not data_valida:
                    messagebox.showerror("Erro", "Data inválida.")
                    return

                # faz o tratamento de novas vagas
                if not novas_vagas.isdigit() or int(novas_vagas) <= 0:
                    messagebox.showwarning("Atenção", "Número de vagas deve ser um inteiro positivo.")
                    return

                evento['data'] = data_valida
                evento['vagas_max'] = int(novas_vagas)
                messagebox.showinfo("Sucesso", f"Evento '{evento['nome_evento']}' atualizado com sucesso.")
                return
            
        messagebox.showerror("Erro", "Evento não encontrado.")

    # Excluir Evento
    def excluir_evento(self, nome_evento):
        nome_evento_normalizado = self.normalizar_nome(nome_evento)

        for evento in self.eventos:
            if self.normalizar_nome(evento['nome_evento']) == nome_evento_normalizado:
                self.eventos.remove(evento)
                messagebox.showinfo("Sucesso", f"Evento '{evento['nome_evento']}' excluído.")
                return
            
        messagebox.showerror("Erro", "Evento não encontrado.")

# ========================================
# =========== Interface Gráfica ==========
# ========================================

sistema = SistemaEventos()

root = tk.Tk()
root.title("Sistema de Gerenciamento de Eventos")
root.geometry("400x500")

# OBSERVAÇÃO:
# Para evitar conflitos de nomes, vamos usar o prefixo "entry_" para as entradas no tkinter.
# Isso é uma boa prática em programação, especialmente quando se trabalha com interfaces gráficas.
# Assim como btn para botões, lbl para rótulos (label), etc.

# ==== Janelas personalizadas ====
def janela_criar_evento():
    janela = tk.Toplevel(root)
    janela.title("Criar Evento")
    janela.geometry("400x400")

    tk.Label(janela, text="Coordenador:").pack(pady=5)
    entry_coordenador = tk.Entry(janela, width=40)
    entry_coordenador.pack()

    tk.Label(janela, text="Nome do Evento:").pack(pady=5)
    entry_nome = tk.Entry(janela, width=40)
    entry_nome.pack()

    tk.Label(janela, text="Data (DD/MM/AAAA):").pack(pady=5)
    entry_data = tk.Entry(janela, width=40)
    entry_data.pack()

    tk.Label(janela, text="Descrição:").pack(pady=5)
    entry_descricao = tk.Entry(janela, width=40)
    entry_descricao.pack()

    tk.Label(janela, text="Número de Vagas:").pack(pady=5)
    entry_vagas = tk.Entry(janela, width=40)
    entry_vagas.pack()

    def janela_criar_evento():
        sistema.criar_evento(
            entry_coordenador.get(),
            entry_nome.get(),
            entry_data.get(),
            entry_descricao.get(),
            entry_vagas.get()
        )
        janela.destroy()

    tk.Button(janela, text="Salvar Evento", command=janela_criar_evento, bg="lightgreen").pack(pady=20)


def janela_inscrever_evento():
    janela = tk.Toplevel(root)
    janela.title("Inscrever em Evento")
    janela.geometry("400x250")

    tk.Label(janela, text="Nome do Evento:").pack(pady=5)
    entry_evento = tk.Entry(janela, width=40)
    entry_evento.pack()

    tk.Label(janela, text="Nome do Aluno:").pack(pady=5)
    entry_aluno = tk.Entry(janela, width=40)
    entry_aluno.pack()

    def inscrever():
        sistema.inscrever_evento(entry_evento.get(), entry_aluno.get())
        janela.destroy()

    tk.Button(janela, text="Inscrever", command=inscrever, bg="lightblue").pack(pady=20)


def janela_visualizar_inscritos():
    janela = tk.Toplevel(root)
    janela.title("Visualizar Inscritos")
    janela.geometry("400x200")

    tk.Label(janela, text="Nome do Evento:").pack(pady=5)
    entry_evento = tk.Entry(janela, width=40)
    entry_evento.pack()

    def visualizar():
        sistema.visualizar_inscritos(entry_evento.get())
        janela.destroy()

    tk.Button(janela, text="Ver Inscritos", command=visualizar, bg="lightyellow").pack(pady=20)


def janela_atualizar_evento():
    janela = tk.Toplevel(root)
    janela.title("Atualizar Evento")
    janela.geometry("400x300")

    tk.Label(janela, text="Nome do Evento:").pack(pady=5)
    entry_nome = tk.Entry(janela, width=40)
    entry_nome.pack()

    tk.Label(janela, text="Nova Data (DD/MM/AAAA):").pack(pady=5)
    entry_data = tk.Entry(janela, width=40)
    entry_data.pack()

    tk.Label(janela, text="Novo número de vagas:").pack(pady=5)
    entry_vagas = tk.Entry(janela, width=40)
    entry_vagas.pack()

    def atualizar():
        sistema.atualizar_evento(entry_nome.get(), entry_data.get(), entry_vagas.get())
        janela.destroy()

    tk.Button(janela, text="Atualizar", command=atualizar, bg="lightblue").pack(pady=20)


def janela_excluir_evento():
    janela = tk.Toplevel(root)
    janela.title("Excluir Evento")
    janela.geometry("400x200")

    tk.Label(janela, text="Nome do Evento:").pack(pady=5)
    entry_nome = tk.Entry(janela, width=40)
    entry_nome.pack()

    def excluir():
        sistema.excluir_evento(entry_nome.get())
        janela.destroy()

    tk.Button(janela, text="Excluir", command=excluir, bg="salmon").pack(pady=20)


def visualizar_eventos():
    sistema.visualizar_eventos()


# ==== Layout principal ====
tk.Label(root, text="Sistema de Eventos", font=("Arial", 16, "bold")).pack(pady=10)

tk.Button(root, text="Criar Evento", command=janela_criar_evento, width=30, height=2, bg="lightgreen").pack(pady=5)
tk.Button(root, text="Visualizar Eventos", command=visualizar_eventos, width=30, height=2).pack(pady=5)
tk.Button(root, text="Inscrever em Evento", command=janela_inscrever_evento, width=30, height=2).pack(pady=5)
tk.Button(root, text="Ver Inscritos", command=janela_visualizar_inscritos, width=30, height=2).pack(pady=5)
tk.Button(root, text="Atualizar Evento", command=janela_atualizar_evento, width=30, height=2, bg="lightblue").pack(pady=5)
tk.Button(root, text="Excluir Evento", command=janela_excluir_evento, width=30, height=2, bg="salmon").pack(pady=5)
tk.Button(root, text="Sair", command=root.destroy, width=30, height=2, bg="gray").pack(pady=20)

root.mainloop()
