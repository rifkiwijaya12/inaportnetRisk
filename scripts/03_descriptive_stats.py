#descriptive statistics - approval
approval_stats = pd.DataFrame({
    'NumberOfData': [df_PKK['approval_minutes'].count()],
    'Minimum': [df_PKK['approval_minutes'].min()],
    'Q1': [df_PKK['approval_minutes'].quantile(0.25)],
    'Median': [df_PKK['approval_minutes'].median()],
    'Mean': [df_PKK['approval_minutes'].mean()],
    'Q3': [df_PKK['approval_minutes'].quantile(0.75)],
    'P95' : [df_PKK['approval_minutes'].quantile(0.95)],
    'Maximum': [df_PKK['approval_minutes'].max()],
    'StdDev': [df_PKK['approval_minutes'].std()]
})
approval_stats = approval_stats.round(3)


import matplotlib.pyplot as plt
from scipy.stats import skew
import numpy as np

P95 = df_PKK['approval_minutes'].quantile(0.95)
# Data volume
data_approval = df_PKK['approval_minutes']
data_approvalP95 = df_PKK[df_PKK['approval_minutes']<P95]
data_approvalP95 = data_approvalP95['approval_minutes']

meanP95 = data_approvalP95.mean()
medianP95 = data_approvalP95.median()
skewnessP95 = skew(data_approvalP95)

# create figure
fig, axes = plt.subplots(1, 2, figsize=(14,5))

# Plot 1 : Histogram
# =====================================================
ax = axes[0]

ax.hist(
    data_approvalP95,
    bins=100,
    edgecolor='grey',
    color='#30D5C8'
)

# Mean
ax.axvline(
    meanP95,
    color='red',
    linestyle='--',
    linewidth=2,
    label=f'Mean = {meanP95:.1f}'
)

# Median
ax.axvline(
    medianP95,
    color='blue',
    linestyle='-',
    linewidth=2,
    label=f'Median = {medianP95:.1f}'
)

# Nilai skewness
ax.text(
    0.98,
    0.95,
    f'Skewness = {skewnessP95:.2f}\n'
    f'Percentile-95 = {P95:.2f}',
    transform=ax.transAxes,
    ha='right',
    va='top',
    bbox=dict(facecolor='white', edgecolor='black')
)

ax.set_title('Distribution of approval in minutes within Percentile95')
ax.set_xlabel('Approval (minutes)')
ax.set_ylabel('Frequency')
ax.legend()
ax.grid(alpha=0.3)

# =====================================================
# Plot 2 : Boxplot
# =====================================================
from matplotlib.lines import Line2D

ax = axes[1]

ax.boxplot(
    data_approval,
    vert=True,
    patch_artist=True,
    showmeans=True,
    meanline=True,
    widths=0.4,
    boxprops=dict(facecolor='skyblue', edgecolor='black'),
    whiskerprops=dict(color='black'),
    capprops=dict(color='black'),
    medianprops=dict(color='red', linewidth=2),
    meanprops=dict(color='blue', linewidth=2),
    flierprops=dict(marker='o',
                    markersize=4,
                    markerfacecolor='gray',
                    markeredgecolor='black',
                    alpha=0.6)
)

legend_elements = [
    Line2D([0], [0], color='red', lw=2, label='Mean'),
    Line2D([0], [0], color='blue', lw=2, label='Median')
]

ax.legend(handles=legend_elements, loc='upper right')
ax.set_title('Approval in Minutes')
ax.set_xlabel('approval')
ax.set_ylabel('minutes')

plt.tight_layout()
plt.show()


#statistic descriptive - volume

volume_port = (
    df_PKK
    .groupby('port')
    .agg(
        volume=('approval_minutes', 'count')
    )
    .reset_index()
)

volume_stats = pd.DataFrame({
    'NumberOfData': [volume_port['volume'].count()],
    'Minimum': [volume_port['volume'].min()],
    'Q1': [volume_port['volume'].quantile(0.25)],
    'Median': [volume_port['volume'].median()],
    'Q3': [volume_port['volume'].quantile(0.75)],
    'Maximum': [volume_port['volume'].max()],
    'Mean': [volume_port['volume'].mean()],
    'Std Dev': [volume_port['volume'].std()]
})
volume_stats = volume_stats.round(2)

print(volume_stats)

import matplotlib.pyplot as plt
from scipy.stats import skew
import numpy as np

# Data volume

data = volume_port['volume']
Per95_volume = volume_port['volume'].quantile(0.95)
data95 = volume_port[volume_port['volume']<Per95_volume]
data95 = data95['volume']


# Statistics
mean = data.mean()
median = data.median()
skewness = skew(data)

# create figure
fig, axes = plt.subplots(1, 2, figsize=(14,5))

# =====================================================
# Plot 1 : Histogram
# =====================================================
ax = axes[0]

ax.hist(
    data,
    bins=160,
    edgecolor='grey',
    color='#1E5D3F'
)

# Mean
ax.axvline(
    mean,
    color='red',
    linestyle='--',
    linewidth=2,
    label=f'Mean = {mean:.1f}'
)

# Median
ax.axvline(
    median,
    color='blue',
    linestyle='-',
    linewidth=2,
    label=f'Median = {median:.1f}'
)

# skewness
ax.text(
    0.98,
    0.95,
    f'Skewness = {skewness:.2f}\n',
    transform=ax.transAxes,
    ha='right',
    va='top',
    bbox=dict(facecolor='white', edgecolor='black')
)

ax.set_title('Histogram of Port Volume')
ax.set_xlabel('Volume')
ax.set_ylabel('Frequency')
ax.legend()
ax.grid(alpha=0.3)

# =====================================================
# Plot 2 : Boxplot
# =====================================================
from matplotlib.lines import Line2D

ax = axes[1]

ax.boxplot(
    data,
    vert=True,
    patch_artist=True,
    showmeans=True,
    meanline=True,
    widths=0.4,
    boxprops=dict(facecolor='skyblue', edgecolor='black'),
    whiskerprops=dict(color='black'),
    capprops=dict(color='black'),
    medianprops=dict(color='red', linewidth=2),
    meanprops=dict(color='blue', linewidth=2),
    flierprops=dict(marker='o',
                    markersize=4,
                    markerfacecolor='gray',
                    markeredgecolor='black',
                    alpha=0.6)
)

legend_elements = [
    Line2D([0], [0], color='blue', lw=2, label='Median'),
    Line2D([0], [0], color='red', lw=2, label='Mean')
]

ax.legend(handles=legend_elements, loc='upper right')

plt.tight_layout()
plt.show()
