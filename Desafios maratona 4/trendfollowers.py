import math
currFollows, goalFollows = [int(x) for x in input().split()]
dailyGrowth = math.ceil(sum([int(x)/30 for x in input().split()]))
print(f"{math.ceil((goalFollows - currFollows)/dailyGrowth)}")