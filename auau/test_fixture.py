import pytest

#teste soma obj na lista
@pytest.fixture
def lista_simples():
    return[1,2,3,4,5]

def test_soma(lista_simples):
    assert sum(lista_simples) == 15

#teste tamanho da lista
@pytest.fixture
def lista_simples():
    return[1,2,3,4,5]

def test_tamanho_lista(lista_simples):
    assert len(lista_simples) == 5

#teste lista em dobro
@pytest.fixture

def lista():
    return [1,2,3,4,5]

def test_dobro_lista(lista):
    assert sum(lista*2)==30

#teste CPF valido
@pytest.fixture

def CPF_valido():
    return [1,2,5,8,8,2,6,5,9,3,6]

def test_valid_CPF(CPF_valido):
    assert sum(CPF_valido) == 55