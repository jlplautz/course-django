from django.test import Client
from pyprg.django_assertions import assert_contains


def test_status_code(client: Client):
    """quando accessamos nosso site fazemos uma chamada do tipo get
    logo na raiz da aplicação. Justamente a view que construimos

    Emulando um request o protocolo http vai retornar um response.
    Aqui queremos nos certificar que esta resposta retornou com sucesso
    """
    resp = client.get('/')
    assert resp.status_code == 200


def test_titulo(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<title>Python Pro</title>')
