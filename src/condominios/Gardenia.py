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

def Gardenia(pdf_filename):
    # Substitua 'nome.pdf' pelo caminho correto do seu pdf_filename
    pdf_filename = 'gardenia.pdf'
    pdf_path = get_pdf_path(pdf_filename)

    # Verifica se o pdf_filename existe antes de tentar abrir
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

            # Define o dia de vencimento como 03
            dia_vencimento = "05"

            # Usa o ano e mês originais para a data de vencimento
            data_vencimento = f"{dia_vencimento}{mes}{ano}"

            print(f"Mês de referência atrasado: {mes_referencia_atrasado}")
            print(f"Data de Vencimento: {data_vencimento}")
        else:
            print("Data de vencimento não encontrada.")

        # Expressão regular para capturar as salas, valores e borderos
        # BLOCO A
        padrao_bloco_A = r"APTO A(\d{4}(?:-\d{2,4})?)\s+.*?Apto:\s*(\d+)(.*?)\n(?=APTO A|\Z)"
        resultados_bloco_A = re.findall(padrao_bloco_A, texto_pdf, flags=re.DOTALL)

        # BLOCO B
        padrao_bloco_B = r"APTO B(\d{4}(?:-\d{2,4})?)\s+.*?Apto:\s*(\d+)(.*?)\n(?=APTO B|\Z)"
        resultados_bloco_B = re.findall(padrao_bloco_B, texto_pdf, flags=re.DOTALL)

        # BLOCO C
        padrao_bloco_C = r"APTO C(\d{4}(?:-\d{2,4})?)\s+.*?Apto:\s*(\d+)(.*?)\n(?=APTO C|\Z)"
        resultados_bloco_C = re.findall(padrao_bloco_C, texto_pdf, flags=re.DOTALL)

        # BLOCO D
        padrao_bloco_D = r"APTO D(\d{4}(?:-\d{2,4})?)\s+.*?Apto:\s*(\d+)(.*?)\n(?=APTO D|\Z)"
        resultados_bloco_D = re.findall(padrao_bloco_D, texto_pdf, flags=re.DOTALL)

        # BLOCO E
        padrao_bloco_E = r"APTO E(\d{4}(?:-\d{2,4})?)\s+.*?Apto:\s*(\d+)(.*?)\n(?=APTO E|\Z)"
        resultados_bloco_E = re.findall(padrao_bloco_E, texto_pdf, flags=re.DOTALL)

        # BLOCO F
        padrao_bloco_F = r"APTO F(\d{4}(?:-\d{2,4})?)\s+.*?Apto:\s*(\d+)(.*?)\n(?=APTO F|\Z)"
        resultados_bloco_F = re.findall(padrao_bloco_F, texto_pdf, flags=re.DOTALL)

        # BLOCO G
        padrao_bloco_G = r"APTO G(\d{4}(?:-\d{2,4})?)\s+.*?Apto:\s*(\d+)(.*?)\n(?=APTO G|\Z)"
        resultados_bloco_G = re.findall(padrao_bloco_G, texto_pdf, flags=re.DOTALL)

        # BLOCO H
        padrao_bloco_H = r"APTO H(\d{4}(?:-\d{2,4})?)\s+.*?Apto:\s*(\d+)(.*?)\n(?=APTO H|\Z)"
        resultados_bloco_H = re.findall(padrao_bloco_H, texto_pdf, flags=re.DOTALL)

        # BLOCO I
        padrao_bloco_I = r"APTO I(\d{4}(?:-\d{2,4})?)\s+.*?Apto:\s*(\d+)(.*?)\n(?=APTO I|\Z)"
        resultados_bloco_I = re.findall(padrao_bloco_I, texto_pdf, flags=re.DOTALL)

        # BLOCO J
        padrao_bloco_J = r"APTO J(\d{4}(?:-\d{2,4})?)\s+.*?Apto:\s*(\d+)(.*?)\n(?=APTO J|\Z)"
        resultados_bloco_J = re.findall(padrao_bloco_J, texto_pdf, flags=re.DOTALL)

        # Escolhendo o condomínio, mês de referência, e data de vencimento
        pyautogui.PAUSE = 2
        pyautogui.press('f5')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.write('39')
        pyautogui.press('enter', presses=2)
        pyautogui.click(x=426, y=302)
        # Inserindo um novo condomínio/ou bloco na Bios
        pyautogui.PAUSE = 1.5
        pyautogui.click(x=510, y=298)
        pyautogui.write('39')
        pyautogui.press('Enter')
        pyautogui.write(mes_referencia_atrasado)
        pyautogui.write(ano)
        pyautogui.press('Enter')
        pyautogui.write(data_vencimento)
        pyautogui.press('Enter')
        pyautogui.write('A.')
        pyautogui.click(x=799, y=298)
        pyautogui.click(x=152, y=365)

        # BLOCO A
        for resultado in resultados_bloco_A:
            numero_sala, protocolo, conteudo_sala = resultado

            # Modificando o protocolo para remover os zeros à esquerda
            protocolo = protocolo.lstrip('0')

            numero_sala = numero_sala.lstrip('0')

            numero_sala = numero_sala.lstrip('0')

            numero_sala = numero_sala.lstrip('0')

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

        # Inserindo um novo condomínio/ou bloco na Bios
        pyautogui.PAUSE = 1.5
        pyautogui.click(x=510, y=298)
        pyautogui.write('39')
        pyautogui.press('Enter')
        pyautogui.write(mes_referencia_atrasado)
        pyautogui.write(ano)
        pyautogui.press('Enter')
        pyautogui.write(data_vencimento)
        pyautogui.press('Enter')
        pyautogui.write('B.')
        pyautogui.click(x=799, y=298)
        pyautogui.click(x=152, y=365)

        # BLOCO B
        for resultado in resultados_bloco_B:
            numero_sala, protocolo, conteudo_sala = resultado

            protocolo = protocolo.lstrip('0')

            numero_sala = numero_sala.lstrip('0')

            numero_sala = numero_sala.lstrip('0')

            numero_sala = numero_sala.lstrip('0')

            valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

            if 'Total:' in conteudo_sala:
                valores = valores[:-1]

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

        # Inserindo um novo condomínio/ou bloco na Bios
        pyautogui.PAUSE = 1.5
        pyautogui.click(x=510, y=298)
        pyautogui.write('39')
        pyautogui.press('Enter')
        pyautogui.write(mes_referencia_atrasado)
        pyautogui.write(ano)
        pyautogui.press('Enter')
        pyautogui.write(data_vencimento)
        pyautogui.press('Enter')
        pyautogui.write('C.')
        pyautogui.click(x=799, y=298)
        pyautogui.click(x=152, y=365)

        # BLOCO C
        for resultado in resultados_bloco_C:
            numero_sala, protocolo, conteudo_sala = resultado

            protocolo = protocolo.lstrip('0')

            numero_sala = numero_sala.lstrip('0')

            valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

            if 'Total:' in conteudo_sala:
                valores = valores[:-1]

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

        # Inserindo um novo condomínio/ou bloco na Bios
        pyautogui.PAUSE = 1.5
        pyautogui.click(x=510, y=298)
        pyautogui.write('39')
        pyautogui.press('Enter')
        pyautogui.write(mes_referencia_atrasado)
        pyautogui.write(ano)
        pyautogui.press('Enter')
        pyautogui.write(data_vencimento)
        pyautogui.press('Enter')
        pyautogui.write('D.')
        pyautogui.click(x=799, y=298)
        pyautogui.click(x=152, y=365)

        # BLOCO D
        for resultado in resultados_bloco_D:
            numero_sala, protocolo, conteudo_sala = resultado

            protocolo = protocolo.lstrip('0')

            numero_sala = numero_sala.lstrip('0')

            valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

            if 'Total:' in conteudo_sala:
                valores = valores[:-1]

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

        # Inserindo um novo condomínio/ou bloco na Bios
        pyautogui.PAUSE = 1.5
        pyautogui.click(x=510, y=298)
        pyautogui.write('39')
        pyautogui.press('Enter')
        pyautogui.write(mes_referencia_atrasado)
        pyautogui.write(ano)
        pyautogui.press('Enter')
        pyautogui.write(data_vencimento)
        pyautogui.press('Enter')
        pyautogui.write('E.')
        pyautogui.click(x=799, y=298)
        pyautogui.click(x=152, y=365)

        # BLOCO E
        for resultado in resultados_bloco_E:
            numero_sala, protocolo, conteudo_sala = resultado

            protocolo = protocolo.lstrip('0')

            numero_sala = numero_sala.lstrip('0')

            valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

            if 'Total:' in conteudo_sala:
                valores = valores[:-1]

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

        # Inserindo um novo condomínio/ou bloco na Bios
        pyautogui.PAUSE = 1.5
        pyautogui.click(x=510, y=298)
        pyautogui.write('39')
        pyautogui.press('Enter')
        pyautogui.write(mes_referencia_atrasado)
        pyautogui.write(ano)
        pyautogui.press('Enter')
        pyautogui.write(data_vencimento)
        pyautogui.press('Enter')
        pyautogui.write('F.')
        pyautogui.click(x=799, y=298)
        pyautogui.click(x=152, y=365)

        # BLOCO F
        for resultado in resultados_bloco_F:
            numero_sala, protocolo, conteudo_sala = resultado

            protocolo = protocolo.lstrip('0')

            numero_sala = numero_sala.lstrip('0')

            valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

            if 'Total:' in conteudo_sala:
                valores = valores[:-1]

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

        # Inserindo um novo condomínio/ou bloco na Bios
        pyautogui.PAUSE = 1.5
        pyautogui.click(x=510, y=298)
        pyautogui.write('39')
        pyautogui.press('Enter')
        pyautogui.write(mes_referencia_atrasado)
        pyautogui.write(ano)
        pyautogui.press('Enter')
        pyautogui.write(data_vencimento)
        pyautogui.press('Enter')
        pyautogui.write('G.')
        pyautogui.click(x=799, y=298)
        pyautogui.click(x=152, y=365)

        # BLOCO G
        for resultado in resultados_bloco_G:
            numero_sala, protocolo, conteudo_sala = resultado

            protocolo = protocolo.lstrip('0')

            numero_sala = numero_sala.lstrip('0')

            valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

            if 'Total:' in conteudo_sala:
                valores = valores[:-1]

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

        # Inserindo um novo condomínio/ou bloco na Bios
        pyautogui.PAUSE = 1.5
        pyautogui.click(x=510, y=298)
        pyautogui.write('39')
        pyautogui.press('Enter')
        pyautogui.write(mes_referencia_atrasado)
        pyautogui.write(ano)
        pyautogui.press('Enter')
        pyautogui.write(data_vencimento)
        pyautogui.press('Enter')
        pyautogui.write('H.')
        pyautogui.click(x=799, y=298)
        pyautogui.click(x=152, y=365)

        # BLOCO H
        for resultado in resultados_bloco_H:
            numero_sala, protocolo, conteudo_sala = resultado

            protocolo = protocolo.lstrip('0')

            numero_sala = numero_sala.lstrip('0')

            valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

            if 'Total:' in conteudo_sala:
                valores = valores[:-1]

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

        # Inserindo um novo condomínio/ou bloco na Bios
        pyautogui.PAUSE = 1.5
        pyautogui.click(x=510, y=298)
        pyautogui.write('39')
        pyautogui.press('Enter')
        pyautogui.write(mes_referencia_atrasado)
        pyautogui.write(ano)
        pyautogui.press('Enter')
        pyautogui.write(data_vencimento)
        pyautogui.press('Enter')
        pyautogui.write('I.')
        pyautogui.click(x=799, y=298)
        pyautogui.click(x=152, y=365)

        # BLOCO I
        for resultado in resultados_bloco_I:
            numero_sala, protocolo, conteudo_sala = resultado

            protocolo = protocolo.lstrip('0')

            numero_sala = numero_sala.lstrip('0')

            valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

            if 'Total:' in conteudo_sala:
                valores = valores[:-1]

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

        # Inserindo um novo condomínio/ou bloco na Bios
        pyautogui.PAUSE = 1.5
        pyautogui.click(x=510, y=298)
        pyautogui.write('39')
        pyautogui.press('Enter')
        pyautogui.write(mes_referencia_atrasado)
        pyautogui.write(ano)
        pyautogui.press('Enter')
        pyautogui.write(data_vencimento)
        pyautogui.press('Enter')
        pyautogui.write('J.')
        pyautogui.click(x=799, y=298)
        pyautogui.click(x=152, y=365)

        # BLOCO J
        for resultado in resultados_bloco_J:
            numero_sala, protocolo, conteudo_sala = resultado

            protocolo = protocolo.lstrip('0')

            numero_sala = numero_sala.lstrip('0')

            valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

            if 'Total:' in conteudo_sala:
                valores = valores[:-1]

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
