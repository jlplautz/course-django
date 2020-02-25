from typing import List

from pyprg.modulos.models import Modulo, Aula


def listar_modulos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por titulos
    :return:
    """
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    """
    definir o slug será uma string e que vamos retornar como resultado o Modulo
    para retornar o modulo apartir do slug vamos colocar Modulo.objects.
    :param slug:
    :return: o atributo slug to meu modelo ter-a que ser igual ao atributo slug que esta sendo recebido
    """
    return Modulo.objects.get(slug=slug)


def lista_aulas_de_modulo_ordenadas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())


def encontrar_aula(slug):
    return Aula.objects.get(slug=slug)
