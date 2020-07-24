from django.contrib import admin
from .models import Tarefa


class TarefaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['nome']}
    search_fields = ['nome', 'slug']
    list_display = ['nome', 'slug', 'data_criacao', 'concluida']


admin.site.register(Tarefa, TarefaAdmin)
