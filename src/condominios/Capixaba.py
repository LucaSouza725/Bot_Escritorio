from PyPDF2 import PdfReader
import re
from datetime import datetime
import pyautogui


def Capixaba(capixaba):
    # Abrindo o PDF do Capixaba
    with open(capixaba, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)

        # Obtendo o número de páginas no PDF
        num_pages = len(pdf_reader.pages)

        # Iterar sobre as páginas do PDF
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            # Extrair o texto da página
            text = page.extract_text()

            # Dividindo o texto em linhas
            padrao_casa = r'Casa: (\d+)'
            padrao_protocolo = r'Apto: (\d+)'
            padrao_valor = r'(\d{1,3}(?:\.\d{3})*,\d{2})$'
            padrao_mes_ano = r'CAPIXABA ITAPE (\d+)/(\d{4})'

            casas = re.findall(padrao_casa, text)
            protocolos = re.findall(padrao_protocolo, text)
            valores = re.findall(padrao_valor, text, re.MULTILINE)
            mes_ano_match = re.search(padrao_mes_ano, text)

            # Extrair mês e ano do padrão encontrado
            if mes_ano_match:
                dia = 15
                mes = int(mes_ano_match.group(1)) - 1  # Subtrai 1 do valor do mês
                ano = mes_ano_match.group(2)
            else:
                mes = "N/A"
                ano = "N/A"

            # Criar data de vencimento
            data_vencimento = datetime(int(ano), int(mes)+(1), int(dia)).strftime("%d%m%Y")
            mes_formatado = str(mes).zfill(2)
            break
        # Escolhendo o condomínio, mês de referência, e data de vencimento
        pyautogui.PAUSE = 1.5
        pyautogui.press('f5')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.write('56')
        pyautogui.press('enter', presses=2)
        pyautogui.click(x=426, y=302)
        pyautogui.click(x=510, y=298)
        pyautogui.write('56')
        pyautogui.press('Enter')
        pyautogui.write(mes_formatado)
        pyautogui.write(ano)
        pyautogui.press('Enter')
        pyautogui.write(data_vencimento)
        pyautogui.click(x=799, y=298)
            
        # Lançando as taxas
        pyautogui.press('Enter',presses=3)
        for i in range(len(casas)):
            pyautogui.PAUSE = 0
            pyautogui.write(casas[i])
            pyautogui.press('Enter')
            pyautogui.write(protocolos[i])
            pyautogui.press('Enter')
            pyautogui.write(valores[i])
            pyautogui.press('Enter')
            pyautogui.press('down',presses=2)
            pyautogui.press('left',presses=4)
