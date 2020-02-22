import pytest
from django.urls import reverse
from model_mommy import mommy
from pyprg.django_assertions import assert_contains
from pyprg.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return mommy.make(Modulo, 2)


@pytest.fixture
def resp(client, modulos):
    resp = client.get(reverse('base:home'))
    return resp

# para fazer este caso temos que criar uma fixture que vai criar efetivamente os modulos
# criar a fixture
# definir seu nome para modulos
# mencionar que usa o db
# usar o modulo mommy.make(Modulo, 2)


def test_titulos_dos_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)
