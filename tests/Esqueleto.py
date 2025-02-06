import fitz  # PyMuPDF
import re

# Substitua 'jk.pdf' pelo caminho correto do seu arquivo
arquivo = 'minas.pdf'
pdf = fitz.open(arquivo)
lista_texto_paginas = []  # Lista para armazenar o texto de cada página
for pagina in pdf:  # Percorre todas as páginas do documento
    texto = pagina.get_text()
    lista_texto_paginas.append(texto)  # Adiciona o texto da página à lista
# Combina o texto de todas as páginas
texto_pdf = ''.join(lista_texto_paginas)

# Expressão regular para encontrar a data de vencimento (formato mm/aaaa)
padrao_referencia_mensal = r"\b(\d{2}/\d{4})\b"
mes_referencia = re.search(padrao_referencia_mensal, texto_pdf)

# ATENÇÃO: o mês de referência é adiantado
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

padrao_salas = r"SL (?:LJ )?(\d+|[\d]{4}(?:[-/][\d]{1,4})*)\s.*?Apto:\s*(\d+)(.*?)(?=SL | Total:|$)"
resultados_salas = re.findall(padrao_salas, texto_pdf, flags=re.DOTALL)

for resultado in resultados_salas:
    numero_sala, protocolo, conteudo_sala = resultado

    # Formata o número da sala para ter 4 dígitos
    numero_sala_formatado = numero_sala.zfill(4)

    # Extraindo todos os valores numéricos da seção capturada
    valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

    # Excluindo o último valor numérico se ele pertencer ao total geral e não ao total da sala
    # Esta lógica assume que o "Total Geral" é sempre o último valor no documento e não pertence a nenhuma sala
    if 'Total:' in conteudo_sala:
        valores = valores[:-1]

    # O último valor numérico é assumido como o valor total da sala
    valor_total = valores[-1] if valores else "Valor não encontrado"

    print(f"Sala: {numero_sala_formatado}")
    print(f"Protocolo: {protocolo}")
    print(f"Valor Total: {valor_total}\n")
