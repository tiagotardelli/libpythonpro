import pytest

from libpythonpro_tardelli.spam.modelos import Usuario
from libpythonpro_tardelli.spam.db import Conexao


@pytest.fixture(scope='session')
def conexao():
    # Setup
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_salvar_usuario(conexao, sessao):
    usuario = Usuario(nome='Tiago')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(conexao, sessao):
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome='Tiago'), Usuario(nome='Marcos')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
