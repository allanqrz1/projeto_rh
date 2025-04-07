import openpyxl
import os
import unicodedata

def copiar_dados(linha):
    # Caminho dos arquivos
    caminho_arquivo1 = r"query_base.xlsm"
    caminho_arquivo2 = r"ficha.xlsm"

    # Diretório de destino na área de trabalho
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    nova_pasta = os.path.join(desktop, "Planilhas_Modificadas")
    os.makedirs(nova_pasta, exist_ok=True)
    

    # Abrir os arquivos Excel
    query_base = openpyxl.load_workbook(caminho_arquivo1)
    ficha = openpyxl.load_workbook(caminho_arquivo2)

    # Acessar as planilhas
    sheet_queryBase = query_base["admissao"]
    sheet_ficha = ficha["ficha"]
    sheet_ficha_conv = ficha["conversao_de_dados"]

    # Obter os valores da linha especificada
    nome = sheet_queryBase[f"B{linha}"].value or ""
    loja = sheet_queryBase[f"D{linha}"].value or ""
    vt = sheet_queryBase[f"E{linha}"].value or ""
    etnia = sheet_queryBase[f"G{linha}"].value or ""
    funcao = sheet_queryBase[f"H{linha}"].value or ""
    turno = sheet_queryBase[f"I{linha}"].value or ""
    data = sheet_queryBase[f'A{linha}'].value or ""
    email = sheet_queryBase[f'J{linha}'].value or ""
    endereco = sheet_queryBase[f'K{linha}'].value or ""

    # Função para remover acentos e caracteres especiais
    def normalizar(texto):
        if not isinstance(texto, str):
            return texto
        texto = unicodedata.normalize("NFKD", texto).encode("ASCII", "ignore").decode("ASCII")
        return texto.upper()

    # Normalizar valores
    nome = normalizar(nome)
    vt = normalizar(vt)
    funcao = normalizar(funcao)


    # Encontrar a primeira linha vazia na planilha "ficha"
    linha_destino = 2  # Começa a verificar a partir da linha 2
    while sheet_ficha[f"B{linha_destino}"].value:
        linha_destino += 1

    # Transferir os valores
    sheet_ficha["C7"] = nome
    sheet_ficha_conv["C1"] = loja
    sheet_ficha["G11"] = vt
    sheet_ficha_conv["D6"] = funcao
    sheet_ficha_conv["D4"] = turno
    sheet_ficha_conv['C5'] = data
    sheet_ficha['J10'] = etnia
    sheet_ficha['C8'] = email
    sheet_ficha['C9'] = endereco

    # Renomar arquivo
    novo_caminho_arquivo2 = os.path.join(nova_pasta, "FICHA - "f'{ nome}'".xlsx")

    # Remover arquivo existente se já existir
    if os.path.exists(novo_caminho_arquivo2):
        os.remove(novo_caminho_arquivo2)
        print("Arquivo existente removido com sucesso!")

    # Salvar alterações
    ficha.save(novo_caminho_arquivo2)
    query_base.close()
    ficha.close()
    os.startfile(novo_caminho_arquivo2)

    print(f"Dados copiados com sucesso! O arquivo foi salvo em: {novo_caminho_arquivo2}")



