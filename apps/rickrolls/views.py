from django.shortcuts import redirect

from . import models


def index_url_rickroll(request):
    url_rickroll = models.RickrollUrl.objects.first()
    url_rickroll.number_of_transitions += 1
    url_rickroll.save()
    return redirect(url_rickroll.url)
