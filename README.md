# Financial Time-Series Forecasting

A learning project for building an end-to-end **CI/CD and MLOps
workflow** around a financial time-series forecasting problem.

## Project Goal

The project will forecast the **next trading day's closing stock price
(t+1)** for a basket of stocks. Each stock will be modeled
independently.

Forecasts will include both a **point prediction** and **prediction
intervals** to represent uncertainty.

Three modeling approaches are planned:

1.  **Zero-shot time-series foundation model**
2.  **Pretrained/adapted model**, potentially fine-tuned on financial
    data
3.  **Custom model** trained from scratch

The models will be evaluated using the same walk-forward forecasting
setup and compared against a simple naive baseline.

## MLOps Roadmap

The project will gradually be extended with:

-   Automated testing and CI
-   Docker
-   MLflow
-   Infrastructure as Code with Terraform
-   Kubernetes and Helm
-   Argo CD / Argo Workflows
-   Model and system monitoring

Model selection, the stock basket, data source, evaluation metrics, and
other modeling details will be decided during the research and
experimentation phases.
