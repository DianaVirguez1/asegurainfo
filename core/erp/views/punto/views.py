from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from core.erp.forms import PuntoForm

from core.erp.models import Punto

class PuntoListView(ListView):
    model = Punto
    template_name = 'punto/list.html'

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
                for i in Punto.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Puntos'
        context['create_url'] = reverse_lazy('erp:punto_create')
        context['list_url'] = reverse_lazy('erp:punto_list')
        context['entity'] = 'Puntos'
        return context
    
class PuntoCreateView(CreateView):
    model = Punto
    form_class = PuntoForm
    template_name = 'punto/create.html'
    success_url = reverse_lazy('erp:punto_list')

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
        context['title'] = 'Creación un punto'
        context['entity'] = 'Puntos'
        context['list_url'] = reverse_lazy('erp:punto_list')
        context['action'] = 'add'
        return context
    
class PuntoUpdateView(UpdateView):
    model = Punto
    form_class = PuntoForm
    template_name = 'punto/create.html'
    success_url = reverse_lazy('erp:punto_list')
    # permission_required = 'change_punto'
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
        context['title'] = 'Edición de un Punto'
        context['entity'] = 'Puntos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class PuntoDeleteView(DeleteView):
    model = Punto
    template_name = 'punto/delete.html'
    success_url = reverse_lazy('erp:punto_list')
    permission_required = 'delete_punto'
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
        context['title'] = 'Eliminación de un Punto'
        context['entity'] = 'Puntos'
        context['list_url'] = self.success_url
        return context