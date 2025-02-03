from datetime import datetime, timedelta
import fitz  # PyMuPDF
import re
import pyautogui

def Minas_Bank(arquivo):
    # Substitua 'nome.pdf' pelo caminho correto do seu arquivo
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

    padrao_salas = r"JK (\d{4}(?:-\d{2,4})?)\s.*?Apto:\s*(\d+)(.*?)(?=\nJK |\Z)"
    resultados_salas = re.findall(padrao_salas, texto_pdf, flags=re.DOTALL)