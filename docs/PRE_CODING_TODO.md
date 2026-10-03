# Fintech Larper --- Pre-Coding TODO

This document tracks the research and decisions to complete before
implementing the main forecasting pipeline. The goal is to define V1
clearly without designing the entire MLOps system upfront.

## 1. Choose the stock basket

- [x] Decide how many stocks to include.
- [x] Select the stocks.
- [x] Decide whether to deliberately represent different sectors or
      market behaviours.
- [x] Decide whether to include only individual stocks or also an
      index/ETF.
- [x] Document why the selected assets were chosen.

**Decision:** NVDA, FDS, XOM, HAE, JJSF

## 2. Choose the historical data source

- [x] Compare historical coverage and reliability.
- [x] Check rate limits and cost/free-tier limitations.
- [x] Check available fields: OHLC, adjusted close, volume, dividends,
      splits.
- [x] Understand how corporate actions are represented.
- [x] Decide whether raw data should be stored or fetched when needed.

## 3. Define exactly what is being forecast

Current direction: daily stock closing prices, with each stock modeled
independently.

- [x] Choose between raw close and adjusted close as the main target.
- [x] Confirm horizons: `t+1`, `t+5`, and `t+20`.
- [x] Confirm that multi-step forecasts predict the complete
      trajectory rather than only the endpoint.
- [x] Define exactly how trading days are handled.

A forecast produces the complete trajectory through the requested horizon:

```text
t+1
t+2
t+3
...
t+20
```

## 4. Define the information available to the models

The project will develop the forecasting problem progressively rather than
fixing all possible regressors before modeling begins.

### V1 — Historical price only

The core V1 benchmark uses only the historical `Close` price of the stock
being forecast.

```text
Historical Close
      ↓
    Model
      ↓
Future Close trajectory
```

- [x] Confirm historical price as the common V1 input.
- [x] Keep V1 univariate and exclude exogenous variables.
- [x] Establish that future information must not leak into model inputs.

### V2 — Simple exogenous variables

V2 may introduce relatively easy-to-define external variables such as
volume, market/sector information, or calendar features.
The exact variables are deliberately not fixed yet. Their usefulness and
compatibility with the selected models will be evaluated during model
development.

### V3 — Advanced exogenous variables (optional)

V3 may explore more difficult financial, macroeconomic, event, news, or
sentiment-based information.
This is optional and is not required for the main project. The project is
primarily a forecasting and MLOps study rather than an attempt to build a
full quantitative trading system.

**V1 input definition**: Historical Close price only.

## 5. Choose the baselines

- [x] Include a last-observed-price / random-walk naive forecast.
- [x] Include a drift forecast.
- [x] Include a conventional statistical forecasting baseline.

The primary baseline is the naive/random-walk forecast, which predicts the
latest observed `Close` for every future horizon.

A drift baseline extrapolates the average historical change in price,
providing a second simple benchmark that allows for trend.

ARIMA will be used as a conventional statistical forecasting baseline,
providing a fitted time-series benchmark between the simple forecasts and
the more advanced model approaches.

All baselines will be evaluated using the same walk-forward framework and
`t+1`, `t+5`, and `t+20` horizons as the main models.

**Selected baselines:** Naive/random walk, drift, and ARIMA.

## 6. Research time-series foundation models

For each candidate, investigate:

- [ ] Zero-shot forecasting support.
- [ ] Multi-horizon forecasting.
- [ ] Probabilistic/quantile forecasts and prediction intervals.
- [ ] Univariate and multivariate support.
- [ ] Historical and known-future covariate support.
- [ ] Fine-tuning support.
- [ ] Pretraining data, where documented.
- [ ] Available checkpoints.
- [ ] Licensing.
- [ ] Compute and memory requirements.
- [ ] Practicality of running locally and/or in the cloud.

Then:

- [ ] Select the zero-shot foundation model.

**Selected foundation model:** TBD

**Reasoning:** TBD

## 7. Define the adapted pretrained approach

Possible directions include fine-tuning the selected foundation model,
adapting another pretrained time-series model, or using a model already
adapted to financial data.

