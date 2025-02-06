import fitz  # PyMuPDF
import re
import pyautogui

# Contador para saber qual o numero do rateio que será feito


def obter_contador():
    try:
        with open("contadorAL.txt", "r") as file:
            contador = int(file.read())
    except FileNotFoundError:
        contador = 0
    return contador


def incrementar_contador():
    contador = obter_contador()
    contador += 1
    with open("contadorAL.txt", "w") as file:
        file.write(str(contador))
    return contador
# Finalização do contador


def Anna_Luiza_Rateio(arquivo):
    # Substitua 'nome.pdf' pelo caminho correto do seu arquivo
    arquivo = 'anna luiza rateio.pdf'
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
    # Inicializando o contador
    valor_do_contador = incrementar_contador()

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

    # Expressão regular para capturar as salas, valores e borderos
    padrao_salas = r"ALUIZA\s+(\d+)\s+.*?Apto:\s*(\d+)\s+(.*?)\n(?=ALUIZA|\Z)"
    resultados_salas = re.findall(padrao_salas, texto_pdf, flags=re.DOTALL)

    # Escolhendo o condomínio, mês de referência, e data de vencimento
    pyautogui.PAUSE = 2
    pyautogui.press('f5')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write('19')
    pyautogui.press('enter', presses=2)
    pyautogui.click(x=426, y=302)

    # Inserindo um novo condomínio/ou bloco na Bios
    pyautogui.PAUSE = 1.5
    pyautogui.click(x=510, y=298)
    pyautogui.write('19')
    pyautogui.press('Enter')
    pyautogui.write(mes)
    pyautogui.write(ano)
    pyautogui.press('Enter')
    pyautogui.write(data_vencimento)
    pyautogui.press('Enter')
    pyautogui.write(f'R{valor_do_contador}/12')
    pyautogui.click(x=799, y=298)
    pyautogui.press('Tab', presses=2)

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
