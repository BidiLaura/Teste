import pytest
import requests 
from unittest.mock import MagicMock

class BancoDeDados:
    def buscar_usuario(self, user_ID):
        raise NotImplementedError
    
def obter_dados_adicionais(user_ID):
    response = requests.get(f"http://api.exemplo.com/dados/{user_ID}")
    return response.json()

def sistema_principal(user_ID, banco):
    usuario = banco.buscar_usuario(user_ID)
    dados_adicionais = obter_dados_adicionais(user_ID)
    usuario.update(dados_adicionais)
    return usuario

@pytest.fixture

def banco_mock(mocker):
    banco = BancoDeDados()
    mocker.patch.object(banco, 'buscar_usuario', return_value={'id': 1, 'nome':'Maria'})
    return banco

def test_sistema_principal(mocker, banco_mock):
    #mockando a chamada a api
    mock_response = mocker.patch('requests.get')
    mock_response.return_value.json.return_value = {'localização': 'brasil'}

    #testando o sistema
    result = sistema_principal(1, banco_mock)

    #verificando o resultado final
    assert result == {'id': 1, 'nome': 'Maria', 'localização': 'brasil'}