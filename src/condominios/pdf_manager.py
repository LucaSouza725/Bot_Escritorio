import os


def get_pdf_path(pdf_filename):
    """
    Retorna o caminho absoluto para um arquivo PDF dentro de resources/documents.
    """
    # Obtém o caminho absoluto até a pasta onde este script (pdf_manager.py) está localizado
    base_path = os.path.abspath(os.path.join(os.path.dirname(
        __file__), "..", "..", "resources", "documents"))

    # Retorna o caminho completo do PDF
    return os.path.join(base_path, pdf_filename)
