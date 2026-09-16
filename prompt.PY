import matplotlib.pyplot as plt
import numpy as np

# Rating Grades
rating_grades = [
    "CNR-I", "CNR-II", "CNR-III", "CNR-IV", "CNR-V",
    "CNR-VI", "CNR-VII", "CNR-VIII", "CNR-IX", "CNR-X", "CNR-XI"
]

# Modified PD values (%)
# N/A values are kept blank using np.nan

data = {
    "Overall CIRM": [
        0.03, 0.13, 0.23, 0.42, 0.75,
        1.36, 2.42, 4.30, 7.51, 12.79, 20.96
    ],

    "LEM": [
        0.03, 0.12, 0.23, 0.45, 0.88,
        1.73, 3.36, 6.43, 15.62, 21.18, 34.69
    ],

    "SME MFG": [
        np.nan, np.nan, 0.06, 0.21, 0.41,
        0.38, 0.70, 1.27, 2.31, 11.65, 7.34
    ],

    "SME Service": [
        np.nan, np.nan, 0.73, 0.73, 1.04,
        1.47, 2.08, 2.94, 4.14, 5.80, 8.07
    ],

    "LTM": [
        np.nan, np.nan, 0.06, 0.14, 0.33,
        0.74, 1.66, 3.69, 8.01, 16.49, 30.94
    ],

    "STM": [
        np.nan, np.nan, np.nan, 0.28, 0.24,
        0.36, 0.82, 2.48, 5.53, 7.29, 8.01
    ],

    "NBFC": [
        0.03, 0.03, 0.03, 0.04, 0.08,
        0.37, 1.60, 3.27, 4.21, 4.36, 4.41
    ],

    "Real Estate": [
        np.nan, np.nan, 0.67, 0.68, 0.71,
        0.82, 1.07, 1.58, 2.88, 5.54, 10.83
    ]
}

# ============================================================
# CREATE CHART
# ============================================================

plt.figure(figsize=(15, 8))

x = np.arange(len(rating_grades))

# Plot all 8 lines
for name, values in data.items():
    plt.plot(
        x,
        values,
        marker="o",
        linewidth=2,
        markersize=5,
        label=name
    )

# X-axis
plt.xticks(
    x,
    rating_grades,
    fontsize=10
)

plt.xlabel(
    "Rating Grades",
    fontsize=12,
    fontweight="bold"
)

# Y-axis
plt.ylabel(
    "Modified PD (%)",
    fontsize=12,
    fontweight="bold"
)

# Title
plt.title(
    "Modified PD Across Rating Grades",
    fontsize=16,
    fontweight="bold"
)

# Grid
plt.grid(
    True,
    linestyle="--",
    alpha=0.5
)

# Legend
plt.legend(
    title="Module",
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)

# Start Y-axis from zero
plt.ylim(bottom=0)

# Adjust layout
plt.tight_layout()

# Display chart
plt.show()
