from django.contrib import admin
from .models import Member, Book, Copy, IssuedBook

admin.site.register(Member)
admin.site.register(Book)
admin.site.register(Copy)
admin.site.register(IssuedBook)
