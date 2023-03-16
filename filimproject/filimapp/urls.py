
from django.urls import path
from . import views
app_name='filimapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('filim/<int:filim_id>/',views.detail,name='detail'),
    path('add/',views.add_filim,name='addfilim'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]