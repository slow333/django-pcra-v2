from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models.functions import Round, Concat
from django.db.models import F, Func, Value, Q, Count, Min, Max, Avg,ExpressionWrapper, DecimalField
from aistore.models import Customer, Order, OrderItem, Product
from quark.forms import SearchForm
from tags.models import TaggedItem, Tag, TaggedItemManager

def home(request):
    query_set = Product.objects.all()
    query_set = query_set.order_by('title')
    
    search_title = request.GET.get('search_title', '')
    sort = request.GET.get('sort', 'title')
    order = request.GET.get('order', 'asc')
    
    # 검색 폼 처리
    search_form = SearchForm(request.GET or None)
    
    if search_title:
        query_set = query_set.filter(title__icontains=search_title)
    
    if sort and order:
        if order == 'desc':
            query_set = query_set.order_by('-' + sort)
        else:
            query_set = query_set.order_by(sort)

    paginator = Paginator(query_set, 10)  # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'name': 'kim',
        'page_obj': page_obj,
        'search_form': search_form,
        'search_title': search_title,
        'sort': sort,
        'order': order,
    }
    return render(request, 'aistore/aistore-home.html', context)