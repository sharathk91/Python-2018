import numpy as np
import matplotlib.pyplot as plt
import random
#calc min distance between datapoints and centroids
def cluster_insert(X, mu):
    cluster = {}
    #for every point calc min distance for all centroids
    for x in X:
        value = min([(i[0],np.linalg.norm(x - mu[i[0]]))for i in enumerate(mu)], key=lambda s:s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster

#calc new centroid points
def new_center(mu,cluster):
    #make sorted order
    keys =sorted(cluster.keys())
    #calc new centroid points
    newmu = np.array([(np.mean(cluster[k],axis = 0))for k in keys])
    return newmu

def matched(newmu, oldmu):
    return (set([tuple(a)for a in newmu]) == set([tuple(a)for a in oldmu]))

#k-means algorithm
def Apply_Kmeans(X, K, N):
    # selecting random centroids from dataset and by number of clusters.

    #set initial centroid points
    t1 = np.random.randint(N, size = K)
    oldmu = np.array([X[i]for i in t1])
    #set new centroid points
    t2 = np.random.randint(N, size = K)
    newmu = np.array([X[i]for i in t2])
    #call the function to calc min distance for all data points
    cluster = cluster_insert(X, oldmu)
    itr = 0
    print("Graph after selecting initial clusters with initial centroids:")
    #plot cluster of points
    plot_cluster(oldmu,cluster,itr)
    #iterate until new and old centroids are matched
    while not matched(newmu, oldmu):
        itr = itr + 1
        oldmu = newmu
        cluster= cluster_insert(X,newmu)
        plot_cluster(newmu, cluster,itr)
        newmu = new_center(newmu,cluster)


    plot_cluster(newmu, cluster, itr)
    return
#plot graph using cluster method
def plot_cluster(mu,cluster, itr):
    color = 10 * ['r.','g.','k.','c.','b.','m.']
    print('Iteration number : ',itr)
    #plot the graph after grouping the points to the cluster
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    plt.scatter(mu[:,0],mu[:,1],marker = 'x', s = 150, linewidths = 5, zorder = 10)
    plt.show()

#create initial clusters for data points
def init_graph(N, p1, p2):
    #form the matrix by selecting random values
    X = np.array([(random.choice(p1),random.choice(p2))for i in range(N)])
    return X

#logic for taking inputs and plotting
def Simulate_Clusters():
    print(".........Starting Cluster Simulation.........")
    #take Tshirt height and weight
    a = np.array([31.6,28.9,34.7,32.6,29.89,36,33.19,37.69,40,34,23,21,26,27,28,29,30,35,36,37,38,39,40])
    b = np.array([18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40])
    #initialize the graph to plot the datapoints from arrays
    X = init_graph(len(a),b,a)
    plt.scatter(X[:, 0], X[:, 1])
    #display the graph to the user
    plt.show()
    #Apply the K means algorithm
    temp = Apply_Kmeans(X, len(b), len(X))

#main function to call the function Simulate_Clusters
if __name__ == '__main__':
    Simulate_Clusters()