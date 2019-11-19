
from django.conf.urls import url
from django.urls import path, include
from appfarmaceutica import views
from django.contrib.auth import views as auth_views
#from django.contrib.auth import views as auth_views 
from .views import (
    home, crearCliente, listarCliente, editarCliente, eliminarCliente, 
    crearCiudad, listarCiudad, editarCiudad, eliminarCiudad,
    crearTipoProducto, listarTipoProducto, editarTipoProducto, eliminarTipoProducto,
    crearSucursal, listarSucursal, editarSucursal, eliminarSucursal,
    crearProducto, listarProducto, editarProducto, eliminarProducto,
    crearTrasladoProducto, listarTrasladoProducto, editarTrasladoProducto, eliminarTrasladoProducto,
    crearDetalleTrasladoProducto, listarDetalleTrasladoProducto, editarDetalleTrasladoProducto, eliminarDetalleTrasladoProducto,
    crearTipoActivoFijo, listarTipoActivoFijo, editarTipoActivoFijo, eliminarTipoActivoFijo,
    crearActivoFijo, listarActivoFijo, editarActivoFijo, eliminarActivoFijo,
    crearDocumento, listarDocumento, editarDocumento, eliminarDocumento,
    crearCaja, listarCaja, editarCaja, eliminarCaja,
    crearPedido, listarPedido, editarPedido, eliminarPedido,
    crearDetallePedido, listarDetallePedido, editarDetallePedido, eliminarDetallePedido,
    crearCardexCaja, listarCardexCaja, editarCardexCaja, eliminarCardexCaja,
    listarUsuario,
    crearTotales, listarTotales, editarTotales, eliminarTotales
    )
 
app_name= 'appfarmaceutica'

