# Sistema de Gerenciamento de Biblioteca Digital

Sistema de linha de comando desenvolvido em Python para gerenciar documentos digitais de uma biblioteca universitária. Permite organizar, adicionar, renomear e remover arquivos como PDFs, ePUBs e outros formatos, sem precisar fazer tudo manualmente.

---

## Funcionalidades

- **Listar documentos por tipo** — agrupa todos os arquivos por extensão (PDF, EPUB, etc.)
- **Listar documentos por ano** — organiza o acervo por ano de publicação, extraído do nome do arquivo
- **Adicionar documento** — copia um arquivo externo para a subpasta correta da biblioteca automaticamente
- **Renomear documento** — renomeia um arquivo dentro da biblioteca
- **Remover documento** — remove um arquivo com confirmação obrigatória
- **Gerenciar diretórios** — listar, criar e remover subpastas do acervo

---

## Requisitos

- Python 3.8 ou superior
- Sem dependências externas — usa apenas módulos da biblioteca padrão do Python (`os`, `re`, `shutil`, `argparse`)

---

## Como instalar

```bash
# 1. Clone o repositório
git clone https://github.com/HbrieL2506/Hora-da-Pr-tica-2---Programa-o-para-Ci-ncia-de-Dados.git

# 2. Entre na pasta do projeto
cd Hora-da-Pr-tica-2---Programa-o-para-Ci-ncia-de-Dados

# 3. Pronto — nenhuma instalação adicional necessária
```

---

## Como usar

Todos os comandos são executados a partir da pasta raiz do projeto:

```bash
python main.py <comando> [argumentos]
```

### Listar documentos por tipo

```bash
python main.py listar-tipo
```

Saída esperada:
```
=== Documentos por Tipo ===

[EPUB] — 1 arquivo(s):
  - livro_filosofia_2022.epub

[PDF] — 2 arquivo(s):
  - artigo_2021.pdf
  - tese_computacao_2023.pdf
```

---

### Listar documentos por ano

```bash
python main.py listar-ano
```

Saída esperada:
```
=== Documentos por Ano ===

[2021] — 1 arquivo(s):
  - artigo_2021.pdf

[2022] — 1 arquivo(s):
  - livro_filosofia_2022.epub

[2023] — 1 arquivo(s):
  - tese_computacao_2023.pdf
```

> O ano é extraído automaticamente do nome do arquivo. Arquivos sem ano no nome aparecem como "Ano desconhecido".

---

### Adicionar documento

```bash
python main.py adicionar <caminho_do_arquivo>
```

Exemplo:
```bash
python main.py adicionar C:\Downloads\tese_computacao_2023.pdf
```

O sistema detecta a extensão e copia o arquivo para a subpasta correta:
- `.pdf` → `documentos/pdf/`
- `.epub` → `documentos/epub/`
- outros → `documentos/outros/`

---

### Renomear documento

```bash
python main.py renomear <nome_atual> <nome_novo>
```

Exemplo:
```bash
python main.py renomear artigo.pdf artigo_fisica_2021.pdf
```

---

### Remover documento

```bash
python main.py remover <nome_do_arquivo>
```

Exemplo:
```bash
python main.py remover artigo_fisica_2021.pdf
```

O sistema exibe o caminho do arquivo e pede confirmação antes de remover:
```
Arquivo encontrado: documentos/pdf/artigo_fisica_2021.pdf
Tem certeza que deseja remover 'artigo_fisica_2021.pdf'? (s/n):
```

---

### Gerenciar diretórios

```bash
# Listar subpastas existentes
python main.py listar-dirs

# Criar nova subpasta
python main.py criar-dir dissertacoes

# Remover subpasta (só funciona se estiver vazia)
python main.py remover-dir dissertacoes
```

---

## Estrutura do projeto

```
biblioteca-digital/
├── biblioteca.py           # funções principais do sistema
├── main.py                 # interface de linha de comando
├── documentos/
│   ├── pdf/                # documentos em formato PDF
│   ├── epub/               # documentos em formato ePUB
│   └── outros/             # outros formatos (DOCX, TXT, etc.)
├── tests/
│   └── test_biblioteca.py  # testes automatizados (24 casos)
├── docs/
│   ├── relatorio_testes.md
│   └── relatorio_feedback.md
└── .gitignore
```

---

## Como executar os testes

```bash
python -m pytest tests/test_biblioteca.py -v
```

Saída esperada: **24 passed**.

---

## Convenção de nomenclatura de arquivos

Para que o sistema identifique o ano automaticamente, recomenda-se nomear os arquivos incluindo o ano de publicação:

```
titulo_ANO.extensao
```

Exemplos:
- `introducao_astronomia_2020.pdf`
- `tese_engenharia_2018.epub`
- `relatorio_pesquisa_2023.docx`

---

## Contribuindo

Consulte o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para instruções sobre como contribuir com o projeto.
