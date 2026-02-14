# Модуль расчёта доходности, риска и ковариационной матрицы.
# Курсовая работа по портфельной теории Марковица.
import math
import numpy as np

#Расчёт логарифмических доходностей, возможно использование обычных арифметических, зависит от выборки.
def calculate_log_returns(prices: list[float]) -> list[float]:
    returns = []
    for i in range(1, len(prices)):
        r = math.log(prices[i] / prices[i - 1])
        returns.append(r)
    return returns

#Средняя доходность за период.
def calculate_average_return(returns: list[float]) -> float:
    return sum(returns) / len(returns)

#Стандартное отклонение выборки.
def calculate_standard_deviation(returns: list[float]) -> float:
    mean = calculate_average_return(returns)
    variance = sum((r - mean) ** 2 for r in returns) / (len(returns) - 1)
    return variance ** 0.5

#Формирование ковариационной матрицы.
def calculate_covariance_matrix(assets: list[dict]) -> np.ndarray:
    n = len(assets)
    cov_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            returns_i = assets[i]["returns"]
            returns_j = assets[j]["returns"]
            mean_i = assets[i]["average_return"]
            mean_j = assets[j]["average_return"]
            cov = sum(
                (r_i - mean_i) * (r_j - mean_j)
                for r_i, r_j in zip(returns_i, returns_j)
            ) / len(returns_i)
            cov_matrix[i][j] = cov

    return cov_matrix