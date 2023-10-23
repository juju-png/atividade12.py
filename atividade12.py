 # Exercício Python 12: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input("Digite um ano: "))

# Verifique se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
    
print(f"""
      Neste código, pedimos ao usuário que insira o ano que deseja verificar. Em seguida, aplicamos a lógica para verificar se o ano é bissexto ou não.
      """)





