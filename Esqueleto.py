from datetime import datetime, timedelta
import fitz  # PyMuPDF
import re

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


# Substitua 'nome.pdf' pelo caminho correto do seu arquivo
arquivo = 'anna luiza rateio.pdf'
pdf = fitz.open(arquivo)
lista_texto_paginas = []  # Lista para armazenar o texto de cada página
for pagina in pdf:  # Percorre todas as páginas do documento
    texto = pagina.get_text()
    lista_texto_paginas.append(texto)  # Adiciona o texto da página à lista
texto_pdf = ''.join(lista_texto_paginas)  # Combina o texto de todas as páginas

# Expressão regular para encontrar a data de vencimento (formato mm/aaaa)
padrao_referencia_mensal = r"\b(\d{2}/\d{4})\b"
mes_referencia = re.search(padrao_referencia_mensal, texto_pdf)
# Inicializando o contador
valor_do_contador = incrementar_contador()

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
padrao_salas = r"ALUIZA\s+(\d+)\s+.*?Apto:\s*(\d+)\s+(.*?)\n(?=ALUIZA|\Z)"
resultados_salas = re.findall(padrao_salas, texto_pdf, flags=re.DOTALL)

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

    print(f"Rateio: R{valor_do_contador}/12")
    print(f"Número do Apartamento: {numero_sala}")
    print(f"Protocolo: {protocolo}")
    print(f"Valor: {valor_total}\n")
