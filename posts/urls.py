from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("<int:pk>/", views.PostView.as_view(), name="post"), # mentioned path converter int, capture integer only in id
    path("tags/<int:id>/",views.tags, name="tag"),
    path("search/", views.search, name="search"),
]