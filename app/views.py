from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import (
    Pessoa, Ocupacao, Cidade, Matricula, Turma, Turno, Curso,
    Livro, KitLivro, KitLivroItem, Editora, Autor,
    Emprestimo, Devolucao, Atraso, Relatorio
)

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


# RF01 – Pessoas
class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.select_related('cidade', 'ocupacao').all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})


# RF02 – Ocupações
class OcupacoesView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})


# RF03 – Cidades
class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})


# RF04 – Matrículas
class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.select_related('pessoa', 'curso').all()
        return render(request, 'matricula.html', {'matriculas': matriculas})


# RF05 – Turmas
class TurmasView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas': turmas})


# RF06 – Turnos
class TurnosView(View):
    def get(self, request, *args, **kwargs):
        turnos = Turno.objects.all()
        return render(request, 'turno.html', {'turnos': turnos})


# RF07 – Cursos
class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.select_related('turno').all()
        return render(request, 'curso.html', {'cursos': cursos})


# RF08 – Livros
class LivrosView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.select_related('autor', 'editora').all()
        return render(request, 'livro.html', {'livros': livros})


# RF09 – Kits de Livro
class KitLivrosView(View):
    def get(self, request, *args, **kwargs):
        kits = KitLivro.objects.select_related('turma').all()
        return render(request, 'kit_livro.html', {'kits': kits})


# RF10 – Itens do Kit de Livro
class KitLivroItensView(View):
    def get(self, request, *args, **kwargs):
        itens = KitLivroItem.objects.select_related('kit_livro', 'livro').all()
        return render(request, 'kit_livro_item.html', {'itens': itens})


# RF11 – Editoras
class EditorasView(View):
    def get(self, request, *args, **kwargs):
        editoras = Editora.objects.select_related('cidade').all()
        return render(request, 'editora.html', {'editoras': editoras})


# RF12 – Autores
class AutoresView(View):
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.select_related('cidade').all()
        return render(request, 'autor.html', {'autores': autores})


# RF13 – Empréstimos
class EmprestimosView(View):
    def get(self, request, *args, **kwargs):
        emprestimos = Emprestimo.objects.select_related('pessoa', 'livro', 'kit_livro_item').all()
        return render(request, 'emprestimo.html', {'emprestimos': emprestimos})


# RF14 – Devoluções
class DevolucoesView(View):
    def get(self, request, *args, **kwargs):
        devolucoes = Devolucao.objects.select_related('emprestimo').all()
        return render(request, 'devolucao.html', {'devolucoes': devolucoes})


# RF15 – Atrasos
class AtrasosView(View):
    def get(self, request, *args, **kwargs):
        atrasos = Atraso.objects.select_related('pessoa', 'livro', 'kit_livro_item').all()
        return render(request, 'atraso.html', {'atrasos': atrasos})


# RF16 – Relatórios
class RelatoriosView(View):
    def get(self, request, *args, **kwargs):
        relatorios = Relatorio.objects.select_related(
            'pessoa', 'livro', 'kit_livro_item', 'emprestimo', 'devolucao', 'atraso'
        ).all()
        return render(request, 'relatorio.html', {'relatorios': relatorios})
