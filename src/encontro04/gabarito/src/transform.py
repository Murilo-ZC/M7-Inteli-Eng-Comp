# Script para transformar os dados extraídos para seu armazenamento
import os
import csv
from datetime import datetime

from shared.tables import Cotacao
from shared.base import session
from sqlalchemy import text


RAW_PATH = f"dados.csv"


def update_date_format(date_input):
    """
    Atualiza o formato da data para YYYY-MM-DD
    """
    
    return date_input.split()[0]


def update_price(price_input):
    """
    Return price as float by removing:
    - "," to convert the number into float first (e.g. from "€100,000.00" to "100000.00")
    """
    price_input = float(price_input.replace(",", ""))
    return price_input


def transform_new_data():
    """
    Apply all transformations for each row in the .csv file before saving it into database
    """
    with open(RAW_PATH, mode="r", encoding="windows-1252") as csv_file:
        # Read the new CSV snapshot ready to be processed
        reader = csv.DictReader(csv_file)
        # Initialize an empty list for our PprRawAll objects
        cotacao_objects = []
        for row in reader:
            print(row)
            # Apply transformations and save as PprRawAll object
            cotacao_objects.append(
                Cotacao(
                    data=update_date_format(row["dataHoraCotacao"]),
                    cotacao_compra=update_price(row["cotacaoCompra"]),
                    cotacao_venda=update_price(row["cotacaoVenda"]),
                )
            )
        # Save all new processed objects and commit
        session.bulk_save_objects(cotacao_objects)
        session.commit()


def main():
    print("[TRANSFORMAÇÃO E CARGA] Iniciando")
    print("[TRANSFORMAÇÃO E CARGA] Transformando os dados novos")
    transform_new_data()
    print("[TRANSFORMAÇÃO E CARGA] Transformação e carga finalizadas")

if __name__ == "__main__":
    main()