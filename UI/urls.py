from django.urls import path
from . import views
app_name='UI'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:group_id>/',views.detail,name='detail'),
    path('<int:group_id>/revise/',views.revise,name='revise'),
    path('<int:group_id>/results/',views.results,name='results')
]