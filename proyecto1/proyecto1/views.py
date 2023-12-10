from django.http import HttpResponse
import datetime
import tensorflow as tf
from django.template import Template, Context
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
from django.template import loader
from django.shortcuts import render
import os

def hacerPrediccion():
    new_model = keras.models.load_model('C:/Users/ricar/Downloads/Practica5/ModeloFinal.h5')
    print("modeloCargado")
    filename='C:/Users/ricar/Desktop/Django/proyecto1/proyecto1/static/imagenes/predecir2.jpg'

    img1 = image.load_img(filename,target_size=(150,150))
    Y = image.img_to_array(img1)
    
    X = np.expand_dims(Y,axis=0)
    val = new_model.predict(X)

    return val

def guardar_imagen(imagen):
    # Aquí puedes guardar la imagen en el lugar que desees
    # Por ejemplo, puedes guardarla en la carpeta de medios (media) de Django
    with open('C:/Users/ricar/Desktop/Django/proyecto1/proyecto1/static/imagenes/predecir2.jpg', 'wb') as archivo:
        for chunk in imagen.chunks():
            archivo.write(chunk)

def prediccion(request):

    if request.method=="POST":


        subject=request.POST["path"]
        img=request.FILES["pathLink"]
        guardar_imagen(img)

        resultado=0
        resultado=hacerPrediccion()
        
        
        


        return render(request, "prediccion.html",{"link":subject,"resultado":resultado})
    else:
        subject="hola2"


  #  path2=request.post["path"]
    return render(request, "prediccion.html")

def subir(request):

    return render(request, "subir.html",)
    


def saludo(request): # primera vista
    nombre="juan"

    return render(request, "pagina.html",{"nombre":nombre})





def fecha(request):
    return render(request, "principal.html")

def calcula(request, edad,ano):
    periodo = ano - 2023
    nueva=edad+periodo
    documento="""
                        <html>
                            <body> 
                                <h2>
                                  en el año %s tendras %s
                                </h2> 
                            </body>
                        </html>"""  % (ano,nueva) 
    return HttpResponse(documento) 