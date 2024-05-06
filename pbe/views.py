from django.http import HttpResponse

def bienvenida (request):
    return HttpResponse("Bienvenido Lunes 6 de Mayo")

def calcula_edad(request,edad):
    if edad >18:
        categoria="mayor de edad"
    else:
        categoria="Menor de edad"
    #result="<h1> Usted es %s <h1/>" %categoria
    result=f"<h1> Usted es {categoria} <h1/>"

    return HttpResponse(result)

def situacion (request,edad2,edad3):
    if edad2>0 and edad3>0:
        estado="Ambos son positivos"
    else:
        estado="Son negativos"
    #result="<h1> Usted es %s <h1/>" %categoria
    result=f"<h1> Estado: {estado} <h1/>"

    return HttpResponse(result)

def maneja (request,maneja1):
    if maneja1 <17:
        m_estado="No puede manejar"

    elif maneja1 ==17:
        m_estado= "Puede manejar con un acompañante con licencia"

    else:
        m_estado="Puede manejar"
    #result="<h1> Usted es %s <h1/>" %categoria
    result=f"<h1>{m_estado} <h1/>"

    return HttpResponse(result)