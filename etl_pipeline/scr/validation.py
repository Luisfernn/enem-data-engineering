import pandas as pd
from pathlib import Path

import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.propagate = False

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DIR = BASE_DIR / 'data' / 'processed'
INPUT_DIR = PROCESSED_DIR / 'renewable_energy_data_clean.csv'
OUTPUT_PATH = PROCESSED_DIR / 'renewable_energy_data_validated.csv'
















if __name__ == '_main__':

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    #logger.setLevel(logging.DEBUG)

    logger.info("="*60)
    logger.info("INICIANDO VALIDAÇÃO")
    logger.info("="*60)

    df = pd.read_csv(INPUT_DIR)
    logger.info(f"📊 Carregados {df(len)} registros")
    

    df = validate_columns(df)


    df.to_csv(OUTPUT_PATH)

 