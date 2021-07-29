from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

def root(request):
    return redirect("/blogs")
def index(request):
    return HttpResponse(f'<h1>Mostrar una lista de todos los blogs<h2>')
def new(request):
    return HttpResponse(f'<p>Mostrar un nuevo formulario para crear un nuevo blog<p>')
def create(request):
    return redirect('/')
def show(request, number):
    return HttpResponse(f'<h3>para mostrar el blog numero {number}</h3>')
def edit(request, number):
    return HttpResponse(f'<h4>Editar el blog {number}</h1>')
def destroy(request, number):
    return redirect('/blogs')
def jres(request):
    data = [{'titulo': 'Nombre_Blog', 'Numero_Blog': '1'}, {'titulo': 'lineas', 'parrafo': '3'}]
    return JsonResponse({'data': data})
