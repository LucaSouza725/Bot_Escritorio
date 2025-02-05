from datetime import datetime  # Removida a duplicidade de importação
import fitz  # PyMuPDF
import re
import pyautogui


def Juscelino_Kubitschek_FR(arquivo):
    # Substitua 'jk.pdf' pelo caminho correto do seu arquivo
    arquivo = 'jk fd reserva.pdf'
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
        dia_vencimento = "05"

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

    # Encontra todas as seções de garagem no texto
    secoes_garagem = re.findall(padrao_garagens, texto_pdf, flags=re.DOTALL)

    # Escolhendo o condomínio, mês de referência, e data de vencimento
    pyautogui.PAUSE = 2
    pyautogui.press('f5')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write('60')
    pyautogui.press('enter', presses=2)
    pyautogui.click(x=426, y=302)
    # Inserindo um novo condomínio/ou bloco na Bios
    pyautogui.PAUSE = 1.5
    pyautogui.click(x=510, y=298)
    pyautogui.write('60')
    pyautogui.press('Enter')
    pyautogui.write(mes)
    pyautogui.write(ano)
    pyautogui.press('Enter')
    pyautogui.write(data_vencimento)
    pyautogui.press('Enter')
    pyautogui.write('F RES')
    pyautogui.click(x=799, y=298)
    pyautogui.press('tab', presses=2)
    for resultado in resultados_salas:
        numero_sala, protocolo, conteudo_sala = resultado

        # Extraindo todos os valores numéricos da seção capturada
        valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

        # O último valor numérico é assumido como o valor total
        valor_total = valores[-1] if valores else "Valor não encontrado"

        pyautogui.PAUSE = 0.5
        pyautogui.write(numero_sala)
        pyautogui.press('Enter')
        pyautogui.write("0"+protocolo)
        pyautogui.press('Enter')
        pyautogui.write(valor_total)
        pyautogui.press('Enter')
        pyautogui.press('down', presses=2)
        pyautogui.press('left', presses=4)
    # Inserindo um novo condomínio/ou bloco na Bios
    pyautogui.PAUSE = 1.5
    pyautogui.click(x=510, y=298)
    pyautogui.write('60')
    pyautogui.press('Enter')
    pyautogui.write(mes)
    pyautogui.write(ano)
    pyautogui.press('Enter')
    pyautogui.write(data_vencimento)
    pyautogui.press('Enter')
    pyautogui.write("FR GA")
    pyautogui.click(x=799, y=298)
    pyautogui.press('Tab', presses=2)

    for secao in secoes_garagem:
        numero_garagem, protocolo, conteudo_garagem = secao
        # Encontra todos os valores numéricos na seção da garagem
        valores = re.findall(r"-?\d{1,3}(?:\.\d{3})*,\d{2}", conteudo_garagem)

        # Se há mais de um valor, seleciona o penúltimo como o valor relevante
        if len(valores) >= 2:
            valor_relevante = valores[-2]
        else:
            valor_relevante = valores[0] if valores else "Valor não encontrado"
        pyautogui.PAUSE = 0.5
        pyautogui.write(numero_garagem)
        pyautogui.press('Enter')
        pyautogui.write("0"+protocolo)
        pyautogui.press('Enter')
        pyautogui.write(valor_relevante)
        pyautogui.press('Enter')
        pyautogui.press('down', presses=2)
        pyautogui.press('left', presses=4)

    for deposito, protocolo, valor in resultados:
        # Inserindo um novo condomínio/ou bloco na Bios para cada subsolo
        pyautogui.PAUSE = 1.5
        pyautogui.click(x=510, y=298)
        pyautogui.write('60')
        pyautogui.press('Enter')
        pyautogui.write(mes)
        pyautogui.write(ano)
        pyautogui.press('Enter')
        pyautogui.write(data_vencimento)
        pyautogui.press('Enter')
        pyautogui.write(f"SUB{deposito}")
        pyautogui.click(x=799, y=298)
        pyautogui.press('Tab', presses=2)
        pyautogui.PAUSE = 0.5
        pyautogui.write(deposito)
        pyautogui.press('Enter')
        pyautogui.write("0"+protocolo)
        pyautogui.press('Enter')
        pyautogui.write(valor)
        pyautogui.press('Enter')
        pyautogui.press('down', presses=2)
        pyautogui.press('left', presses=4)

    # Inserindo um novo condomínio/ou bloco na Bios
    pyautogui.PAUSE = 1.5
    pyautogui.click(x=510, y=298)
    pyautogui.write('60')
    pyautogui.press('Enter')
    pyautogui.write(mes)
    pyautogui.write(ano)
    pyautogui.press('Enter')
    pyautogui.write(data_vencimento)
    pyautogui.press('Enter')
    pyautogui.write("F BIS")
    pyautogui.click(x=799, y=298)
    pyautogui.press('Tab', presses=2)
    for bistro in resultados_bistro:
        # Extrair todos os valores numéricos da seção do Bistrô
        valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", bistro)
        valor_total = valores[-1] if valores else "Valor não encontrado"
        pyautogui.PAUSE = 0.5
        pyautogui.write(f"0001")
        pyautogui.press('Enter')
        pyautogui.write("0"+protocolo)
        pyautogui.press('Enter')
        pyautogui.write(valor_total)
        pyautogui.press('Enter')
        pyautogui.press('down', presses=2)
        pyautogui.press('left', presses=4)
