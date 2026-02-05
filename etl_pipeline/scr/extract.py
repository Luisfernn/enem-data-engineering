from pathlib import Path
import pandas as pd

import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.propagate = False

def extract_data(file_path: Path = None):

    if file_path is None:
        base_dir = Path(__file__).resolve().parent
        file_path = base_dir / 'data' / 'raw' / 'monthly_capacity_wind_solar_raw_data.csv'

    if not file_path.exists():
        logger.error(f"❌ Arquivo não encontrado: {file_path}")
        return None

    try:
        df = pd.read_excel(file_path, sheet_name='Country')
    except Exception as e:
        logger.error(f"⚠️ Erro ao ler o arquivo: {e}")
        return df
    
    try:
        df = df.to_csv('data/raw/monthly_capacity_wind_solar_data.csv', index=False, encoding='utf-8') 
    except Exception as e:
        logger.error(f"⚠️ Erro ao transformar o arquivo: {e} em csv")
        return df

    file_path = base_dir / 'data' / 'raw' / 'monthly_capacity_wind_solar_data.csv'

    if not file_path.exists():
        logger.error(f"❌ Arquivo não encontrado: {file_path}")

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        logger.error(f"⚠️ Erro ao ler o arquivo: {e}") 
        return df      