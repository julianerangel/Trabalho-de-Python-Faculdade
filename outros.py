# funções para auxiliar no programa...

def calc_acrescimo(valor_original, perc_acresc):
    # fonte de informação da função 'type':
    # https://dicasdepython.com.br/python-como-descobrir-o-tipo-de-uma-variavel-ou-objeto/
    preco = float(valor_original.replace(',', '.')) if type(valor_original) == "<class 'str'>" else valor_original
    acrescimo = (preco * perc_acresc)
    return acrescimo + preco
