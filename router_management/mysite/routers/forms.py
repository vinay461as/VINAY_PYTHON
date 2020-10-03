from django import forms

from mysite.routers.models import Router


class RouterForm(forms.ModelForm):
    class Meta:
        model = Router
        fields = ('sapid', 'hostname', 'loopback', 'mac_address')
