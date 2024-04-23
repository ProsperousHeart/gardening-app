from django.db import models

# class Resource(models.Model):
#     author = models.CharField(max_length=50)
#     url = models.URLField(blank=True)
#     related_plants = models.ManyToManyField('Plant', blank=True)

class Profile(models.Model):
    name = models.CharField(max_length=50)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

# Create your models here.
class Plant(models.Model):
    EXPOSURE_CHOICES = [
        ('fs', 'Full Sun (6+)'),
        ('pu', 'Partial Sun (morning, 4-6H)'),
        ('pd', 'Partial Shade (morning, <=4H)'),
        ('sh', 'Shade'),
    ]
    TYPE_CHOICES = [
        ('an', 'Annual'),
        ('bi', 'Biennial'),
        ('pe', 'Perennial'),
        ('sh', 'Shrub'),
        ('tr', 'Tree'),
        ('vi', 'Vine'),
    ]
    HARDINESS_ZONES = [
        ('1a', '1a (-60 to -55 °F/-51.1 to -48.3 °C)'),
        ('1b', '1b (-55 to -50 °F/-48.3 to -45.6 °C)'),
        ('2a', '2a (-50 to -45 °F/-45.6 to -42.8 °C)'),
        ('2b', '2b (-45 to -40 °F/-42.8 to -40 °C)'),
        ('3a', '3a (-40 to -35 °F/-40 to -37.2 °C)'),
        ('3b', '3b (-35 to -30 °F/-37.2 to -34.4 °C)'),
        ('4a', '4a (-30 to -25 °F/-34.4 to -31.7 °C)'),
        ('4b', '4b (-25 to -20 °F/-31.7 to -28.9 °C)'),
        ('5a', '5a (-20 to -15 °F/-28.9 to -26.1 °C)'),
        ('5b', '5b (-15 to -10 °F/-26.1 to -23.3 °C)'),
        ('6a', '6a (-10 to -5 °F/-23.3 to -20.6 °C)'),
        ('6b', '6b (-5 to 0 °F/-20.6 to -17.8 °C)'),
        ('7a', '7a (0 to 5 °F/-17.8 to -15 °C)'),
        ('7b', '7b (5 to 10 °F/-15 to -12.2 °C)'),
        ('8a', '8a (10 to 15 °F/-12.2 to -9.4 °C)'),
        ('8b', '8b (15 to 20 °F/-9.4 to -6.7 °C)'),
        ('9a', '9a (20 to 25 °F/-6.7 to -3.9 °C)'),
        ('9b', '9b (25 to 30 °F/-3.9 to -1.1 °C)'),
        ('10a', '10a (30 to 35 °F/-1.1 to 1.7 °C)'),
        ('10b', '10b (35 to 40 °F/1.7 to 4.4 °C)'),
        ('11a', '11a (40 to 45 °F/4.4 to 7.2 °C)'),
        ('11b', '11b (45 to 50 °F/7.2 to 10 °C)'),
        ('12a', '12a (50 to 55 °F/10 to 12.8 °C)'),
        ('12b', '12b (55 to 60 °F/12.8 to 15.6 °C)'),
        ('13a', '13a (60 to 65 °F/15.6 to 18.3 °C)'),
        ('13b', '13b (65 to 70 °F/18.3 to 21.1 °C)'),
    ]
    name_common = models.CharField(max_length=100)
    name_scientific = models.CharField(max_length=100)
    plant_type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='pe')
    exposure = models.CharField(max_length=2, choices=EXPOSURE_CHOICES, default='fs')
    description = models.TextField()
    earth_kind = models.BooleanField(default=False)
    hardiness_zone_low = models.CharField(max_length=3, choices=HARDINESS_ZONES, default='8b')
    hardiness_zone_high = models.CharField(max_length=3, choices=HARDINESS_ZONES, default='8b')
    spacing_min = models.PositiveSmallIntegerField(default=0)
    spacing_max = models.PositiveSmallIntegerField(default=0)
    height_min = models.PositiveSmallIntegerField(default=0)
    height_max = models.PositiveSmallIntegerField(default=0)
    suggested_container_size = models.PositiveIntegerField(default=0)
    medicinal_benefits = models.TextField(blank=True)
    # companion_plants = models.ManyToManyField('self', blank=True)
    # companion_plants = models.TextField()
    # image = models.ImageField(upload_to='plants/', null=True, blank=True)
    germination_days = models.PositiveSmallIntegerField(default=0)
    maturity_days = models.PositiveSmallIntegerField(default=0)
    # links = models.ManyToManyField('PlantLink', blank=True)

    def __str__(self):
        return f"{self.name_common} ({self.name_scientific})"

class PlantLink(models.Model):
    LINK_TYPE_CHOICES = [
        ('aa', 'Academic Article'),
        ('bl', 'Blog'),
        ('bk', 'Book'),
        ('mg', 'Master Gardener'),
        ('ot', 'Other'),
        ('yt', 'YouTube'),
    ]
    # resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    url = models.URLField()
    type = models.CharField(max_length=2, choices=LINK_TYPE_CHOICES)
    # plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    plant = models.ManyToManyField(Plant, blank=True, related_name='links')

    class Meta:
        ordering = ['type', 'title']

    def __str__(self):
        type = [item for item in self.LINK_TYPE_CHOICES 
                if item[0] == self.type][0][1]
        if not self.plant:
            return f'{type} ({self.plant}):\t"{self.title}"'
        else:
            return f'{type}:\t"{self.title}"'
