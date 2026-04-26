import matplotlib.pyplot as plt
import  numpy as  np 

def plot_graphs(store_IDs, cum_growth, predictions, best_store_index, future_best):

    months = [1,2,3,4]
    months_extended = [1,2,3,4,5]

    fig, ax = plt.subplots(2, 1, figsize=(8,8))

    # GRAPH 1
    ax[0].set_title("Original Cumulative Growth")
    ax[0].set_xlabel("Months")
    ax[0].set_ylabel("Cumulative Growth")
    ax[0].grid(True)

    for i in range(len(store_IDs)):
        if i == best_store_index:
            ax[0].plot(months, cum_growth[i], marker='o',
                       label=f"Store {store_IDs[i]} (Best)")
        else:
            ax[0].plot(months, cum_growth[i], marker='o',
                       label=f"Store {store_IDs[i]}")

    ax[0].legend()

    # GRAPH 2
    ax[1].set_title("Cumulative Growth with Prediction")
    ax[1].set_xlabel("Months")
    ax[1].set_ylabel("Cumulative Growth")
    ax[1].grid(True)

    for i in range(len(store_IDs)):
        extended = np.append(cum_growth[i], predictions[i])

        if i == future_best:
            ax[1].plot(months_extended, extended, marker='o',
                       color='green', linewidth=3,
                       label=f"Store {store_IDs[i]} (Future Best)")

        elif i == best_store_index:
            ax[1].plot(months_extended, extended, marker='o',
                       color='red', linewidth=3,
                       label=f"Store {store_IDs[i]} (Current Best)")

        else:
            ax[1].plot(months_extended, extended, marker='o',
                       linestyle='--',
                       label=f"Store {store_IDs[i]}")

    ax[1].legend()

    plt.tight_layout()
    plt.show()