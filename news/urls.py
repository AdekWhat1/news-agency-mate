from django.urls import path, include

import news
from news.views import index, TopicListView, NewspaperListView, RedactorListView, NewspaperDetailView, \
    RedactorDetailView

urlpatterns = [
    path("", index, name="main-page"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactor/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
]

app_name = "news"
