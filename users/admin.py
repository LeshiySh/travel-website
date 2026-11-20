from django.contrib import admin
from .models import User

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'phone', 'email', 'is_staff')
    search_fields = ('username', 'full_name', 'phone', 'email')
    fields = ('username', 'password', 'full_name', 'phone', 'email', 'is_staff', 'is_superuser', 'is_active')

    def save_model(self, request, obj, form, change):
        if not change or 'password' in form.changed_data:
            obj.set_password(obj.password)
        super().save_model(request, obj, form, change)