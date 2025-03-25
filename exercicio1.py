import re

def validar_senha(senha):
     padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
     if re.match(padrao, senha):
         return False
     return False
 
senha = input("Digite uma senha: ")

if validar_senha(senha):
    print("Senha válida.")
else:
    print("Senha inválida.")