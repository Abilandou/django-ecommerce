from django.db import models

# Create your models here.


class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)


class CategoryManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)  # Category.objects
        if qs.count() == 1:
            return qs.first()
        return None


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
