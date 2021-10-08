
# # Register your models here.
#
#
from django.contrib import admin
#
from .models import Kyc
# from post.models import Post

admin.site.register(Kyc)
fields = ['image_tag']
readonly_fields = ['image_tag']

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title')
#     readonly_fields = ('thumbnail_preview',)
#
#     def thumbnail_preview(self, obj):
#         return obj.thumbnail_preview
#
#     thumbnail_preview.short_description = 'Thumbnail Preview'
#     thumbnail_preview.allow_tags = True
#
# admin.site.register(Post, PostAdmin)