from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from core.erp.forms import NormaForm

from core.erp.models import Norma

class NormaListView(ListView):
    model = Norma
    template_name = 'norma/list.html'

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
                for i in Norma.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Normas'
        context['create_url'] = reverse_lazy('erp:norma_create')
        context['list_url'] = reverse_lazy('erp:norma_list')
        context['entity'] = 'Normas'
        return context
    
class NormaCreateView(CreateView):
    model = Norma
    form_class = NormaForm
    template_name = 'norma/create.html'
    success_url = reverse_lazy('erp:norma_list')
    url_redirect = success_url
    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación una Norma'
        context['entity'] = 'Normas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class NormaUpdateView( UpdateView):
    model = Norma
    form_class = NormaForm
    template_name = 'norma/create.html'
    success_url = reverse_lazy('erp:norma_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una Norma'
        context['entity'] = 'Normas'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class NormaDeleteView(DeleteView):
    model = Norma
    template_name = 'norma/delete.html'
    success_url = reverse_lazy('erp:norma_list')
    permission_required = 'delete_norma'
    url_redirect = success_url

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
        context['title'] = 'Eliminación de una Norma'
        context['entity'] = 'Normas'
        context['list_url'] = self.success_url
        return context
