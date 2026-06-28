from django.urls import path, include

import news
from news.views import index, TopicListView, NewspaperListView, RedactorListView

urlpatterns = [
    path("", index, name="main-page"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
]

app_name = "news"
