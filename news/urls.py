from django.urls import path, include

import news
from news.views import index, TopicListView, NewspaperListView, RedactorListView, NewspaperDetailView, \
    RedactorDetailView, NewspaperCreateView, TopicCreateView, RedactorCreateView, TopicUpdateView, TopicDeleteView, \
    NewspaperUpdateView, NewspaperDeleteView

urlpatterns = [
    path("", index, name="main-page"),
    #Topic CRUD
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topic/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topic/<int:pk>/update/", TopicUpdateView.as_view(), name="topic-update"),
    path("topic/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic-delete"),
    # Newspaper CRUD
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("newspaper/create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path("newspaper/<int:pk>/update/", NewspaperUpdateView.as_view(), name="newspaper-update"),
    path("newspaper/<int:pk>/delete/", NewspaperDeleteView.as_view(), name="newspaper-delete"),

    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactor/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path("redactor/create/", RedactorCreateView.as_view(), name="redactor-create"),
]

app_name = "news"
