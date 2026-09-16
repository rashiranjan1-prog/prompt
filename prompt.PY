import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ============================================================
# DATA
# ============================================================

rating_grades = [
    "CNR-I", "CNR-II", "CNR-III", "CNR-IV", "CNR-V",
    "CNR-VI", "CNR-VII", "CNR-VIII", "CNR-IX", "CNR-X", "CNR-XI"
]

data = {
    "Overall CIRM": [
        0.03, 0.03, 0.04, 0.08, 0.17,
        0.35, 0.72, 1.50, 3.08, 6.22, 12.16
    ],

    "LEM": [
        0.03, 0.03, 0.04, 0.10, 0.24,
        0.58, 1.36, 3.16, 7.20, 15.52, 30.35
    ],

    "SME MFG": [
        np.nan, np.nan, 0.02, 0.05, 0.11,
        0.26, 0.60, 1.38, 3.12, 6.94, 14.67
    ],

    "SME Service": [
        np.nan, np.nan, 0.03, 0.03, 0.03,
        0.48, 0.79, 1.30, 2.14, 4.49, 0.03
    ],

    "LTM": [
        np.nan, np.nan, 0.00, 0.01, 0.04,
        0.15, 0.48, 1.57, 4.97, 14.68, 36.12
    ],

    "STM": [
        np.nan, np.nan, np.nan, 0.13, 0.06,
        0.06, 0.06, 0.67, 9.48, 13.73, 14.22
    ],

    "NBFC": [
        0.03, 0.03, 0.03, 0.04, 0.07,
        0.27, 0.99, 1.47, 13.97, 1.68, 1.71
    ],

    "Real Estate": [
        np.nan, np.nan, 0.30, 0.30, 0.32,
        0.41, 0.77, 2.11, 4.31, 5.62, 9.69
    ]
}


# ============================================================
# 1. LINE CHART
# ============================================================

plt.figure(figsize=(15, 8))

x = np.arange(len(rating_grades))

for name, values in data.items():
    plt.plot(
        x,
        values,
        marker="o",
        linewidth=2,
        markersize=5,
        label=name
    )

plt.xticks(x, rating_grades, fontsize=10)

plt.xlabel(
    "Rating Grades",
    fontsize=12,
    fontweight="bold"
)

plt.ylabel(
    "Modified PD (%)",
    fontsize=12,
    fontweight="bold"
)

plt.title(
    "Modified PD Across Rating Grades",
    fontsize=16,
    fontweight="bold"
)

plt.grid(
    True,
    linestyle="--",
    alpha=0.5
)

plt.legend(
    title="Module",
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)

plt.ylim(bottom=0)

plt.tight_layout()

plt.show()


# ============================================================
# 2. PIVOT TABLE
# ============================================================

# Convert the dictionary into a DataFrame
df = pd.DataFrame(
    data,
    index=rating_grades
)

# Give the index the required name
df.index.name = "Grades"

# Convert into required pivot-style format
pivot_table = df.reset_index().melt(
    id_vars="Grades",
    var_name="Module Name",
    value_name="Modified PD"
)

# Create actual pivot table
pivot = pivot_table.pivot(
    index="Grades",
    columns="Module Name",
    values="Modified PD"
)

# Keep original rating grade order
pivot = pivot.reindex(rating_grades)

# Keep original module order
pivot = pivot.reindex(columns=data.keys())

# Display blank instead of NaN
pivot = pivot.fillna("")


# ============================================================
# DISPLAY PIVOT TABLE
# ============================================================

print("\n" + "=" * 100)
print("PIVOT TABLE")
print("=" * 100)

print(pivot.to_string())
