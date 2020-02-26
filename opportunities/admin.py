from django.contrib import admin

# Register your models here.
from opportunities.models import Opportunity, Language, Skills, Category

admin.site.register(Opportunity)
admin.site.register(Language)
admin.site.register(Skills)
admin.site.register(Category)