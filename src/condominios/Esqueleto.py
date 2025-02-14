import fitz  # PyMuPDF
from datetime import datetime, timedelta
import re
import os
import sys

# Obtém o diretório da pasta `src`
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona `src` ao caminho de importação
sys.path.append(BASE_DIR)

# Importação do módulo
from condominios.pdf_manager import get_pdf_path

# Nome do arquivo PDF
pdf_filename = "capixaba.pdf"

# Obtendo o caminho do PDF
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

        # Expressão regular para encontrar a data de vencimento (formato mm/aaaa)
        # ATENÇÃO: o mês de referência é atrasado
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
            dia_vencimento = "15"

            # Usa o ano e mês originais para a data de vencimento
            data_vencimento = f"{dia_vencimento}{mes}{ano}"

            print(f"Mês de referência atrasado: {mes_referencia_atrasado}")
            print(f"Data de Vencimento: {data_vencimento}")
        else:
            print("Data de vencimento não encontrada.")

        padrao_salas = r"Casa: (?:LJ )?(\d+|[\d]{4}(?:[-/][\d]{1,4})*)\s.*?Apto:\s*(\d+)(.*?)(?=Casa:| Total:|$)"
        resultados_salas = re.findall(padrao_salas, texto_pdf, flags=re.DOTALL)

        for resultado in resultados_salas:
            numero_sala, protocolo, conteudo_sala = resultado

            # Formata o número da sala para ter 4 dígitos
            numero_sala_formatado = numero_sala.zfill(2)

            # Extraindo todos os valores numéricos da seção capturada
            valores = re.findall(r"(\d{1,3}(?:\.\d{3})*,\d{2})", conteudo_sala)

            # Excluindo o último valor numérico se ele pertencer ao total geral e não ao total da sala
            # Esta lógica assume que o "Total Geral" é sempre o último valor no documento e não pertence a nenhuma sala
            if 'Total:' in conteudo_sala:
                valores = valores[:-1]

            # O último valor numérico é assumido como o valor total da sala
            valor_total = valores[-1] if valores else "Valor não encontrado"

            print(f"Sala: {numero_sala_formatado}")
            print(f"Protocolo: {protocolo}")
            print(f"Valor Total: {valor_total}\n")
