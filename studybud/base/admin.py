from django.contrib import admin
from .models import Topic, Room, Message, User

# Register your models here.
admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Room)

admin.site.register(Message) 