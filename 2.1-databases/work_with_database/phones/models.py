from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id=models.IntegerField(primary_key=True)
    name=models.TextField(max_length=60, unique=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='static/uploads/')
    release_date=models.DateField()
    lte_exists=models.BooleanField()
    slug=models.SlugField(unique=True)

