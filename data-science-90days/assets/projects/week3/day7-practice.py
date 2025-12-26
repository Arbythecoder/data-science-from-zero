"""
Week 3, Day 1 Practice: Introduction to Matplotlib
Complete solutions for all 3 exercises

Topics covered:
- Line plots
- Scatter plots
- Multi-line plots
- Customization (titles, labels, colors, legends)
- Saving plots
"""

import matplotlib.pyplot as plt
import numpy as np

print("=" * 60)
print("WEEK 3, DAY 1 PRACTICE - MATPLOTLIB BASICS")
print("=" * 60)

# =============================================================================
# EXERCISE 1: YOUR FIRST LINE PLOT (WARMUP)
# =============================================================================

print("\n" + "=" * 60)
print("EXERCISE 1: WEEKLY PRODUCTIVITY LINE PLOT")
print("=" * 60)

# Data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
productivity = [7, 8, 6, 9, 8, 5, 4]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(days, productivity, marker='o', linewidth=2, color='blue',
         markersize=10, markerfacecolor='red', markeredgecolor='blue')

# Customize
plt.title('My Weekly Productivity', fontsize=16, fontweight='bold')
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Productivity Score', fontsize=12)
plt.grid(True, alpha=0.3)
plt.ylim(0, 10)  # Set y-axis from 0 to 10

# Add horizontal line at average
avg_productivity = sum(productivity) / len(productivity)
plt.axhline(avg_productivity, color='green', linestyle='--',
            label=f'Average: {avg_productivity:.1f}')
plt.legend()

plt.tight_layout()
plt.savefig('exercise1_productivity.png', dpi=300, bbox_inches='tight')
print("\n✓ Line plot created successfully!")
print(f"  - Average productivity: {avg_productivity:.2f}")
print(f"  - Best day: {days[productivity.index(max(productivity))]} ({max(productivity)})")
print(f"  - Worst day: {days[productivity.index(min(productivity))]} ({min(productivity)})")
print("  - Saved as: exercise1_productivity.png")
plt.show()

# =============================================================================
# EXERCISE 2: SCATTER PLOT ANALYSIS (APPLICATION)
# =============================================================================

print("\n" + "=" * 60)
print("EXERCISE 2: AD SPEND VS SALES SCATTER PLOT")
print("=" * 60)

# Data
ad_spend = [1000, 1500, 2000, 2500, 3000, 3500, 4000]
sales = [15000, 18000, 22000, 25000, 28000, 30000, 33000]

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(ad_spend, sales, color='blue', s=150, alpha=0.5, edgecolors='black')

