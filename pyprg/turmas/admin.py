from django.contrib import admin

# Register your models here.
from pyprg.turmas.models import Turma


class MatriculaInline(admin.TabularInline):
    # para acessae a tabela intermdiaria atraves tdo parametro through
    model = Turma.alunos.through
    extra = 1
    readonly_fields = ('data',)
    autocomplete_fields = ('usuario',)
    ordering = ('-data',)


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    # indicar para admin quem é lista de inlines que será mostrada
    inlines = [MatriculaInline]
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = {'slug': ('nome',)}
    # ordernar de forma descrecente
    ordering = ('-inicio',)
