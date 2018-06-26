from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
data=load_iris()
x=data.data
y=data.target
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.2, random_state=12)
ldamodel=LinearDiscriminantAnalysis()
logmodel=LogisticRegression()
ldamodel.fit(train_x,train_y)
liprediction=ldamodel.predict(test_x)
print("linear regression accuracy is ", accuracy_score(liprediction, test_y))
logmodel.fit(train_x, train_y)
loprediction=logmodel.predict(test_x)
print("logistic regression accuracy is ", accuracy_score(loprediction, test_y))