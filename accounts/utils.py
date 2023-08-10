import re

def validar_cnpj(cnpj):
    cnpj = re.sub(r'\D', '', cnpj)  

    if len(cnpj) != 14:
        return False

    if cnpj == cnpj[0] * 14:
        return False

    return True


def validar_cnae(cnae):
    cnae = re.sub(r'\D', '', cnae)  


    if len(cnae) != 8:
        return False

    return True

def editar_cnpj(cnpj):
    cnpj_editado = re.sub(r'\D', '', cnpj) 
    return cnpj_editado