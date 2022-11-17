from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Stream latest songs from your favorite Artiste.")


   