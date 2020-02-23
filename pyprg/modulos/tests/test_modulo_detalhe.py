import pytest
from django.urls import reverse
from model_mommy import mommy
from pyprg.django_assertions import assert_contains
from pyprg.modulos.models import Modulo


# para fazer este caso temos que criar uma fixture que vai criar efetivamente os modulos
# criar a fixture
# definir seu nome para modulos
# mencionar que usa o db
# usar o modulo mommy.make(Modulo, 2)

@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def resp(client, modulo):
    resp = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return resp


def test_titulo(resp, modulo: Modulo):
    assert_contains(resp, modulo.titulo)


def test_descricao(resp, modulo: Modulo):
    assert_contains(resp, modulo.decricao)


def test_publico(resp, modulo: Modulo):
    assert_contains(resp, modulo.publico)
