import openpyxl
import os
import unicodedata
import pandas as pd
import re
from openpyxl.worksheet.table import Table
from datetime import datetime, timedelta

# Caminho dos arquivos
URL_ADMISSAO = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTRkuVSGXW_6OrUSwRte-vI3otElocyXR6adEDB6ngFJhi1b0glrnaOi01xI-MMq2DTgBXqa8NSlu5I/pub?gid=776761626&single=true&output=csv"
CAMINHO_EXCEL = r"QUADRO AUTOMATIZADO.xlsx"

def copiar_dados(data,linha, url_admissao, caminho_excel):
    # Ler os dados do Google Sheets
    df = pd.read_csv(url_admissao)

    # Abrir o arquivo Excel
    try:
        base_funcionarios = openpyxl.load_workbook(caminho_excel)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_excel}' não foi encontrado.")
        return

    aba_excel = base_funcionarios["QUADRO"]

    # Função para extrair texto entre parênteses
    def extrair_parenteses(texto):
        if isinstance(texto, str):
            match = re.search(r"\((.*?)\)", texto)
            return match.group(1).strip() if match else None
        return None
    def tratamento(valor):
        if valor in [1,2,3,4,5,7,10,13,15,16,22,28,32,36,37,41,42,43,44,"ESCRITORIO"]:
            matriz = "AL"
        else:
            matriz = "JR"    
        # Função para remover acentos e caracteres especiais
    def normalizar(texto):
        if not isinstance(texto, str):
            return texto
        texto = unicodedata.normalize("NFKD", texto).encode("ASCII", "ignore").decode("ASCII")
        return texto.upper()
    def calcular_datas30(data_inicial_str):
        try:
            data_inicial = datetime.strptime(data_inicial_str, "%d/%m/%Y")
            data_mais_29 = data_inicial + timedelta(days=29)
            return data_mais_29.strftime("%d/%m/%Y")
        except ValueError:
            print("Erro: Certifique-se de inserir a data no formato correto (DD/MM/AAAA).")
            return None
        
    def calcular_datas60(data_inicial_str):
        try:
            data_inicial = datetime.strptime(data_inicial_str, "%d/%m/%Y")
            data_mais_60 = data_inicial + timedelta(days=89)
            return data_mais_60.strftime("%d/%m/%Y")
        except ValueError:
            print("Erro: Certifique-se de inserir a data no formato correto (DD/MM/AAAA).")
            return None


    # Obter os valores da linha especificada
    try:
        nome = df.iloc[linha - 2, 1]  # Coluna B (NOME)
        cpf = df.iloc[linha - 2, 2]  # Coluna C (CPF)
        funcao = df.iloc[linha - 2, 11]  # Coluna L (FUNCAO)
        loja = extrair_parenteses(df.iloc[linha - 2, 13])  # Coluna N (LOJA)
        telefone = df.iloc[linha - 2, 19]  # Coluna S (TELEFONE)
        email = df.iloc[linha - 2, 17]  # Coluna Q (EMAIL)
        pix = df.iloc[linha - 2, 16]  # Coluna P (PIX)  
        optante_vt = df.iloc[linha - 2, 9]  # Coluna J (OPTANTE VT)
        data_nascimento = df.iloc[linha - 2, 20]  # Coluna T (NASCIMENTO)
    except IndexError:
        print(f"Erro: A linha {linha} está fora do intervalo de dados disponíveis.")
        return

    # Normalizar valores
    nome = normalizar(nome)
    funcao = normalizar(funcao)
    int(loja)
    matriz = tratamento(loja)
    data30 = calcular_datas30(data)
    data60 = calcular_datas60(data)


    # Adicionar os dados na tabela
    nova_linha = ["","Ativo", nome, cpf, loja, "", funcao, funcao, data,data30,data60,"","","","","","","","", pix, email, telefone, data_nascimento, optante_vt]
    adicionar_linha_na_tabela(aba_excel, nova_linha)

    # Salvar alterações
    base_funcionarios.save(caminho_excel)
    base_funcionarios.close()

    print(f"Dados copiados com sucesso para a linha {linha}. O arquivo foi atualizado.")

def adicionar_linha_na_tabela(aba, nova_linha):
    # Encontrar a tabela chamada "BASE"
    tabela = None
    for tabela_obj in aba.tables.values():
        if tabela_obj.name == "BASE":
            tabela = tabela_obj
            break

    if not tabela:
        print("Tabela 'BASE' não encontrada na aba 'QUADRO'.")
        return

    # Descobrir o próximo índice de linha da tabela
    ref = tabela.ref
    inicio, fim = ref.split(":")
    ultima_linha = int(fim[1:])  # Capturar o número da última linha na tabela

    # Adicionar nova linha na primeira coluna após o final da tabela
    for col_index, valor in enumerate(nova_linha, start=1):
        aba.cell(row=ultima_linha + 1, column=col_index, value=valor)

    # Atualizar o intervalo da tabela
    nova_ultima_linha = ultima_linha + 1
    tabela.ref = f"{inicio}:{fim[0]}{nova_ultima_linha}"  # Atualiza a referência


# Executar a função com entrada do usuário
linha = int(input("Digite o número da linha: "))
data = input("Digite a data: ")
copiar_dados(data,linha, URL_ADMISSAO, CAMINHO_EXCEL)

os.startfile(CAMINHO_EXCEL)