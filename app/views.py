from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class PessoasView(View):  # RF01
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})

class OcupacoesView(View):  # RF02
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})

class CidadesView(View):  # RF03
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class MatriculasView(View):  # RF04
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matricula.html', {'matriculas': matriculas})

class TurmasView(View):  # RF05
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas': turmas})

class TurnosView(View):  # RF06
    def get(self, request, *args, **kwargs):
        turnos = Turno.objects.all()
        return render(request, 'turno.html', {'turnos': turnos})

class CursosView(View):  # RF07
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos': cursos})

class LivrosView(View):  # RF08
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'livro.html', {'livros': livros})

class KitLivrosView(View):  # RF09
    def get(self, request, *args, **kwargs):
        kits = KitLivro.objects.all()
        return render(request, 'kit_livro.html', {'kits': kits})

class KitLivroItensView(View):  # RF10
    def get(self, request, *args, **kwargs):
        itens = KitLivroItem.objects.all()
        return render(request, 'kit_livro_item.html', {'itens': itens})

class EditorasView(View):  # RF11
    def get(self, request, *args, **kwargs):
        editoras = Editora.objects.all()
        return render(request, 'editora.html', {'editoras': editoras})

class AutoresView(View):  # RF12
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.all()
        return render(request, 'autor.html', {'autores': autores})

class EmprestimosView(View):  # RF13
    def get(self, request, *args, **kwargs):
        emprestimos = Emprestimo.objects.all()
        return render(request, 'emprestimo.html', {'emprestimos': emprestimos})

class DevolucoesView(View):  # RF14
    def get(self, request, *args, **kwargs):
        devolucoes = Devolucao.objects.all()
        return render(request, 'devolucao.html', {'devolucoes': devolucoes})

class AtrasosView(View):  # RF15
    def get(self, request, *args, **kwargs):
        atrasos = Atraso.objects.all()
        return render(request, 'atraso.html', {'atrasos': atrasos})

class RelatoriosView(View):  # RF16
    def get(self, request, *args, **kwargs):
        relatorios = Relatorio.objects.all()
        return render(request, 'relatorio.html', {'relatorios': relatorios})