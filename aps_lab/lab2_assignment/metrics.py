from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


def calculate_metrics(model, X_test, y_test):

    y_pred = model.predict(X_test)

    print(
        "Sklearn accuracy:",
        accuracy_score(y_test, y_pred)
    )

    print(
        "Sklearn precision_score:",
        precision_score(y_test, y_pred)
    )

    print(
        "Sklearn recall_score:",
        recall_score(y_test, y_pred)
    )

    print(
        "Sklearn f1_score:",
        f1_score(y_test, y_pred)
    )
