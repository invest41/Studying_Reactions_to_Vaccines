import time

fw, err = open('2021_adverse_vaccine.csv','w'), {}
co = wh= 0
for line in open('2021VAERSDATA.csv','rb'):
	try: 
		line = line.decode()
		for ordc in [ ord(c) for c in line ]:
			if ordc>128:	line = line.replace(chr(ordc),' ')
		fw.write(line)
		wh += 1
	except Exception as e: 
		print(e)
		err[co] = (e,line)
	co += 1
print(f'{wh} lines have been written\n{len(err)} lines are errors')
fw.close()
