<!--bookmark page 만들기-->
#Bookmark page 만들기 

##1. models.py 
```py
from django.db import models

# Create your models here.

class Bookmark(models.Model):
    title=models.CharField(max_length=100, blank=True, null=True)
    url=models.URLField('url',unique=True)

    def __str__(self):
        return self.title
```

2. admin.py
테이블을 새로 만들 때는 models.py 와 admin.py 를 함께 수정해야 한다. 
```py
from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.
# models.py 에 있는 'Bookmark 클래스'가 Admin 사이트에서 어떤 모습으로 보여줄지 정의하는 클래스
class BookmarkAdmin(admin.ModelAdmin):
    list_display=('title','url')

# admin.site.register() 함수 : Bookmark, BookmarkAdmin 클래스 등록 
admin.site.register(Bookmark,BookmarkAdmin)
```

3. migrations
migrate를 통해 models.py의 클래스를 테이블로 생성시킨다. 
```py
cd mysite
python manage.py makemigrations
python manage.py migrate
```

4. urls.py
```py
from django.contrib import admin
# 장고의 내장함수인 url()함수를 가져온다. (아래있는 path들)
from django.urls import path
from bookmark.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',BookmarkLV,name="home"),
    path('detail/<str:id>',BookmarkDV,name="detail"),

]
```
5. views.py 
```py
from django.shortcuts import get_object_or_404, render
#Bookmark 클래스를 불러온다.
from .models import Bookmark

# Create your views here.

def BookmarkLV(request):
    bookmark=Bookmark.objects.all()
    return render(request,'bookmark_list.html',{'bookmark':bookmark})


def BookmarkDV(request, id):
    blog=get_object_or_404(Bookmark,pk=id)
    return render(request,'bookmark_detail.html',{'blog':blog})
```

6. templates
* bookmark_list.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Bookmark List</h1>

    <div class="container">

        {%for bookmark in bookmark %}
            <li><a href="{% url 'detail' bookmark.id %}">{{bookmark}}</a></li>

        {% endfor %}
    </div>
</body>
</html>
```

* bookmark_list.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>detail.html</title>
</head>
<body>
    <h1>{{blog.title}}</h1> 
    <li>URL : <a href="{% url 'detail' blog.id %}">{{blog.url}}</a></li>

</body>
</html>
```
