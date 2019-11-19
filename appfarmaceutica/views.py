from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import (render, redirect, get_object_or_404)

from appfarmaceutica.models import (
    Usuario, Cliente, Ciudad, TipoProducto, Sucursal, 
    Producto, TrasladoProducto, DetalleTrasladoProducto, 
    TipoActivoFijo, ActivoFijo, Documento, Caja, Pedido,
    DetallePedido, CardexCaja, Totales, DominioUsuario
    ) 
from appfarmaceutica.forms import (
    ClienteForm, CiudadForm, TipoProductoForm, SucursalForm, 
    ProductoForm, TrasladoProductoForm, DetalleTrasladoProductoForm,
    TipoActivoFijoForm, ActivoFijoForm, DocumentoForm, CajaForm, 
    PedidoForm, DetallePedidoForm, CardexCajaForm, TotalesForm

    )

#login
def auth_login(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if action == 'signup':
            user = User.objects.create_user(username=username, password=password)
            user.save()
        elif action == 'login':
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('appfarmaceutica:crear_pedido')
    context = {}
    return render(request, 'page-login.html', context)


def home(request):
    return render(request,'index.html')

#crud Cliente
@login_required

def crearCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('appfarmaceutica:crear_cliente')
    else:
        form = ClienteForm()
    return render(request, 'cliente/crear_cliente.html', {'form':form})


@login_required
def listarCliente (request, pk):

    sucursal=DominioUsuario.objects.filter(User=pk).values_list("Sucursal")
    
    
    print (sucursal)
    for  dato in sucursal:
        print(dato)

        for lista in dato:
            sucursal_usuario=lista
        
    print(sucursal_usuario)    
    

    cliente = Cliente.objects.filter(Sucursal=sucursal_usuario)
    

    context = {
        'cliente' : cliente

    }
    return render(request,'cliente/listar_cliente.html', context)

@login_required
def editarCliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == 'GET':
        form = ClienteForm(instance = cliente)
    else:
        form = ClienteForm(request.POST, instance = cliente)
        if form.is_valid():
            form.save()
        return redirect('appfarmaceutica:crear_cliente')
    return render(request,'cliente/editar_cliente.html', {'form':form})

@login_required
def eliminarCliente(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('appfarmaceutica:crear_cliente')
    return render(request, 'cliente/eliminar_cliente.html', {'cliente':cliente})

#crud CIUDAD
@login_required
def crearCiudad(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appfarmaceutica:listar_ciudad')
    else:
        form = CiudadForm()
    return render(request, 'ciudad/crear_ciudad.html', {'form':form})

@login_required
def listarCiudad (request):
    ciudad = Ciudad.objects.all()
    context = {
        'ciudad' : ciudad
    }
    return render(request,'ciudad/listar_ciudad.html', context)

@login_required
def editarCiudad(request, pk):
    ciudad = Ciudad.objects.get(pk=pk)
    if request.method == 'GET':
        form = CiudadForm(instance = ciudad)
    else:
        form = CiudadForm(request.POST, instance = ciudad)
        if form.is_valid():
            form.save()
        return redirect('appfarmaceutica:listar_ciudad')
    return render(request,'ciudad/editar_ciudad.html', {'form':form})

@login_required
def eliminarCiudad(request, pk):
    ciudad = Ciudad.objects.get(pk=pk)
    if request.method == 'POST':
        ciudad.delete()
        return redirect('appfarmaceutica:listar_ciudad')
    return render(request, 'ciudad/eliminar_ciudad.html', {'ciudad':ciudad})

#crud TipoProducto
@login_required
def crearTipoProducto(request):
    if request.method == 'POST':
        form = TipoProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appfarmaceutica:listar_tipo_producto')
    else:
        form = TipoProductoForm()
    return render(request, 'tipo_producto/crear_tipo_producto.html', {'form':form})

@login_required
def listarTipoProducto (request):
    tipo_producto = TipoProducto.objects.all()
    context = {
        'tipo_producto' : tipo_producto
    }
    return render(request,'tipo_producto/listar_tipo_producto.html', context)

@login_required
def editarTipoProducto(request, pk):
    tipo_producto = TipoProducto.objects.get(pk=pk)
    if request.method == 'GET':
        form = TipoProductoForm(instance = tipo_producto)
    else:
        form = TipoProductoForm(request.POST, instance = tipo_producto)
        if form.is_valid():
            form.save()
        return redirect('appfarmaceutica:listar_tipo_producto')
    return render(request,'tipo_producto/editar_tipo_producto.html', {'form':form})

@login_required
def eliminarTipoProducto(request, pk):
    tipo_producto = TipoProducto.objects.get(pk=pk)
    if request.method == 'POST':
        tipo_producto.delete()
        return redirect('appfarmaceutica:listar_tipo_producto')
    return render(request, 'tipo_producto/eliminar_tipo_producto.html', {'tipo_producto':tipo_producto})


#crud Sucursal
@login_required
def crearSucursal(request):
    if request.method == 'POST':
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appfarmaceutica:listar_sucursal')
    else:
        form = SucursalForm()
    return render(request, 'sucursal/crear_sucursal.html', {'form':form})

@login_required
def listarSucursal (request):
    sucursal = Sucursal.objects.all()
    context = {
        'sucursal' : sucursal
    }
    return render(request,'sucursal/listar_sucursal.html', context)

@login_required
def editarSucursal(request, pk):
    sucursal = Sucursal.objects.get(pk=pk)
    if request.method == 'GET':
        form = SucursalForm(instance = sucursal)
    else:
        form = SucursalForm(request.POST, instance = sucursal)
        if form.is_valid():
            form.save()
        return redirect('appfarmaceutica:listar_sucursal')
    return render(request,'sucursal/editar_sucursal.html', {'form':form})

@login_required
def eliminarSucursal(request, pk):
    sucursal = Sucursal.objects.get(pk=pk)
    if request.method == 'POST':
        sucursal.delete()
        return redirect('appfarmaceutica:listar_sucursal')
    return render(request, 'sucursal/eliminar_sucursal.html', {'sucursal':sucursal})

#crud Producto
@login_required
def crearProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appfarmaceutica:crear_producto')
    else:
        form = ProductoForm()
    return render(request, 'producto/crear_producto.html', {'form':form})

@login_required
def listarProducto (request, pk):
    
    
    sucursal=DominioUsuario.objects.filter(User=pk).values_list("Sucursal")
    
    
    print (sucursal)
    for  dato in sucursal:
        print(dato)

        for lista in dato:
            sucursal_usuario=lista
        
    print(sucursal_usuario)    
    

    producto = Producto.objects.filter(Sucursal_id=sucursal_usuario)
    context = {
        'producto' : producto,   
        'sucursal': sucursal
    }
    return render(request,'producto/listar_producto.html', context)

@login_required
def editarProducto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'GET':
        form = ProductoForm(instance = producto)
    else:
        form = ProductoForm(request.POST, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('appfarmaceutica:crear_producto')
    return render(request,'producto/editar_producto.html', {'form':form})

@login_required
def eliminarProducto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('appfarmaceutica:crear_producto')
    return render(request, 'producto/eliminar_producto.html', {'producto':producto})

#crud Traslado de producto
@login_required
def crearTrasladoProducto(request):
    if request.method == 'POST':
        form = TrasladoProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appfarmaceutica:listar_traslado_producto')
    else:
        form = TrasladoProductoForm()
    return render(request, 'traslado_producto/crear_traslado_producto.html', {'form':form})

@login_required
def listarTrasladoProducto (request, pk):
    sucursal=DominioUsuario.objects.filter(User=pk).values_list("Sucursal")
    
    
    print (sucursal)
    for  dato in sucursal:
        print(dato)

        for lista in dato:
            sucursal_usuario=lista
        
    print(sucursal_usuario)    
    

    traslado_producto = TrasladoProducto.objects.filter(id=sucursal_usuario)
    
    context = {
        'traslado_producto' : traslado_producto
    }
    return render(request,'traslado_producto/listar_traslado_producto.html', context)

@login_required
def editarTrasladoProducto(request, pk):
    traslado_producto = TrasladoProducto.objects.get(pk=pk)
    if request.method == 'GET':
        form = TrasladoProductoForm(instance = traslado_producto)
    else:
        form = TrasladoProductoForm(request.POST, instance = traslado_producto)
        if form.is_valid():
            form.save()
        return redirect('appfarmaceutica:listar_traslado_producto')
    return render(request,'traslado_producto/editar_traslado_producto.html', {'form':form})

@login_required
def eliminarTrasladoProducto(request, pk):
    traslado_producto = TrasladoProducto.objects.get(pk=pk)
    if request.method == 'POST':
        traslado_producto.delete()
        return redirect('appfarmaceutica:listar_traslado_producto')
    return render(request, 'traslado_producto/eliminar_traslado_producto.html', {'traslado_producto':traslado_producto})

#crud Detalle de Traslado de Producto
@login_required
def crearDetalleTrasladoProducto(request):
    if request.method == 'POST':
        form = DetalleTrasladoProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appfarmaceutica:crear_detalle_traslado_producto')
    else:
        form = DetalleTrasladoProductoForm()
    return render(request, 'detalle_traslado_producto/crear_detalle_traslado_producto.html', {'form':form})

@login_required
def listarDetalleTrasladoProducto (request, TrasladoProducto):
    detalle_traslado_producto = DetalleTrasladoProducto.objects.filter(TrasladoProducto=TrasladoProducto)
    print(detalle_traslado_producto)
    
    context = {
        'detalle_traslado_producto' : detalle_traslado_producto,
    }
    return render(request,'detalle_traslado_producto/listar_detalle_traslado_producto.html', context)

@login_required
def editarDetalleTrasladoProducto(request, pk):
    detalle_traslado_producto = DetalleTrasladoProducto.objects.get(pk=pk)
    if request.method == 'GET':
        form = DetalleTrasladoProductoForm(instance = detalle_traslado_producto)
    else:
        form = DetalleTrasladoProductoForm(request.POST, instance = detalle_traslado_producto)
        if form.is_valid():
            form.save()
        return redirect('appfarmaceutica:crear_detalle_traslado_producto')
    return render(request,'detalle_traslado_producto/editar_detalle_traslado_producto.html', {'form':form})

@login_required
def eliminarDetalleTrasladoProducto(request, pk):
    detalle_traslado_producto = DetalleTrasladoProducto.objects.get(pk=pk)
    if request.method == 'POST':
        detalle_traslado_producto.delete()
        return redirect('appfarmaceutica:crear_detalle_traslado_producto')
    return render(request, 'detalle_traslado_producto/eliminar_detalle_traslado_producto.html', {'detalle_traslado_producto':detalle_traslado_producto})

#crud Tipo de Activo Fijo
@login_required
def crearTipoActivoFijo(request):
    if request.method == 'POST':
        form = TipoActivoFijoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appfarmaceutica:listar_tipo_activo_fijo')
    else:
        form = TipoActivoFijoForm()
    return render(request, 'tipo_activo_fijo/crear_tipo_activo_fijo.html', {'form':form})

@login_required
def listarTipoActivoFijo (request):
    
    tipo_activo_fijo = TipoActivoFijo.objects.all()
    context = {
        'tipo_activo_fijo' : tipo_activo_fijo
    }
    return render(request,'tipo_activo_fijo/listar_tipo_activo_fijo.html', context)

@login_required
def editarTipoActivoFijo(request, pk):
    tipo_activo_fijo = TipoActivoFijo.objects.get(pk=pk)
    if request.method == 'GET':
        form = TipoActivoFijoForm(instance = tipo_activo_fijo)
    else:
        form = TipoActivoFijoForm(request.POST, instance = tipo_activo_fijo)
        if form.is_valid():
            form.save()
        return redirect('appfarmaceutica:crear_tipo_activo_fijo')
    return render(request,'tipo_activo_fijo/editar_tipo_activo_fijo.html', {'form':form})

@login_required
def eliminarTipoActivoFijo(request, pk):
    tipo_activo_fijo = TipoActivoFijo.objects.get(pk=pk)
    if request.method == 'POST':
        tipo_activo_fijo.delete()
        return redirect('appfarmaceutica:listar_tipo_activo_fijo')
    return render(request, 'tipo_activo_fijo/eliminar_tipo_activo_fijo.html', {'tipo_activo_fijo':tipo_activo_fijo})

#crud Activo Fijo
@login_required
def crearActivoFijo(request):
    if request.method == 'POST':
        form = ActivoFijoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appfarmaceutica:crear_activo_fijo')
    else:
        form = ActivoFijoForm()
    return render(request, 'activo_fijo/crear_activo_fijo.html', {'form':form})

@login_required
def listarActivoFijo (request, pk):
    sucursal=DominioUsuario.objects.filter(User=pk).values_list("Sucursal")
    
    
    print (sucursal)
    for  dato in sucursal:
        print(dato)

        for lista in dato:
            sucursal_usuario=lista
        
    print(sucursal_usuario)    
    

    activo_fijo = ActivoFijo.objects.filter(Sucursal=sucursal_usuario)
    
    context = {
        'activo_fijo' : activo_fijo
    }
    return render(request,'activo_fijo/listar_activo_fijo.html', context)

@login_required
def editarActivoFijo(request, pk):
    activo_fijo = ActivoFijo.objects.get(pk=pk)
    if request.method == 'GET':
        form = ActivoFijoForm(instance = activo_fijo)
    else:
        form = ActivoFijoForm(request.POST, instance = activo_fijo)
        if form.is_valid():
            form.save()
        return redirect('appfarmaceutica:crear_activo_fijo')
    return render(request,'activo_fijo/editar_activo_fijo.html', {'form':form})

@login_required
def eliminarActivoFijo(request, pk):
    activo_fijo = ActivoFijo.objects.get(pk=pk)
    if request.method == 'POST':
        activo_fijo.delete()
        return redirect('appfarmaceutica:crear_activo_fijo')
    return render(request, 'activo_fijo/eliminar_activo_fijo.html', {'activo_fijo':activo_fijo})

#crud Documento
@login_required
def crearDocumento(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appfarmaceutica:listar_documento')
    else:
        form = DocumentoForm()
    return render(request, 'documento/crear_documento.html', {'form':form})

@login_required
def listarDocumento (request):
    documento = Documento.objects.all()
    context = {
        'documento' : documento
    }
    return render(request,'documento/listar_documento.html', context)

@login_required
def editarDocumento(request, pk):
    documento = Documento.objects.get(pk=pk)
    if request.method == 'GET':
        form = DocumentoForm(instance = documento)
    else:
        form = DocumentoForm(request.POST, instance = documento)
        if form.is_valid():
            form.save()
        return redirect('appfarmaceutica:listar_documento')
    return render(request,'documento/editar_documento.html', {'form':form})

@login_required
def eliminarDocumento(request, pk):
    documento = Documento.objects.get(pk=pk)
    if request.method == 'POST':
        documento.delete()
        return redirect('appfarmaceutica:listar_documento')
    return render(request, 'documento/eliminar_documento.html', {'documento':documento})

#crud Caja
@login_required
def crearCaja(request):
    if request.method == 'POST':
        form = CajaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appfarmaceutica:crear_caja')
    else:
        form = CajaForm()
    return render(request, 'caja/crear_caja.html', {'form':form})

@login_required
def listarCaja (request, pk):
    sucursal=DominioUsuario.objects.filter(User=pk).values_list("Sucursal")
    
    
    print (sucursal)
    for  dato in sucursal:
        print(dato)

        for lista in dato:
            sucursal_usuario=lista
        
    print(sucursal_usuario)    
    

    caja = Caja.objects.filter(Sucursal=sucursal_usuario)
    
    context = {
        'caja' : caja
    }
    return render(request,'caja/listar_caja.html', context)

@login_required
def editarCaja(request, pk):
    caja = Caja.objects.get(pk=pk)
    if request.method == 'GET':
        form = CajaForm(instance = caja)
    else:
        form = CajaForm(request.POST, instance = caja)
        if form.is_valid():
            form.save()
        return redirect('appfarmaceutica:crear_caja')
    return render(request,'caja/editar_caja.html', {'form':form})

@login_required
def eliminarCaja(request, pk):
    caja = Caja.objects.get(pk=pk)
    if request.method == 'POST':
        caja.delete()
        return redirect('appfarmaceutica:crear_caja')
    return render(request, 'caja/eliminar_caja.html', {'caja':caja})

#curd Pedido
@login_required
def crearPedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appfarmaceutica:crear_detalle_pedido')
    else:
        form = PedidoForm()
    return render(request, 'pedido/crear_pedido.html', {'form':form})

@login_required
def listarPedido (request, pk):
    sucursal=DominioUsuario.objects.filter(User=pk).values_list("Sucursal")
    
    
    print (sucursal)
    for  dato in sucursal:
        print(dato)

        for lista in dato:
            sucursal_usuario=lista
        
    print(sucursal_usuario)    
    

    pedido = Pedido.objects.filter(Sucursal=sucursal_usuario)
    
    context = {
        'pedido' : pedido
    }
    return render(request,'pedido/listar_pedido.html', context)

@login_required
def editarPedido(request, pk):
    pedido = Pedido.objects.get(pk=pk)
    if request.method == 'GET':
        form = PedidoForm(instance = pedido)
    else:
        form = PedidoForm(request.POST, instance = pedido)
        if form.is_valid():
            form.save()
        return redirect('appfarmaceutica:crear_pedido')
    return render(request,'pedido/editar_pedido.html', {'form':form})

@login_required
def eliminarPedido(request, pk):
    pedido = Pedido.objects.get(pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('appfarmaceutica:crear_pedido')
    return render(request, 'pedido/eliminar_pedido.html', {'pedido':pedido})

#crud Detalle Pedido
@login_required
def crearDetallePedido(request):
    if request.method == 'POST':
        form = DetallePedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appfarmaceutica:crear_detalle_pedido')
    else:
        form = DetallePedidoForm()
    return render(request, 'detalle_pedido/crear_detalle_pedido.html', {'form':form})

@login_required
def listarDetallePedido (request, Pedido):
    detalle_pedido = DetallePedido.objects.filter(Pedido=Pedido)
    context = {
        'detalle_pedido' : detalle_pedido
    }
    return render(request,'detalle_pedido/listar_detalle_pedido.html', context)

@login_required
def editarDetallePedido(request, pk):
    detalle_pedido = DetallePedido.objects.get(pk=pk)
    if request.method == 'GET':
        form = DetallePedidoForm(instance = detalle_pedido)
    else:
        form = DetallePedidoForm(request.POST, instance = detalle_pedido)
        if form.is_valid():
            form.save()
        return redirect('appfarmaceutica:listard_pedido')
    return render(request,'detalle_pedido/editar_detalle_pedido.html', {'form':form})

@login_required
def eliminarDetallePedido(request, pk):
    detalle_pedido = DetallePedido.objects.get(pk=pk)
    if request.method == 'POST':
        detalle_pedido.delete()
        return redirect('appfarmaceutica:listar_pedido')
    return render(request, 'detalle_pedido/eliminar_detalle_pedido.html', {'detalle_pedido':detalle_pedido})

#crud Cardex Caja
@login_required
def crearCardexCaja(request):
    if request.method == 'POST':
        form = CardexCajaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appfarmaceutica:listar_cardex_caja')
    else:
        form = CardexCajaForm()
    return render(request, 'cardex_caja/crear_cardex_caja.html', {'form':form})

@login_required
def listarCardexCaja (request):
    cardex_caja = CardexCaja.objects.all()
    context = {
        'cardex_caja' : cardex_caja
    }
    return render(request,'cardex_caja/listar_cardex_caja.html', context)

@login_required
def editarCardexCaja(request, pk):
    cardex_caja = CardexCaja.objects.get(pk=pk)
    if request.method == 'GET':
        form = CardexCajaForm(instance = cardex_caja)
    else:
        form = CardexCajaForm(request.POST, instance = cardex_caja)
        if form.is_valid():
            form.save()
        return redirect('appfarmaceutica:listar_cardex_caja')
    return render(request,'cardex_caja/editar_cardex_caja.html', {'form':form})

@login_required
def eliminarCardexCaja(request, pk):
    cardex_caja = CardexCaja.objects.get(pk=pk)
    if request.method == 'POST':
        cardex_caja.delete()
        return redirect('appfarmaceutica:listar_cardex_caja')
    return render(request, 'cardex_caja/eliminar_cardex_caja.html', {'cardex_caja':cardex_caja})

#Usuario
@login_required
def listarUsuario(request):
    usuario = User.objects.all()
    context = {
        'usuario' : usuario
    }
    return render(request,'plantilla.html', context)

#crud Totales
@login_required
def crearTotales(request):
    if request.method == 'POST':
        form = TotalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appfarmaceutica:listar_totales')
    else:
        form = TotalesForm()
    return render(request, 'totales/crear_totales.html', {'form':form})

@login_required
def listarTotales (request):
    totales = Totales.objects.all()
    context = {
        'totales' : totales
    }
    return render(request,'totales/listar_totales.html', context)

@login_required
def editarTotales(request, pk):
    totales = Totales.objects.get(pk=pk)
    if request.method == 'GET':
        form = TotalesForm(instance = totales)
    else:
        form = TotalesForm(request.POST, instance = totales)
        if form.is_valid():
            form.save()
        return redirect('appfarmaceutica:listar_totales')
    return render(request,'totales/editar_totales.html', {'form':form})

@login_required
def eliminarTotales(request, pk):
    totales = Totales.objects.get(pk=pk)
    if request.method == 'POST':
        totales.delete()
        return redirect('appfarmaceutica:listar_totales')
    return render(request, 'totales/eliminar_totales.html', {'totales':totales})