from django.contrib import admin
from .models import Contents, Coments, Content_tag, Image

# Register your models here.
admin.site.register(Contents)
admin.site.register(Coments)
admin.site.register(Content_tag)
admin.site.register(Image)