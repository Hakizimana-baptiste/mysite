from django.contrib import admin
from .models import User
from .models import Song, Artist
from .models import Playlist


# class UserAdmin(admin.ModelAdmin):
#     model = User
#     fields = ["username", "email", "role"]


class ArtistAdmin(admin.ModelAdmin):
    model = Artist
    fields = ["name", "age", "sex"]


admin.site.register(Artist, ArtistAdmin)
# admin.site.register(User, UserAdmin)
admin.site.register(Song)
admin.site.register(Playlist)
# Register your models here.
