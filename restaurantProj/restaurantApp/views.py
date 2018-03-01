from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuItem
from .models import Order, OrderwMenuItem, MenuItem
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from decimal import Decimal

def index(request):
    context = {}
    context["menuitem"] = MenuItem.objects.all()
    context["order"] = Order.objects.all()
    return render(request, 'restaurantProj/index.html', context)

class MenuItemListView(ListView):
    model = MenuItem

    def get_queryset(self):
        search_key = self.request.GET.get('search','')
        name_search = self.model.objects.all().filter(name__icontains=search_key)
        id_search = self.model.objects.filter(id__icontains=search_key)
        # Ref: https://stackoverflow.com/questions/431628/how-to-combine-2-or-more-querysets-in-a-django-view
        from itertools import chain
        object_list = list(chain(name_search, id_search))
        self.found = len(object_list)
        return object_list

    #Ref: https://stackoverflow.com/questions/9168447/cant-add-extra-context-to-a-listview
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MenuItemListView, self).get_context_data(**kwargs)
        context['found'] = self.found
        return context

    def get_template_names(self):
        return 'restaurantProj/menu_search.html'

class MenuItemDeleteView(DeleteView):
    model = MenuItem

    # Ref: https://stackoverflow.com/questions/35796195/how-to-redirect-to-previous-page-in-django-after-post-request
    def get_success_url(self):
        return self.request.POST.get('next', '/')

    def get_template_names(self):
        return 'restaurantProj/menu_delete.html'

class MenuItemCreateView(CreateView):
    model = MenuItem
    fields = ['name','type','price']
    success_url = reverse_lazy('home')

    def get_template_names(self):
        return 'restaurantProj/menu_add.html'


def orderview(request,pk):
    table = Order.objects.get(id=pk)
    context = {}
    context["object_list"] = OrderwMenuItem.objects.filter(order=table)
    context["table"] = table.table
    sum = 0
    for item in context["object_list"]:
        sum += Decimal(item.menuitem.price)
    tax = round(Decimal(float(sum) * 0.08),2)
    sum += tax
    context["sum"] = sum
    context["tax"] = tax
    return render(request, 'restaurantProj/order_view.html', context)

class OrderwMenuItemDeleteView(DeleteView):
    model = OrderwMenuItem
    success_url = reverse_lazy('home')

    def get_template_names(self):
        return 'restaurantProj/order_delete.html'

class OrderwMenuItemCreateView(CreateView):
    model = OrderwMenuItem
    fields = ['order','menuitem']

    #Ref: https://stackoverflow.com/questions/35796195/how-to-redirect-to-previous-page-in-django-after-post-request
    def get_success_url(self):
        return self.request.POST.get('next','/')

    def get_template_names(self):
        return 'restaurantProj/orderwmenuitem_add.html'


class OrderListView(ListView):
    model = Order

    def get_template_names(self):
        return 'restaurantProj/index.html'

class OrderCreateView(CreateView):
    model = Order
    fields = ['table']
    success_url = reverse_lazy('home')

    def get_template_names(self):
        return 'restaurantProj/order_add.html'

class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('home')

    def get_template_names(self):
        return 'restaurantProj/order_delete.html'
