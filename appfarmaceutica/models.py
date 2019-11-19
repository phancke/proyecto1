from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario (models.Model):
    nombre_usuario = models.CharField(max_length=100, null=True)
    apellido_usuario = models.CharField(max_length=100,null=True)
    telefono_usuario = models.IntegerField(null=True)
    username = models.CharField(unique =True, max_length=100, null=True)
    password = models.CharField(max_length=50, null=True)
    estadoProfile = models.BooleanField(default = True)

    def __str__(self):
        return self.nombre_usuario



class Ciudad (models.Model):
    nombre_ciudad = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nombre_ciudad


class TipoProducto (models.Model):
    descripcion_tipo_producto = models.CharField(max_length=100, null=True)

    def __str__ (self):
        return self.descripcion_tipo_producto




class Sucursal (models.Model):
    nombre_sucursal = models.CharField(max_length=100, null=True)
    direccion_sucursal = models.CharField(max_length=100, null=True)
    telefono_sucursal = models.IntegerField(null=True)
    estado_sucursal = models.BooleanField(default = True, null=True)
    Ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, null= True)
    User = models.ForeignKey('auth.User', related_name='sucursal', on_delete=models.CASCADE, null=True)
    #idUsuario

    def __str__(self):
        return str(self.nombre_sucursal)

class Cliente (models.Model):
    nombre_cliente = models.CharField(max_length=100, null=True)
    apellido_cliente = models.CharField(max_length=100, null=True)
    direccion_cliente = models.CharField(max_length=100, null=True)
    telefono_cliente = models.IntegerField(null=True)
    email_cliente = models.EmailField(max_length = 125)
    nit_cliente = models.CharField(max_length=100, null=True)
    Sucursal = models.ForeignKey(Sucursal, blank=True, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return self.nombre_cliente


class DominioUsuario (models.Model):
    User = models.ForeignKey('auth.User',on_delete=models.CASCADE, null=True)
    Sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return str(self.id)
    
class Producto (models.Model):
    nombre_producto = models.CharField(max_length=225, null=True)
    codigo_producto = models.IntegerField(null=True)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    costo_producto = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    cantidad_producto = models.IntegerField(null=True)
    estado_producto = models.BooleanField(default=True, null=True)
    fecha_creado = models.DateField(auto_now_add=True, null=True)
    fecha_modificado = models.DateField(blank=True, null=True)
    fecha_eliminado = models.DateField(blank=True, null=True)
    Sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null= True)
    TipoProducto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE, null= True)
    User = models.ForeignKey('auth.User', related_name='producto', on_delete=models.CASCADE, null=True)
    #idUsuario

    def __str__ (self):
        return self.nombre_producto
        
    
class TrasladoProducto (models.Model):
    fecha_traslado = models.DateField(null=True)
    fecha_creado_traslado = models.DateField(auto_now_add=True, null=True)
    Sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null= True)
    User = models.ForeignKey('auth.User', related_name='trasladoproducto', on_delete=models.CASCADE, null=True)
    #idUsuario

    def __str__(self):
        return str(self.id)

    def usuario(self, username):
        User.objects.get(username='username')
        self.username

class DetalleTrasladoProducto(models.Model):
    cantidad_detalle_traslado_producto = models.IntegerField(null=True)
    TrasladoProducto = models.ForeignKey(TrasladoProducto, on_delete=models.CASCADE, null=True)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.cantidad_detalle_traslado_producto)

class TipoActivoFijo(models.Model):
    descripcion_tipo_activo_fijo = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.descripcion_tipo_activo_fijo

class ActivoFijo(models.Model):
    nombre_activo_fijo = models.CharField(max_length=100, null=True)
    codigo_activo_fijo = models.IntegerField(null=True)
    costo_activo_fijo = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    cantidad_activo_fijo = models.IntegerField(null=True)
    Sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null= True)
    TipoActivoFijo = models.ForeignKey(TipoActivoFijo, on_delete=models.CASCADE, null=True)


class Documento (models.Model):
    tipo_documento = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.tipo_documento


class Caja (models.Model):
    descripcion_caja = models.CharField(max_length=100, null=True)
    saldo_caja = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fecha_creado_caja = models.DateField(auto_now_add=True, null=True)
    Sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null= True)
    Documento = models.ForeignKey(Documento, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return self.descripcion_caja

class Pedido (models.Model):
    fecha_creado_pedido = models.DateField(auto_now_add=True, null=True)
    total_pedido = models.DecimalField(max_digits=10, blank=True, decimal_places=2, null=True)
    numero_pedido = models.IntegerField(null=True)
    Sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null= True)
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null= True)
    Caja = models.ForeignKey(Caja, on_delete=models.CASCADE, null= True)
    Documento = models.ForeignKey(Documento, on_delete=models.CASCADE, null= True)
    User = models.ForeignKey('auth.User', related_name='pedido', on_delete=models.CASCADE, null=True)
    
    #idUsuario

    def __str__(self):
        return str(self.numero_pedido)


class DetallePedido (models.Model):
    cantidad = models.IntegerField(null=True)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null= True)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return str(self.cantidad)



class CardexCaja (models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    numero_pedido = models.IntegerField(null=True)
    fecha_creado_cardex_caja = models.DateField(auto_now_add=True, null=True)
    Pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null= True)
    Caja = models.ForeignKey(Caja, on_delete=models.CASCADE, null= True)

    def __str__(self):
        return str(self.fecha_creado_cardex_caja)
    

class Totales(models.Model):

    codigo = models.IntegerField(null=True)
    nombre = models.CharField(max_length=100, null=True)
    numero_factura = models.IntegerField(unique=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.name

  