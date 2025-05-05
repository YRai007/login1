from django.contrib import admin
from .models import Contact

# Customize the admin site
admin.site.site_header = "GameVerse Admin Panel"
admin.site.site_title = "GameVerse Admin"
admin.site.index_title = "Welcome to the GameVerse Dashboard"

# Customize Contact admin view
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')

# Register the Contact model with custom admin
admin.site.register(Contact, ContactAdmin)


