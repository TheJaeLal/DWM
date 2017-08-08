import copy
def cal_dist(data,point):
	diff = []
	for i in data:
		diff.append(abs(i-point))
	#print(diff)	
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
		my_sum = 0
		size = len(clusters[c])
		for i in range(size): #Each cluster may be of different size
			#print(c,i)			
			my_sum+=clusters[c][i]
		centroids[c] = my_sum/size     

def display_clusters(clusters):
	print('********The Clusters are as follows**********')
	for i in range(M):
		print('C{}'.format(i),end = '\t')
	print('')
	print('------------------------------')
	i = 0
	while(True):
		count = 0
		for c in range(M):
			if i+1<=len(clusters[c]):
				count+=1
				print(clusters[c][i],end = '\t')
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
data = [40,12,25,75,30,10]
N = len(data)

#print('Enter the number of clusters')
#M = int(input())
M = 2

#Select the first 3 data points as centroids...
centroids = data[:M]
#print(centroids)

#Intialize clusters as list of lists...
clusters = []
for i in range(M):
	clusters.append([])
#print(clusters)

#Initialize distance as list of lists...
dist = []
for c in range(M):
	#print('finding difference with respect to',centroids[c])
	dist.append(cal_dist(data,centroids[c]))
	#print(dist)

#print('final')
#print(dist)

#print(clusters)
assign_cluster(clusters,dist,M,data)
#print(clusters)

cal_centroid(clusters,M,centroids)
#print(centroids)

while(True):
	dist = []
	for c in range(M):
		#print('finding difference with respect to',centroids[c])
		dist.append(cal_dist(data,centroids[c]))
		#print(dist)

	#print(dist)

	clusters = []
	for i in range(M):
		clusters.append([])

	assign_cluster(clusters,dist,M,data)
	#print(clusters)

	old_centroids = copy.deepcopy(centroids)
	cal_centroid(clusters,M,centroids)
	#print(centroids)

	if old_centroids==centroids:
		break

print(clusters)
display_clusters(clusters)