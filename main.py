#Основной модуль.
#Курсовая работа по портфельной теории Марковица.
from data_loader import download_data, extract_monthly_closes, prepare_asset_data
from statistics import (
    calculate_log_returns,
    calculate_average_return,
    calculate_standard_deviation,
    calculate_covariance_matrix
)
from portfolio import optimize_portfolio
from visualization import plot_efficient_frontier


def main():
    #Здесь настраивается период для выборки цен за акции
    start_date = "2009-03-01"
    end_date = "2017-06-02"
    risk_free_rate = 0.0032

    tickers_input = input("Введите тикеры через запятую: ")
    tickers = [t.strip() for t in tickers_input.split(",")]

    n_portfolios = int(input("Введите количество портфелей: "))

    data = download_data(tickers, start_date, end_date)
    monthly_data = extract_monthly_closes(data)
    assets = prepare_asset_data(monthly_data)

    # Расчёт статистик
    for asset in assets:
        returns = calculate_log_returns(asset["prices"])
        asset["returns"] = returns
        asset["average_return"] = calculate_average_return(returns)
        asset["risk"] = calculate_standard_deviation(returns)

    cov_matrix = calculate_covariance_matrix(assets)

    best_portfolio, all_portfolios = optimize_portfolio(
        assets,
        cov_matrix,
        n_portfolios,
        risk_free_rate
    )
    print("\nОптимальный портфель:")
    print(best_portfolio)
    print("\nОптимальные веса:")
    for ticker, weight in zip(tickers, best_portfolio["weights"]):
        print(f"{ticker}: {weight:.4f}")

    plot_efficient_frontier(all_portfolios, best_portfolio, risk_free_rate)

main()