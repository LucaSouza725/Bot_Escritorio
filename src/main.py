import subprocess
import pyautogui
import sys
import os
import time

# Obtém o diretório raiz do projeto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona o diretório `src` ao sys.path
sys.path.append(BASE_DIR)

# Importando cada condomínio ao código principal
from condominios.Minas_Bank import Minas
from condominios.NW_FR import New_World_FR
from condominios.Clave import Clave_do_Sol
from condominios.Buena_Vista import Buena_vista
from condominios.Bahia_Blanca import Bahia_blanca
from condominios.Bahamas import Bahamas
from condominios.Aldeia import Aldeia_bueno
from condominios.Jacuma import Jacuma
from condominios.Icaro import Icaro
from condominios.Harvard import Harvard
from condominios.Gardenia import Gardenia
from condominios.Verde import Verde
from condominios.Prive import Prive
from condominios.Acres import Acres
from condominios.NW import New_World
from condominios.JK_FR import Juscelino_Kubitschek_FR
from condominios.JK import Juscelino_Kubitschek
from condominios.Capixaba import Capixaba
from condominios.Anna_Luiza_Rateio import Anna_Luiza_Rateio
from condominios.Anna_Luiza import Anna_Luiza
from condominios.DJ import Dj_oliveira
from condominios.Mirante import Mirante_do_Bosque
from condominios.Marcela import Marcela
from condominios.Ingrid import Ingred_Bergman
from condominios.Ilha_Bela import Ilha_bela
from condominios.Bello import Bello_Trindade
from condominios.Indiapora import Indiapora
from condominios.Indiapora_Rateio import Indiapora_rateio
from condominios.Lyceu import Lyceu
from condominios.Monte_Libano import Monte_libano
from condominios.Tocantins import Tocantins

# Função que abrirá a BIOS no computador
def abrir_programa(program_path):
    try:
        # Verifica se o arquivo existe no caminho especificado
        if os.path.isfile(program_path):
            # Abre o programa usando uma lista de argumentos
            subprocess.Popen([program_path], cwd=os.path.dirname(program_path))
            print(f"Programa {program_path} aberto com sucesso.")
        else:
            print(f"O caminho {program_path} não existe.")
            # Sai do programa com código de status 1 (indica um erro)
            sys.exit(1)
    except FileNotFoundError as e:
        print(f"Ocorreu um erro ao tentar abrir o programa: {e}")
        sys.exit(1)  # Sai do programa com código de status 1 (indica um erro)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)  # Sai do programa com código de status 1 (indica um erro)


program_path = r"C:\BIOS INFO\BIOSFin.exe"


def listar_pdfs():
    # Esta função lista todos os arquivos PDFs na pasta atual
    diretorio = os.getcwd()
    arquivos = os.listdir(diretorio)
    # Filtra apenas os PDFs
    arquivos_pdf = [
        arquivo for arquivo in arquivos if arquivo.endswith('.pdf')]
    return arquivos_pdf


def extrair_nome(nome_arquivo):
    # Extrai o nome do condomínio do nome do arquivo
    return nome_arquivo.replace(".pdf", "")


pyautogui.FAILSAFE = False

# Lista todos os PDFs da pasta
arquivos_pdf = listar_pdfs()

# Dicionário de condomínios e suas funções correspondentes
condominios = {
    "anna luiza": Anna_Luiza,
    "anna luiza rateio": Anna_Luiza_Rateio,
    "capixaba": Capixaba,
    "jk": Juscelino_Kubitschek,
    "jk fd reserva": Juscelino_Kubitschek_FR,
    "nw": New_World,
    "acres": Acres,
    "prive": Prive,
    "verde": Verde,
    "gardenia": Gardenia,
    "harvard": Harvard,
    "icaro": Icaro,
    "jacuma": Jacuma,
    "aldeia": Aldeia_bueno,
    "bahamas": Bahamas,
    "bahia": Bahia_blanca,
    "buena vista": Buena_vista,
    "clave": Clave_do_Sol,
    "dj": Dj_oliveira,
    "mirante": Mirante_do_Bosque,
    "marcela": Marcela,
    "ingrid": Ingred_Bergman,
    "ilha bela": Ilha_bela,
    "bello": Bello_Trindade,
    "indiapora": Indiapora,
    "indiapora rateio": Indiapora_rateio,
    "lyceu": Lyceu,
    "monte libano": Monte_libano,
    "tocantins": Tocantins,
    "nw fd reserva": New_World_FR,
    "minas": Minas,
    # Adicione outros condomínios conforme necessário
}

# Agora vamos para as ações na BIOS
pyautogui.PAUSE = 1

# Abrindo a Bios
abrir_programa(program_path)

# Colocando a Senha na Bios primeira vez
time.sleep(8)
pyautogui.click(x=367, y=41)
pyautogui.write("725725")
pyautogui.press("Enter")
time.sleep(10)

# Abrindo a Bios
abrir_programa(program_path)

# Colocando a Senha na Bios
time.sleep(8)
pyautogui.click(x=367, y=41)
pyautogui.write("725725")
pyautogui.press("Enter")
time.sleep(10)

# Abrindo o condomínio
pyautogui.click(x=336, y=335)
pyautogui.press('alt')
pyautogui.press('1')
pyautogui.press('3')
pyautogui.press('4')
# Processa cada arquivo PDF na lista
for pdf in arquivos_pdf:
    # Obtem o nome do condominio a partir do nome do arquivo
    nome_condominio = extrair_nome(pdf)
    # Verifica se o Condomínio está no
    # Dicionário
    if nome_condominio in condominios:
        # Processa o arquivo PDF com a função correspondente ao condomínio
        condominios[nome_condominio](pdf)
        # Remove o arquivo PDF após processá-lo
        try:
            os.remove(pdf)
            print(f"Arquivo removido com sucesso: {pdf}")
        except OSError as e:
            print(f"Erro ao remover o arquivo {pdf}: {e.strerror}")
    else:
        print("Condomínio não encontrado:", nome_condominio)
