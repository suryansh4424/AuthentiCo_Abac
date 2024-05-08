from django.contrib import admin
# Register your models here.

from .models import Profile, Skill, Message, Role

admin.site.register(Role)
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Message)
