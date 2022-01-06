from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Location)
admin.site.register(ArticleCategories)

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'Author']
    save_on_top = True
admin.site.register(Articles, ArticlesAdmin)


@admin.register(Terms_and_Conditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ['heading']
    list_filter = ['heading']
    search_fields = ['heading']
    save_on_top = True


@admin.register(Cancellation_Policy)
class CancellationPolicyAdmin(admin.ModelAdmin):
    list_display = ['point']

@admin.register(Privacy_Policy)
class Privacy_PolicyAdmin(admin.ModelAdmin):
    list_display = ['heading']
    list_filter = ['heading']
    search_fields = ['heading']
    save_on_top = True


@admin.register(Disclaimer)
class CancellationPolicyAdmin(admin.ModelAdmin):
    list_display = ['disclaimer']

admin.site.register(Activities_Grid_Photos)


@admin.register(Trek)
class TrekAdmin(admin.ModelAdmin):
    list_display = ['title', 'district', 'price']
    list_filter = ['best', 'district']
    search_fields = ['title']
    save_on_top = True

@admin.register(Trek_days)
class Trek_daysAdmin(admin.ModelAdmin):
    list_display = ['trek', 'id', 'day_no', 'days']
    list_editable = ['days']
    list_filter = ['trek', 'day_no', 'id']

admin.site.register(About_trek)

@admin.register(Village_Tours)
class Village_ToursAdmin(admin.ModelAdmin):
    list_display = ['title', 'district', 'price']
    list_filter = ['best', 'district']
    search_fields = ['title']
    save_on_top = True

@admin.register(VillageTour_days)
class VillageTour_daysAdmin(admin.ModelAdmin):
    list_display = ['village_Tour', 'day_no', 'days']
    list_filter = ['village_Tour', 'day_no']

admin.site.register(About_villageTours)

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'updated']
    list_filter = ['title', 'email']

@admin.register(Gallery_category)
class Gallery_categoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'id']


@admin.register(Gallery_photo)
class Gallery_photoAdmin(admin.ModelAdmin):
    list_display = ['category', 'image']


@admin.register(Item)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ['title', 'video', 'updated']
    list_editable = ['video']
    list_display_links = ['title', 'updated']
    save_on_top = True
    search_fields = ['title']
    list_filter = ['title']

admin.site.register(about_us)



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['Email', 'Mobile', 'Name', 'notify_on', 'RegDate']
    ordering = ['Email']
    search_fields = ['Email', 'Mobile', 'Name', 'Place']
    date_hierarchy = 'RegDate'
    list_filter = ['Trek1', 'VillageTours1', 'Place']
    ordering = ['-RegDate']
    save_on_top = True


admin.site.register(Community_Work)


@admin.register(Upcoming_Events)
class Upcoming_EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'starts_on', 'duration_days', 'price']
    list_filter = ['starts_on', 'duration_days', 'trek', 'Activities', 'VillageTours']
    search_fields = ['title']
    date_hierarchy = 'starts_on'
    ordering = ['-starts_on']
    save_on_top = True



@admin.register(Event)
class Upcomin_Events_Form_Manyu_Admin(admin.ModelAdmin):
    list_display = ['Email', 'Mobile', 'Name', 'notify_on', 'RegDate']
    ordering = ['Email']
    search_fields = ['Email', 'Mobile', 'Name', 'Place']
    date_hierarchy = 'RegDate'
    list_filter = ['event', 'Place']
    ordering = ['-RegDate']
    save_on_top = True



@admin.register(Adventure_Sports)
class Adventure_SportsAdmin(admin.ModelAdmin):
    list_display = ['head']
    list_filter = ['head']
    search_fields = ['head']
    save_on_top = True

admin.site.register(Main_Slider)

admin.site.register(Contact_Us)
