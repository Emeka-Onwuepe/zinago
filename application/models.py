from django.db import models
from publishers.models import Article

# Create your models here.
class Application(models.Model):
    """Model definition for Application."""
    job = models.ForeignKey(Article, verbose_name="post", 
                            on_delete=models.CASCADE,related_name="post_applications")
    full_name = models.CharField("full_name", max_length=100)
    email = models.EmailField("email", max_length=50,unique=True)
    phone_number = models.CharField('phone_number', max_length=50)
    address = models.CharField('address', max_length=256)
    evelator_speech = models.TextField('evelator_speech')
    cv = models.FileField("cv")
    selected = models.BooleanField("selected",default=False)
    employed = models.BooleanField("employed",default=False)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Application."""

        verbose_name = 'Application'
        verbose_name_plural = 'Applications'

    def __str__(self):
        """Unicode representation of Application."""
        return f"{self.full_name} {self.phone_number}"

