from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')
def home_page(request):
    return render(request, 'coloring/home_page.html')
def choose_a_theme(request):
    return render(request, 'coloring/choose_a_theme.html')
def free_drawing(request):
    return render(request, 'coloring/free_drawing.html')
def my_gallary(request):
    return render(request, 'coloring/my_gallary.html')
def drawing(request):
    return render(request, 'coloring/drawing.html')
def original_drawing(request):
    return render(request, 'coloring/original_drawing.html')