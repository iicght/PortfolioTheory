#Модуль формирования и оптимизации портфеля.
import numpy as np
import pandas as pd

#Генерация случайных весов (равномерное распределение Дирихле).
def generate_random_weights(n: int) -> np.ndarray:
    return np.random.dirichlet(np.ones(n))

#Ожидаемая доходность портфеля.
def calculate_portfolio_return(weights: np.ndarray, assets: list[dict]) -> float:
    total_return = 0
    for weight, asset in zip(weights, assets):
        total_return += weight * asset["average_return"]
    return total_return

#Риск портфеля (стандартное отклонение).
def calculate_portfolio_risk(weights: np.ndarray, cov_matrix: np.ndarray) -> float:
    return np.sqrt(weights @ cov_matrix @ weights.T)

#Генерация множества портфелей и выбор оптимального по коэффициенту Шарпа.
def optimize_portfolio(assets: list[dict], cov_matrix: np.ndarray, n_portfolios: int, risk_free_rate: float):
    results = []
    n = len(assets)
    for _ in range(n_portfolios):
        weights = generate_random_weights(n)
        portfolio_return = calculate_portfolio_return(weights, assets)
        portfolio_risk = calculate_portfolio_risk(weights, cov_matrix)
        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_risk

        results.append({
            "return": portfolio_return,
            "risk": portfolio_risk,
            "sharpe": sharpe_ratio,
            "weights": weights
        })
    df = pd.DataFrame(results)
    best_portfolio = df.loc[df["sharpe"].idxmax()]

    return best_portfolio, df