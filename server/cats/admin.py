from django.contrib import admin

from . import models


@admin.register(models.Cat)
class CatAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
