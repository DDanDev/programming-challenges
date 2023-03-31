rows, cols, pos = [int(x) for x in input().split()]

while [rows,cols,pos] != [0,0,0]:
	pos -= 1
	brokeat = False
	for rowi in range(rows):
		row = [int(x) for x in input().split()]
		if row[pos] != 0:
			print(f"BOOM {rowi+1} {pos+1}")
			brokeat = rowi
			break
		else:
			for searchi in range(pos-1,-1,-1):
				if row[searchi] != 0:
					leftfani = searchi
					break
			for searchi in range(pos+1,cols):
				if row[searchi] != 0:
					rightfani = searchi
					break
			pos += row[leftfani]-row[rightfani]
			if pos <= leftfani:
				print(f"BOOM {rowi+1} {leftfani+1}")
				brokeat = rowi
				break
			elif pos >= rightfani:
				print(f"BOOM {rowi+1} {rightfani+1}")
				brokeat = rowi
				break
	else: 
		if not brokeat: print(f"OUT {pos+1}")
		else:
			for _ in range(brokeat+1, rows):
				input()

	rows, cols, pos = [int(x) for x in input().split()]