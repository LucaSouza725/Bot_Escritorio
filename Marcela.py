from datetime import datetime, timedelta
import fitz  # PyMuPDF
import re
import pyautogui


def Marcela(arquivo):
    # Substitua 'nome.pdf' pelo caminho correto do seu arquivo
    arquivo = 'marcela.pdf'
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
        dia_vencimento = "05"

        # Usa o ano e mês originais para a data de vencimento
        data_vencimento = f"{dia_vencimento}{mes}{ano}"

        print(f"Mês de referência atrasado: {mes_referencia_atrasado}")
        print(f"Data de Vencimento: {data_vencimento}")
    else:
        print("Data de vencimento não encontrada.")

    # Expressão regular para capturar as salas, valores e borderos
    padrao_salas = r"M (\d{4}(?:-\d{2,4})?)\s+.*?Apto:\s*(\d+)(.*?)\n(?=M|\Z)"
    resultados_salas = re.findall(padrao_salas, texto_pdf, flags=re.DOTALL)

    # Escolhendo o condomínio, mês de referência, e data de vencimento
    pyautogui.PAUSE = 2
    pyautogui.press('f5')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write('66')
    pyautogui.press('enter', presses=2)
    pyautogui.click(x=426, y=302)
    # Inserindo um novo condomínio/ou bloco na Bios
    pyautogui.PAUSE = 1.5
    pyautogui.click(x=510, y=298)
    pyautogui.write('66')
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

        # Excluindo o último valor numérico se ele pertencer ao total geral e não ao total da sala
        # Esta lógica assume que o "Total Geral" é sempre o último valor no documento e não pertence a nenhuma sala
        if 'Total:' in conteudo_sala:
            # Remove o último valor, que é o total geral do documento
            valores = valores[:-1]

        # O último valor numérico é assumido como o valor total da sala
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
