from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pessoas/', PessoasView.as_view(), name='pessoas'),
    path('ocupacoes/', OcupacoesView.as_view(), name='ocupacoes'),
    path('cidades/', CidadesView.as_view(), name='cidades'),
    path('matriculas/', MatriculasView.as_view(), name='matriculas'),  # Corrigido aqui!
    path('turmas/', TurmasView.as_view(), name='turmas'),
    path('turnos/', TurnosView.as_view(), name='turnos'),
    path('cursos/', CursosView.as_view(), name='cursos'),
    path('livros/', LivrosView.as_view(), name='livros'),
    path('kitlivros/', KitLivrosView.as_view(), name='kitlivros'),
    path('kitlivroitens/', KitLivroItensView.as_view(), name='kitlivroitens'),
    path('editoras/', EditorasView.as_view(), name='editoras'),
    path('autores/', AutoresView.as_view(), name='autores'),
    path('emprestimos/', EmprestimosView.as_view(), name='emprestimos'),
    path('devolucoes/', DevolucoesView.as_view(), name='devolucoes'),
    path('atrasos/', AtrasosView.as_view(), name='atrasos'),
    path('relatorios/', RelatoriosView.as_view(), name='relatorios'),
]
