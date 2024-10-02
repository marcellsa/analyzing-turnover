"""
Módulo responsável por carregar os dados do arquivo Excel.
"""

import pandas as pd


def load_data(file_path):
    """
    Carrega o arquivo Excel para um DataFrame.

    Args:
        file_path (str): Caminho do arquivo Excel.

    Returns:
        pd.DataFrame: Dataset carregado.
    """
    return pd.read_excel(file_path)
