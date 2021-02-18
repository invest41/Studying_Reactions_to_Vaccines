#1.0
from zipfile import ZipFile

#2.0
file_name = "2021VAERSDATA.csv.zip"

#3.0
with ZipFile(file_name, 'r') as zip: 
	zip.printdir() 

#3.1
print('Extracting all the files now...') 
zip.extractall()
print('Done!')
