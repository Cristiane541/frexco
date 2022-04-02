from django.db import models

class Region(models.Model):
    name = models.CharField('Nome', max_length=100)

    def __str__(self) -> str:
        return self.name

class Fruit(models.Model):
    name = models.CharField('Nome', max_length=100)

    region = models.ForeignKey(
        Region,
        on_delete=models.SET_NULL,
        verbose_name='região',
        related_name='fruits',
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.name




