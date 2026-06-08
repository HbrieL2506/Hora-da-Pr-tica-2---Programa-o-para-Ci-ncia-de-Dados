# Relatório de Testes

**Projeto:** Sistema de Gerenciamento de Biblioteca Digital  
**Data:** 08/06/2025  
**Total de testes:** 24  
**Resultado final:** ✅ 24 aprovados — 0 reprovados

---

## Como executar os testes

```bash
python -m pytest tests/test_biblioteca.py -v
```

---

## Resultado completo

```
tests/test_biblioteca.py::TestExtrairAno::test_ano_com_texto_antes_e_depois PASSED
tests/test_biblioteca.py::TestExtrairAno::test_ano_fora_do_padrao_ignorado   PASSED
tests/test_biblioteca.py::TestExtrairAno::test_ano_inicio_seculo             PASSED
tests/test_biblioteca.py::TestExtrairAno::test_ano_valido_no_nome            PASSED
tests/test_biblioteca.py::TestExtrairAno::test_sem_ano_retorna_desconhecido  PASSED
tests/test_biblioteca.py::TestListagem::test_listar_por_ano_biblioteca_vazia PASSED
tests/test_biblioteca.py::TestListagem::test_listar_por_ano_com_arquivos     PASSED
tests/test_biblioteca.py::TestListagem::test_listar_por_tipo_biblioteca_vazia PASSED
tests/test_biblioteca.py::TestListagem::test_listar_por_tipo_com_arquivos    PASSED
tests/test_biblioteca.py::TestManipulacaoArquivos::test_adicionar_arquivo_inexistente_nao_lanca_excecao PASSED
tests/test_biblioteca.py::TestManipulacaoArquivos::test_adicionar_duplicado_nao_sobrescreve            PASSED
tests/test_biblioteca.py::TestManipulacaoArquivos::test_adicionar_epub_vai_para_subpasta_correta       PASSED
tests/test_biblioteca.py::TestManipulacaoArquivos::test_adicionar_extensao_desconhecida_vai_para_outros PASSED
tests/test_biblioteca.py::TestManipulacaoArquivos::test_adicionar_pdf_vai_para_subpasta_correta        PASSED
tests/test_biblioteca.py::TestManipulacaoArquivos::test_remover_documento_cancelado                    PASSED
tests/test_biblioteca.py::TestManipulacaoArquivos::test_remover_documento_com_confirmacao              PASSED
tests/test_biblioteca.py::TestManipulacaoArquivos::test_renomear_arquivo_inexistente_nao_lanca_excecao PASSED
tests/test_biblioteca.py::TestManipulacaoArquivos::test_renomear_documento_com_sucesso                 PASSED
tests/test_biblioteca.py::TestDiretorios::test_criar_diretorio_com_sucesso                             PASSED
tests/test_biblioteca.py::TestDiretorios::test_criar_diretorio_duplicado_nao_lanca_excecao             PASSED
tests/test_biblioteca.py::TestDiretorios::test_listar_diretorios_nao_lanca_excecao                     PASSED
tests/test_biblioteca.py::TestDiretorios::test_remover_diretorio_com_arquivos_recusado                 PASSED
tests/test_biblioteca.py::TestDiretorios::test_remover_diretorio_inexistente_nao_lanca_excecao         PASSED
tests/test_biblioteca.py::TestDiretorios::test_remover_diretorio_vazio                                 PASSED

24 passed in 0.14s
```

---

## Descrição dos testes por grupo

### TestExtrairAno (5 testes)

Testa a função `extrair_ano`, responsável por identificar o ano de publicação no nome do arquivo.

| Teste | O que verifica |
|-------|----------------|
| `test_ano_valido_no_nome` | Extrai `2021` de `tese_2021.pdf` |
| `test_ano_inicio_seculo` | Extrai `1998` de `artigo_1998.epub` |
| `test_ano_com_texto_antes_e_depois` | Extrai `2019` de `filosofia_moderna_2019_v2.pdf` |
| `test_sem_ano_retorna_desconhecido` | Retorna `"Ano desconhecido"` para `documento.pdf` |
| `test_ano_fora_do_padrao_ignorado` | Ignora `1800` (fora do intervalo 1900–2099) |

