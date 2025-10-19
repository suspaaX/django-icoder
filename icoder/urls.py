
from django.contrib import admin
from django.urls import path ,include

admin.site.site_header = "Icoder Admin" 
admin.site.site_title = "Icoder Admin pannel"
admin.site.index_title = "Welcome to Icoder Admin pannel" 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('blog/',include('blog.urls')),
]
