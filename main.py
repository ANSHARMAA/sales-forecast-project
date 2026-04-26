import pandas as pd

from analysis.revenue_analysis import analyze_revenue
from ml.prediction import predict_future
from visualization.plot import plot_graphs

# Load data
df = pd.read_csv("data/sales.csv")

# Analysis
store_IDs, total_revenue, best_store_index, cum_growth = analyze_revenue(df)

# ML Prediction
predictions, future_best = predict_future(cum_growth, store_IDs)


# Output
print("-----Revenue-----")
for i in range(len(store_IDs)):
    print(f"Store {store_IDs[i]} -> {total_revenue[i]}")

print(f"\nCurrent Best Store: {store_IDs[best_store_index]}")
print(f"Future Best Store: {store_IDs[future_best]}")

# Visualization
plot_graphs(store_IDs, cum_growth, predictions, best_store_index, future_best)