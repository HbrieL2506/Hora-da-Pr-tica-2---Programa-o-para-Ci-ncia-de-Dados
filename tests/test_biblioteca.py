"""
Testes automatizados para o sistema de biblioteca digital.

Cada teste usa uma pasta temporária isolada para não afetar os documentos reais.
A pasta é criada antes de cada teste (setUp) e apagada depois (tearDown).
"""

import os
import shutil
import tempfile
import unittest
from unittest.mock import patch

import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import biblioteca


class TestExtrairAno(unittest.TestCase):
    """Testes para a função extrair_ano."""

    def test_ano_valido_no_nome(self):
        self.assertEqual(biblioteca.extrair_ano("tese_2021.pdf"), "2021")

    def test_ano_inicio_seculo(self):
        self.assertEqual(biblioteca.extrair_ano("artigo_1998.epub"), "1998")

    def test_ano_com_texto_antes_e_depois(self):
        self.assertEqual(biblioteca.extrair_ano("filosofia_moderna_2019_v2.pdf"), "2019")

    def test_sem_ano_retorna_desconhecido(self):
        self.assertEqual(biblioteca.extrair_ano("documento.pdf"), "Ano desconhecido")

    def test_ano_fora_do_padrao_ignorado(self):
        # 1800 não entra no padrão 1900-2099
        self.assertEqual(biblioteca.extrair_ano("arquivo_1800.pdf"), "Ano desconhecido")


class TestListagem(unittest.TestCase):
    """Testes para listar_por_tipo e listar_por_ano."""

    def setUp(self):
        # Cria estrutura temporária isolada para cada teste
        self.pasta_temp = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.pasta_temp, "pdf"))
        os.makedirs(os.path.join(self.pasta_temp, "epub"))
        os.makedirs(os.path.join(self.pasta_temp, "outros"))
        self.pasta_original = biblioteca.PASTA_DOCUMENTOS
        biblioteca.PASTA_DOCUMENTOS = self.pasta_temp

    def tearDown(self):
        biblioteca.PASTA_DOCUMENTOS = self.pasta_original
        shutil.rmtree(self.pasta_temp)

    def _criar_arquivo(self, subpasta, nome):
        """Cria arquivo vazio para simular documento na biblioteca."""
        caminho = os.path.join(self.pasta_temp, subpasta, nome)
        open(caminho, "w").close()

    def test_listar_por_tipo_biblioteca_vazia(self):
        # Não deve lançar erro com biblioteca vazia
        try:
            biblioteca.listar_por_tipo()
        except Exception as e:
            self.fail(f"listar_por_tipo lançou exceção inesperada: {e}")

    def test_listar_por_tipo_com_arquivos(self):
        self._criar_arquivo("pdf", "artigo_2023.pdf")
        self._criar_arquivo("epub", "livro_2022.epub")
        try:
            biblioteca.listar_por_tipo()
        except Exception as e:
            self.fail(f"listar_por_tipo lançou exceção: {e}")

    def test_listar_por_ano_biblioteca_vazia(self):
        try:
            biblioteca.listar_por_ano()
        except Exception as e:
            self.fail(f"listar_por_ano lançou exceção inesperada: {e}")

    def test_listar_por_ano_com_arquivos(self):
        self._criar_arquivo("pdf", "tese_2020.pdf")
        self._criar_arquivo("epub", "livro_2018.epub")
        try:
            biblioteca.listar_por_ano()
        except Exception as e:
            self.fail(f"listar_por_ano lançou exceção: {e}")


