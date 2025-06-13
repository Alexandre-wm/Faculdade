"""
Objetivos do programa
Adicionar vários alunos, depois pegar os nomes.
Registrar notas de cada aluno, sem um número fixo de notas.
Calcular a média de cada aluno.
Determinar a situação (Aprovado, Recuperação ou Reprovado).
Permitir buscar alunos pelo nome.
"""
# precisa de instalar essa biblioteca
# pip install unidecode
from unidecode import unidecode

class Alunos:
    def __init__(self):
        self.alunos = {
            'nomes': [], 
            'notas': [], 
            'media': [], 
            'situação': [] 
        }

    # Função para pegar a nota do aluno 
    def obter_numero(self, msg, minimo=0, maximo=10, apenas_inteiro=False):
        while True:
            try:
                valor = float(input(msg).replace(',', '.'))  # Permite entrada com vírgula

                if apenas_inteiro and not valor.is_integer():
                    print("Por favor, digite um número inteiro válido.\n")
                    continue
                if minimo <= valor <= maximo:
                    return int(valor) if apenas_inteiro else valor  # Mantém float para notas
                else:
                    print(f"O valor deve estar entre {minimo} e {maximo}.\n")

            except ValueError:
                print("\nEntrada inválida! Digite um número válido.\n")

    # Função para pegar o nome do aluno
    def obter_nome(self, msg):
        while True:
            nome = input(msg).strip()

            if nome and any(char.isalpha() for char in nome):  # Deve conter ao menos uma letra
                return nome

            print("\nO nome não pode estar vazio ou conter apenas números!\n")

    # Função para adicionar alunos
    def adicionar_alunos(self):

        # Pegar a quantidade de alunos e notas
        qtd_alunos = self.obter_numero('\nDigite a quantidade de alunos: ', 1, float('inf'), True)
        qtd_notas = self.obter_numero('\nDigite a quantidade de notas de cada aluno: ', 1, float('inf'), True)

        # Adicionar alunos
        for i in range(qtd_alunos):
            nome = self.obter_nome(f'\nDigite o nome do {i+1}° aluno: ')

            # Normaliza o nome para comparação (sem acento)
            nome_normalizado = unidecode(nome).lower()

            # Verificar se o aluno já foi adicionado
            if nome_normalizado in [unidecode(nome).lower() for nome in self.alunos['nomes']]:
                print("Esse aluno já foi adicionado!\n")
                continue  # Pula para o próximo aluno

            # Adicionar notas
            notas = [self.obter_numero(f'Digite a {n+1}° nota do {i+1}° aluno: ', 0, 10) for n in range(qtd_notas)]
            
            # Fazer a média
            media = round(sum(notas) / len(notas), 2)
            
            # Determinar situação
            situacao = "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"

            # Adicionar tudo no dicionário inicial
            self.alunos['nomes'].append(nome)  # Guarda os nomes exatamente como foram digitados
            self.alunos['notas'].append(notas)
            self.alunos['media'].append(media)
            self.alunos['situação'].append(situacao)

        print("Alunos cadastrados com sucesso!\n")

    # Função para buscar alunos
    def buscar_aluno(self):
        nome_busca = input('Digite o nome do aluno para buscar: ').strip().lower()

        # Normaliza a busca removendo acentos
        nome_busca_normalizado = unidecode(nome_busca)

        print()  

        # Normaliza todos os nomes ao buscar
        if nome_busca_normalizado in [unidecode(nome).lower() for nome in self.alunos['nomes']]:  
            indice = [unidecode(nome).lower() for nome in self.alunos['nomes']].index(nome_busca_normalizado)
            print("\nAluno Encontrado:")
            print(f"Nome: {self.alunos['nomes'][indice]}")  # Exibe o nome com acentos
            print(f"Notas: {self.alunos['notas'][indice]}")
            print(f"Média: {self.alunos['media'][indice]}")
            print(f"Situação: {self.alunos['situação'][indice]}")
        else:
            print("Aluno não encontrado.\n")


# Inicializando o programa
turma = Alunos()

while True:
    print("\nMenu:"
          "\n1 - Adicionar alunos"
          "\n2 - Buscar aluno"
          "\n3 - Sair")
    opcao = input("\nDigite a opção desejada: ")

    if opcao == '1':
        turma.adicionar_alunos()
    elif opcao == '2':
        turma.buscar_aluno()
    elif opcao == '3':
        break
    else:
        print("Opção inválida! Tente novamente.\n")

print("Programa encerrado.\n")