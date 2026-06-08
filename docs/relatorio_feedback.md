# Relatório de Feedback

**Projeto:** Sistema de Gerenciamento de Biblioteca Digital  
**Data:** 08/06/2025  
**Participantes:** 2 bibliotecárias da biblioteca universitária

---

## Metodologia

As bibliotecárias testaram o sistema por aproximadamente 30 minutos cada uma, realizando tarefas reais do dia a dia: adicionar documentos ao acervo, listar por tipo e por ano, renomear arquivos com nomes inconsistentes e remover documentos desatualizados.

Cada participante registrou os pontos positivos e as dificuldades encontradas. Os feedbacks foram analisados e incorporados ao projeto conforme descrito abaixo.

---

## Participante 1 — Ana Paula, bibliotecária chefe

> *"Trabalho há 12 anos organizando o acervo digital. Precisava de algo que funcionasse sem depender de programas caros ou interfaces complicadas."*

### Feedback recebido

**Positivo:**
- Gostou da separação automática por subpastas ao adicionar um documento
- Achou prático que o sistema encontre o arquivo em qualquer subpasta ao renomear ou remover, sem precisar saber onde está

**Dificuldades encontradas:**

1. *"Quando tento remover um arquivo, o sistema pergunta se tenho certeza — mas antes eu não sabia exatamente onde ele estava guardado. Poderia mostrar o caminho antes de perguntar?"*

2. *"Quando digitei o nome do arquivo errado no comando renomear, o sistema não fez nada e não ficou claro se tinha dado erro ou se simplesmente não havia nada para fazer."*

### Ajustes realizados

**Feedback 1 — exibir caminho antes da confirmação de remoção:**

Implementado. O sistema agora mostra o caminho completo do arquivo antes de pedir confirmação:

```
Arquivo encontrado: documentos/pdf/artigo_fisica_2021.pdf
Tem certeza que deseja remover 'artigo_fisica_2021.pdf'? (s/n):
```

Isso dá ao bibliotecário a certeza de que está removendo o arquivo correto.

**Feedback 2 — mensagem de erro mais clara no renomear:**

A mensagem de erro já existia, mas foi verificado que ela aparece corretamente:

```
Erro: 'nome_errado.pdf' não encontrado na biblioteca.
```

A bibliotecária não havia percebido a mensagem porque o terminal rolou o texto. Orientada a aumentar a janela do terminal ou usar `python main.py renomear ... | more` para paginar a saída.

---

## Participante 2 — Carla, auxiliar de biblioteca

> *"Não tenho muita experiência com computadores. Prefiro coisas simples e diretas."*

### Feedback recebido

**Positivo:**
- Achou os comandos intuitivos após ler o README
- Gostou da mensagem de confirmação antes de remover ("me dá segurança")

**Dificuldades encontradas:**

1. *"Tentei adicionar um arquivo e não sabia se tinha funcionado. O sistema poderia confirmar melhor onde o arquivo foi parar?"*

2. *"Não entendi o que colocar no campo 'caminho' do comando adicionar. Achei que era só o nome do arquivo."*

3. *"Tenho vários documentos com nomes como 'scan001.pdf', 'scan002.pdf'. O sistema não consegue identificar o ano deles — ficam como 'Ano desconhecido'. Isso é um problema?"*

### Ajustes realizados

**Feedback 1 — confirmação ao adicionar:**

A mensagem de sucesso já existia, mas foi tornado mais visível indicando o destino completo:

```
Documento 'tese_computacao_2023.pdf' adicionado em documentos/pdf/.
```

**Feedback 2 — documentação do comando adicionar:**

O README foi atualizado com um exemplo mais detalhado mostrando como obter o caminho completo de um arquivo no Windows (clicar com botão direito → "Copiar como caminho").

**Feedback 3 — arquivos sem padrão de nomenclatura:**

O sistema funciona corretamente — arquivos sem ano identificável aparecem agrupados em "Ano desconhecido" na listagem por ano, e continuam acessíveis normalmente em todas as outras funções. Não é um erro, é uma limitação esperada do método de extração por nome.

A seção **"Convenção de nomenclatura"** do README foi criada justamente por causa desse feedback, orientando bibliotecários a incluir o ano no nome dos arquivos para aproveitar melhor a listagem.

---

## Resumo das alterações incorporadas

| Feedback | Participante | Ação tomada |
|----------|-------------|-------------|
| Mostrar caminho antes de confirmar remoção | Ana Paula | Implementado em `remover_documento` |
| Melhorar visibilidade da mensagem de erro | Ana Paula | Confirmado funcionamento, orientação de uso |
| Tornar confirmação de adição mais informativa | Carla | Já implementado, mensagem inclui subpasta de destino |
| Explicar como obter caminho do arquivo | Carla | Adicionado ao README |
| Documentar comportamento para arquivos sem ano | Carla | Seção "Convenção de nomenclatura" criada no README |

---

## Conclusão

O feedback das bibliotecárias foi fundamental para identificar pontos de melhoria na experiência de uso do sistema. As principais contribuições foram:

- A exibição do caminho completo antes da confirmação de remoção, que aumenta a segurança da operação
- A criação da seção de convenção de nomenclatura no README, que orienta o uso correto do sistema desde o início

Ambas as participantes consideraram o sistema útil e mais prático do que a gestão manual que realizavam anteriormente.
