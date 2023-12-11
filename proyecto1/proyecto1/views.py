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
import matplotlib.pyplot as plt
from django.http import HttpResponse
import json
import csv
from django.http import HttpResponse, JsonResponse

def hola(request):
    return JsonResponse({'message': 'Hello, world!'})
   

def grafica_csv(request):
    # Ruta al archivo CSV, reemplázala con la ruta real
    csv_file_path = 'C:/Users/ricar/Desktop/Django/proyecto1/proyecto1/static/codigo/historial_entrenamiento.csv'

    new_model = tf.keras.models.load_model('C:/Users/ricar/Downloads/Practica5/ModeloFinal.h5')

    # Obtener el resumen del modelo
    model_summary = []
    new_model.summary(print_fn=lambda x: model_summary.append(x))
    model_summary = '\n'.join(model_summary)

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Obtén las etiquetas del CSV

        # Verifica que las columnas esperadas estén presentes
        if set(['loss', 'accuracy', 'val_loss', 'val_accuracy']) != set(header):
            return HttpResponse("El archivo CSV no tiene las columnas esperadas.")

        # Extrae datos de las columnas
        datos = {label: [] for label in header}

        for row in csv_reader:
            for i, label in enumerate(header):
                datos[label].append(float(row[i]))

    # Genera la gráfica
    fig, ax = plt.subplots()
    for label, valores in datos.items():
        ax.plot(valores, label=label)

    ax.set(xlabel='Índice', ylabel='Valor',
           title='Gráfico desde archivo CSV')
    ax.legend()

    with open('C:/Users/ricar/Desktop/Django/proyecto1/proyecto1/static/codigo/info.json', 'r') as json_file:
        dataset_info = json.load(json_file)

    # Guarda la gráfica en un archivo temporal
    img_path = 'C:/Users/ricar/Desktop/Django/proyecto1/proyecto1/static/imagenes/grafica.png'  # Ruta donde se guardará la imagen
    plt.savefig(img_path)

    # Envía la gráfica y el resumen del modelo al template
    return render(request, 'grafica_template.html', {'img_path': img_path, 'model_summary': model_summary,'dataset_info': dataset_info})

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