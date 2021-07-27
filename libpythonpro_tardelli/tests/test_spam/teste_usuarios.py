from libpythonpro_tardelli.spam.modelos import Usuario


def test_salvar_usuario(conexao, sessao):
    usuario = Usuario(nome='Tiago', email='contato@tiagotardelli.com.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(conexao, sessao):
    sessao = conexao.gerar_sessao()
    usuarios = [
        Usuario(nome='Tiago', email='contato@tiagotardelli.com.br'),
        Usuario(nome='Marcos', email='contato@tiagotardelli.com.br')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
