from django.db import models

class Resource(models.Model):
    author = models.CharField(max_length=50)
    url = models.URLField(blank=True)
    related_plants = models.ManyToManyField('Plant', blank=True)

class Profile(models.Model):
    name = models.CharField(max_length=50)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

# Create your models here.
class Plant(models.Model):
    name_common = models.CharField(max_length=100)
    name_scientific = models.CharField(max_length=100)
    description = models.TextField()
    hardiness_zone_low = models.PositiveSmallIntegerField()
    hardiness_zone_high = models.PositiveSmallIntegerField()
    spacing = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    suggested_container_size = models.PositiveIntegerField()
    medicinal_benefits = models.TextField()
    # companion_plants = models.ManyToManyField('self', blank=True)
    companion_plants = models.TextField()
    # price = models.DecimalField(max_digits=5, decimal_places=2)
    # stock = models.IntegerField()
    resources = models.TextField()
    # image = models.ImageField(upload_to='plants/', null=True, blank=True)
    germination_days = models.PositiveSmallIntegerField()
    maturity_days = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name} ({self.name_scientific})"
