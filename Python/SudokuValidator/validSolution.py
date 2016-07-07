def validSolution(sudoku):
	row=[]
	column=[]
	box=[]
	for i in range(9):
		row.append([])
		column.append([])
		box.append([])
	for r in sudoku:
		i= sudoku.index(r)
		for c in r:
			j= r.index(c)
			if c in row[i] or c in column[j] or c in box[(i/3)*3+j/3]:
				return False
			else:
				row[i].append(c)
				column[j].append(c)
				box[(i/3)*3+j/3].append(c)
	return True