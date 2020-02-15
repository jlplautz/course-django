import pytest
from django.urls import reverse
from pyprg.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    """quando accessamos nosso site fazemos uma chamada do tipo get
    logo na raiz da aplicação. Justamente a view que construimos

    Emulando um request o protocolo http vai retornar um response.
    Aqui queremos nos certificar que esta resposta retornou com sucesso
    """
    assert resp.status_code == 200


def test_titulo(resp):
    assert_contains(resp, '<title>Python Pro - Home</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Python Pro</a>')


def test_email_link(resp):
    assert_contains(resp, 'href="mailto:jorge.plautz@gmail.com"')
