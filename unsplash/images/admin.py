from django.contrib import admin
from .models import User, Image, tags

admin.site.register(User)
admin.site.register(Image)
admin.site.register(tags)