- [ ] Decide what is being adapted.
- [ ] Decide what data will be used for adaptation.
- [ ] Investigate full vs parameter-efficient fine-tuning where
      relevant.
- [ ] Estimate compute requirements.
- [ ] Confirm that the approach supports the forecasting outputs
      required by the experiment.

**Selected approach:** TBD

## 8. Choose the custom-model direction

The exact hyperparameters do not need to be decided yet.

- [ ] Choose a general model family.
- [ ] Define its expected inputs.
- [ ] Decide how multi-step forecasting will work.
- [ ] Determine whether it can produce uncertainty estimates directly.
- [ ] Define the training procedure at a high level.

Possible families include statistical models, tree-based models, neural
networks, and Transformer-based approaches.

**Selected custom-model direction:** TBD

## 9. Design the walk-forward evaluation

Random train/test splitting should not be used. Evaluation should
simulate forecasts using only information available at the time.

```text
Historical data ──────────────┐
                              │
                     Train / provide context
                              │
                              ▼
                       Forecast t+1...t+H
                              │
                              ▼
                     Reveal actual values
                              │
                              ▼
                       Move origin forward
                              │
                              └──────► repeat
```

- [ ] Choose the initial training/context window.
- [ ] Choose the held-out evaluation period.
- [ ] Decide between expanding and rolling windows where applicable.
- [ ] Define how frequently trainable models are refitted during
      backtesting.
- [ ] Ensure every model receives equivalent information at each
      forecast origin.
- [ ] Ensure no look-ahead leakage is possible.

**Evaluation design:** TBD

## 10. Choose evaluation metrics

### Point forecasts

- [ ] Research appropriate metrics such as MAE and RMSE.
- [ ] Decide how to compare stocks with different price scales.
- [ ] Decide how results are reported across `t+1`, `t+5`, and `t+20`.
- [ ] Decide how results are aggregated across the stock basket.

### Probabilistic forecasts

- [ ] Research coverage/calibration metrics.
- [ ] Consider interval width/sharpness.
- [ ] Research proper probabilistic scoring methods where appropriate.

**Selected metrics:** TBD

## 11. Define the uncertainty experiment

Where possible, forecasts should include uncertainty rather than only a
point estimate.

```text
Point forecast:          $201.34
80% prediction interval: $198.20 – $204.10
95% prediction interval: $195.80 – $207.30
```

The interval levels above are examples, not final decisions.

- [ ] Choose the uncertainty representation.
- [ ] Choose interval/quantile levels.
- [ ] Determine how to handle point-only models.
- [ ] Define how calibration/coverage is evaluated.
- [ ] Define how interval width is evaluated.

**Uncertainty setup:** TBD

## 12. Write the V1 experiment specification

Before implementing the main experiment, summarize the decisions in one
short specification:

```text
Assets:
Data source:
Date range:

Target:
Forecast horizons:

Inputs:

Baseline:
Zero-shot model:
Adapted model:
Custom model:

Backtesting method:

Point metrics:
Probabilistic metrics:
```

- [ ] Complete the specification.
- [ ] Review it for look-ahead leakage.
- [ ] Confirm that the model families can be compared fairly.
- [ ] Commit the specification before the main modeling experiments
      begin.

This becomes the initial contract for V1. It can change when the data or
research provides a good reason, but changes should be deliberate and
documented.

## Not deciding yet

These are deliberately outside the pre-coding phase:

- MLflow architecture
- Docker image design
- Cloud provider/infrastructure
- Terraform structure
- Kubernetes architecture
- Helm
- Argo CD
- Argo Workflows
- Production deployment architecture
- Model registry strategy
- Continuous-training cadence
- Drift-triggered retraining

These should be introduced when the project creates a real reason to use
them.

## Immediate order of work

```text
Choose stock basket
        ↓
Choose data source
        ↓
Define target and inputs
        ↓
Choose baselines
        ↓
Research foundation models
        ↓
Define adapted + custom approaches
        ↓
Design walk-forward evaluation
        ↓
Choose metrics + uncertainty evaluation
        ↓
Write V1 experiment specification
        ↓
Start implementation
```

The first task is:

> **Choose and justify the stock basket.**

```

```
