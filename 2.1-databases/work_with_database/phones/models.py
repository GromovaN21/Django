from django.db import models
from django.template.defaultfilters import slugify

class Phone(models.Model):
    name = models.CharField(u'Название', max_length=64)
    price = models.DecimalField( max_digits=8, decimal_places=2)
    image = models.URLField( null=True, blank=True)
    release_date = models.DateField(u'Дата выхода')
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

   