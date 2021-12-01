from django import urls

from . import views

app_name = 'tarefas'

urlpatterns = [
    urls.re_path(r'^complexidade/$', views.complexidade, name='complexidade'),
    urls.re_path(r'^atividade/$', views.atividade, name='atividade'),
    urls.re_path(r'^plano/$', views.plano, name='plano'),
]
