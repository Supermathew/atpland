from django.shortcuts import render, get_object_or_404, redirect
from category.models import Category
from django.http import HttpResponse
from django.contrib import messages
from propertystore.models import Product
from django.db.models import Q
from category.models import Category

from dashboard.models import Messagemodel

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator




def home(request, category_slug=None):
    categories = None
    products = None
    agriculture = None
    house = None
    vwnture = None
    commercial=None
    farm =None
    Agriculture_Lands = None
    Farm_House=None
    Commercial_Lands=None
    Venture_Plots=None
    House_Property=None,
    
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, verifyed=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(verifyed=True).order_by('id')
        print(len(products))
        product_count = products.count()
        try:
          agriculture = Category.objects.get(category_name='Agriculture Lands')
        except Exception as e:
             agriculture = None
        print(agriculture)
        print(products)
        try:
          house= Category.objects.get(category_name='House Property')
        except Exception as e:
             house = None   
        try:
          vwnture= Category.objects.get(category_name='Venture Plots')
        except Exception as e:
             vwnture = None
        try:
         commercial= Category.objects.get(category_name='Commercial Lands')
        except Exception as e:
             commercial = None
        try:
         farm= Category.objects.get(category_name='Farm House')
        except Exception as e:
             farm = None       


        Agriculture_Lands = Product.objects.all().filter(verifyed=True,category=agriculture)[:5]
        House_Property = Product.objects.all().filter(verifyed=True,category=house)[:5]
        Venture_Plots = Product.objects.all().filter(verifyed=True,category=vwnture)[:5]
        Commercial_Lands = Product.objects.all().filter(verifyed=True,category=commercial)[:5]
        Farm_House = Product.objects.all().filter(verifyed=True,category=farm)[:5]
        print(Agriculture_Lands)

    context = {
        'agriculture': agriculture,
        'house': house,
        'vwnture': vwnture,
        'commercial':commercial,
        'farm':farm,
        'products': products,
        'product_count': product_count,
        'Agriculture_Lands': Agriculture_Lands,
        'Farm_House':Farm_House,
        'Commercial_Lands':Commercial_Lands,
        'Venture_Plots':Venture_Plots,
        'House_Property':House_Property,
    }
    return render(request, 'home.html', context)

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        productss = Product.objects.filter(category=categories, verifyed=True)
        paginator = Paginator(productss,4)
        page=request.GET.get('pg')
        products = paginator.get_page(page)
        # product_count = products.count()

    else:
        productss = Product.objects.all().filter(verifyed=True).order_by('id')
        paginator = Paginator(productss,4)
        page=request.GET.get('pg')
        productss = paginator.get_page(page)

    context = {
        'productss': productss,
        
    }
    return render(request, 'dashboard/seeall.html', context)


def property_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        noofmessage = Messagemodel.objects.filter(property=single_product).count()
    except Exception as e:
        raise e

    user = request.user

    context = {
        'noofmessage': noofmessage,
        'single_product': single_product,
        'user':user,
        }
    return render(request, 'property/propertydetail.html', context)


def search(request):
    if 'keyword' or 'category' or 'price' in request.GET:
        keyword = request.GET.get('keyword', False)
        print(keyword)
        cat = request.GET.get('category',False)
        print(cat)
        min = request.GET.get('price', False)


        productss = Product.objects.filter(verifyed=True)

        try: 
           cate = Category.objects.get(category_name=cat)
        except Exception as e:
            cate = None 

        if keyword:
            productss = productss.filter(Q(property_address__icontains=keyword) | Q(property_pincode__icontains=keyword) | Q(district__icontains=keyword))
        if cat and (cate is not None):
            productss = productss.filter(category=cate)
        if min:
            productss = productss.filter(price__gte=min)

        product_count = productss.count()

        paginator = Paginator(productss,6)
        page=request.GET.get('pg')
        products = paginator.get_page(page)
        # product_count = products.count()
    context = {
        'productss': productss,
        # 'product_count': product_count,
    }
    return render(request, 'dashboard/seeall.html', context)


