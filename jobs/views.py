from django.shortcuts import render

from .models import Job

# This is taking you to the jobs folder and then searching for home.html which we have  # noqa
# created in templates --> jobs --> home.html


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})
