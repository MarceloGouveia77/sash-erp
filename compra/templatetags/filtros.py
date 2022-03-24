from django import template

register = template.Library()

@register.filter(name='obter_icone_pago')
def obter_icone_pago(pago):
    if pago:
        return '<span class="badge rounded-pill bg-success badge-sm me-1 mb-1 mt-1">SIM</span>'
    return '<span class="badge rounded-pill bg-danger badge-sm me-1 mb-1 mt-1">NÃO</span>'
    