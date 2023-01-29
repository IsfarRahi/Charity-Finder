from django.contrib import admin
from django.urls import path
from charity import views

urlpatterns = [
    path('admin/' , admin.site.urls),
    path('make' , views.make),
    path('all-list' , views.show),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update)
]