class TestManipulacaoArquivos(unittest.TestCase):
    """Testes para adicionar, renomear e remover documentos."""

    def setUp(self):
        self.pasta_temp = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.pasta_temp, "pdf"))
        os.makedirs(os.path.join(self.pasta_temp, "epub"))
        os.makedirs(os.path.join(self.pasta_temp, "outros"))
        self.pasta_original = biblioteca.PASTA_DOCUMENTOS
        biblioteca.PASTA_DOCUMENTOS = self.pasta_temp
        # Pasta separada para simular arquivos externos à biblioteca
        self.pasta_externa = tempfile.mkdtemp()

    def tearDown(self):
        biblioteca.PASTA_DOCUMENTOS = self.pasta_original
        shutil.rmtree(self.pasta_temp)
        shutil.rmtree(self.pasta_externa)

    def _criar_externo(self, nome):
        """Cria arquivo fora da biblioteca (simula download ou área de trabalho)."""
        caminho = os.path.join(self.pasta_externa, nome)
        open(caminho, "w").close()
        return caminho

    def test_adicionar_pdf_vai_para_subpasta_correta(self):
        origem = self._criar_externo("artigo_2023.pdf")
        biblioteca.adicionar_documento(origem)
        destino = os.path.join(self.pasta_temp, "pdf", "artigo_2023.pdf")
        self.assertTrue(os.path.exists(destino))

    def test_adicionar_epub_vai_para_subpasta_correta(self):
        origem = self._criar_externo("livro_2022.epub")
        biblioteca.adicionar_documento(origem)
        destino = os.path.join(self.pasta_temp, "epub", "livro_2022.epub")
        self.assertTrue(os.path.exists(destino))

    def test_adicionar_extensao_desconhecida_vai_para_outros(self):
        origem = self._criar_externo("relatorio_2021.docx")
        biblioteca.adicionar_documento(origem)
        destino = os.path.join(self.pasta_temp, "outros", "relatorio_2021.docx")
        self.assertTrue(os.path.exists(destino))

    def test_adicionar_arquivo_inexistente_nao_lanca_excecao(self):
        try:
            biblioteca.adicionar_documento("arquivo_fantasma.pdf")
        except Exception as e:
            self.fail(f"adicionar_documento lançou exceção: {e}")

    def test_adicionar_duplicado_nao_sobrescreve(self):
        origem = self._criar_externo("artigo_2023.pdf")
        biblioteca.adicionar_documento(origem)
        # Modifica o arquivo externo para detectar se houve sobrescrita
        with open(origem, "w") as f:
            f.write("conteudo diferente")
        biblioteca.adicionar_documento(origem)
        # Arquivo na biblioteca deve continuar com tamanho zero (original)
        destino = os.path.join(self.pasta_temp, "pdf", "artigo_2023.pdf")
        self.assertEqual(os.path.getsize(destino), 0)

    def test_renomear_documento_com_sucesso(self):
        open(os.path.join(self.pasta_temp, "pdf", "velho.pdf"), "w").close()
        biblioteca.renomear_documento("velho.pdf", "novo.pdf")
        self.assertFalse(os.path.exists(os.path.join(self.pasta_temp, "pdf", "velho.pdf")))
        self.assertTrue(os.path.exists(os.path.join(self.pasta_temp, "pdf", "novo.pdf")))

    def test_renomear_arquivo_inexistente_nao_lanca_excecao(self):
        try:
            biblioteca.renomear_documento("nao_existe.pdf", "novo.pdf")
        except Exception as e:
            self.fail(f"renomear_documento lançou exceção: {e}")

    @patch("builtins.input", return_value="s")
    def test_remover_documento_com_confirmacao(self, mock_input):
        open(os.path.join(self.pasta_temp, "pdf", "remover.pdf"), "w").close()
        biblioteca.remover_documento("remover.pdf")
        self.assertFalse(os.path.exists(os.path.join(self.pasta_temp, "pdf", "remover.pdf")))

    @patch("builtins.input", return_value="n")
    def test_remover_documento_cancelado(self, mock_input):
        open(os.path.join(self.pasta_temp, "pdf", "manter.pdf"), "w").close()
        biblioteca.remover_documento("manter.pdf")
        self.assertTrue(os.path.exists(os.path.join(self.pasta_temp, "pdf", "manter.pdf")))


class TestDiretorios(unittest.TestCase):
    """Testes para listar, criar e remover diretórios."""

    def setUp(self):
        self.pasta_temp = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.pasta_temp, "pdf"))
        self.pasta_original = biblioteca.PASTA_DOCUMENTOS
        biblioteca.PASTA_DOCUMENTOS = self.pasta_temp

    def tearDown(self):
        biblioteca.PASTA_DOCUMENTOS = self.pasta_original
        shutil.rmtree(self.pasta_temp)

    def test_listar_diretorios_nao_lanca_excecao(self):
        try:
            biblioteca.listar_diretorios()
        except Exception as e:
            self.fail(f"listar_diretorios lançou exceção: {e}")

    def test_criar_diretorio_com_sucesso(self):
        biblioteca.criar_diretorio("dissertacoes")
        self.assertTrue(os.path.isdir(os.path.join(self.pasta_temp, "dissertacoes")))

    def test_criar_diretorio_duplicado_nao_lanca_excecao(self):
        biblioteca.criar_diretorio("dissertacoes")
        try:
            biblioteca.criar_diretorio("dissertacoes")
        except Exception as e:
            self.fail(f"criar_diretorio lançou exceção no duplicado: {e}")

    @patch("builtins.input", return_value="s")
    def test_remover_diretorio_vazio(self, mock_input):
        os.makedirs(os.path.join(self.pasta_temp, "vazio"))
        biblioteca.remover_diretorio("vazio")
        self.assertFalse(os.path.isdir(os.path.join(self.pasta_temp, "vazio")))

    @patch("builtins.input", return_value="s")
    def test_remover_diretorio_com_arquivos_recusado(self, mock_input):
        os.makedirs(os.path.join(self.pasta_temp, "cheio"))
        open(os.path.join(self.pasta_temp, "cheio", "doc.pdf"), "w").close()
        biblioteca.remover_diretorio("cheio")
        # Pasta deve continuar existindo — sistema recusou a remoção
        self.assertTrue(os.path.isdir(os.path.join(self.pasta_temp, "cheio")))

    def test_remover_diretorio_inexistente_nao_lanca_excecao(self):
        try:
            biblioteca.remover_diretorio("nao_existe")
        except Exception as e:
            self.fail(f"remover_diretorio lançou exceção: {e}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
