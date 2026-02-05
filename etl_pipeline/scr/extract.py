from pathlib import Path
import pandas as pd

import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.propagate = False

def extract_data(file_path: Path = None):

    base_dir = Path(__file__).resolve().parent

    if file_path is None:
        file_path = base_dir / 'data' / 'raw' / 'renewable_energy_data_raw.xlsx'

    if not file_path.exists():
        logger.error(f"❌ Arquivo não encontrado: {file_path}")
        return None

    try:
        df = pd.read_excel(file_path, sheet_name='Country')
    except Exception as e:
        logger.error(f"⚠️ Erro ao ler o arquivo: {e}")
        return None
    
    try:
        df.to_csv(base_dir / 'data' / 'raw' / 'renewable_energy_data.csv' , index=False, encoding='utf-8') 
    except Exception as e:
        logger.error(f"⚠️ Erro ao transformar o arquivo: {e} em csv")
        return None   