from django.contrib import admin
from django.urls import path,re_path,include
from book.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", homepage,name="homepage"),
    path ("insert/", insert,name="insertpage"),
    path ("generous/<int:cat_id>/", viewPost,name="generous"),
    path ("show/<int:post_id>/", singlePost,name="singlePost"),
    path ("search/", search,name="search"),
    path("/delete/<int:id>/", deleteBooks, name="delete"),
    path("edit/<int:id>/edit/", editBooks, name="editBooks"),
    path("view/<int:id>/view/", viewBooks, name="viewBooks"),

    path("login/",signIn, name="signIn"),
    path("logout/",signOut, name="signOut"),
    path("register/",signUp, name="signUp"),

    re_path('^', include('django.contrib.auth.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)