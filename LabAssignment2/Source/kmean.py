#import sklearn package for accuracy,metrics,datasets,split train & test data
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import neighbors,datasets
#load iris datasets
dataset =datasets.load_iris()
#load data & target into x and y
x=dataset.data
y=dataset.target
#split training & testing data into x and y with 20% testing data & 80%training data
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.2, random_state=22)
#define the kmean model
kmeanmodel=neighbors.KNeighborsClassifier(n_neighbors=60)
#fit training data into kmeanmodel
kmeanmodel.fit(train_x, train_y)
#predict kmean for test data
predict=kmeanmodel.predict(test_x)
#calc the accuracy score using kmean model
print("Accuracy is: :", accuracy_score(predict, test_y))