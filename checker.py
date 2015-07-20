import sys

print sys.argv

# read dict
wlist = []
with open('master', 'r') as f:
	words = f.readlines()

	for aword in words:
		wlist.append(aword.rstrip())
f.closed


# compare with master
def valid_word(needle, haystack, testdata):
	return needle in haystack and needle not in testdata


# read input
testdata = []
with open(sys.argv[1], 'r') as f:
	testlist = f.readlines()

	wc = 0
	for aword in testlist:
		if valid_word(aword.rstrip(), wlist, testdata):
			testdata.append(aword.rstrip())
			wc+=1

f.closed

print testdata
print "Word Count: %s" % wc


