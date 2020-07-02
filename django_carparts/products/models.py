from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    category    = models.CharField(max_length=70)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    review      = models.TextField(null=True, blank=True)
    isUsed      = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("product", kwargs={"prod_id": self.id})

    def set_review(self, review):
        self.review = review
