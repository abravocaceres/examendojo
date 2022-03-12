import json
from django.shortcuts import render, HttpResponse, redirect
from app.models import Usuario
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')


def registro(request):
    print(request.POST)
    
    passencriptado = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()
    usuario = Usuario.objects.filter(email = request.POST["email"])
    if usuario:
        messages.error(request,"Email ya se encuentra registrado")
        return redirect("/")
    if request.POST["password"] != request.POST["password_confirmation"]:
        messages.error(request, "Contraseña debe coincidir")
        return redirect("/")
        
        
    Usuario.objects.create(
        nombre = request.POST["nombre"],
        alias = request.POST["alias"],
        email = request.POST["email"],
        birthday = request.POST["birthday"],
        password = passencriptado,
    )
    messages.success(request,"Ingresado exitosamente")
    return redirect("/")


def login(request):
    
    usuario = Usuario.objects.filter(email = request.POST["email"])
    
    if usuario:
        usuario_log = usuario[0]
        
        if bcrypt.checkpw(request.POST["password"].encode(), usuario_log.password.encode()):
            messages.success(request,"Usuario Correcto") 
            request.session['usuario'] = json.dumps(usuario_log)  
            
            return redirect("/pokes") 
            
        else:
            messages.error(request,"Usuario no es correcto") 
    else:
        messages.error(request,"Usuario no existe")    
       
    return redirect("/")


def pokes(request):
    print ("******************************************") 

    return render(request, '/pokes.html')
