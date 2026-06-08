"""
Sistema de Gerenciamento de Biblioteca Digital
Biblioteca universitária — manipulação de documentos digitais.
"""

import os
import re

# Pasta raiz onde todos os documentos ficam armazenados
PASTA_DOCUMENTOS = "documentos"


def listar_por_tipo():
    """Lista todos os documentos da biblioteca organizados por tipo de arquivo."""
    documentos_por_tipo = {}  # dicionário: extensão -> lista de nomes de arquivos

    # os.walk percorre a pasta e todas as subpastas automaticamente
    for pasta, subpastas, arquivos in os.walk(PASTA_DOCUMENTOS):
        for arquivo in arquivos:
            # Ignora arquivos ocultos como .gitkeep
            if arquivo.startswith("."):
                continue

            # os.path.splitext separa o nome da extensão: "artigo.pdf" -> ("artigo", ".pdf")
            _, extensao = os.path.splitext(arquivo)
            extensao = extensao.lower()  # garante que .PDF e .pdf sejam tratados igual

            # Se essa extensão ainda não existe no dicionário, cria uma lista vazia
            if extensao not in documentos_por_tipo:
                documentos_por_tipo[extensao] = []

            documentos_por_tipo[extensao].append(arquivo)

    # Avisa se a biblioteca estiver vazia
    if not documentos_por_tipo:
        print("Nenhum documento encontrado na biblioteca.")
        return

    print("\n=== Documentos por Tipo ===")
    for tipo, arquivos in sorted(documentos_por_tipo.items()):
        rotulo = tipo.upper() if tipo else "SEM EXTENSÃO"
        print(f"\n[{rotulo}] — {len(arquivos)} arquivo(s):")
        for arquivo in sorted(arquivos):
            print(f"  - {arquivo}")


def extrair_ano(nome_arquivo):
    """Procura um ano (4 dígitos entre 1900 e 2099) no nome do arquivo.

    Retorna o ano como string, ou "Ano desconhecido" se não encontrar.
    """
    # re.search busca o padrão em qualquer posição do texto
    # \\b marca fronteira de palavra, evita pegar "12023" como "2023"
    resultado = re.search(r"\b(19\d{2}|20\d{2})\b", nome_arquivo)
    if resultado:
        return resultado.group(1)  # retorna só o trecho que casou com o padrão
    return "Ano desconhecido"


def listar_por_ano():
    """Lista todos os documentos da biblioteca organizados por ano de publicação."""
    documentos_por_ano = {}  # dicionário: ano -> lista de nomes de arquivos

    for pasta, subpastas, arquivos in os.walk(PASTA_DOCUMENTOS):
        for arquivo in arquivos:
            if arquivo.startswith("."):
                continue

            ano = extrair_ano(arquivo)

            if ano not in documentos_por_ano:
                documentos_por_ano[ano] = []

            documentos_por_ano[ano].append(arquivo)

    if not documentos_por_ano:
        print("Nenhum documento encontrado na biblioteca.")
        return

    print("\n=== Documentos por Ano ===")
    # sorted coloca "Ano desconhecido" no final porque letras vêm depois de números
    for ano in sorted(documentos_por_ano.keys()):
        print(f"\n[{ano}] — {len(documentos_por_ano[ano])} arquivo(s):")
        for arquivo in sorted(documentos_por_ano[ano]):
            print(f"  - {arquivo}")
