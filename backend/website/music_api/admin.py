from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

class UserDetailInline(admin.StackedInline):
  model = UserDetail
  can_delete = False

@admin.register(User)
class UserAdmin(BaseUserAdmin):
  fieldsets = (
    (None, {'fields': ('email', 'password', 'username')}),
    )
  add_fieldsets = (
    (None, {
    'classes': ('wide',),
    'fields': ('email', 'password1', 'password2'),
    }),
  )
  list_display = ('pk', 'email', 'is_staff')
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('pk',)
  inlines = (UserDetailInline, )

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
  list_display = ('title', 'artist', 'album', 'year')#[f.name for f in Song._meta.fields]
  search_fields = ('title', 'artist', 'album', 'year')
  ordering = ('title',)

@admin.register(FavoriteSongs)
class FavoriteSongsAdmin(admin.ModelAdmin):
  list_display = [f.name for f in FavoriteSongs._meta.fields]
  # search_fields = ('title', 'artist', 'album', 'year')
  ordering = ('user',)

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
  list_display = [f.name for f in UserDetail._meta.fields]
  # search_fields = ('title', 'artist', 'album', 'year')
  ordering = ('user',)
