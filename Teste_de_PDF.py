import fitz  # PyMuPDF

arquivo_pdf = 'minas.pdf'
pdf = fitz.open(arquivo_pdf)

# Verifica todas as páginas
for num_pagina in range(len(pdf)):
    pagina = pdf[num_pagina]
    texto = pagina.get_text("text")  # Extrai o texto bruto

    print(f"📄 Página {num_pagina +
          1} (Tamanho: {len(texto)} caracteres)\n{'-'*50}")
    # Mostra apenas os primeiros 1000 caracteres para evitar flood
    print(texto[:1000])
    print("\n\n")

pdf.close()
