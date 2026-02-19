from urllib import request

from django.shortcuts import render

def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def blog_details(request):
    return render(request, 'blog_details.html')
def booking(request):
    return render(request, 'booking.html')
def contact(request):
    return render(request, 'contact.html')
def destination_details(request):
    return render(request, 'destination_details.html')
def destinations(request):
    return render(request, 'destinations.html')
def faq(request):
    return render(request, 'faq.html')
def starter_page(request):
    return render(request, 'starter_page.html')
def terms(request):
    return render(request, 'terms.html')
def testimonials(request):
    return render(request, 'testimonials.html')
def tour_details(request):
    return render(request, 'tour_details.html')
def tours(request):
    return render(request, 'tours.html')
def index(request):
    return render(request, 'index.html')
def gallery(request):
    return render(request, 'gallery.html')
def privacy(request):
    return render(request, 'privacy.html')
def tot(request):
    return render(request, '404.html')
# Create your views here.
