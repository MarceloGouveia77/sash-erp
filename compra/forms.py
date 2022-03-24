from django import forms
from compra.models import Compra

class CompraForm(forms.ModelForm):
    
    class Meta:
        model = Compra
        exclude = ('data', 'pago', 'valor_total', 'entregue', 'concluida')