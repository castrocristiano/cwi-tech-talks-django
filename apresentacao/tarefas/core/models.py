from django.db import models


class Tarefa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    data_criacao = models.DateField(
        'Data de criação',
        auto_now_add=True,
        null=False,
        blank=False
    )
    concluida = models.BooleanField('Concluída', default=False)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['concluida', 'nome']
