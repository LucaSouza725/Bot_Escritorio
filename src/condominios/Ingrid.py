from datetime import datetime, timedelta
import fitz  # PyMuPDF
import re
import pyautogui


def Ingred_Bergman(arquivo):
    arquivo = 'ingrid.pdf'
    pdf = fitz.open(arquivo)
    lista_texto_paginas = []  # Lista para armazenar o texto de cada página
    for pagina in pdf:  # Percorre todas as páginas do documento
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
        dia_vencimento = "20"

        # Usa o ano e mês originais para a data de vencimento
        data_vencimento = f"{dia_vencimento}{mes}{ano}"

        print(f"Mês de referência atrasado: {mes_referencia_atrasado}")
        print(f"Data de Vencimento: {data_vencimento}")
    else:
        print("Data de vencimento não encontrada.")

    # Expressão regular para capturar as salas, valores e borderos
    # Expressão regular atualizada para capturar as seções com base na palavra "Apto:"
    secoes = re.split(r'Apto:\s*\n', texto_pdf)

    padrao_valores = r"(\d{1,3}(?:\.\d{3})*,\d{2})"
    # Atualizado para capturar o número completo do apartamento
    padrao_apto = r"(\d{16})"

    # Escolhendo o condomínio, mês de referência, e data de vencimento
    pyautogui.PAUSE = 2
    pyautogui.press('f5')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write('27')
    pyautogui.press('enter', presses=2)
    pyautogui.click(x=426, y=302)
    # Inserindo um novo condomínio/ou bloco na Bios
    pyautogui.PAUSE = 1.5
    pyautogui.click(x=510, y=298)
    pyautogui.write('27')
    pyautogui.press('Enter')
    pyautogui.write(mes)
    pyautogui.write(ano)
    pyautogui.press('Enter')
    pyautogui.write(data_vencimento)
    pyautogui.press('Enter')
    pyautogui.click(x=799, y=298)
    pyautogui.click(x=152, y=365)

    pyautogui.PAUSE = 0.5

    for i, secao in enumerate(secoes[1:], start=1):  # Começa da segunda seção
        apto_match = re.search(padrao_apto, secao)
        valores = re.findall(padrao_valores, secao)

        if apto_match and valores:
            protocolo = apto_match.group(1).lstrip('0')
            valor_total = valores[-2] if i == len(
                secoes[1:]) and len(valores) > 1 else valores[-1]

            pyautogui.write(f"{i:02}00")  # Formata i com dois dígitos
            pyautogui.press('Enter')
            pyautogui.write(f"000{protocolo}")
            pyautogui.press('Enter')
            pyautogui.write(valor_total)
            pyautogui.press('Enter')
            pyautogui.press('down', presses=2)
            pyautogui.press('left', presses=4)
