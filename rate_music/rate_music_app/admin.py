from django.contrib import admin

from .models import *

# in admin you can have Class objects listed like below
# (what you see depends on __str__ method, otherwise it would be (in this example) Album object 1, 2, etc.)
admin.site.register(Album)


# or a table-like view with whatever model attribute
@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'city', 'label_current', 'active']


admin.site.register(Label)
admin.site.register(Rating)
admin.site.register(Gender)
admin.site.register(GeoCity)
admin.site.register(GeoCountry)
