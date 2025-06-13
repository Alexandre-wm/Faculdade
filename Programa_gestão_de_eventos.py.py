"""
Você foi contratado para desenvolver um sistema de gerenciamento de eventos para a
UniFECAF. Esse sistema será utilizado por alunos e coordenadores para organizar e
controlar eventos como workshops, palestras, e até a "Tech Week". O sistema deverá
permitir que novos eventos sejam cadastrados, os detalhes do evento sejam atualizados e
que os usuários possam se inscrever nos eventos. Além disso, o sistema deve exibir a lista
de eventos disponíveis e os participantes registrados.

REQUISITOS
1. Cadastro de Eventos: O sistema deve permitir que o organizador crie novos
eventos, incluindo o nome do evento, a data, a descrição e o número máximo de
participantes.

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

class Evento:
    def __init__(self, nome, data, descricao, vagas_max):
        self.nome = nome
        self.data = data
        self.descricao = descricao
        self.vagas_max = vagas_max
        self.inscritos = []

    def atualizar_evento(self, nome=None, data=None, descricao=None, vagas_max=None):
        if nome:
            self.nome = nome
        if data:
            self.data = data
        if descricao:
            self.descricao = descricao
        if vagas_max is not None:
            self.vagas_max = vagas_max

    def inscrever_participante(self, participante):
        if len(self.inscritos) < self.vagas_max:
            self.inscritos.append(participante)
            return True
        return False

    def listar_inscritos(self):
        return self.inscritos

    def excluir_evento(self):
        del self

evento = Evento()
