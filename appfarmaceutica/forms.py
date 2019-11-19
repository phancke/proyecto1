from django import forms 
from .models import (
    Cliente, 
    Ciudad, 
    TipoProducto, 
    Sucursal, 
    Producto,
    TrasladoProducto,
    DetalleTrasladoProducto,
    TipoActivoFijo,
    ActivoFijo,
    Documento,
    Caja,
    Pedido,
    DetallePedido,
    CardexCaja,
    User,
    Totales
    )

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = [
            'nombre_cliente', 
            'apellido_cliente', 
            'direccion_cliente', 
            'telefono_cliente', 
            'email_cliente', 
            'nit_cliente',
            'Sucursal',
            ]

class CiudadForm(forms.ModelForm):
    
    class Meta:
        model = Ciudad
        fields = (
            "nombre_ciudad",
            )

class TipoProductoForm(forms.ModelForm):
    
    class Meta:
        model = TipoProducto     
        fields = (
            "descripcion_tipo_producto",
            )

class SucursalForm(forms.ModelForm):
    
    class Meta:
        model = Sucursal
        fields = (
            'nombre_sucursal',
            'Ciudad', 
            'direccion_sucursal', 
            'telefono_sucursal', 
            'estado_sucursal',
            'User', 
            )
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = (
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
            'User', 
            )

class TrasladoProductoForm(forms.ModelForm):
    
    class Meta:
        model = TrasladoProducto
        fields = (
            'Sucursal',
            'fecha_traslado',
            'User', 
            )

class DetalleTrasladoProductoForm(forms.ModelForm):
    
    class Meta:
        model = DetalleTrasladoProducto
        fields = ( 
            'TrasladoProducto', 
            'Producto',
            'cantidad_detalle_traslado_producto',
            )

class TipoActivoFijoForm(forms.ModelForm):
    
    class Meta:
        model = TipoActivoFijo
        fields = (
            'descripcion_tipo_activo_fijo',
            )

class ActivoFijoForm(forms.ModelForm):
    
    class Meta:
        model = ActivoFijo
        fields = (
            'Sucursal', 
            'nombre_activo_fijo', 
            'TipoActivoFijo', 
            'codigo_activo_fijo', 
            'costo_activo_fijo', 
            'cantidad_activo_fijo',
            )

class DocumentoForm(forms.ModelForm):
    
    class Meta:
        model = Documento
        fields = (
            'tipo_documento',
            )

class CajaForm(forms.ModelForm):
    
    class Meta:
        model = Caja
        fields = (
            'Sucursal', 
            'descripcion_caja', 
            'saldo_caja', 
            'Documento',
            )

class PedidoForm(forms.ModelForm):
    
    class Meta:
        model = Pedido
        fields = (
            'Sucursal', 
            'Caja', 
            'numero_pedido',  
            'Cliente',  
            'total_pedido', 
            'Documento',
            'User', 
            )

class DetallePedidoForm(forms.ModelForm):
    
    class Meta:
        model = DetallePedido
        fields = (
            'Pedido',
            'Producto',
            'cantidad', 
            'precio_producto', 
            'total_pedido',             
            )

class CardexCajaForm(forms.ModelForm):
    
    class Meta:
        model = CardexCaja
        fields = ( 
            'Pedido', 
            'Caja', 
            'numero_pedido', 
            'monto',
            )

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = (
            "id", 
            "username", 
            "password",
            )


class TotalesForm(forms.ModelForm):
    
    class Meta:
        model = Totales
        fields = (
            'id',
            'codigo',
            'nombre',
            'numero_factura',
            'total',
        )