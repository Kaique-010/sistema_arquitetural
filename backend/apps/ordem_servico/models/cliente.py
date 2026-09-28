from django.db import models


class Cliente(models.Model):
    empresa = models.IntegerField()
    codigo = models.IntegerField()

    nome = models.CharField(
        max_length=150,
    )

    documento = models.CharField(
        max_length=20,
        blank=True,
    )

    telefone = models.CharField(
        max_length=30,
        blank=True,
    )

    ativo = models.BooleanField(
        default=True,
    )

    class Meta:
        db_table = "clientes"

        constraints = [
            models.UniqueConstraint(
                fields=["empresa", "codigo"],
                name="uq_cliente_empresa_codigo",
            ),
        ]

        indexes = [
            models.Index(
                fields=["empresa", "nome"],
                name="idx_cliente_empresa_nome",
            ),
        ]

    def __str__(self):
        return f"{self.codigo} - {self.nome}"