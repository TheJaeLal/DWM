import copy
def cal_dist(data,point):
	diff = []
	for i in data:
		diff.append(((i[0]-point[0])**2 + (i[1]-point[1])**2)**(1/2))
	return diff

def assign_cluster(clusters,dist,M,data):
	for i in range(N): #Iterate over dataset..
		min_dist = 100000 #Infinite
		min_c = -1 # Initialized
		for c in range(M): #Iterate over clusters..
			if dist[c][i] < min_dist:
				min_dist = dist[c][i]
				min_c = c
		clusters[min_c].append(data[i])
		
def cal_centroid(clusters,M,centroids):
	for c in range(M):
		my_sumx = 0
		my_sumy = 0
		size = len(clusters[c])
		for i in range(size): #Each cluster may be of different size
			my_sumx+=clusters[c][i][0]
			my_sumy+=clusters[c][i][1]

		centroids[c][0] = my_sumx/size
		centroids[c][1] = my_sumy/size 

def display_clusters(clusters):
	print('********The Clusters are as follows**********')
	for i in range(M):
		print(' C{}'.format(i),end = '\t ')
	print(' ')
	print('------------------------------')
	i = 0
	while(True):
		count = 0
		for c in range(M):
			if i+1<=len(clusters[c]):
				count+=1
				print('({0},{1})'.format(clusters[c][i][0],clusters[c][i][1]),end = '\t')
			else:
				print('\t',end = '')
		if count==0:
			break
		else:
			i+=1
		print('')

#main starts here...        
#print('Enter the data set separating each element with spaces:')
#rip = input().split()
#data = [int(i) for i in rip]
#print(data)
data = [[40,53],[70,12],[21,25],[100,75],[5,30],[10,10]]
N = len(data)

#print('Enter the number of clusters')
#M = int(input())
M = 2

#Select the first 3 data points as centroids...
centroids = copy.deepcopy(data[:M])
#print(centroids)

#Intialize clusters as list of lists...
clusters = []
for i in range(M):
	clusters.append([])

#Initialize distance as list of lists...
dist = []
for c in range(M):
	dist.append(cal_dist(data,centroids[c]))

assign_cluster(clusters,dist,M,data)
#print(clusters)

cal_centroid(clusters,M,centroids)
#print(centroids)

while(True):
	dist = []
	for c in range(M):
		dist.append(cal_dist(data,centroids[c]))

	clusters = []
	for i in range(M):
		clusters.append([])

	assign_cluster(clusters,dist,M,data)

	old_centroids = copy.deepcopy(centroids)
	cal_centroid(clusters,M,centroids)

	if old_centroids==centroids:
		break

print(clusters)
display_clusters(clusters)
