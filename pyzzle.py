import pylab
import array
import sys

# read dict
wlist = []
with open('wlist', 'r') as f:
	words = f.readlines()

	for aword in words:
		wlist.append(aword.rstrip().lower())
f.closed
#print wlist

# create check matrix
gridchk = [[0 for x in range(4)] for x in range(4)] 
#print gridchk


def drawm(matrix):
	for i, row in enumerate(matrix):
		print ' '.join(row)

# letter grid
grid = []
solution = []

grid.append(['A', 'M', 'S', 'T'])
grid.append(['K', 'L', 'F', 'O'])
grid.append(['P', 'A', 'D', 'F'])
grid.append(['R', 'X', 'E', 'W'])

drawm(grid)

'''
subm = []
ptr = {'row': 3, 'column':0}
#print grid[0][0]
#sys.exit()
if(ptr['row']-2<0):
	row_start=0
else:
	row_start = ptr['row']-1
if(ptr['row']+2>4):
	row_end=4
else:
	row_end = ptr['row']+2

if(ptr['column']-2<0):
 	col_start=0
else:
	col_start=ptr['column']-1

if(ptr['column']+2>4):
	col_end=4
else:
	col_end=ptr['column']+2

print "\nrow_start: %s" % row_start
print "row_end: %s" % row_end
print "col_start: %s" % col_start
print "col_end: %s" % col_end

for row in range(row_start,row_end):
	rowm = []
	for column in range(col_start,col_end):
		#print grid[row][column]
		rowm.append(grid[row][column])		
	subm.append(rowm)

print '\n\nSubm'
drawm(subm)
sys.exit()
'''

def append_next(ptr):

	# generate subm
	
	# loop subm
	append_next(ptr)

	

def getnext(ptr):
	print 'Trying to get next pointer'
	#print ptr['row']
	#sys.exit()

	for row in range(0,4):
		for column in range(0,4):
			if (row==ptr['row']) and (column==ptr['column']):
				print 'Naa, pointer match'
				continue
			elif (gridchk[row][column]==1):
				print 'Tile used in this iteration'
				continue
			else:
				gridchk[row][column]=1
				
				print 'Got Next'
				print {'row': row, 'column':column}
		
				return {'row': row, 'column':column}

	'''
	for row in range(0,4):
		for column in range(0,4):
			if (row==ptr['row']) and (column==ptr['column']):
				print 'Naa, pointer match'
				continue
			elif (gridchk[row][column]==1):
				print 'Tile used in this iteration'
				continue
			else:
				gridchk[row][column]=1
				
				print 'Got Next'
				print {'row': row, 'column':column}
		
				return {'row': row, 'column':column}
	'''	
	return False



def gettile(ptr):
	print 'Fetching tile'
	#print ptr['row']
	
	return grid[ptr['row']][ptr['column']]

def valid_word(needle, haystack):
	return 	needle in haystack



rowval = ''
for row in range(0,4):
	for column in range(0,4):
		# reset gridchk
		gridchk = [[0 for x in range(4)] for x in range(4)] 

		# start processing
		rowval = rowval + ' ' + grid[row][column]

		# build word
		cw = ''
		ptr = []
		ptr = {'row':row, 'column':column}
		print 'Root ptr'
		print ptr

		has_more = True
		while has_more:
			ptr = getnext(ptr)
			if ptr:
				w = gettile(ptr).lower()
				print 'Next tile %s' % w
			
				cw = cw + w
				print "cw: " + cw
				if valid_word(cw, wlist):
					print 'Got a new word: ' + cw
					solution.append(cw)	
			else:
				has_more = False
			
		
		
		print solution	
		print "Word Count: %s" % len(solution)
		sys.exit();

	#print rowval
	rowval = ''	


print solution
print "Word Count: %s" % len(solution)
