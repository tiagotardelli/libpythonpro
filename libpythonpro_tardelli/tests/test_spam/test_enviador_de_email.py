import pytest

from libpythonpro_tardelli.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['tiagob.tardelli@gmail.com', 'tiago.tardelli@greenconcept.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
            destinatario,
            'contato@tiagotardelli.com.br',
            'Cursos Python Pro',
            'Turma Henrique Bastos quase terminando'
        )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['', 'tiago.tardelli']
)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
                destinatario,
                'contato@tiagotardelli.com.br',
                'Cursos Python Pro',
                'Turma Henrique Bastos quase terminando'
            )
