import pytest

from libpythonpro_tardelli.spam.enviador_de_email import Enviador
from libpythonpro_tardelli.spam.main import EnviadorDeSpam
from libpythonpro_tardelli.spam.modelos import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Tiago', email='contato@tiagotardelli.com.br'),
            Usuario(nome='Marcos', email='contato@tiagotardelli.com.br')
        ],
        [
            Usuario(nome='Tiago', email='contato@tiagotardelli.com.br')
        ]
    ]
)
def test_qtde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'contato@tiagotardelli.com.br',
        'Cursos Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Tiago', email='contato@tiagotardelli.com.br')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'tiagob.tardelli@gmail.com.br',
        'Cursos Python Pro',
        'Confira os módulos fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'tiagob.tardelli@gmail.com.br',
        'contato@tiagotardelli.com.br',
        'Cursos Python Pro',
        'Confira os módulos fantásticos'
    )
