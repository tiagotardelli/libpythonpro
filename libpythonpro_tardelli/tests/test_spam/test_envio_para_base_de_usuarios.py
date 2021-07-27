from unittest.mock import Mock

import pytest

from libpythonpro_tardelli.spam.main import EnviadorDeSpam
from libpythonpro_tardelli.spam.modelos import Usuario


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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'contato@tiagotardelli.com.br',
        'Cursos Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Tiago', email='contato@tiagotardelli.com.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'tiagob.tardelli@gmail.com.br',
        'Cursos Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with == (
        'tiagob.tardelli@gmail.com.br',
        'contato@tiagotardelli.com.br',
        'Cursos Python Pro',
        'Confira os módulos fantásticos'
    )
