from django.urls import path
from app_final.views import *
from app_final import views

urlpatterns = [
    path('', home, name='home'),
    path('personas/', views.personas, name='personas'),
    path('productos/', views.productos, name='productos'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('sobre_mi/', views.sobre_mi, name='sobre_mi'),
]

formularios = [
    path('nueva_persona/', views.nueva_persona, name='nueva_persona'),
    path('nuevo_producto/', views.nuevo_producto, name='nuevo_producto'),
    path('nuevo_pedido/', views.nuevo_pedido, name='nuevo_pedido'),
]

urlpatterns += formularios

busquedas = [
    path('buscar_persona', views.buscar_persona, name='buscar_persona'),
    path('search_persona/', views.search_persona, name='search_persona'),
    path('buscar_producto', views.buscar_producto, name='buscar_producto'),
    path('search_producto/', views.search_producto, name='search_producto'),
    path('buscar_pedido', views.buscar_pedido, name='buscar_pedido'),
    path('search_pedido/', views.search_pedido, name='search_pedido'),
]

urlpatterns += busquedas

actualizar = [
    path('actualizar_producto/<pk>', views.ProductoUpdateView.as_view(), name='actualizar_producto'),
    path('actualizacion_producto/', views.actualizacion_producto, name='actualizacion_producto'),
    path('actualizar_pedido/<pk>', views.PedidoUpdateView.as_view(), name='actualizar_pedido'),
    path('actualizacion_pedido/', views.actualizacion_pedido, name='actualizacion_pedido'),
]

urlpatterns += actualizar