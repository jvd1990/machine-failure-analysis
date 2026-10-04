# Machine Failure Analysis with Python

This project explores machine failure data using pandas and Matplotlib.

## Objectives

- Load and inspect the AI4I 2020 Predictive Maintenance dataset.
- Calculate the overall failure rate and rates for each failure type.
- Compare average process temperature, torque, and tool wear between samples with and without machine failure.

## Tools

- Python
- pandas
- Matplotlib

## Results

- Total samples: 10,000
- Samples with machine failure: 339
- Overall machine failure rate: 3.39%
- No missing values were found.

### Failure rates by type

Each rate is calculated relative to all 10,000 samples.

| Failure type | Rate (%) |
| --- | --- |
| TWF | 0.46 |
| HDF | 1.15 |
| PWF | 0.95 |
| OSF | 0.98 |
| RNF | 0.19 |

### Comparison of averages

| Measurement | Without failure | With failure |
| --- | --- | --- |
| Torque (Nm) | 39.63 | 50.17 |
| Tool wear (min) | 106.69 | 143.78 |
| Process temperature (K) | 310.00 | 310.29 |

Samples with failure had higher average torque and tool wear.
The difference in average process temperature was small.
These comparisons describe associations and do not establish causation.

## Charts

### Torque
![Average torque](average_torque.png)

### Tool wear
![Average tool wear](average_tool_wear.png)

### Process temperature
![Average process temperature](average_process_temperature.png)
## How to run

1. Install Python.
2. Place `ai4i2020.csv` in the same folder as `main.py`.
3. Open a terminal in the project folder.
4. Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

5. Run the analysis:

```bash
python main.py
```

Close each chart window to continue to the next chart.

## Output files

- `comparison_summary.csv`: average torque, tool wear, and rotational speed by failure status.
- `failure_type_rates.csv`: percentage of samples for each failure type.
- Three PNG charts comparing torque, tool wear, and process temperature.

## Dataset source

AI4I 2020 Predictive Maintenance Dataset (2020).
UCI Machine Learning Repository.

- Dataset: https://archive.ics.uci.edu/dataset/601/ai4i
- DOI: https://doi.org/10.24432/C5HS5C
- License: CC BY 4.0
- License link: https://creativecommons.org/licenses/by/4.0/

The dataset contains 10,000 synthetic samples representing
industrial predictive maintenance conditions.
The original CSV is used without modification.