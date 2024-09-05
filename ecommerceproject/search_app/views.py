from django.shortcuts import render
from shopapp.models import Product
from django.db.models import Q

# Create your views here.
def serch_results(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    
    # Ensure an HttpResponse is always returned
        return render(request, 'search.html', {'products': products, 'query': query})