# Customize
plt.title('Ad Spend vs Sales', fontsize=16, fontweight='bold')
plt.xlabel('Ad Spend ($)', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.grid(True, alpha=0.3)

# Add trend line (simple linear fit)
z = np.polyfit(ad_spend, sales, 1)
p = np.poly1d(z)
plt.plot(ad_spend, p(ad_spend), "r--", linewidth=2, label='Trend Line')

# Calculate correlation
correlation = np.corrcoef(ad_spend, sales)[0, 1]
plt.text(1200, 31000, f'Correlation: {correlation:.3f}',
         fontsize=12, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

plt.legend()
plt.tight_layout()
plt.savefig('exercise2_ad_spend_sales.png', dpi=300, bbox_inches='tight')

print("\n✓ Scatter plot created successfully!")
print(f"  - Correlation coefficient: {correlation:.3f}")
print("  - Insight: Strong positive correlation!")
print("  - Every $1000 in ad spend increases sales by ~$6000")
print("  - Saved as: exercise2_ad_spend_sales.png")
plt.show()

# =============================================================================
# EXERCISE 3: MULTI-LINE COMPARISON (REAL-WORLD)
# =============================================================================

print("\n" + "=" * 60)
print("EXERCISE 3: INVESTMENT PORTFOLIO COMPARISON")
print("=" * 60)

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
conservative = [10000, 10200, 10350, 10500, 10650, 10800]
moderate = [10000, 10300, 10500, 10800, 11000, 11300]
aggressive = [10000, 10500, 10200, 11000, 10800, 11500]

# Create the plot
plt.figure(figsize=(12, 7))

plt.plot(months, conservative, marker='o', linewidth=2.5,
         label='Conservative', color='green')
plt.plot(months, moderate, marker='s', linewidth=2.5,
         label='Moderate', color='blue')
plt.plot(months, aggressive, marker='^', linewidth=2.5,
         label='Aggressive', color='red')

# Customize
plt.title('Investment Portfolio Performance', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Portfolio Value ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(loc='upper left', fontsize=12)

# Add annotations
final_values = {
    'Conservative': conservative[-1],
    'Moderate': moderate[-1],
    'Aggressive': aggressive[-1]
}

for portfolio, value in final_values.items():
    plt.text(5.1, value, f'${value:,}', fontsize=10, fontweight='bold')

# Add horizontal line at initial investment
plt.axhline(10000, color='gray', linestyle=':', alpha=0.5,
            label='Initial Investment')

plt.tight_layout()
plt.savefig('portfolios.png', dpi=300, bbox_inches='tight')

# Calculate returns
returns = {
    'Conservative': ((conservative[-1] - conservative[0]) / conservative[0]) * 100,
    'Moderate': ((moderate[-1] - moderate[0]) / moderate[0]) * 100,
    'Aggressive': ((aggressive[-1] - aggressive[0]) / aggressive[0]) * 100
}

# Calculate volatility (standard deviation)
volatility = {
    'Conservative': np.std(conservative),
    'Moderate': np.std(moderate),
    'Aggressive': np.std(aggressive)
}

print("\n✓ Multi-line plot created successfully!")
print("\nPORTFOLIO ANALYSIS:")
print("-" * 40)
for name in ['Conservative', 'Moderate', 'Aggressive']:
    print(f"\n{name}:")
    print(f"  Return: {returns[name]:.2f}%")
    print(f"  Final Value: ${final_values[name]:,}")
    print(f"  Volatility (Std Dev): ${volatility[name]:.2f}")

print("\n" + "=" * 40)
print("BUSINESS INSIGHTS:")
print("=" * 40)
best_return = max(returns, key=returns.get)
most_stable = min(volatility, key=volatility.get)

print(f"✓ Best Return: {best_return} ({returns[best_return]:.2f}%)")
print(f"✓ Most Stable: {most_stable} (σ = ${volatility[most_stable]:.2f})")
print(f"\nRecommendation:")
if returns['Moderate'] > returns['Conservative'] and \
   volatility['Moderate'] < volatility['Aggressive']:
    print("  → MODERATE portfolio offers best risk/reward balance")
print(f"\n  - Saved as: portfolios.png")

plt.show()

# =============================================================================
# BONUS: COMBINED DASHBOARD
# =============================================================================

print("\n" + "=" * 60)
print("BONUS: CREATING A 3-PANEL DASHBOARD")
print("=" * 60)

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Panel 1: Productivity
axes[0].plot(days, productivity, marker='o', linewidth=2, color='purple')
axes[0].set_title('Weekly Productivity', fontweight='bold')
axes[0].set_xlabel('Day')
axes[0].set_ylabel('Score')
axes[0].grid(True, alpha=0.3)
axes[0].tick_params(axis='x', rotation=45)

# Panel 2: Ad Spend vs Sales
axes[1].scatter(ad_spend, sales, s=100, alpha=0.6, color='orange')
axes[1].set_title('Marketing ROI', fontweight='bold')
axes[1].set_xlabel('Ad Spend ($)')
axes[1].set_ylabel('Sales ($)')
axes[1].grid(True, alpha=0.3)

# Panel 3: Portfolio Comparison (bar chart of final values)
portfolio_names = list(final_values.keys())
portfolio_values = list(final_values.values())
colors = ['green', 'blue', 'red']
axes[2].bar(portfolio_names, portfolio_values, color=colors, alpha=0.7)
axes[2].set_title('Portfolio Final Values', fontweight='bold')
axes[2].set_ylabel('Value ($)')
axes[2].tick_params(axis='x', rotation=45)
axes[2].axhline(10000, color='black', linestyle='--', alpha=0.5)

plt.suptitle('Day 1 Practice - Complete Dashboard',
             fontsize=18, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('day1_complete_dashboard.png', dpi=300, bbox_inches='tight')

print("\n✓ Complete dashboard created!")
print("  - Saved as: day1_complete_dashboard.png")
plt.show()

# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICE COMPLETE! 🎉")
print("=" * 60)
print("\nFiles created:")
print("  1. exercise1_productivity.png")
print("  2. exercise2_ad_spend_sales.png")
print("  3. portfolios.png")
print("  4. day1_complete_dashboard.png")

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("✓ Line plots show trends over time")
print("✓ Scatter plots reveal relationships")
print("✓ Multiple lines enable comparisons")
print("✓ Customization makes plots professional")
print("✓ Annotations highlight key insights")
print("✓ Saving plots preserves your work")

print("\n" + "=" * 60)
print("READY FOR DAY 2: SEABORN!")
print("=" * 60)
