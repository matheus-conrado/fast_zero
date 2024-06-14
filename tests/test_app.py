from fastapi.testclient import TestClient
from http import HTTPStatus
from fast_zero.app import app


def test_read_root_dev_retornar_ok_e_ola_mundo():
    client = TestClient(app) # Arrange(organização)
    
    response = client.get('/') #Act(ação)
    
    assert response.status_code == HTTPStatus.OK #Assert (afirmando)
    assert response.json() == {'message':'Olá Mundo!'}