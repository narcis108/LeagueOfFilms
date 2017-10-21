from django.http.response import HttpResponse

# Create your views here.
from django.template import loader


def index(request):
    template = loader.get_template('index.html')

    return HttpResponse(template.render())
