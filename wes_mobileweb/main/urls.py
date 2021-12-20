from django.urls import path
from django.contrib import admin

from .views import *

# 이미지를 업로드하자
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('upload/', upload, name='upload'),
    #URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('upload/<int:pk>/',posting, name="posting"),
    path('upload/new_post/', new_post, name="new_post"),
    path('upload/<int:pk>/remove/', remove_post),
    path('upload/<int:pk>/result/', result),

]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)