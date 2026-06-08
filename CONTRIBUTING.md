# Guia de Contribuição

Obrigado pelo interesse em contribuir com o Sistema de Biblioteca Digital! Este guia explica o passo a passo para contribuir corretamente usando Git e GitHub.

---

## Pré-requisitos

- Git instalado na máquina ([download aqui](https://git-scm.com))
- Conta no GitHub
- Python 3.8 ou superior

---

## 1. Fazendo fork e clonando o repositório

**Fork** cria uma cópia do repositório na sua conta do GitHub, para que você possa fazer alterações sem afetar o projeto original.

1. Acesse a página do repositório no GitHub
2. Clique no botão **Fork** (canto superior direito)
3. Clone o fork para sua máquina:

```bash
git clone https://github.com/SEU_USUARIO/Hora-da-Pr-tica-2---Programa-o-para-Ci-ncia-de-Dados.git
cd Hora-da-Pr-tica-2---Programa-o-para-Ci-ncia-de-Dados
```

4. Adicione o repositório original como referência remota:

```bash
git remote add upstream https://github.com/HbrieL2506/Hora-da-Pr-tica-2---Programa-o-para-Ci-ncia-de-Dados.git
```

---

## 2. Criando uma branch para sua alteração

Nunca trabalhe diretamente na branch `main`. Crie sempre uma branch separada para cada funcionalidade ou correção:

```bash
# Certifique-se de estar na main atualizada
git checkout main
git pull upstream main

# Crie e entre na nova branch
git checkout -b nome-da-sua-branch
```

**Exemplos de nomes de branch:**
- `feat/busca-por-titulo`
- `fix/erro-remover-arquivo`
- `docs/atualiza-readme`

---

## 3. Fazendo alterações e commits

Depois de fazer suas alterações no código, registre-as com um commit:

```bash
# Veja o que foi alterado
git status

# Adicione os arquivos modificados
git add nome_do_arquivo.py

# Crie o commit com mensagem descritiva
git commit -m "tipo: descrição curta do que foi feito"
```

### Formato da mensagem de commit

Use o prefixo correto para cada tipo de alteração:

| Prefixo  | Quando usar                                      |
|----------|--------------------------------------------------|
| `feat:`  | Nova funcionalidade                              |
| `fix:`   | Correção de bug                                  |
| `docs:`  | Alteração em documentação                        |
| `test:`  | Adição ou correção de testes                     |
| `refactor:` | Refatoração sem alterar comportamento         |

**Exemplos de boas mensagens:**
```
feat: adiciona busca de documento por título
fix: corrige erro ao renomear arquivo com espaços no nome
docs: atualiza exemplos de uso no README
test: adiciona teste para arquivo sem extensão
```

**Exemplos de mensagens ruins (evite):**
```
ajustes
corrigido
wip
alterações finais
```

---

## 4. Enviando para o GitHub (push)

Envie sua branch para o seu fork no GitHub:

```bash
git push origin nome-da-sua-branch
```

---

## 5. Abrindo um Pull Request

Um **Pull Request (PR)** é uma solicitação para que suas alterações sejam incorporadas ao projeto principal.

1. Acesse seu fork no GitHub
2. Clique em **Compare & pull request** (aparece automaticamente após o push)
3. Preencha o formulário:
   - **Título:** descrição curta e clara da alteração
   - **Descrição:** explique o que foi feito, por que foi feito e como testar
4. Clique em **Create pull request**

### Exemplo de descrição de PR

```
## O que foi feito
Adicionada função de busca de documento por título parcial.

## Por que foi feito
Bibliotecários relataram dificuldade em encontrar documentos
quando não lembravam o nome completo do arquivo.

## Como testar
python main.py buscar "astronomia"
```

---

## 6. Mantendo sua branch atualizada

Se o repositório original receber novos commits enquanto você trabalha, atualize sua branch:

```bash
git fetch upstream
git rebase upstream/main
```

---

## Boas práticas

- Faça commits pequenos e focados — um commit por mudança lógica
- Execute os testes antes de abrir um PR: `python -m pytest tests/ -v`
- Mantenha o código seguindo o estilo PEP 8 (padrão Python)
- Não suba arquivos desnecessários (`.env`, pastas `__pycache__`, etc.) — o `.gitignore` já cuida disso
