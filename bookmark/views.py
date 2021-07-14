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
