from django import forms


class InputForm(forms.Form):
    foto= forms.CharField(max_length=20)
    titulo= forms.CharField(max_length=15)
    descripcion = forms.CharField(max_length=20)
    tags= forms.CharField(max_length=10)
    url=forms.CharField(max_length=20)