fname = "romeo.txt"
fh = open(fname)
st = set()
for line in fh:
	st = st.union(set(line.rstrip().split()))
lst = list(st)
lst.sort()
print lst
