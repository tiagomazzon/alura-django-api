import re
from validate_docbr import CPF

def validate_cpf(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def validate_nome(nome):
    return nome.isalpha()
    
def validate_rg(rg):
    return len(rg) == 9

def validate_celular(celular):
    ''' Verifica se o celular é válido (11 91234-1234)'''
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta