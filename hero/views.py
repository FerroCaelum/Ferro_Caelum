from django.shortcuts import render_to_response
from hero.models import Hero

def index(request):
    return render_to_response('hero/display_stats.html', {'hi'})