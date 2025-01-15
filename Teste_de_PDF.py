import fitz  # Importa a biblioteca PyMuPDF

# Substitua 'seu_arquivo.pdf' pelo caminho até o seu arquivo PDF
arquivo_pdf = 'indiapora.pdf'

# Abre o arquivo PDF
pdf = fitz.open(arquivo_pdf)

# Itera por cada página do PDF
for num_pagina, pagina in enumerate(pdf, start=1):
    texto = pagina.get_text()  # Obtém o texto da página
    print(f"Página {num_pagina}:\n{texto}\n")  # Imprime o texto da página

# Fecha o documento PDF
pdf.close()
