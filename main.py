import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
data = pd.read_csv("ai4i2020.csv")


# Inspect the dataset
print("First five rows:")
print(data.head())

print("\nDataset shape (rows, columns):")
print(data.shape)

print("\nColumn names:")
print(data.columns.tolist())

print("\nMissing values by column:")
print(data.isna().sum())


# Count samples by machine failure status
# 0 = No failure, 1 = Failure
print("\nMachine failure counts:")
print(data["Machine failure"].value_counts())


# Calculate the overall machine failure rate
failure_count = data["Machine failure"].sum()
total_count = len(data)
failure_rate = (failure_count / total_count) * 100

print(f"\nOverall machine failure rate: {failure_rate:.2f}%")


# Calculate process temperature minus air temperature for each sample
data["Temperature difference [K]"] = (
    data["Process temperature [K]"] - data["Air temperature [K]"]
)


# Calculate average measurements for each failure status
features = [
    "Torque [Nm]",
    "Tool wear [min]",
    "Rotational speed [rpm]",
    "Temperature difference [K]",
]

comparison = data.groupby("Machine failure")[features].mean()

print("\nAverage measurements by failure status:")
print(comparison.round(2))


# Save the comparison table
comparison.round(2).to_csv("comparison_summary.csv")


# Calculate failure type rates as percentages of all samples
# The mean of a binary column is the fraction of samples with value 1
failure_types = ["TWF", "HDF", "PWF", "OSF", "RNF"]
failure_type_rates = data[failure_types].mean() * 100

print("\nFailure rates by type (%):")
print(failure_type_rates.round(2))


# Save failure type rates
failure_type_rates.round(2).to_csv(
    "failure_type_rates.csv",
    header=["Failure rate (%)"],
)


# Plot average torque by machine failure status
plt.figure()
ax = comparison["Torque [Nm]"].plot(kind="bar", rot=0)

plt.title("Average torque by failure status")
plt.xlabel("Machine failure (0 = No, 1 = Yes)")
plt.ylabel("Average torque [Nm]")

ax.bar_label(ax.containers[0], fmt="%.2f", padding=3)
ax.margins(y=0.15)

plt.tight_layout()
plt.savefig("average_torque.png", dpi=150)
plt.show()


# Plot average tool wear by machine failure status
plt.figure()
ax = comparison["Tool wear [min]"].plot(kind="bar", rot=0)

plt.title("Average tool wear by failure status")
plt.xlabel("Machine failure (0 = No, 1 = Yes)")
plt.ylabel("Average tool wear [min]")

ax.bar_label(ax.containers[0], fmt="%.2f", padding=3)
ax.margins(y=0.15)

plt.tight_layout()
plt.savefig("average_tool_wear.png", dpi=150)
plt.show()


# Plot average temperature difference by machine failure status
# This comparison includes all machine failures, not only HDF
plt.figure()
ax = comparison["Temperature difference [K]"].plot(kind="bar", rot=0)

plt.title("Average temperature difference by failure status")
plt.xlabel("Machine failure (0 = No, 1 = Yes)")
plt.ylabel("Average process − air temperature [K]")

ax.bar_label(ax.containers[0], fmt="%.2f", padding=3)
ax.margins(y=0.15)

plt.tight_layout()
plt.savefig("average_temperature_difference.png", dpi=150)
plt.show()


# Plot failure type rates
# Each percentage uses all samples as its denominator
plt.figure()
ax = failure_type_rates.plot(kind="bar", rot=0)

plt.title("Failure rates by type")
plt.xlabel("Failure type")
plt.ylabel("Samples with this failure type (%)")

ax.bar_label(ax.containers[0], fmt="%.2f%%", padding=3)
ax.margins(y=0.15)

plt.tight_layout()
plt.savefig("failure_type_rates.png", dpi=150)
plt.show()