from django.db import models

class ProductCategory(models.Model):
    """Product Category for grouping products."""
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')

    def __str__(self):
        return self.name 