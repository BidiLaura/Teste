import requests 
from unittest.mock import MagicMock
import pytest

class BancoDeDados:
    def buscar_pedido(self, pedido_id):
        raise NotImplementedError("Consulta real ao banco de dados")
    

def calcular_valor_total(pedido_id):
    resposta = requests.get(f"http://api.loja.com/pedidos/{pedido_id}")
    dados_produtos = resposta.json()
    
    total = sum(item["preco"] * item["quantidade"] for item in dados_produtos)
    return total

def obter_pedido_com_valor_total(pedido_id, banco):
    pedido = banco.buscar_pedido(pedido_id)
    valor_total = calcular_valor_total(pedido_id)
    pedido["valor_total"] = valor_total
    
    return pedido

@pytest.fixture

def banco_mock(mocker):
    banco = BancoDeDados()
    mocker.patch.object(banco, 'buscar_pedido', return_value={"id": 1, "cliente": "Guilherme"})
    return banco

def test_obter_pedido_com_valor_total(mocker, banco_mock):
    mock_response = mocker.patch('requests.get')
    mock_response.return_value.json.return_value = {'cliente': 'Guilherme'}

    result = obter_pedido_com_valor_total(banco_mock)

    assert result == {'id': 1, 'nome': 'Maria', 'localização': 'brasil'}