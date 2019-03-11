from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

SiteUser = get_user_model()

class SiteUserAdmin(UserAdmin):
    # # The forms to add and change user instances
    # # form = UserAdminChangeForm
    # add_form = UserAdminCreationForm

    # # The fields to be used in displaying the User model.
    # # These override the definitions on the base UserAdmin
    # # that reference specific fields on auth.User.
    list_display = ('email', 'admin',)
    # # The filters to filter results on the admin site
    list_filter = ('admin', 'staff', 'active')
    readonly_fields = ['date_joined', 'reset_token', 'last_login']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth')}),
        ('Permissions', {'fields': ('admin', 'staff', 'active')}),
        ('These Fields cannot be changed', {'fields': ('date_joined', 'reset_token', 'last_login')})
    )
    # # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',
            	'first_name', 'last_name', 'date_of_birth')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    # filter_horizontal = ()


admin.site.register(SiteUser, SiteUserAdmin)