from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Ocupação")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)
    email = models.EmailField()
    data_nasc = models.DateField()
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Turno(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class Matricula(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    num_de_matricula = models.CharField(max_length=20, unique=True)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.num_de_matricula
    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    data_nasc = models.DateField()
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    volume = models.CharField(max_length=10)
    serie = models.CharField(max_length=20)
    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

class KitLivro(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data_criacao = models.DateField()
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Kit de Livros"
        verbose_name_plural = "Kits de Livros"

class KitLivroItem(models.Model):
    kit_livro = models.ForeignKey(KitLivro, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.kit_livro} - {self.livro}"
    class Meta:
        verbose_name = "Item do Kit de Livro"
        verbose_name_plural = "Itens do Kit de Livro"

class Emprestimo(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, null=True, blank=True)
    kit_livro_item = models.ForeignKey(KitLivroItem, on_delete=models.CASCADE)
    data_entrega = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"Empréstimo de {self.pessoa} em {self.data_entrega}"
    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"

class Devolucao(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    data_devolucao = models.DateField()
    condicao = models.CharField(
        max_length=20,
        choices=[("bom", "Bom"), ("danificado", "Danificado"), ("perdido", "Perdido")]
    )
    def __str__(self):
        return f"Devolução de {self.emprestimo}"
    class Meta:
        verbose_name = "Devolução"
        verbose_name_plural = "Devoluções"

class Atraso(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, null=True, blank=True)
    kit_livro_item = models.ForeignKey(KitLivroItem, on_delete=models.CASCADE)
    data_prevista_devolucao = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[("em dia", "Em dia"), ("atrasado", "Atrasado")]
    )
    def __str__(self):
        return f"Atraso de {self.pessoa}"
    class Meta:
        verbose_name = "Atraso"
        verbose_name_plural = "Atrasos"

class Relatorio(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, null=True, blank=True)
    kit_livro_item = models.ForeignKey(KitLivroItem, on_delete=models.CASCADE)
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    devolucao = models.ForeignKey(Devolucao, on_delete=models.CASCADE)
    atraso = models.ForeignKey(Atraso, on_delete=models.CASCADE)
    def __str__(self):
        return f"Relatório de {self.pessoa}"
    class Meta:
        verbose_name = "Relatório"
        verbose_name_plural = "Relatórios"