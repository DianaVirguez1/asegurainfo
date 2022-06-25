from django.urls import path
from core.erp.views.norma.views import *
from core.erp.views.dashboard.views import *
from core.erp.views.punto.views import *
from core.erp.views.item.views import *
from core.erp.views.requisito.views import *
from core.erp.views.empresa.views import *
app_name = 'erp'

urlpatterns = [
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # norma
    path('norma/list/', NormaListView.as_view(), name='norma_list'),
    path('norma/add/', NormaCreateView.as_view(), name='norma_create'),
    path('norma/update/<int:pk>/', NormaUpdateView.as_view(), name='norma_update'),
    path('norma/delete/<int:pk>/', NormaDeleteView.as_view(), name='norma_delete'),
    # punto
    path('punto/list/', PuntoListView.as_view(), name='punto_list'),
    path('punto/add/', PuntoCreateView.as_view(), name='punto_create'),
    path('punto/update/<int:pk>/', PuntoUpdateView.as_view(), name='punto_update'),
    path('punto/delete/<int:pk>/', PuntoDeleteView.as_view(), name='punto_delete'),

    # item
    path('item/list/', ItemListView.as_view(), name='item_list'),
    path('item/add/', ItemCreateView.as_view(), name='item_create'),
    path('item/update/<int:pk>/', ItemUpdateView.as_view(), name='item_update'),
    path('item/delete/<int:pk>/', ItemDeleteView.as_view(), name='item_delete'),

    # requisito
    path('requisito/list/', RequisitoListView.as_view(), name='requisito_list'),
    path('requisito/add/', RequisitoCreateView.as_view(), name='requisito_create'),
    path('requisito/update/<int:pk>/', RequisitoUpdateView.as_view(), name='requisito_update'),
    path('requisito/delete/<int:pk>/', RequisitoDeleteView.as_view(), name='requisito_delete'),


    # empresa
    path('empresa/list/', EmpresaListView.as_view(), name='empresa_list'),
    path('empresa/add/', EmpresaCreateView.as_view(), name='empresa_create'),
    path('empresa/update/<int:pk>/', EmpresaUpdateView.as_view(), name='empresa_update'),
    path('empresa/delete/<int:pk>/', EmpresaDeleteView.as_view(), name='empresa_delete'),

]
