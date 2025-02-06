import fitz  # PyMuPDF
import re

# Substitua 'jkF.pdf' pelo caminho correto do seu arquivo
arquivo = 'jk fd reserva.pdf'
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

# Certificando-se de capturar ambos depósitos, Subsolo 1 e 3
padrao_depositos = r"DEPÓSITO SUBSOLO (\d)\n.*?\nApto:\n(\d+)\n(\d+,\d{2})"
resultados = re.findall(padrao_depositos, texto_pdf, flags=re.DOTALL)

padrao_salas = r"JKF (\d{4}(?:-\d{2,4})?)\s.*?Apto:\s*(\d+)(.*?)(?=\nJKF |\Z)"
resultados_salas = re.findall(padrao_salas, texto_pdf, flags=re.DOTALL)

# Supondo que `texto_pdf` seja a string com o conteúdo do PDF.
padrao_bistro = r"(JKF BISTRÔ.*?Apto:\s*\d+.*?)(?=JKF G|$)"

resultados_bistro = re.findall(padrao_bistro, texto_pdf, flags=re.DOTALL)

# Expressão regular para capturar a seção de cada garagem
padrao_garagens = r"JKF G\s+(\d+).*?Apto:\s*(\d+)(.*?)(?=JKF G|Total:|$)"
secoes_garagem = re.findall(padrao_garagens, texto_pdf, flags=re.DOTALL)

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

    # Verifica se "Total:" está presente no conteúdo da garagem
    if "Total:" in conteudo_garagem:
        # Separa o conteúdo da garagem antes do "Total:"
        conteudo_antes_total = conteudo_garagem.split("Total:")[0].strip()
        # Encontra todos os valores numéricos no conteúdo antes do "Total:"
        valores_antes_total = re.findall(r"-?\d{1,3}(?:\.\d{3})*,\d{2}", conteudo_antes_total)
        # Se houver valores antes do "Total:", seleciona o último, caso contrário, seleciona o penúltimo valor na seção da garagem
        valor_relevante = valores_antes_total[-2] if valores_antes_total else valores[-2] if len(valores) >= 2 else "Valor não encontrado"
    else:
        valor_relevante = valores[-1] if valores else "Valor não encontrado"

    print(f"Garagem: {numero_garagem}")
    print(f"Protocolo: {protocolo}")
    print(f"Valor Relevante: {valor_relevante}\n")

for deposito, protocolo, valor in resultados:
    print(f"Deposito: {deposito}")
    print(f"Protocolo: {protocolo}")
    print(f"Valor: {valor}\n")

for bistro in resultados_bistro:
    # Extrair todos os valores numéricos da seção do Bistrô
    valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", bistro)
    valor_total = valores[-1] if valores else "Valor não encontrado"
    print(f"BISTRO")
    print(f"Protocolo: {protocolo}")
    print(f"Valor Total: {valor_total}\n")
