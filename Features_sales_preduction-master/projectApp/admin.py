from django.contrib import admin
from .models import *
# Register your models here.
class Features_sales_preductionAdmin(admin.ModelAdmin):
    list_display = ('TV', 'Radio','Newspaper')
admin.site.register(Features_sales_preduction,Features_sales_preductionAdmin)

# Predict
admin.site.register(Predict)


