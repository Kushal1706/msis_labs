from data_loader import load_dataset

from data_analysis import (
    show_basic_information,
    show_class_distribution
)

from data_split import split_data

from model import (
    create_model,
    train_model
)

from predictions import (
    generate_probabilities,
    create_results,
    create_predictions
)

from threshold_analysis import (
    compare_threshold_predictions,
    show_confusion_matrices,
    calculate_threshold_metrics
)

from metrics import calculate_metrics


def main():


    data, X, y = load_dataset()



    show_basic_information(
        data,
        X,
        y
    )


    show_class_distribution(y)



    X_train, X_test, y_train, y_test = split_data(
        X,
        y
    )


    model = create_model()

    model = train_model(
        model,
        X_train,
        y_train
    )


    probabilities = generate_probabilities(
        model,
        X_test
    )


    results = create_results(
        probabilities,
        y_test
    )

    results = create_predictions(
        results,
        threshold=0.50
    )


    thresholds = [
        0.10,
        0.20,
        0.30,
        0.50,
        0.70
    ]

    compare_threshold_predictions(
        results,
        thresholds
    )


    actual_malignant = (
        y_test.values == 0
    ).astype(int)

    show_confusion_matrices(
        results,
        actual_malignant,
        thresholds
    )


    calculate_metrics(
        model,
        X_test,
        y_test
    )

    threshold_metrics = calculate_threshold_metrics(
        results,
        actual_malignant,
        thresholds
    )


if __name__ == "__main__":
    main()
