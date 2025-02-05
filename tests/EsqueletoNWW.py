from cgitb import text
import fitz  # PyMuPDF
import re

# Substitua 'jk.pdf' pelo caminho correto do seu arquivo
arquivo = 'nw fd reserva.pdf'
pdf = fitz.open(arquivo)
lista_texto_paginas = []  # Lista para armazenar o texto de cada página
for pagina in pdf:  # Percorre todas as páginas do documento
    texto = pagina.get_text()
    lista_texto_paginas.append(texto)  # Adiciona o texto da página à lista
texto_pdf = ''.join(lista_texto_paginas)  # Combina o texto de todas as páginas

# Expressão regular para encontrar a data de vencimento (formato mm/aaaa)
padrao_referencia_mensal = r"\b(\d{2}/\d{4})\b"
mes_referencia = re.search(padrao_referencia_mensal, texto_pdf)

if mes_referencia:
    # Extrai o mês e o ano
    mes, ano = mes_referencia.group().split('/')

    # Define o dia de vencimento como 10
    dia_vencimento = "10"

    # Formata a data de vencimento no formato ddmmaaaa
    data_vencimento = f"{dia_vencimento}{mes}{ano}"

    print(f"Mês de referência: {mes}{ano}")
    print(f"Data de Vencimento armazenada como: {data_vencimento}")
else:
    print("Data de vencimento não encontrada.")

# Expressão regular para capturar a seção de cada sala
padrao_salas = r"N (\d{4}(?:-\d{2,4})?)\s.*?Apto:\s*(\d+)(.*?)(?=\nNWF|\Z)"
resultados_salas = re.findall(padrao_salas, texto_pdf, flags=re.DOTALL)

# Expressão regular para capturar a seção de cada garagem
padrao_garagens = r"NWF G\s+(\d+).*?Apto:\s*(\d+)(.*?)(?=NWF G|NW LOJA 1|$)"
secoes_garagem = re.findall(padrao_garagens, texto_pdf, flags=re.DOTALL)

# Expressão regular para capturar os dados da loja 1 - 1/4
padrao_loja1 = r"NWF LOJA 1 - 1/4\n(.+?)\nApto:\s*(\d+)(.*?)(?=\nNWF LOJA 1|\Z)"
match_loja1 = re.search(padrao_loja1, texto_pdf, flags=re.DOTALL)

# Expressão regular para capturar os dados da loja 1 - 2/4
padrao_loja2 = r"NWF LOJA 1 - 2/4\n(.+?)\nApto:\s*(\d+)(.*?)(?=\nNWF LOJA 1|\Z)"
match_loja2 = re.search(padrao_loja2, texto_pdf, flags=re.DOTALL)

# Expressão regular para capturar os dados da loja 1 - 3/4
padrao_loja3 = r"NWF LOJA 1 - 3/4\n(.+?)\nApto:\s*(\d+)(.*?)(?=\nNWF LOJA 1|\Z)"
match_loja3 = re.search(padrao_loja3, texto_pdf, flags=re.DOTALL)

# Expressão regular para capturar os dados da loja 1 - 4/4
padrao_loja4 = r"NWF LOJA 1 - 4/4\n(.+?)\nApto:\s*(\d+)(.*?)(?=NWF LOJA|$)"
match_loja4 = re.search(padrao_loja4, texto_pdf, flags=re.DOTALL)

# Expressão regular para capturar os dados da loja 2
padrao_loja5 = r"NWF LOJA 2\n(.+?)\nApto:\s*(\d+)(.*?)(?=NWF LOJA|$)"
match_loja5 = re.search(padrao_loja5, texto_pdf, flags=re.DOTALL)

# Expressão regular para capturar os dados da loja 3
padrao_loja6 = r"NWF LOJA 3\n(.+?)\nApto:\s*(\d+)(.*?)(?=NWF LOJA|$)"
match_loja6 = re.search(padrao_loja6, texto_pdf, flags=re.DOTALL)

# Expressão regular para capturar os dados da loja 4
padrao_loja7 = r"NWF LOJA 4\n(.+?)\nApto:\s*(\d+)(.*?)(?=NWF Total:|$)"
match_loja7 = re.search(padrao_loja7, texto_pdf, flags=re.DOTALL)

for resultado in resultados_salas:
    numero_sala, protocolo, conteudo_sala = resultado

    # Extraindo todos os valores numéricos da seção capturada
    valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

    # O último valor numérico é assumido como o valor total
    valor_total = valores[-1] if valores else "Valor não encontrado"

    print(f"Sala: {numero_sala}")
    print(f"Protocolo: {protocolo}")
    print(f"Valor Total: {valor_total}\n")

