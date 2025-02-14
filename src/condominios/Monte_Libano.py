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

def Monte_libano(pdf_filename):
    # Substitua 'nome.pdf' pelo caminho correto do seu pdf_filename
    pdf_filename = 'monte libano.pdf'
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
        padrao_referencia_mensal = r"\b(\d{2}/\d{4})\b"
        mes_referencia = re.search(padrao_referencia_mensal, texto_pdf)

        if mes_referencia:
            # Extrai o mês e o ano
            mes, ano = mes_referencia.group().split('/')

            # Define o dia de vencimento como 10
            dia_vencimento = "15"

            # Formata a data de vencimento no formato ddmmaaaa
            data_vencimento = f"{dia_vencimento}{mes}{ano}"

            print(f"Mês de referência: {mes}{ano}")
            print(f"Data de Vencimento armazenada como: {data_vencimento}")
        else:
            print("Data de vencimento não encontrada.")

        # Expressão regular para capturar as salas, valores e borderos
        padrao_LJ = r"ML LJ\s+(\d+)\s+.*?Apto:\s*(\d+)\s+(.*?)\n(?=ML|\Z)"
        resultados_LJ = re.findall(padrao_LJ, texto_pdf, flags=re.DOTALL)

        padrao_SL = r"ML SL\s+(\d+)\s+.*?Apto:\s*(\d+)\s+(.*?)\n(?=ML|\Z)"
        resultados_SL = re.findall(padrao_SL, texto_pdf, flags=re.DOTALL)

        # Escolhendo o condomínio, mês de referência, e data de vencimento
        pyautogui.PAUSE = 2
        pyautogui.press('f5')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.write('65')
        pyautogui.press('enter', presses=2)
        pyautogui.click(x=426, y=302)

        # Inserindo um novo condomínio/ou bloco na Bios
        pyautogui.PAUSE = 1.5
        pyautogui.click(x=510, y=298)
        pyautogui.write('65')
        pyautogui.press('Enter')
        pyautogui.write(mes)
        pyautogui.write(ano)
        pyautogui.press('Enter')
        pyautogui.write(data_vencimento)
        pyautogui.press('Enter')
        pyautogui.click(x=799, y=298)
        pyautogui.click(x=152, y=365)
        
        for resultado in resultados_LJ:
            numero_sala, protocolo, conteudo_sala = resultado

            # Modificando o protocolo para remover os zeros à esquerda
            protocolo = protocolo.lstrip('0')

            # Extraindo todos os valores numéricos da seção capturada
            valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

            # O último valor numérico é assumido como o valor total da sala
            valor_total = valores[-1] if valores else "Valor não encontrado"

            pyautogui.PAUSE = 0.5
            pyautogui.write("LJ "+numero_sala)
            pyautogui.press('Enter')
            pyautogui.write(protocolo)
            pyautogui.press('Enter')
            pyautogui.write(valor_total)
            pyautogui.press('Enter')
            pyautogui.press('down', presses=2)
            pyautogui.press('left', presses=4)

        for resultado in resultados_SL:
            numero_sala, protocolo, conteudo_sala = resultado

            # Modificando o protocolo para remover os zeros à esquerda
            protocolo = protocolo.lstrip('0')

            # Extraindo todos os valores numéricos da seção capturada
            valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

            # Excluindo o último valor numérico se ele pertencer ao total geral e não ao total da sala
            # Esta lógica assume que o "Total Geral" é sempre o último valor no documento e não pertence a nenhuma sala
            if 'Total:' in conteudo_sala:
                valores = valores[:-1]

            # O último valor numérico é assumido como o valor total da sala
            valor_total = valores[-1] if valores else "Valor não encontrado"

            pyautogui.PAUSE = 0.5
            pyautogui.write(numero_sala)
            pyautogui.press('Enter')
            pyautogui.write(protocolo)
            pyautogui.press('Enter')
            pyautogui.write(valor_total)
            pyautogui.press('Enter')
            pyautogui.press('down', presses=2)
            pyautogui.press('left', presses=4)
