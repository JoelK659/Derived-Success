from django.db import models
from django.utils.text import slugify
# Create your models here.
class Session(models.Model):
    student_username = models.CharField(max_length=200, null=True, blank=True)
    student_name = models.CharField(max_length=200)
    tutor_name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    description = models.TextField()
    time = models.CharField(max_length=200)
    status = models.CharField(max_length=10, default="Pending")
    decline_reason = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.tutor_name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.student_name)
            slug = base_slug
            i = 1
            while Session.objects.filter(slug=slug).exists():
                slug = f"{slug}-{i}"
                i += 1
            self.slug = slug

        super().save(*args, **kwargs)