urlpatterns = [
   
    url(r'^plantilla/', listarUsuario,),
    path('', views.auth_login, name= 'authentication'), 
    #path('signup', views.auth_login, name='signup'),
    url('^logout/$', auth_views.LogoutView.as_view(), {'next_page':'/'}, name= 'logout'),
    

    url(r'^cliente/crear_cliente/', crearCliente, name= 'crear_cliente'),
    url(r'^cliente/listar_cliente/(?P<pk>[\w\-]+)/$', listarCliente, name = 'listar_cliente'),
    url(r'^cliente/editar_cliente/(?P<pk>\d+)/$', editarCliente, name= "editar_cliente"),
    url(r'^cliente/eliminar_cliente/(?P<pk>\d+)/$', eliminarCliente, name= "eliminar_cliente"),
  
    url(r'^ciudad/crear_ciudad/', crearCiudad, name='crear_ciudad'),
    url(r'^ciudad/listar_ciudad/', listarCiudad, name="listar_ciudad"),
    url(r'^ciudad/editar_ciudad/(?P<pk>\d+)/$', editarCiudad, name= "editar_ciudad"),
    url(r'^ciudad/eliminar_ciudad/(?P<pk>\d+)/$', eliminarCiudad, name= "eliminar_ciudad"),

    url(r'^tipo_producto/crear_tipo_producto/', crearTipoProducto, name='crear_tipo_producto'),
    url(r'^tipo_producto/listar_tipo_producto/', listarTipoProducto, name="listar_tipo_producto"),
    url(r'^tipo_producto/editar_tipo_producto/(?P<pk>\d+)/$', editarTipoProducto, name= "editar_tipo_producto"),
    url(r'^tipo_producto/eliminar_tipo_producto/(?P<pk>\d+)/$', eliminarTipoProducto, name= "eliminar_tipo_producto"),

    url(r'^sucursal/crear_sucursal/', crearSucursal, name='crear_sucursal'),
    url(r'^sucursal/listar_sucursal/', listarSucursal, name="listar_sucursal"),
    url(r'^sucursal/editar_sucursal/(?P<pk>\d+)/$', editarSucursal, name= "editar_sucursal"),
    url(r'^sucursal/eliminar_sucursal/(?P<pk>\d+)/$', eliminarSucursal, name= "eliminar_sucursal"),

    url(r'^producto/crear_producto/', crearProducto, name='crear_producto'),
    url(r'^producto/listar_producto/(?P<pk>[\w\-]+)/$', listarProducto, name="listar_producto"),
    url(r'^producto/editar_producto/(?P<pk>[\w\-]+)/$', editarProducto, name= "editar_producto"),
    url(r'^producto/eliminar_producto/(?P<pk>[\w\-]+)/$', eliminarProducto, name= "eliminar_producto"),

    url(r'^traslado_producto/crear_traslado_producto/', crearTrasladoProducto, name='crear_traslado_producto'),
    url(r'^traslado_producto/listar_traslado_producto/(?P<pk>[\w\-]+)/$', listarTrasladoProducto, name="listar_traslado_producto"),
    url(r'^traslado_producto/editar_traslado_producto/(?P<pk>\d+)/$', editarTrasladoProducto, name= "editar_traslado_producto"),
    url(r'^traslado_producto/eliminar_traslado_producto/(?P<pk>\d+)/$', eliminarTrasladoProducto, name= "eliminar_traslado_producto"),

    url(r'^detalle_traslado_producto/crear_detalle_traslado_producto/', crearDetalleTrasladoProducto, name='crear_detalle_traslado_producto'),
    url(r'^detalle_traslado_producto/listar_detalle_traslado_producto/(?P<TrasladoProducto>[\w\-]+)/$', listarDetalleTrasladoProducto, name="listar_detalle_traslado_producto"),
    url(r'^detalle_traslado_producto/editar_detalle_traslado_producto/(?P<pk>\d+)/$', editarDetalleTrasladoProducto, name= "editar_detalle_traslado_producto"),
    url(r'^detalle_traslado_producto/eliminar_detalle_traslado_producto/(?P<pk>\d+)/$', eliminarDetalleTrasladoProducto, name= "eliminar_detalle_traslado_producto"),

    url(r'^tipo_activo_fijo/crear_tipo_activo_fijo/', crearTipoActivoFijo, name='crear_tipo_activo_fijo'),
    url(r'^tipo_activo_fijo/listar_tipo_activo_fijo/', listarTipoActivoFijo, name="listar_tipo_activo_fijo"),
    url(r'^tipo_activo_fijo/editar_tipo_activo_fijo/(?P<pk>\d+)/$', editarTipoActivoFijo, name= "editar_tipo_activo_fijo"),
    url(r'^tipo_activo_fijo/eliminar_tipo_activo_fijo/(?P<pk>\d+)/$', eliminarTipoActivoFijo, name= "eliminar_tipo_activo_fijo"),

    url(r'^activo_fijo/crear_activo_fijo/', crearActivoFijo, name='crear_activo_fijo'),
    url(r'^activo_fijo/listar_activo_fijo/(?P<pk>[\w\-]+)/$', listarActivoFijo, name="listar_activo_fijo"),
    url(r'^activo_fijo/editar_activo_fijo/(?P<pk>\d+)/$', editarActivoFijo, name= "editar_activo_fijo"),
    url(r'^activo_fijo/eliminar_activo_fijo/(?P<pk>\d+)/$', eliminarActivoFijo, name= "eliminar_activo_fijo"),

    url(r'^documento/crear_documento/', crearDocumento, name='crear_documento'),
    url(r'^documento/listar_documento/', listarDocumento, name="listar_documento"),
    url(r'^documento/editar_documento/(?P<pk>\d+)/$', editarDocumento, name= "editar_documento"),
    url(r'^documento/eliminar_documento/(?P<pk>\d+)/$', eliminarDocumento, name= "eliminar_documento"),

    url(r'^caja/crear_caja/', crearCaja, name='crear_caja'),
    url(r'^caja/listar_caja/(?P<pk>[\w\-]+)/$', listarCaja, name="listar_caja"),
    url(r'^caja/editar_caja/(?P<pk>\d+)/$', editarCaja, name= "editar_caja"),
    url(r'^caja/eliminar_caja/(?P<pk>\d+)/$', eliminarCaja, name= "eliminar_caja"),

    url(r'^pedido/crear_pedido/', crearPedido, name='crear_pedido'),
    url(r'^pedido/listar_pedido/(?P<pk>[\w\-]+)/$', listarPedido, name="listar_pedido"),
    url(r'^pedido/editar_pedido/(?P<pk>\d+)/$', editarPedido, name= "editar_pedido"),
    url(r'^pedido/eliminar_pedido/(?P<pk>\d+)/$', eliminarPedido, name= "eliminar_pedido"),

    url(r'^detalle_pedido/crear_detalle_pedido/', crearDetallePedido, name='crear_detalle_pedido'),
    url(r'^detalle_pedido/listar_detalle_pedido/(?P<Pedido>\d+)/$', listarDetallePedido, name="listar_detalle_pedido"),
    url(r'^detalle_pedido/editar_detalle_pedido/(?P<pk>\d+)/$', editarDetallePedido, name= "editar_detalle_pedido"),
    url(r'^detalle_pedido/eliminar_detalle_pedido/(?P<pk>\d+)/$', eliminarDetallePedido, name= "eliminar_detalle_pedido"),

    url(r'^cardex_caja/crear_cardex_caja/', crearCardexCaja, name='crear_cardex_caja'),
    url(r'^cardex_caja/listar_cardex_caja/', listarCardexCaja, name="listar_cardex_caja"),
    url(r'^cardex_caja/editar_cardex_caja/(?P<pk>\d+)/$', editarCardexCaja, name= "editar_cardex_caja"),
    url(r'^cardex_caja/eliminar_cardex_caja/(?P<pk>\d+)/$', eliminarCardexCaja, name= "eliminar_cardex_caja"),

    url(r'^usuario/usuario', listarUsuario, name='listar_usuario'),

    url(r'^totales/crear_totales/', crearTotales, name='crear_totales'),
    url(r'^totales/listar_totales/', listarTotales, name="listar_totales"),
    url(r'^totales/editar_totales/(?P<pk>\d+)/$', editarTotales, name= "editar_totales"),
    url(r'^totales/eliminar_totales/(?P<pk>\d+)/$', eliminarTotales, name= "eliminar_totales"),
]