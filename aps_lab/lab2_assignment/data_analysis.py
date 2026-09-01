import pandas as pd
import matplotlib.pyplot as plt


def show_basic_information(data, X, y):

    print(y.value_counts())

    print("Feature matrix Shape:", X.shape)
    print("Target Shape:", y.shape)
    print("Class name:", data.target_names)


def show_class_distribution(y):

    class_counts = y.value_counts().sort_index()

    class_distribution = pd.DataFrame({
        "Class": ["Malignant", "Benign"],
        "Count": class_counts.values,
        "Probability": class_counts.values / len(y)
    })

    print(class_distribution)

    class_distribution.plot(
        x="Class",
        y="Count",
        kind="bar",
        legend=False,
        color=["tomato", "steelblue"]
    )

    plt.ylabel("Number of observations")
    plt.title("Class Distribution")
    plt.xticks(rotation=0)
    plt.show()
