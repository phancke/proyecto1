from django.contrib import admin
from appfarmaceutica.models import (Usuario, Cliente, Ciudad, TipoProducto, 
                                Sucursal, Producto, TrasladoProducto, 
                                DetalleTrasladoProducto, TipoActivoFijo, 
                                ActivoFijo, Documento, Caja, Pedido, 
                                DetallePedido, CardexCaja, Totales, DominioUsuario
                                )

# Register your models here.
@admin.register(Usuario)
class AdminUsuario (admin.ModelAdmin):
    list_display = ('id', 'nombre_usuario', 'apellido_usuario', 'telefono_usuario', 'username', 'password', 'estadoProfile',)
    list_filter = ('nombre_usuario', )

@admin.register(Cliente)
class AdminCliente (admin.ModelAdmin):
    list_display = (
        'id', 
        'nombre_cliente', 
        'apellido_cliente', 
        'direccion_cliente', 
        'telefono_cliente', 
        'email_cliente', 
        'nit_cliente',
        'Sucursal',
        )
    list_filter = ('nombre_cliente',)
       
@admin.register(Ciudad)
class AdminCiudad (admin.ModelAdmin):
    list_display = (
        'id', 
        'nombre_ciudad',
        )
    list_filter = ('nombre_ciudad',)

@admin.register(TipoProducto)
class AdminTipoProducto (admin.ModelAdmin):
    list_display = (
        'id', 
        'descripcion_tipo_producto',
        )
    list_filter = ('descripcion_tipo_producto', )

@admin.register(Sucursal)
class AdminSucursal (admin.ModelAdmin):
    list_display = (
        'id', 
        'nombre_sucursal',
        'Ciudad', 
        'direccion_sucursal', 
        'telefono_sucursal', 
        'estado_sucursal', 
        )
    list_filter = ('nombre_sucursal', )

@admin.register(Producto)
class AdminProducto (admin.ModelAdmin):
    list_display = (
        'id', 
        'fecha_creado',
        'Sucursal', 
        'nombre_producto', 
        'codigo_producto',
        'TipoProducto', 
        'precio_producto', 
        'costo_producto', 
        'cantidad_producto', 
        'estado_producto', 
        'fecha_modificado', 
        'fecha_eliminado',  
        )
    list_filter = ('nombre_producto', )

@admin.register(TrasladoProducto)
class AdminTrasladoProducto (admin.ModelAdmin):
    list_display = (
        'id',
        'fecha_creado_traslado',
        'Sucursal',
        'fecha_traslado', 
        )
    list_filter = ('fecha_traslado',)

@admin.register(DetalleTrasladoProducto)
class AdminDetalleTrasladoProducto(admin.ModelAdmin):
    list_display = (
        'id',
        'TrasladoProducto',  
        'Producto',
        'cantidad_detalle_traslado_producto', 
        )
    list_filter = ('cantidad_detalle_traslado_producto', )

@admin.register(TipoActivoFijo)
class AdminTipoActivoFijo(admin.ModelAdmin):
    list_display = (
        'id', 
        'descripcion_tipo_activo_fijo',
        )
    list_filter = ('descripcion_tipo_activo_fijo', )

@admin.register(ActivoFijo)
class AdminActivoFijo(admin.ModelAdmin):
    list_display = (
        'id',
        'Sucursal', 
        'nombre_activo_fijo', 
        'TipoActivoFijo', 
        'codigo_activo_fijo', 
        'costo_activo_fijo', 
        'cantidad_activo_fijo', 
        )
    list_filter = ('nombre_activo_fijo',)

@admin.register(Documento)
class AdminDocumento(admin.ModelAdmin):
    list_display = (
        'id', 
        'tipo_documento', 
        )
    list_filter = ('tipo_documento',)

@admin.register(Caja)
class AdminCaja (admin.ModelAdmin):
    list_display = (
        'id', 
        'fecha_creado_caja', 
        'Sucursal', 
        'descripcion_caja', 
        'saldo_caja', 
        'Documento', 
        )
    list_filter = ('descripcion_caja',)

@admin.register(Pedido)
class AdminPedido (admin.ModelAdmin):
    list_display = (
        'id',
        'fecha_creado_pedido', 
        'Sucursal', 
        'Caja', 
        'numero_pedido',  
        'Cliente',  
        'total_pedido', 
        'Documento', 
        )
    list_filter = ('fecha_creado_pedido',  )

@admin.register(DetallePedido)
class AdminDetallePedido(admin.ModelAdmin):
    list_display = (
        'id',
        'Pedido', 
        'Producto', 
        'cantidad', 
        'precio_producto', 
        'total_pedido',  
        )
    list_filter = ('cantidad', )

@admin.register(CardexCaja)
class AdminCardexCaja(admin.ModelAdmin):
    list_display = (
        'id', 
        'fecha_creado_cardex_caja', 
        'Pedido', 
        'Caja', 
        'numero_pedido', 
        'monto', 
        )
    list_filter = ('monto', )


@admin.register(Totales)
class totalesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'codigo',
        'nombre',
        'numero_factura',
        'total',
        )
    list_filter =('nombre',)


@admin.register(DominioUsuario)
class DominoUsuario(admin.ModelAdmin):
    list_display = (
        'id',
        'User',
        'Sucursal',
    )

    