import pandas as pd


def generate_probabilities(model, X_test):

    probabilities = model.predict_proba(X_test)

    print(probabilities[:5])

    print(probabilities[:5].sum(axis=1))

    return probabilities


def create_results(probabilities, y_test):

    results = pd.DataFrame({
        "Actual_class": y_test.values,
        "P_malignant": probabilities[:, 0],
        "P_benign": probabilities[:, 1]
    })

    print(results.head(10))

    results["Actual_label"] = results[
        "Actual_class"
    ].map({
        0: "Malignant",
        1: "Benign"
    })

    print(
        results[
            [
                "Actual_label",
                "P_malignant",
                "P_benign"
            ]
        ].head(10)
    )

    return results


def create_predictions(results, threshold=0.50):

    results["Predicted_malignant"] = (
        results["P_malignant"] >= threshold
    ).astype(int)

    results["Predicted_label"] = results[
        "Predicted_malignant"
    ].map({
        1: "Malignant",
        0: "Benign"
    })

    print(
        results[
            [
                "Actual_label",
                "P_malignant",
                "Predicted_label"
            ]
        ].head(10)
    )

    return results
