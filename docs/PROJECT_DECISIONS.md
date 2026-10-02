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

_Not decided yet._

## 4. Model Inputs

_Not decided yet._

## 5. Baselines

_Not decided yet._

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
