from django import forms
from cam.models import *

class Location_form(forms.ModelForm):
    loc_id = forms.IntegerField()
    location_name = forms.CharField(max_length=100)
    parent_id = forms.IntegerField()
    description = forms.CharField(max_length=500)
    longitude = forms.DecimalField(max_digits=30, decimal_places=15)
    latitude = forms.DecimalField(max_digits=30, decimal_places=15)


    class Meta :
        model = Location
        fields = ['loc_id','location_name', 'parent_id','description','longitude','latitude',]
