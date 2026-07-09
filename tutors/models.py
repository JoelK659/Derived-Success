from django.db import models
from django.utils.text import slugify

# Create your models here.
class Tutor(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    description = models.TextField()
    availability = models.CharField(max_length=200)
    availability_time = models.CharField(max_length=200, null=True, blank=True)
    price_per_hour = models.FloatField()
    specialties = models.TextField()
    image = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            i = 1
            while Tutor.objects.filter(slug=slug).exists():
                slug = f"{base.slug}-{i}"
                i += 1
            self.slug = slug

        super().save(*args, **kwargs)
