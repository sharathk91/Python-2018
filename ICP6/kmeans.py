#import pandas library
import pandas
import pylab as pl
#import kmeans
from sklearn.cluster import KMeans
#import pca for calc elbow curve
from sklearn.decomposition import PCA
#import the csv file
variables = pandas.read_csv('sample_stocks.csv')
#load the column values of dataset
Y = variables[['returns']]
X = variables[['dividendyield']]
#calc normal values
X_norm = (X - X.mean()) / (X.max() - X.min())
Y_norm = (Y - Y.mean()) / (Y.max() - Y.min())
#define the range
Nc = range(1, 20)
#define the range to calc kmeans algorithm for range of 20 nos
kmeans = [KMeans(n_clusters=i) for i in Nc]
kmeans
#dalc score for all kmeans ranging from 1 to 20 nos
score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]
score
#plot the elbow curve
pl.plot(Nc,score)
#define the labels
pl.xlabel('Number of Clusters')
pl.ylabel('Score')
pl.title('Elbow Curve')
#show the elbow curve
pl.show()
#define the components to fit into model
pca = PCA(n_components=1).fit(Y)
#calc cluster values
pca_d = pca.transform(Y)
pca_c = pca.transform(X)
#call the kmeans with k=3
kmeans=KMeans(n_clusters=3)
#define the kmeans to fit into model
kmeansoutput=kmeans.fit(Y)
kmeansoutput
#define the labels
pl.figure('3 Cluster K-Means')
pl.scatter(pca_c[:, 0], pca_d[:, 0], c=kmeansoutput.labels_)
pl.xlabel('Dividend Yield')
pl.ylabel('Returns')
pl.title('3 Cluster K-Means')
#sho the plotted graph for 3 clusters
pl.show()