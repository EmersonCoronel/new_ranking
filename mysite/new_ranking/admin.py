from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Admin, Trainer, Member

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Trainer)
admin.site.register(Member)