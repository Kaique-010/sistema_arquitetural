from django.db import models

class Produto(models.Model):
    empresa = models.IntegerField()
    codigo = models.IntegerField()

    nome = models.CharField(
        max_length=150,
    )

    descricao = models.TextField(
        blank=True,
    )

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    ativo = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "produtos"

        constraints = [
            models.UniqueConstraint(
                fields=["empresa", "codigo"],
                name="uq_produto_empresa_codigo",
            ),
        ]

        indexes = [
            models.Index(
                fields=["empresa", "nome"],
                name="idx_produto_empresa_nome",
            ),
        ]

    def __str__(self):
        return f"{self.codigo} - {self.nome}"
