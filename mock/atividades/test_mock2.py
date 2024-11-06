import requests

#função que chama a API (exemplo)
def obter_dados_api(url):
    response = requests.get(url)
    return response.json()

#teste sem chamar a API
def test_obter_dados_api(mocker):
    #mockando a resposta da função request.get
    mock_response = mocker.patch('requests.get')

    #define um retorno ficticio para o mock
    mock_response.return_value.json.return_value = { "id": 1, "nome": "teste"}

    #testando a função como mock
    result = obter_dados_api("http://api.exemplo.com/dados")

    #verificar se o resultado e o esperado
    assert result == { "id": 1, "nome": "teste"}