from django.conf.urls import url
from django.urls import include

from .views import home, tarefas


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^tarefas/', tarefas, name='tarefas')
]