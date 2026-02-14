#Модуль загрузки и подготовки рыночных данных.
import yfinance as yf
import pandas as pd

#Загрузка данных через API yfinance.
def download_data(tickers: list[str], start: str, end: str) -> pd.DataFrame:
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)
    if isinstance(data.columns, pd.MultiIndex):
        data = data["Close"]
    return data

#Получение последней цены каждого месяца.
def extract_monthly_closes(data: pd.DataFrame) -> pd.DataFrame:
    monthly_data = data.resample("M").last()
    return monthly_data

#Преобразование DataFrame в список словарей активов.
def prepare_asset_data(data: pd.DataFrame) -> list[dict]:
    assets = []
    for column in data.columns:
        prices = data[column].dropna().tolist()
        assets.append({
            "name": column,
            "prices": prices
        })
    return assets