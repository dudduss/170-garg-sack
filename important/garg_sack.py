import pprint

N = 5
M = 5
P = 5
items = ['dfdsf', 'sdfsdf']

(name, class_, weight, cost, resale_value)

def knapsack(items, N, M, P):

	resale_matrix = [[[0 for k in range(M)] for j in range(P)] for i in range(N)]
	items_matrix = [[[[] for k in range(M)] for j in range(P)] for i in range(N)]

	for i in range(1,N+1,1):
	    name,item_class, weight, cost, resale_value = items[i-1]
	    for p in range(1,P+1,1):
	   		for m in range(1, M+1,1):
		        if weight <= p and cost <= m:
		        	#Make the constraint check here 
		        	if ((resale_value + resale_matrix[i-1][p-weight][m-cost]) > resale_matrix[i-1][p][m]):
		            	resale_matrix[i][p][m] = resale_value + resale_matrix[i-1][p-weight][m-cost]
		            	items_matrix[i][p][m] = items_matrix[i-1][p][m].append(item)
		        	else:
		        		resale_matrix[i][p][m] = resale_matrix[i-1][p][m]
						items_matrix[i][p][m] = items_matrix[i-1][p][m]
		        else:
		            resale_matrix[i][p][m] = resale_matrix[i-1][p][m]
		            items_matrix[i][p][m] = items_matrix[i-1][p][m]

	return (resale_matrix[N-1][P-1][M-1], items_matrix[N-1][P-1][M-1])


