from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','content_length','updated_at'] #화면에 보여지는 항목 설정
    list_filter = ['updated_at'] # 필터링 옵션항목  설정
    search_fields = ['title'] # 검색용 항목 설정

    prepopulated_fields = {
        'slug':['title'],
    } #slug 자동입력 설정

    def content_length(self, post):
        return '{}글자'.format(len(post.content))

admin.site.register(Post, PostAdmin)