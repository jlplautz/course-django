from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=64)
    publico = models.TextField()
    decricao = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        """
        retornar utilizando a função reverse do Django depois cria rum link na api de modulos
        respectiva ao detalhe do modulo.
        Para identificar o modulos vamos passar aqui para o reverse um campo de slug que vai identificar
        unicamente o modulo. Vamos colocar aqui respectivo a esta chave um campo de slug do modulo
        :return:
        """
        return reverse('modulos:detalhe', kwargs={'slug': self.slug})


class Aula(OrderedModel):
    titulo = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    modulo = models.ForeignKey('Modulo', on_delete=models.PROTECT)
    order_with_respect_to = 'modulo'

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos:aula', kwargs={'slug': self.slug})
