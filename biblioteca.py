"""
Sistema de Gerenciamento de Biblioteca Digital
Biblioteca universitária — manipulação de documentos digitais.
"""

import os

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
