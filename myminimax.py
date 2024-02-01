import timeit, math
import random

def minimaax(scores, minormax):  #basic idea
	while(len(scores)!=1):
		i=0
		while(i<len(scores)-1):
			if(minormax):
				scores[i]=max(scores[i], scores[i+1])
			else:
				scores[i]=min(scores[i], scores[i+1])
			del scores[i+1]
			i+=1
		minormax^=1
	return scores[0]

def minimax(scores, minormax):  #optimized version
	rng = math.log2(len(scores))
	i=0
	while(i<rng):
		for j in range(0, (len(scores))-(2**i), 2**(i+1)):
			if(minormax):
				scores[j]=max(scores[j], scores[j+2**i])
			else:
				scores[j]=min(scores[j], scores[j+2**i])
		i+=1
		minormax^=1
	return scores[0]


test_arr = [46, 36, 32, 57, 68, 68, 71, 87, 65, 11, 34, 44, 1, 1, 26, 11, 15, 54, 57, 70, 39, 58, 75, 25, 10, 23, 25, 94, 9, 57, 8, 64, 5, 31, 63, 67, 38, 51, 100, 83, 91, 39, 39, 48, 52, 46, 60, 70, 37, 15, 10, 10, 11, 78, 3, 52, 19, 24, 95, 16, 42, 27, 78, 20, 23, 14, 26, 89, 18, 49, 66, 43, 43, 11, 46, 87, 5, 56, 63, 68, 58, 81, 25, 74, 19, 83, 4, 50, 50, 66, 83, 96, 76, 24, 83, 4, 84, 88, 50, 61]


start = timeit.timeit()
result = minimax(test_arr, 1)
end = timeit.timeit()
print(end-start)
print("\n", result)