from django.contrib import admin
from .models import Signup
from .models import books
from .models import borrowedbooks

# Register your models here.


admin.site.register(Signup)
admin.site.register(books)
admin.site.register(borrowedbooks)
