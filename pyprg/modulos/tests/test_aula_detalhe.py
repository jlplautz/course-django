import pytest
from django.urls import reverse
from model_mommy import mommy
from pyprg.django_assertions import assert_contains
from pyprg.modulos.models import Modulo, Aula


# para fazer este caso temos que criar uma fixture que vai criar efetivamente os modulos
# criar a fixture
# definir seu nome para modulos
# mencionar que usa o db
# usar o modulo mommy.make(Modulo, 2)

@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def aula(modulo):
    return mommy.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_titulo(resp, aula: Aula):
    assert_contains(resp, aula.titulo)
