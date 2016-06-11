def hand_rank(hand):

	"""Return a value indicating how high the hand ranks."""
	groups = group(["--23456789TJQKA".index(r) for r,s in hand])
	counts, ranks = unzip(groups)
	if ranks == (14,5,4,3,2):
		ranks = (5,4,3,2,1)
	straight = len(ranks) == 5 and max(ranks)-min(ranks)==4 
	flush = len(set([s for s in hand])) == 1 
	return (9 if (5,) == counts else
		    8 if straight and flush else
		    7 if (4,1) == counts else
		    6 if (3,2) == counts else
		    5 if flush else
		    4 if straight else
		    3 if (3,1,1) == counts else
		    2 if (2,2,1) == counts else
		    1 if (2,1,1,1,1) == counts else
		    0), ranks


def group(items):
	"""return a list of [(count, x)....], hightest count first
	"""
	groups = [(items.count(x),x) for x in set(items)]
	return sorted(groups, reverse=True)

def unzip(groups):
	count = tuple([(i[0]) for i in groups])
	ranks = tuple([i[1] for i in groups])
	return [count, ranks]

def unzip1(pairs):
	return zip(*pairs)


yep= group([7,10,7,9,7])
pairs = group([7,10,7,9,7])
print unzip(yep)
print unzip1(pairs)
