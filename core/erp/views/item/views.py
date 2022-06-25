from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from core.erp.forms import ItemForm

from core.erp.models import Item

class ItemListView(ListView):
    model = Item
    template_name = 'item/list.html'

    @method_decorator(csrf_exempt)
    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Item.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Items'
        context['create_url'] = reverse_lazy('erp:item_create')
        context['list_url'] = reverse_lazy('erp:item_list')
        context['entity'] = 'Items'
        return context
    
class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item/create.html'
    success_url = reverse_lazy('erp:item_list')

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             form = self.get_form()
    #             data = form.save()
    #         else:
    #             data['error'] = 'No ha ingresado a ninguna opción'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación un item'
        context['entity'] = 'Items'
        context['list_url'] = reverse_lazy('erp:item_list')
        context['action'] = 'add'
        return context
    
class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item/create.html'
    success_url = reverse_lazy('erp:item_list')
    # permission_required = 'change_item'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        # self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         action = request.POST['action']
    #         if action == 'edit':
    #             form = self.get_form()
    #             data = form.save()
    #         else:
    #             data['error'] = 'No ha ingresado a ninguna opción'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Item'
        context['entity'] = 'Items'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item/delete.html'
    success_url = reverse_lazy('erp:item_list')
    permission_required = 'delete_item'
    url_redirect = success_url

    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Item'
        context['entity'] = 'Items'
        context['list_url'] = self.success_url
        return context    