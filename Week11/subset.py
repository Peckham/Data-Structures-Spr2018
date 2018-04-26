from probe_hash_map import ProbeHashMap

def is_subset(l1, l2):
	''' checks if every element in l2 exists in l1.
	@l1: the large python list
	@l2: the subset python list

	return: True if l2 is subset of l1
	'''
	# To do
	pass

def main():
	l1 = [1,2,3,4,5,6,7,8,9,0]
	l2 = [5,2,8,9,0,2,1,2]
	l3 = [5,2,8,9,0,2,1,2,"haha"]
	print("l2 should be subset of l1........")
	print("Your result:", is_subset(l1, l2))
	print("l3 should not be subset of l1........")
	print("Your result:", is_subset(l1, l3))
main()


