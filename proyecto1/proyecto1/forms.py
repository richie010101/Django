from django import forms

class MultipleFileField(forms.FileField):
    def to_python(self, data):
        if not data:
            return []
        elif isinstance(data, list):
            return [super().to_python(item) for item in data]
        else:
            return [super().to_python(data)]

class CarpetaImagenForm(forms.Form):
    carpeta_imagenes = MultipleFileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Cargar imágenes')

#class CarpetaImagenForm(forms.Form):
#    carpeta_imagenes = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
