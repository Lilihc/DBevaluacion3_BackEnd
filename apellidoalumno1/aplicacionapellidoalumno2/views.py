from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse
from .models import Alumno
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json



# Create your views here.

class AlumnoView(View):
    
    #cerar un despachador de la exespcion csrf cross file para poder ejecutar el metodo POST
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,rut=''):
        if (rut!=''):
            alumnos= list(Alumno.objects.filter(rut=rut).values())
           
            if len(alumnos)>0:
                integrante=alumnos[0]
                datos={'messages':"Success",'alumnos':integrante}
            else:
                datos={'message':"Alumno no encotrado"}
            return JsonResponse(datos)
        else:
            alumnos = list(Alumno.objects.values())
            if len(alumnos)>0:
                datos={'messages':"Success",'alumnos':alumnos}
            else:
                datos={'message':"Alumno no encotrado"}
            return JsonResponse(datos)
    
    def post(self,request):
        jd = json.loads(request.body)
        Alumno.objects.create(rut=jd['rut'],nombrecompleto=jd['nombrecompleto'],carrera=jd['carrera'])
        datos={'message':"Success"}
        return JsonResponse(datos)
        
    def put(self,request,rut):
        jd = json.loads(request.body)
        alumnos= list(Alumno.objects.filter(rut=rut).values())
        if len(alumnos)>0:
            integrante = Alumno.objects.get(rut=rut)
            integrante.nombrecompleto = jd['nombrecompleto']
            integrante.carrera = jd['carrera']
            integrante.save()
            datos={'message':"Success"}   
        else:
            datos={'message':"Alumno no existe"}
        return JsonResponse(datos)
        
    def delete(self,request, rut):
        alumnos= list(Alumno.objects.filter(rut=rut).values())
        if len(alumnos)>0:
            Alumno.objects.filter(rut=rut).delete()
            datos={'message':"Success"}   
        else:
            datos={'message':"Alumno no existe"}
        return JsonResponse(datos)
            
        
     #def get(self,request,rut=''):
       # if (rut==''):
          #  alumnos= list(Alumno.objects.filter(rut=rut).values())
           
           # if len(alumnos)>0:
            #    integrante=alumnos[0]
             #   datos={'messages':"Success",'alumnos':integrante}
            #else:
             #   datos={'message':"Alumno no encotrado"}
            #return JsonResponse(datos)
       # else:
        
        #    alumnos = list(Alumno.objects.values())
         #   if len(alumnos)>0:
          #      datos={'messages':"Success",'alumnos':alumnos}
           # else:
            #    datos={'message':"Alumno no encotrado"}
            #return JsonResponse(datos)
    