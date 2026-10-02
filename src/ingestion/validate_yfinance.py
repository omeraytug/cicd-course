import yfinance as yf


TICKERS = ["NVDA", "FDS", "XOM", "HAE", "JJSF"]


def validate_ticker(ticker: str) -> None:
    stock = yf.Ticker(ticker)

    history = stock.history(
        period="max",
        interval="1d",
        auto_adjust=False,
        actions=True,
    )

    print(f"\n{'=' * 50}")
    print(f"Ticker: {ticker}")
    print(f"{'=' * 50}")

    if history.empty:
        print("No historical data returned.")
        return

    print(f"Start: {history.index.min()}")
    print(f"End:   {history.index.max()}")
    print(f"Rows:  {len(history)}")

    print("\nColumns:")
    for column in history.columns:
        print(f"- {column}")

    print("\nMissing values:")
    print(history.isna().sum())

    print(f"\nDuplicate dates: {history.index.duplicated().sum()}")

    if "Dividends" in history.columns:
        dividends = history[history["Dividends"] != 0]

        if not dividends.empty:
            print("\nDividend events:")
            print(dividends[["Close", "Adj Close", "Dividends"]].tail())

    if "Stock Splits" in history.columns:
        splits = history[history["Stock Splits"] != 0]

        if not splits.empty:
            print("\nStock split events:")
            print(splits[["Close", "Adj Close", "Stock Splits"]])


def main() -> None:
    for ticker in TICKERS:
        validate_ticker(ticker)


if __name__ == "__main__":
    main()