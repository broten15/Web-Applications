from django.shortcuts import render

from pizzas.models import Pizza

# Create your views here.

def index(request):
    """The home page for Learning Logs"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Show all pizzas"""
    pizzas = Pizza.objects.order_by('text')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """Shows a single pizzas and all of it's topping (and info)"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza':pizza, 'toppings':toppings}
    return render(request, 'pizzas/pizza.html', context)

    