from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from core.erp.forms import RequisitoForm

from core.erp.models import Requisito

class RequisitoListView(ListView):
    model = Requisito
    template_name = 'requisito/list.html'

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
                for i in Requisito.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Requisitos'
        context['create_url'] = reverse_lazy('erp:requisito_create')
        context['list_url'] = reverse_lazy('erp:requisito_list')
        context['entity'] = 'Requisitos'
        return context
    
class RequisitoCreateView(CreateView):
    model = Requisito
    form_class = RequisitoForm
    template_name = 'requisito/create.html'
    success_url = reverse_lazy('erp:requisito_list')

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
        context['title'] = 'Creación de un Requisito'
        context['entity'] = 'Requisito'
        context['list_url'] = reverse_lazy('erp:requisito_list')
        context['action'] = 'add'
        return context
    
class RequisitoUpdateView(UpdateView):
    model = Requisito
    form_class = RequisitoForm
    template_name = 'requisito/create.html'
    success_url = reverse_lazy('erp:requisito_list')
    # permission_required = 'change_requisito'
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
        context['title'] = 'Edición de un Requisito'
        context['entity'] = 'Requisitos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class RequisitoDeleteView(DeleteView):
    model = Requisito
    template_name = 'requisito/delete.html'
    success_url = reverse_lazy('erp:requisito_list')
    permission_required = 'delete_requisito'
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
        context['title'] = 'Eliminación de un Requisito'
        context['entity'] = 'Requisitos'
        context['list_url'] = self.success_url
        return context