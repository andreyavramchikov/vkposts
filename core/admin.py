from django.contrib import admin

# Register your models here.
from .forms import PostForm
from .models import Post, Account


class PostAdmin(admin.ModelAdmin):
    form = PostForm


class AccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Account, AccountAdmin)
