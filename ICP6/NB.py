from sklearn import datasets,metrics
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split


irisdatasets=datasets.load_iris()
x=irisdatasets.data
y=irisdatasets.target

#split the data for training and testing cross validation
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

model=GaussianNB()
model.fit(x_train,y_train)
print(model.score(x_train,y_train))
y_pred = model.predict(x_test)
print("Accuracy",metrics.accuracy_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test,y_pred,average='weighted'))
print("Recall:",metrics.recall_score(y_test,y_pred,average='weighted'))
print("F1 Score:",metrics.f1_score(y_test,y_pred,average='weighted'))