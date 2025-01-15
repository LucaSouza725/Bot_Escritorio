from datetime import datetime, timedelta
import fitz  # PyMuPDF
import re
import pyautogui


def Verde(arquivo):
    # Substitua 'nome.pdf' pelo caminho correto do seu arquivo
    arquivo = 'verde.pdf'
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
        dia_vencimento = "07"

        # Usa o ano e mês originais para a data de vencimento
        data_vencimento = f"{dia_vencimento}{mes}{ano}"

        print(f"Mês de referência atrasado: {mes_referencia_atrasado}")
        print(f"Data de Vencimento: {data_vencimento}")
    else:
        print("Data de vencimento não encontrada.")

    # Expressão regular para capturar as salas, valores e borderos
    # BLOCO 1A
    padrao_bloco_1A = r"V 1-A (\d{3})\s+.*?Apto:\s*(\d+)(.*?)\n(?=V |\Z)"
    resultados_bloco_1A = re.findall(
        padrao_bloco_1A, texto_pdf, flags=re.DOTALL)

    # BLOCO 1B
    padrao_bloco_1B = r"V 1-B (\d{3})\s+.*?Apto:\s*(\d+)(.*?)\n(?=V |\Z)"
    resultados_bloco_1B = re.findall(
        padrao_bloco_1B, texto_pdf, flags=re.DOTALL)

    # BLOCO 2A
    padrao_bloco_2A = r"V 2-A (\d{3})\s+.*?Apto:\s*(\d+)(.*?)\n(?=V |\Z)"
    resultados_bloco_2A = re.findall(
        padrao_bloco_2A, texto_pdf, flags=re.DOTALL)

    # BLOCO 2B
    padrao_bloco_2B = r"V 2-B (\d{3})\s+.*?Apto:\s*(\d+)(.*?)\n(?=V |\Z)"
    resultados_bloco_2B = re.findall(
        padrao_bloco_2B, texto_pdf, flags=re.DOTALL)

    # BLOCO 3A
    padrao_bloco_3A = r"V 3-A (\d{3})\s+.*?Apto:\s*(\d+)(.*?)\n(?=V |\Z)"
    resultados_bloco_3A = re.findall(
        padrao_bloco_3A, texto_pdf, flags=re.DOTALL)

    # BLOCO 3B
    padrao_bloco_3B = r"V 3-B (\d{3})\s+.*?Apto:\s*(\d+)(.*?)\n(?=V |\Z)"
    resultados_bloco_3B = re.findall(
        padrao_bloco_3B, texto_pdf, flags=re.DOTALL)

    # BLOCO 3C
    padrao_bloco_3C = r"V 3-C (\d{3})\s+.*?Apto:\s*(\d+)(.*?)\n(?=V |\Z)"
    resultados_bloco_3C = re.findall(
        padrao_bloco_3C, texto_pdf, flags=re.DOTALL)

    # BLOCO 4A
    padrao_bloco_4A = r"V 4-A (\d{3})\s+.*?Apto:\s*(\d+)(.*?)\n(?=V |\Z)"
    resultados_bloco_4A = re.findall(
        padrao_bloco_4A, texto_pdf, flags=re.DOTALL)

    # BLOCO 4B
    padrao_bloco_4B = r"V 4-B (\d{3})\s+.*?Apto:\s*(\d+)(.*?)\n(?=V |\Z)"
    resultados_bloco_4B = re.findall(
        padrao_bloco_4B, texto_pdf, flags=re.DOTALL)

    # BLOCO 4C
    padrao_bloco_4C = r"V 4-C (\d{3})\s+.*?Apto:\s*(\d+)(.*?)\n(?=V |\Z)"
    resultados_bloco_4C = re.findall(
        padrao_bloco_4C, texto_pdf, flags=re.DOTALL)

    # Escolhendo o condomínio, mês de referência, e data de vencimento
    pyautogui.PAUSE = 2
    pyautogui.press('f5')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write('13')
    pyautogui.press('enter', presses=2)
    pyautogui.click(x=426, y=302)
    # Inserindo um novo condomínio/ou bloco na Bios
    pyautogui.PAUSE = 1.5
    pyautogui.click(x=510, y=298)
    pyautogui.write('13')
    pyautogui.press('Enter')
    pyautogui.write(mes_referencia_atrasado)
    pyautogui.write(ano)
    pyautogui.press('Enter')
    pyautogui.write(data_vencimento)
    pyautogui.press('Enter')
    pyautogui.write('1A')
    pyautogui.click(x=799, y=298)
    pyautogui.click(x=152, y=365)

    for resultado in resultados_bloco_1A:
        numero_sala, protocolo, conteudo_sala = resultado

        # Extraindo todos os valores numéricos da seção capturada
        valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

        # O último valor numérico é assumido como o valor total
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
    pyautogui.write('13')
    pyautogui.press('Enter')
    pyautogui.write(mes_referencia_atrasado)
    pyautogui.write(ano)
    pyautogui.press('Enter')
    pyautogui.write(data_vencimento)
    pyautogui.press('Enter')
    pyautogui.write('1B')
    pyautogui.click(x=799, y=298)
    pyautogui.click(x=152, y=365)

    for resultado in resultados_bloco_1B:
        numero_sala, protocolo, conteudo_sala = resultado

        # Extraindo todos os valores numéricos da seção capturada
        valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

        # O último valor numérico é assumido como o valor total
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
    pyautogui.write('13')
    pyautogui.press('Enter')
    pyautogui.write(mes_referencia_atrasado)
    pyautogui.write(ano)
    pyautogui.press('Enter')
    pyautogui.write(data_vencimento)
    pyautogui.press('Enter')
    pyautogui.write('2A')
    pyautogui.click(x=799, y=298)
    pyautogui.click(x=152, y=365)

    for resultado in resultados_bloco_2A:
        numero_sala, protocolo, conteudo_sala = resultado

        # Extraindo todos os valores numéricos da seção capturada
        valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

        # O último valor numérico é assumido como o valor total
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
    pyautogui.write('13')
    pyautogui.press('Enter')
    pyautogui.write(mes_referencia_atrasado)
    pyautogui.write(ano)
    pyautogui.press('Enter')
    pyautogui.write(data_vencimento)
    pyautogui.press('Enter')
    pyautogui.write('2B')
    pyautogui.click(x=799, y=298)
    pyautogui.click(x=152, y=365)

    for resultado in resultados_bloco_2B:
        numero_sala, protocolo, conteudo_sala = resultado

        # Extraindo todos os valores numéricos da seção capturada
        valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

        # O último valor numérico é assumido como o valor total
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
    pyautogui.write('13')
    pyautogui.press('Enter')
    pyautogui.write(mes_referencia_atrasado)
    pyautogui.write(ano)
    pyautogui.press('Enter')
    pyautogui.write(data_vencimento)
    pyautogui.press('Enter')
    pyautogui.write('3A')
    pyautogui.click(x=799, y=298)
    pyautogui.click(x=152, y=365)

    for resultado in resultados_bloco_3A:
        numero_sala, protocolo, conteudo_sala = resultado

        # Extraindo todos os valores numéricos da seção capturada
        valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

        # O último valor numérico é assumido como o valor total
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
    pyautogui.write('13')
    pyautogui.press('Enter')
    pyautogui.write(mes_referencia_atrasado)
    pyautogui.write(ano)
    pyautogui.press('Enter')
    pyautogui.write(data_vencimento)
    pyautogui.press('Enter')
    pyautogui.write('3B')
    pyautogui.click(x=799, y=298)
    pyautogui.click(x=152, y=365)

    for resultado in resultados_bloco_3B:
        numero_sala, protocolo, conteudo_sala = resultado

        # Extraindo todos os valores numéricos da seção capturada
        valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

        # O último valor numérico é assumido como o valor total
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
    pyautogui.write('13')
    pyautogui.press('Enter')
    pyautogui.write(mes_referencia_atrasado)
    pyautogui.write(ano)
    pyautogui.press('Enter')
    pyautogui.write(data_vencimento)
    pyautogui.press('Enter')
    pyautogui.write('3C')
    pyautogui.click(x=799, y=298)
    pyautogui.click(x=152, y=365)

    for resultado in resultados_bloco_3C:
        numero_sala, protocolo, conteudo_sala = resultado

        # Extraindo todos os valores numéricos da seção capturada
        valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

        # O último valor numérico é assumido como o valor total
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
    pyautogui.write('13')
    pyautogui.press('Enter')
    pyautogui.write(mes_referencia_atrasado)
    pyautogui.write(ano)
    pyautogui.press('Enter')
    pyautogui.write(data_vencimento)
    pyautogui.press('Enter')
    pyautogui.write('4A')
    pyautogui.click(x=799, y=298)
    pyautogui.click(x=152, y=365)

    for resultado in resultados_bloco_4A:
        numero_sala, protocolo, conteudo_sala = resultado

        # Extraindo todos os valores numéricos da seção capturada
        valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

        # O último valor numérico é assumido como o valor total
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
    pyautogui.write('13')
    pyautogui.press('Enter')
    pyautogui.write(mes_referencia_atrasado)
    pyautogui.write(ano)
    pyautogui.press('Enter')
    pyautogui.write(data_vencimento)
    pyautogui.press('Enter')
    pyautogui.write('4B')
    pyautogui.click(x=799, y=298)
    pyautogui.click(x=152, y=365)

    for resultado in resultados_bloco_4B:
        numero_sala, protocolo, conteudo_sala = resultado

        # Extraindo todos os valores numéricos da seção capturada
        valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

        # O último valor numérico é assumido como o valor total
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
    pyautogui.write('13')
    pyautogui.press('Enter')
    pyautogui.write(mes_referencia_atrasado)
    pyautogui.write(ano)
    pyautogui.press('Enter')
    pyautogui.write(data_vencimento)
    pyautogui.press('Enter')
    pyautogui.write('4C')
    pyautogui.click(x=799, y=298)
    pyautogui.click(x=152, y=365)

    for resultado in resultados_bloco_4C:
        numero_sala, protocolo, conteudo_sala = resultado

        protocolo = protocolo.lstrip('0')

        valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

        if 'Total:' in conteudo_sala:
            valores = valores[:-1]

        valor_total = valores[-1] if valores else "Valor não encontrado"

        pyautogui.PAUSE = 0.5
        pyautogui.write(numero_sala)
        pyautogui.press('Enter')
        pyautogui.write("0" + protocolo)
        pyautogui.press('Enter')
        pyautogui.write(valor_total)
        pyautogui.press('Enter')
        pyautogui.press('down', presses=2)
        pyautogui.press('left', presses=4)
