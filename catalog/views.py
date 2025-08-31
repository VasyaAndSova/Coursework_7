from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from catalog.forms import ProductForm

class ProductListView(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"


