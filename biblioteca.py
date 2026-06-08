"""
Sistema de Gerenciamento de Biblioteca Digital
Biblioteca universitária — manipulação de documentos digitais.
"""

import os
import re
import shutil

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


def adicionar_documento(caminho_origem):
    """Copia um documento para a subpasta correta da biblioteca.

    Detecta a extensão do arquivo e o coloca em documentos/pdf,
    documentos/epub ou documentos/outros automaticamente.
    """
    # Verifica se o arquivo de origem realmente existe
    if not os.path.isfile(caminho_origem):
        print(f"Erro: arquivo '{caminho_origem}' não encontrado.")
        return

    nome_arquivo = os.path.basename(caminho_origem)  # extrai só o nome: "artigo_2023.pdf"
    _, extensao = os.path.splitext(nome_arquivo)
    extensao = extensao.lower()

    # Define em qual subpasta o arquivo deve ir
    if extensao == ".pdf":
        subpasta = "pdf"
    elif extensao == ".epub":
        subpasta = "epub"
    else:
        subpasta = "outros"

    destino = os.path.join(PASTA_DOCUMENTOS, subpasta, nome_arquivo)

    # Evita sobrescrever um arquivo que já existe
    if os.path.exists(destino):
        print(f"Aviso: '{nome_arquivo}' já existe em documentos/{subpasta}/.")
        return

    shutil.copy2(caminho_origem, destino)  # copy2 preserva data de modificação original
    print(f"Documento '{nome_arquivo}' adicionado em documentos/{subpasta}/.")


def renomear_documento(nome_atual, nome_novo):
    """Renomeia um documento dentro da biblioteca.

    Busca o arquivo em todas as subpastas automaticamente.
    Mantém o arquivo na mesma subpasta após renomear.
    """
    caminho_atual = None

    # Percorre toda a biblioteca procurando o arquivo pelo nome
    for pasta, subpastas, arquivos in os.walk(PASTA_DOCUMENTOS):
        if nome_atual in arquivos:
            caminho_atual = os.path.join(pasta, nome_atual)
            break  # encontrou, não precisa continuar procurando

    if caminho_atual is None:
        print(f"Erro: '{nome_atual}' não encontrado na biblioteca.")
        return

    # Monta o caminho de destino na mesma pasta do arquivo original
    pasta_do_arquivo = os.path.dirname(caminho_atual)
    caminho_novo = os.path.join(pasta_do_arquivo, nome_novo)

    # Garante que o novo nome não está sendo usado por outro arquivo
    if os.path.exists(caminho_novo):
        print(f"Erro: já existe um arquivo chamado '{nome_novo}' nessa pasta.")
        return

    os.rename(caminho_atual, caminho_novo)
    print(f"'{nome_atual}' renomeado para '{nome_novo}' com sucesso.")


def remover_documento(nome_arquivo):
    """Remove um documento da biblioteca após confirmação do usuário.

    Busca o arquivo em todas as subpastas automaticamente.
    Pede confirmação antes de deletar para evitar remoções acidentais.
    """
    caminho_arquivo = None

    for pasta, subpastas, arquivos in os.walk(PASTA_DOCUMENTOS):
        if nome_arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            break

    if caminho_arquivo is None:
        print(f"Erro: '{nome_arquivo}' não encontrado na biblioteca.")
        return

    # Mostra onde o arquivo está antes de pedir confirmação
    print(f"Arquivo encontrado: {caminho_arquivo}")
    confirmacao = input(f"Tem certeza que deseja remover '{nome_arquivo}'? (s/n): ")

    # Só remove se o usuário digitar exatamente "s"
    if confirmacao.lower() == "s":
        os.remove(caminho_arquivo)
        print(f"'{nome_arquivo}' removido com sucesso.")
    else:
        print("Remoção cancelada.")


# ── Funções de Diretório ──────────────────────────────────────────────────────

def listar_diretorios():
    """Lista todas as subpastas existentes dentro da biblioteca."""
    print("\n=== Diretórios da Biblioteca ===")

    # os.listdir retorna nomes de tudo dentro da pasta (arquivos e pastas)
    for item in sorted(os.listdir(PASTA_DOCUMENTOS)):
        caminho = os.path.join(PASTA_DOCUMENTOS, item)
        if os.path.isdir(caminho):  # filtra só as pastas, ignora arquivos soltos
            total = sum(1 for f in os.listdir(caminho) if not f.startswith("."))
            print(f"  {item}/  ({total} documento(s))")


def criar_diretorio(nome):
    """Cria uma nova subpasta dentro da biblioteca."""
    caminho = os.path.join(PASTA_DOCUMENTOS, nome)

    if os.path.exists(caminho):
        print(f"Erro: o diretório '{nome}' já existe.")
        return

    os.makedirs(caminho)  # makedirs cria pastas intermediárias se necessário
    print(f"Diretório '{nome}' criado com sucesso.")


def remover_diretorio(nome):
    """Remove uma subpasta da biblioteca após confirmação.

    Só remove se a pasta estiver vazia, evitando perda acidental de documentos.
    """
    caminho = os.path.join(PASTA_DOCUMENTOS, nome)

    if not os.path.isdir(caminho):
        print(f"Erro: o diretório '{nome}' não existe.")
        return

    # Conta arquivos reais (ignora .gitkeep e similares)
    arquivos_reais = [f for f in os.listdir(caminho) if not f.startswith(".")]
    if arquivos_reais:
        print(f"Erro: '{nome}' contém {len(arquivos_reais)} documento(s). Remova-os antes.")
        return

    confirmacao = input(f"Remover o diretório '{nome}'? (s/n): ")
    if confirmacao.lower() == "s":
        shutil.rmtree(caminho)  # rmtree remove a pasta e tudo dentro (só .gitkeep aqui)
        print(f"Diretório '{nome}' removido com sucesso.")
    else:
        print("Remoção cancelada.")
