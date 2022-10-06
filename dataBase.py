import json
from os.path import exists
while  True:

	file_exists = exists("data_file.json")
	if file_exists:
		with open("data_file.json", "r") as read_content:
 			database=json.load(read_content)
	else:
		database = dict()
		
 	print("1. Create Table")
	print("2. View Tables")
	option=int(input("Enter Option="))
	
	if option == 0:
		break
	elif option==1:
		new_table=dict()
		table_name=str(input("Enter table name="))
		fields_count=int(input("Enter no. of fields="))
		fields=list()
		for f_nm in range(fields_count):
			fields.append(str(input("Enter "+str(f_nm+1)+"th Field name=")))
		new_table["table_name"]=table_name
		new_table["fields_count"]=fields_count
		new_table["fields"]=fields
		database[table_name]=new_table
		with open( "data_file.json" , "w" ) as write:
			json.dump( database , write )
		print("Table Saved!")
		# with open("data_file.json", "r") as read_content:
  #   		print(json.load(read_content))
		print("=====================================================================")
		continue
	elif option==2:
		with open("data_file.json", "r") as read_content:
 			tables=json.load(read_content)
 			for table in tables:
 				print(table)
 				print("=====================")
 				table_meta=tables[table]
 				for meta in table_meta:
 					print(meta," : ",table_meta[meta])

 			
		
		continue
