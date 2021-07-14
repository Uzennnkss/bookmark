from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.
# models.py 에 있는 'Bookmark 클래스'가 Admin 사이트에서 어떤 모습으로 보여줄지 정의하는 클래스
class BookmarkAdmin(admin.ModelAdmin):
    list_display=('title','url')

# admin.site.register() 함수 : Bookmark, BookmarkAdmin 클래스 등록 
admin.site.register(Bookmark,BookmarkAdmin)
