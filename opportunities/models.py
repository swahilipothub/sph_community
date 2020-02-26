from django.db import models
from django.utils.translation import ugettext_lazy as _

class Skills(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Opportunity(models.Model):
    
    AVAILLABILITY = (
       ('full_time', _('Full Time')),
       ('part_time', _('Part Time')),
       ('remote', _('Remote')),
    )

    EDUCATION = (
       ('high_school', _('High School')),
       ('graduate', _('Graduate')),
       ('post_graduate', _('Post Graduate')),
       ('doctrate', _('Doctrate')),
    )

    STATUS = (
        ('draft', _('Draft')),
        ('published', _('Published')),
        ('filled', _('Vacancy Filled')),
    )

    name = models.CharField(max_length=128)
    location = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField()
    skills = models.ManyToManyField(Skills, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    availability = models.CharField(max_length=32, choices=AVAILLABILITY, null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    education = models.CharField(max_length=32, choices=EDUCATION, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)
    logo = models.ImageField(upload_to='company_logos', blank=True)
    status = models.CharField(max_length=32, choices=STATUS, default='draft')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('opportunity', kwargs={'pk': self.pk})