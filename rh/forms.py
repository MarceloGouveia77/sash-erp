from django import forms
from rh.models import Funcionario

class CadastrarFuncionarioForm(forms.ModelForm):
    
    class Meta:
        model = Funcionario
        exclude = ('data_demissao', 'ativo',)
        
    def __init__(self, *args, **kwargs):
        super(CadastrarFuncionarioForm, self).__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs['data-mask'] = '000.000.000-00'    
        self.fields['celular'].widget.attrs['data-mask'] = '(00)00000-0000'    
        self.fields['endereco_cep'].widget.attrs['data-mask'] = '00000-000'    