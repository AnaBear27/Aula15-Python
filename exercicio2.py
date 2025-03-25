import re

texto = "Confira nossos produtos em https://www.exemplo.com/produtos e faça suas compras online."

padrao = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))'
urls = re.findall(padrao, texto)

print("URLs encontradas:")

for url in urls:
    print(url)