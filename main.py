"""
Interface de linha de comando para o Sistema de Biblioteca Digital.

Uso:
    python main.py listar-tipo
    python main.py listar-ano
    python main.py adicionar <caminho_do_arquivo>
    python main.py renomear <nome_atual> <nome_novo>
    python main.py remover <nome_do_arquivo>
    python main.py listar-dirs
    python main.py criar-dir <nome>
    python main.py remover-dir <nome>
"""

import argparse
import biblioteca


def main():
    # ArgumentParser gerencia os comandos digitados no terminal
    parser = argparse.ArgumentParser(
        description="Sistema de Gerenciamento de Biblioteca Digital",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # subparsers permite criar subcomandos: "python main.py listar-tipo"
    subparsers = parser.add_subparsers(dest="comando", metavar="comando")
    subparsers.required = True  # exige que um comando seja informado

    # ── Listagem ──────────────────────────────────────────────────────────────

    subparsers.add_parser(
        "listar-tipo",
        help="Lista todos os documentos organizados por tipo de arquivo",
    )

    subparsers.add_parser(
        "listar-ano",
        help="Lista todos os documentos organizados por ano de publicação",
    )

    # ── Documentos ────────────────────────────────────────────────────────────

    p_adicionar = subparsers.add_parser("adicionar", help="Adiciona um documento à biblioteca")
    # add_argument define os parâmetros que o subcomando aceita
    p_adicionar.add_argument("caminho", help="Caminho completo do arquivo a ser adicionado")

    p_renomear = subparsers.add_parser("renomear", help="Renomeia um documento da biblioteca")
    p_renomear.add_argument("nome_atual", help="Nome atual do arquivo")
    p_renomear.add_argument("nome_novo", help="Novo nome para o arquivo")

    p_remover = subparsers.add_parser("remover", help="Remove um documento da biblioteca")
    p_remover.add_argument("nome", help="Nome do arquivo a ser removido")

    # ── Diretórios ────────────────────────────────────────────────────────────

    subparsers.add_parser(
        "listar-dirs",
        help="Lista todos os diretórios da biblioteca",
    )

    p_criar_dir = subparsers.add_parser("criar-dir", help="Cria um novo diretório na biblioteca")
    p_criar_dir.add_argument("nome", help="Nome do diretório a ser criado")

    p_remover_dir = subparsers.add_parser("remover-dir", help="Remove um diretório da biblioteca")
    p_remover_dir.add_argument("nome", help="Nome do diretório a ser removido")

    # ── Execução ──────────────────────────────────────────────────────────────

    # parse_args lê o que foi digitado no terminal e separa em partes
    args = parser.parse_args()

    # Chama a função correta de biblioteca.py de acordo com o comando digitado
    if args.comando == "listar-tipo":
        biblioteca.listar_por_tipo()
    elif args.comando == "listar-ano":
        biblioteca.listar_por_ano()
    elif args.comando == "adicionar":
        biblioteca.adicionar_documento(args.caminho)
    elif args.comando == "renomear":
        biblioteca.renomear_documento(args.nome_atual, args.nome_novo)
    elif args.comando == "remover":
        biblioteca.remover_documento(args.nome)
    elif args.comando == "listar-dirs":
        biblioteca.listar_diretorios()
    elif args.comando == "criar-dir":
        biblioteca.criar_diretorio(args.nome)
    elif args.comando == "remover-dir":
        biblioteca.remover_diretorio(args.nome)


# Garante que main() só roda quando o arquivo é executado diretamente,
# não quando é importado por outro módulo
if __name__ == "__main__":
    main()
