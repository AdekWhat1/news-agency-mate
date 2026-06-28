from django.contrib.auth import get_user, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from news.forms import NewspaperForm, RedactorCreationForm
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


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = ["name"]
    template_name = "news/topic_form.html"
    success_url = reverse_lazy("news:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = ["name"]
    template_name = "news/topic_form.html"
    success_url = reverse_lazy("news:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    template_name = "news/topic_confirm_delete.html"
    success_url = reverse_lazy("news:topic-list")


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    context_object_name = "newspapers_list"
    template_name = "news/newspaper_list.html"
    paginate_by = 5

    def get_queryset(self):
        return Newspaper.objects.select_related(
            "topic"
        ).prefetch_related("publishers").order_by("-published_date")


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper
    context_object_name = "newspaper"
    template_name = "news/newspaper_detail.html"

    def get_queryset(self):
        return Newspaper.objects.select_related(
            "topic"
        ).prefetch_related("publishers")


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = "news/newspaper_form.html"
    success_url = reverse_lazy("news:newspaper-list")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    template_name = "news/newspaper_form.html"

    def get_success_url(self):
        return reverse_lazy("news:newspaper-list", kwargs={"pk": self.object.id})


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    template_name = "news/newspaper_confirm_delete.html"
    success_url = reverse_lazy("news:newspaper-list")


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    context_object_name = "redactors_list"
    template_name = "news/redactor_list.html"
    paginate_by = 5


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    context_object_name = "redactor"
    template_name = "news/redactor_detail.html"

    def get_queryset(self):
        return Redactor.objects.prefetch_related("newspapers__topic")


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = get_user_model()
    form_class = RedactorCreationForm
    template_name = "news/redactor_form.html"
    success_url = reverse_lazy("news:redactor-list")