### TestListagem (4 testes)

Testa `listar_por_tipo` e `listar_por_ano` em biblioteca vazia e com arquivos.

| Teste | O que verifica |
|-------|----------------|
| `test_listar_por_tipo_biblioteca_vazia` | Não lança erro com acervo vazio |
| `test_listar_por_tipo_com_arquivos` | Executa sem erros com PDFs e EPUBs |
| `test_listar_por_ano_biblioteca_vazia` | Não lança erro com acervo vazio |
| `test_listar_por_ano_com_arquivos` | Executa sem erros com arquivos datados |

### TestManipulacaoArquivos (9 testes)

Testa adição, renomeação e remoção de documentos.

| Teste | O que verifica |
|-------|----------------|
| `test_adicionar_pdf_vai_para_subpasta_correta` | PDF copiado para `documentos/pdf/` |
| `test_adicionar_epub_vai_para_subpasta_correta` | EPUB copiado para `documentos/epub/` |
| `test_adicionar_extensao_desconhecida_vai_para_outros` | DOCX copiado para `documentos/outros/` |
| `test_adicionar_arquivo_inexistente_nao_lanca_excecao` | Trata erro de arquivo não encontrado |
| `test_adicionar_duplicado_nao_sobrescreve` | Segundo envio do mesmo arquivo não sobrescreve |
| `test_renomear_documento_com_sucesso` | Arquivo renomeado corretamente na mesma pasta |
| `test_renomear_arquivo_inexistente_nao_lanca_excecao` | Trata erro de arquivo não encontrado |
| `test_remover_documento_com_confirmacao` | Arquivo removido ao confirmar com `s` |
| `test_remover_documento_cancelado` | Arquivo mantido ao responder `n` |

### TestDiretorios (6 testes)

Testa listagem, criação e remoção de subpastas.

| Teste | O que verifica |
|-------|----------------|
| `test_listar_diretorios_nao_lanca_excecao` | Listagem executa sem erros |
| `test_criar_diretorio_com_sucesso` | Nova pasta criada corretamente |
| `test_criar_diretorio_duplicado_nao_lanca_excecao` | Trata tentativa de criar pasta já existente |
| `test_remover_diretorio_vazio` | Pasta vazia removida ao confirmar |
| `test_remover_diretorio_com_arquivos_recusado` | Sistema recusa remover pasta com documentos |
| `test_remover_diretorio_inexistente_nao_lanca_excecao` | Trata erro de pasta não encontrada |

---

## Bug encontrado durante os testes

Durante a primeira execução dos testes, **3 testes falharam** no grupo `TestExtrairAno`:

```
FAILED tests/test_biblioteca.py::TestExtrairAno::test_ano_valido_no_nome
FAILED tests/test_biblioteca.py::TestExtrairAno::test_ano_inicio_seculo
FAILED tests/test_biblioteca.py::TestExtrairAno::test_ano_com_texto_antes_e_depois

AssertionError: 'Ano desconhecido' != '2021'
```

**Causa identificada:** A expressão regular usava `\b` (fronteira de palavra) para delimitar o ano. Em Python, o caractere `_` (underscore) é considerado parte de uma palavra, então em `tese_2021.pdf` não há fronteira entre `_` e `2` — o padrão nunca casava.

**Correção aplicada:** Substituído `\b` por lookahead e lookbehind negativos (`(?<!\d)` e `(?!\d)`), que verificam apenas se o ano não está adjacente a outro dígito, ignorando o underscore.

```python
# Antes (com bug)
resultado = re.search(r"\b(19\d{2}|20\d{2})\b", nome_arquivo)

# Depois (corrigido)
resultado = re.search(r"(?<!\d)(19\d{2}|20\d{2})(?!\d)", nome_arquivo)
```

Após a correção, todos os 24 testes passaram.

---

## Conclusão

Todas as funcionalidades do sistema foram testadas e operam corretamente. O processo de testes foi essencial para identificar e corrigir um bug real na extração de ano, que não teria sido detectado apenas por inspeção manual do código.
