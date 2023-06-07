from django.contrib import admin
from web.models import Testimonial, Promoter, Faq, Subscribe


class TestimonialAdmin(admin.ModelAdmin):
    List_display = ["id", "name", "designation", "description", "image"]

admin.site.register(Testimonial,TestimonialAdmin)


class PromoterAdmin(admin.ModelAdmin):
    List_display = ["id", "name", "image"]

admin.site.register(Promoter,PromoterAdmin)


class FaqAdmin(admin.ModelAdmin):
    List_display = ["id", "title", "faq_type", "discription"]

admin.site.register(Faq,FaqAdmin)

admin.site.register(Subscribe)