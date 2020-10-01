from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

#class es para indicar que es un objeto
#Post es el ombre de nuestro objeto
#models.Model significa que la publicación es un modelo de Django, por lo que Django sabe que debe guardarse en la base de datos.


# propiedades title, author, text create_date, published_date

# models.CharField - así es como se define el texto con un número limitado de caracteres.
# models.TextField- esto es para texto largo sin límite.
# models.DateTimeField - esta es una fecha y hora.
# models.ForeignKey - este es un enlace a otro modelo.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # metodos
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title