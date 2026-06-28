from django.urls import path, include

from news.views import index

urlpatterns = [path("", index, name="main-page")]

app_name = "news"
