from django.db import models


class Servico(models.Model):
    empresa = models.IntegerField()
    codigo = models.IntegerField()

    descricao = models.CharField(
        max_length=200,
    )

    preco = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )

    ativo = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "servicos"

        constraints = [
            models.UniqueConstraint(
                fields=["empresa", "codigo"],
                name="uq_servico_empresa_codigo",
            ),
        ]

        indexes = [
            models.Index(
                fields=["empresa", "descricao"],
                name="idx_servico_empresa_descricao",
            ),
        ]

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"