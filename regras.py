def regraB3_S23(vivos, atual):
    retorno = 0

    if atual == 1 and vivos < 2:
        retorno = 0
    
    if atual == 1 and vivos in (2, 3):
        retorno = 1
    
    if atual == 1 and vivos > 3:
        retorno = 0
    
    if atual == 0 and vivos == 3:
        retorno = 1

    return retorno

def regraB36_S23(vivos, atual):
    retorno = 0

    if atual == 1 and vivos < 2:
        retorno = 0
    
    if atual == 1 and vivos in (2, 3):
        retorno = 1
    
    if atual == 1 and vivos > 3:
        retorno = 0
    
    if atual == 0 and vivos in (3, 6):
        retorno = 1

    return retorno

def regraB3_S236(vivos, atual):
    retorno = 0

    if atual == 1 and vivos < 2:
        retorno = 0
    
    if atual == 1 and vivos in (2, 3, 6):
        retorno = 1
    
    if atual == 1 and vivos > 3:
        retorno = 0
    
    if atual == 0 and vivos == 3:
        retorno = 1

    return retorno
