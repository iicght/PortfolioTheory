#Модуль визуализации результатов оптимизации.
import matplotlib.pyplot as plt
import numpy as np

#Построение графика риск–доходность и линии Шарпа.
def plot_efficient_frontier(portfolios, best_portfolio, risk_free_rate):
    risks = portfolios["risk"]
    returns = portfolios["return"] * 100

    plt.scatter(risks, returns, s=5)
    plt.scatter(best_portfolio["risk"],
                best_portfolio["return"] * 100,
                color="red",
                label="Оптимальный портфель")

    # Линия Шарпа
    x0, y0 = 0, risk_free_rate * 100
    x1, y1 = best_portfolio["risk"], best_portfolio["return"] * 100

    m = (y1 - y0) / x1
    x = np.linspace(0, x1 * 1.5, 100)
    y = y0 + m * x

    plt.plot(x, y, linestyle="--", label="Линия Шарпа")
    plt.title("Доходность – Риск")
    plt.xlabel("Риск (σ)")
    plt.ylabel("Ожидаемая доходность (%)")
    plt.legend()
    plt.grid(True)
    plt.show()