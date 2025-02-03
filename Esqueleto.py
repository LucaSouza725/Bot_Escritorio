import fitz  # PyMuPDF
import re

# Substitua pelo caminho correto do seu arquivo PDF
arquivo = 'minas.pdf'
pdf = fitz.open(arquivo)
lista_texto_paginas = []  # Lista para armazenar o texto de cada página

for pagina in pdf:  # Percorre todas as páginas do documento
    texto = pagina.get_text("text")
    lista_texto_paginas.append(texto)  # Adiciona o texto da página à lista

# Combina o texto de todas as páginas
texto_pdf = '\n'.join(lista_texto_paginas)

# Verificar se o texto está correto
print("Texto extraído do PDF:")
print(texto_pdf)  # Exibir para depuração

padrao_salas = r"SL (\d{4}(?:-\d{2,4})?)\s.*?Apto:\s*(\d+)(.*?)(?=\nSL |\Z)"
resultados_salas = re.findall(padrao_salas, texto_pdf, flags=re.DOTALL)

# Encontrando todas as correspondências no texto extraído
resultados_salas = re.findall(padrao_salas, texto_pdf)

# Verificar se encontramos resultados
if not resultados_salas:
    print("Nenhum dado encontrado. Verifique o formato do PDF ou ajuste a regex.")
else:
    for resultado in resultados_salas:
        numero_apto, protocolo, valor_base, valor_total = resultado

        # Modificando o protocolo para remover os zeros à esquerda
        protocolo = protocolo.lstrip('0')

        print(f"Número do Apartamento: {numero_apto}")
        print(f"Protocolo: {protocolo}")
        print(f"Valor Base: {valor_base}")
        print(f"Valor Total: {valor_total}\n")
