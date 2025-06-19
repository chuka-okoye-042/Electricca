from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'siteapp/index.html')
def about(request):
    return render(request, 'siteapp/about.html')
def services(request):
    return render(request, 'siteapp/services.html')    
def testimonial(request):
    return render(request, 'siteapp/testimonial.html')  
def contact(request):
    return render(request, 'siteapp/contact.html')    
def blog(request):
    return render(request, 'siteapp/blog.html')