# Encontra todas as seções de garagem no texto
secoes_garagem = re.findall(padrao_garagens, texto_pdf, flags=re.DOTALL)

for secao in secoes_garagem:
    numero_garagem, protocolo, conteudo_garagem = secao
    # Encontra todos os valores numéricos na seção da garagem
    valores = re.findall(r"-?\d{1,3}(?:\.\d{3})*,\d{2}", conteudo_garagem)

    # Se há mais de um valor, seleciona o penúltimo como o valor relevante
    if len(valores) >= 2:
        valor_relevante = valores[-2]
    else:
        valor_relevante = valores[0] if valores else "Valor não encontrado"

    print(f"Garagem: {numero_garagem}")
    print(f"Protocolo: {protocolo}")
    print(f"Valor Relevante: {valor_relevante}\n")

if match_loja1:
    protocolo = match_loja1.group(2)
    valores = match_loja1.group(3).split("\n")

    # Filtrar os valores numéricos
    valores_numericos = [valor.strip() for valor in valores if valor.strip(
    ).replace('.', '').replace(',', '').isdigit()]

    # O último valor numérico é assumido como o valor total
    valor_total = valores_numericos[-1] if valores_numericos else "Valor não encontrado"

    print(f"Loja 1 - 1/4")
    print(f"Protocolo: {protocolo}")
    print(f"Valor Total: {valor_total}\n")

if match_loja2:
    protocolo = match_loja2.group(2)
    valores = match_loja2.group(3).split("\n")

    # Filtrar os valores numéricos
    valores_numericos = [valor.strip() for valor in valores if valor.strip(
    ).replace('.', '').replace(',', '').isdigit()]

    # O último valor numérico é assumido como o valor total
    valor_total = valores_numericos[-1] if valores_numericos else "Valor não encontrado"

    print(f"Loja 1 - 2/4")
    print(f"Protocolo: {protocolo}")
    print(f"Valor Total: {valor_total}\n")

if match_loja3:
    protocolo = match_loja3.group(2)
    valores = match_loja3.group(3).split("\n")

    # Filtrar os valores numéricos
    valores_numericos = [valor.strip() for valor in valores if valor.strip(
    ).replace('.', '').replace(',', '').isdigit()]

    # O último valor numérico é assumido como o valor total
    valor_total = valores_numericos[-1] if valores_numericos else "Valor não encontrado"

    print(f"Loja 1 - 3/4")
    print(f"Protocolo: {protocolo}")
    print(f"Valor Total: {valor_total}\n")

if match_loja4:
    protocolo = match_loja4.group(2)
    valores = match_loja4.group(3).split("\n")

    # Filtrar os valores numéricos
    valores_numericos = [valor.strip() for valor in valores if valor.strip(
    ).replace('.', '').replace(',', '').isdigit()]

    # O último valor numérico é assumido como o valor total
    valor_total = valores_numericos[-1] if valores_numericos else "Valor não encontrado"

    print(f"Loja 1 - 4/4")
    print(f"Protocolo: {protocolo}")
    print(f"Valor Total: {valor_total}\n")

if match_loja5:
    protocolo = match_loja5.group(2)
    valores = match_loja5.group(3).split("\n")

    # Filtrar os valores numéricos
    valores_numericos = [valor.strip() for valor in valores if valor.strip(
    ).replace('.', '').replace(',', '').isdigit()]

    # O último valor numérico é assumido como o valor total
    valor_total = valores_numericos[-1] if valores_numericos else "Valor não encontrado"

    print(f"Loja 2")
    print(f"Protocolo: {protocolo}")
    print(f"Valor Total: {valor_total}\n")

if match_loja6:
    protocolo = match_loja6.group(2)
    valores = match_loja6.group(3).split("\n")

    # Filtrar os valores numéricos
    valores_numericos = [valor.strip() for valor in valores if valor.strip(
    ).replace('.', '').replace(',', '').isdigit()]

    # O último valor numérico é assumido como o valor total
    valor_total = valores_numericos[-1] if valores_numericos else "Valor não encontrado"

    print(f"Loja 3")
    print(f"Protocolo: {protocolo}")
    print(f"Valor Total: {valor_total}\n")

if match_loja7:
    protocolo = match_loja7.group(2)
    valores = match_loja7.group(3).split("\n")

    # Filtrar os valores numéricos
    valores_numericos = [valor.strip() for valor in valores if valor.strip(
    ).replace('.', '').replace(',', '').isdigit()]

    # O último valor numérico é assumido como o valor total
    valor_total = valores_numericos[-2] if valores_numericos else "Valor não encontrado"

    print(f"Loja 4")
    print(f"Protocolo: {protocolo}")
    print(f"Valor Total: {valor_total}\n")
