from django.urls import path
from .import views

urlpatterns = [
    # path('',views.Databaselist, name="database"),
    path('databaselist/',views.databaselist, name="lists"),
    path('postdetails',views.postdetails, name="POST"),
    path('postupdates/<str:pk>',views.databaseUpdate, name="UPDATE"),
    path('postdeletes/<str:pk>',views.databaseDelete, name="DELETE")
]