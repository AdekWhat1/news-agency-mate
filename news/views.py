from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from news.models import Newspaper, Redactor, Topic


@login_required
def index(request):

    num_newspaper = Newspaper.objects.count()
    num_redactor = Redactor.objects.count()
    num_topic = Topic.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    latest_newspaper = Newspaper.objects.select_related(
        "topic"
    ).prefetch_related("publishers").order_by("published_date")[:5]

    context = {
        "num_newspaper": num_newspaper,
        "num_redactor": num_redactor,
        "num_topic": num_topic,
        "num_visits": num_visits + 1,
        "latest_newspaper": latest_newspaper,
    }
    return render(request, "news/index.html", context=context)
