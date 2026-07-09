from django.db import models

class Society(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class Block(models.Model):
    society = models.ForeignKey(
        Society,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Flat(models.Model):
    block = models.ForeignKey(
        Block,
        on_delete=models.CASCADE
    )
    flat_number = models.CharField(max_length=20)

    def __str__(self):
        return self.flat_number