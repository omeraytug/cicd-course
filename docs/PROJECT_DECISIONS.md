# Fintech Larper --- Project Decisions

This file records the decisions made while working through
`PRE_CODING_TODO.md`. Detailed research and experimentation belong
elsewhere; this is only a concise record of what was decided and why.

## 1. Stock Basket

**Basket:** 5 individual U.S. stocks from different sectors, with a
market-cap mix of **2 large, 2 mid, and 1 small**.

Ticker Company Sector Size

---

`NVDA` NVIDIA Information Technology Large
`FDS` FactSet Research Systems Financials Mid
`XOM` Exxon Mobil Energy Large
`HAE` Haemonetics Healthcare Mid
`JJSF` J&J Snack Foods Consumer Staples Small

The five sectors were chosen to give the experiment exposure to
different market and business dynamics. Information Technology was
deliberately assigned a large-cap stock, with NVIDIA selected to include
exposure to the recent AI-driven growth cycle. This does not assume that
AI exposure makes the series easier or harder to forecast; it simply
gives the basket a deliberately interesting source of heterogeneity.

The remaining size categories were randomly assigned before selecting
companies:

```text
Financials       → Mid
Energy           → Large
Healthcare       → Mid
Consumer Staples → Small
```

Stocks were then selected based on their assigned sector/size, adequate
historical data, and reasonable liquidity rather than known historical
forecasting performance. Market-cap labels refer to the approximate
classification at the time of selection (October 2026) and may change
over time.

---

## 2. Historical Data Source

**Source:** Yahoo Finance via `yfinance`.

Yahoo Finance was selected because it provides sufficient long-term daily market data for all five stocks without requiring a paid data service. `yfinance` is an unofficial client, so the project will not rely on Yahoo having a stable API contract or documented rate limit.

The source was validated against the full V1 basket (`NVDA`, `FDS`, `XOM`, `HAE`, `JJSF`). It provides OHLC, adjusted close, volume, dividends, and stock splits with decades of historical coverage. Initial validation found no missing values, duplicate dates, non-positive prices, or negative volumes. One inconsistent OHLC observation was detected for FDS, reinforcing the need for validation during ingestion.

Corporate actions are retained explicitly. Yahoo's historical `Close` is split-adjusted, while `Adj Close` additionally accounts for distributions such as dividends. Dividend and split events will also be preserved rather than discarded.

Fetched market data will be persisted in **PostgreSQL** instead of being downloaded directly by model-training code. The planned flow is:

`Yahoo Finance → yfinance → ingestion → validation → PostgreSQL → ML pipeline`

The initial ingestion will backfill historical data, while later runs will fetch recent data incrementally. Because Yahoo access is unofficial, ingestion should minimize requests and eventually handle retries/rate-limit failures.

## 3. Forecast Target

**Target:** Daily `Close` price for each stock independently.

Forecasts will be evaluated at `t+1`, `t+5`, and `t+20`, where horizons
refer to U.S. market trading sessions rather than calendar days. Multi-step
forecasts will predict the complete trajectory through the horizon rather
than only the final endpoint.

Forecasts should include point predictions together with predictive
uncertainty where supported. The exact uncertainty representation and
interval/quantile levels will be decided separately in Decision 11.

## 4. Model Inputs

**V1:** Historical `Close` price only. Each stock is modeled independently
without exogenous variables.

**V2:** May introduce relatively simple exogenous variables. The exact
features will be selected during experimentation based on their usefulness
and model support rather than fixed in advance.

**V3:** Optionally explores more advanced external information such as
macroeconomic, event, news, or sentiment features. This is outside the core
scope of the project and is not required for completion.

Only the V1 input specification is currently locked. V2 and V3 are
experimental directions and may change as the selected models are
evaluated.

## 5. Baselines

Three baselines will be used: **naive/random walk, drift, and ARIMA**.

The naive forecast predicts the most recently observed `Close` throughout
the forecast horizon. Drift provides a simple trend-extrapolation benchmark,
while ARIMA provides a conventional fitted statistical forecasting
benchmark.

All baselines will use the same data and walk-forward evaluation framework
as the main model approaches.

## 6. Foundation Model

_Not decided yet._

## 7. Adapted Pretrained Approach

_Not decided yet._

## 8. Custom Model

_Not decided yet._

## 9. Walk-Forward Evaluation

_Not decided yet._

## 10. Evaluation Metrics

_Not decided yet._

## 11. Uncertainty Experiment

_Not decided yet._

## 12. V1 Experiment Specification

_Not decided yet._
