from datetime import datetime, timedelta
import fitz  # PyMuPDF
import re
import pyautogui
import os
import sys

# Obtém o diretório da pasta `src`
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona `src` ao caminho de importação
sys.path.append(BASE_DIR)

# Importação do módulo
from condominios.pdf_manager import get_pdf_path

def Ilha_bela(pdf_filename):
    pdf_filename = 'ilha bela.pdf'
    pdf_path = get_pdf_path(pdf_filename)

    # Verifica se o arquivo existe antes de tentar abrir
    if not os.path.exists(pdf_path):
        print(f"ERRO: O arquivo {pdf_filename} não foi encontrado no caminho: {pdf_path}")
    else:
        # Abrindo o PDF
        with fitz.open(pdf_path) as pdf:
            lista_texto_paginas = []  # Lista para armazenar o texto de cada página
            
            # Percorre todas as páginas do documento
            for pagina in pdf:
                texto = pagina.get_text()
                lista_texto_paginas.append(texto)  # Adiciona o texto da página à lista
            
            # Combina o texto de todas as páginas
            texto_pdf = ''.join(lista_texto_paginas)

        # Expressão regular para encontrar a data de vencimento (formato mm/aaaa)
        padrao_referencia_mensal = r"\b(\d{2})/(\d{4})\b"
        mes_referencia = re.search(padrao_referencia_mensal, texto_pdf)

        if mes_referencia:
            mes, ano = mes_referencia.groups()  # Extrai o mês e o ano como grupos

            # Converte para datetime para facilitar a manipulação da data
            # Retrocede um dia para obter o mês anterior
            data_referencia = datetime(int(ano), int(mes), 1) - timedelta(days=1)
            # Formata para o mês de referência atrasado (mmYYYY)
            mes_referencia_atrasado = data_referencia.strftime('%m%Y')

            # Define o dia de vencimento como 12
            dia_vencimento = "12"

            # Usa o ano e mês originais para a data de vencimento
            data_vencimento = f"{dia_vencimento}{mes}{ano}"

            print(f"Mês de referência atrasado: {mes_referencia_atrasado}")
            print(f"Data de Vencimento: {data_vencimento}")
        else:
            print("Data de vencimento não encontrada.")

        # Expressão regular para capturar as salas, valores e borderos
        padrao_salas = r"APTO -\s+(\d+)\s+.*?Apto:\s*(\d+)\s+(.*?)\n(?=APTO|\Z)"
        resultados_salas = re.findall(padrao_salas, texto_pdf, flags=re.DOTALL)

        # Escolhendo o condomínio, mês de referência, e data de vencimento
        pyautogui.PAUSE = 2
        pyautogui.press('f5')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.write('17')
        pyautogui.press('enter', presses=2)
        pyautogui.click(x=426, y=302)

        # Inserindo um novo condomínio/ou bloco na Bios
        pyautogui.PAUSE = 1.5
        pyautogui.click(x=510, y=298)
        pyautogui.write('17')
        pyautogui.press('Enter')
        pyautogui.write(mes)
        pyautogui.write(ano)
        pyautogui.press('Enter')
        pyautogui.write(data_vencimento)
        pyautogui.press('Enter')
        pyautogui.click(x=799, y=298)
        pyautogui.click(x=152, y=365)
        
        for resultado in resultados_salas:
            numero_sala, protocolo, conteudo_sala = resultado

            # Extraindo todos os valores numéricos da seção capturada
            valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

            # Modificando o protocolo para remover os zeros à esquerda
            protocolo = protocolo.lstrip('0')

            # Esta lógica assume que o "Total Geral" é sempre o último valor no documento e não pertence a nenhuma sala
            if 'Total:' in conteudo_sala:
                    valores = valores[:-1]

            # Verificando se há valores para evitar erro de indexação
            if valores:
                # O último valor numérico é assumido como o valor total da sala
                valor_total = valores[-1]
            else:
                valor_total = "Valor não encontrado"

            pyautogui.PAUSE = 0.5
            pyautogui.write(numero_sala)
            pyautogui.press('Enter')
            pyautogui.write(protocolo)
            pyautogui.press('Enter')
            pyautogui.write(valor_total)
            pyautogui.press('Enter')
            pyautogui.press('down', presses=2)
            pyautogui.press('left', presses=4)
