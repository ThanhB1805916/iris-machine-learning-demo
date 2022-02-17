import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree


def tree_predict(data=[]):
    iris = pd.read_csv("data/iris.csv")

    X = iris.drop(columns=['variety'])
    y = iris['variety']

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.25)

    model = tree.DecisionTreeClassifier(criterion="gini")
    model.fit(X_train, y_train)

    df = pd.DataFrame(data=[data], columns=[
                      "sepal.length", "sepal.width",	"petal.length",	"petal.width"])
    y_pred = model.predict(df)

    return y_pred[0]
