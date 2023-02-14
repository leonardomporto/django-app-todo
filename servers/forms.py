from django import forms
from .models import Server


class ServerForm(forms.ModelForm):

    # birthday = forms.DateField(label=('Date birth'), input_formats=['%d/%m/%Y','%Y-%m-%d',], required=True,  widget=forms.DateInput(attrs={'type': 'date'}))
    # date_payment = forms.DateField(label=('Data Pagamento'), input_formats=['%d/%m/%Y','%Y-%m-%d',], required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    # email = forms.EmailField(required=False)

    class Meta:
        model = Server
        fields = ['name', 'descripition', 'price',]
