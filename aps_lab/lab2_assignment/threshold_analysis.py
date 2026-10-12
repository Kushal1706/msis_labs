import pandas as pd

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


def compare_threshold_predictions(
    results,
    thresholds
):

    for threshold in thresholds:

        predictions = (
            results["P_malignant"] >= threshold
        ).astype(int)

        print(
            f"Threshold={threshold}: "
            f"Predicted malignant cases = "
            f"{predictions.sum()}"
        )


def show_confusion_matrices(
    results,
    actual_malignant,
    thresholds
):

    for threshold in thresholds:

        predicted_malignant = (
            results["P_malignant"] >= threshold
        ).astype(int)

        cm = confusion_matrix(
            actual_malignant,
            predicted_malignant
        )

        print(f"\nThreshold = {threshold}")
        print(cm)


def calculate_threshold_metrics(
    results,
    actual_malignant,
    thresholds
):

    threshold_metrics = []

    for threshold in thresholds:

        predicted_malignant = (
            results["P_malignant"] >= threshold
        ).astype(int)

        cm = confusion_matrix(
            actual_malignant,
            predicted_malignant
        )

        tn = cm[0, 0]
        fp = cm[0, 1]
        fn = cm[1, 0]
        tp = cm[1, 1]

        threshold_metrics.append({
            "Threshold": threshold,
            "TP": tp,
            "TN": tn,
            "FP": fp,
            "FN": fn,

            "Accuracy": accuracy_score(
                actual_malignant,
                predicted_malignant
            ),

            "Precision": precision_score(
                actual_malignant,
                predicted_malignant
            ),

            "Recall": recall_score(
                actual_malignant,
                predicted_malignant
            ),

            "F1 Score": f1_score(
                actual_malignant,
                predicted_malignant
            )
        })

    threshold_metrics = pd.DataFrame(
        threshold_metrics
    )

    print("\nThreshold Metrics:")

    print(
        threshold_metrics.round(3).to_string(
            index=False
        )
    )

    return threshold_metrics
