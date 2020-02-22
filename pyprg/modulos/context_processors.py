from pyprg.modulos import facade


def listar_modulos(request):
    # la no template foi definido uma variavel MODULOS
    return {'MODULOS': facade.listar_modulos_ordenados()}
