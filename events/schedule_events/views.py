from django.shortcuts import render



def index(request):
    templ = 'schedule_events/index.html'

    return render(request, templ)

