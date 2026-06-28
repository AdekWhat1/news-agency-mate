from django.contrib.auth import get_user, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from news.models import Newspaper, Redactor, Topic


@login_required
def index(request):

    num_newspaper = Newspaper.objects.count()
    num_redactor = Redactor.objects.count()
    num_topic = Topic.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    latest_newspapers = Newspaper.objects.select_related(
        "topic"
    ).prefetch_related("publishers").order_by("published_date")[:5]

    context = {
        "num_newspaper": num_newspaper,
        "num_redactor": num_redactor,
        "num_topic": num_topic,
        "num_visits": num_visits + 1,
        "latest_newspapers": latest_newspapers,
    }
    return render(request, "news/index.html", context=context)


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "news/topic_list.html"



class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    context_object_name = "newspapers_list"
    template_name = "news/newspaper_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Newspaper.objects.select_related(
            "topic"
        ).prefetch_related("publishers").order_by("published_date")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    context_object_name = "redactors_list"
    template_name = "news/redactor_list.html"
    paginate_by = 5