from django.db import models
from django.utils.text import slugify

from users.models import Usuario

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField(blank=True) # decidi criar um slug para a url da página ficar mais bonita, sem ser só o pk da post
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True) # o blank permite não ter uma imagem
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None, related_name='posts')

    # para salvar o slug de acordo com o título
    def save(self, *args, **kwargs): 
        if not self.slug: 
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
