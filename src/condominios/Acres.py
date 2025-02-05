import fitz  # PyMuPDF
import re
import pyautogui

def Acres(arquivo):
    # Substitua 'nome.pdf' pelo caminho correto do seu arquivo
    arquivo = 'acres.pdf'
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
        dia_vencimento = "20"

        # Formata a data de vencimento no formato ddmmaaaa
        data_vencimento = f"{dia_vencimento}{mes}{ano}"

        print(f"Mês de referência: {mes}{ano}")
        print(f"Data de Vencimento armazenada como: {data_vencimento}")
    else:
        print("Data de vencimento não encontrada.")

    # Padrão atualizado para capturar o identificador da sala, número do apartamento e o último valor total
    secoes = re.split(r'\n(?=\d{2}\s)', texto_pdf)

    padrao_valores = r"(\d{1,3}(?:\.\d{3})*,\d{2})"
    padrao_apto = r"Apto:\s*(\d+)"

    # Escolhendo o condomínio, mês de referência, e data de vencimento
    pyautogui.PAUSE = 2
    pyautogui.press('f5')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write('30')
    pyautogui.press('enter', presses=2)
    pyautogui.click(x=426, y=302)
    # Inserindo um novo condomínio/ou bloco na Bios
    pyautogui.PAUSE = 1.5
    pyautogui.click(x=510, y=298)
    pyautogui.write('30')
    pyautogui.press('Enter')
    pyautogui.write(mes)
    pyautogui.write(ano)
    pyautogui.press('Enter')
    pyautogui.write(data_vencimento)
    pyautogui.press('Enter')
    pyautogui.click(x=799, y=298)
    pyautogui.click(x=152, y=365)
    
    pyautogui.PAUSE = 0.5

    for i, secao in enumerate(secoes, start=1):
        apto_match = re.search(padrao_apto, secao)
        valores = re.findall(padrao_valores, secao)
        
        if apto_match and valores:
            protocolo = apto_match.group(1).lstrip('0')
            valor_total = valores[-2] if i == len(secoes) and len(valores) > 1 else valores[-1]
            
            pyautogui.write(f"{i-1:02}")  # Formata i com dois dígitos
            pyautogui.press('Enter')
            pyautogui.write(protocolo)
            pyautogui.press('Enter')
            pyautogui.write(valor_total)
            pyautogui.press('Enter')
            pyautogui.press('down', presses=2)
            pyautogui.press('left', presses=4)