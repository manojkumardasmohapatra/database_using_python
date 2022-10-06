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
	print("3. Insert Record")
	print("4. Delete Table")
	
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
		new_table["data"]=list()
		database[table_name]=new_table
		with open( "data_file.json" , "w" ) as write:
			json.dump( database , write )
		print("Table Saved!")
		print("=====================================================================")
		continue
	elif option==2:
		with open("data_file.json", "r") as read_content:
 			database=json.load(read_content)
 			for table in database:
 				print(table)
 				print("=====================")
 				table_meta=database[table]
 				for meta in table_meta:
 					print(meta," : ",table_meta[meta])

 			
		
		continue
	elif option==3:
		with open("data_file.json", "r") as read_content:
 			database=json.load(read_content)
 			print("Select Table")
 			print("============")
 			i=0
 			assoc=dict()
 			for table in database:
 				assoc[i]=table
 				print(i,". ",table)
 				i+=1
 				# table_meta=database[table]
 				# for meta in table_meta:
 				# 	print(meta," : ",table_meta[meta])
 			selected_table_no=int(input("Enter Option="))
 			selected_table=database[assoc[selected_table_no]]
 			table_data=dict()
 			for field in selected_table["fields"]:
 				table_data[field]=str(input("Enter "+field+"="))

 			

 			(selected_table["data"]).append(table_data)
 			database[assoc[selected_table_no]]=selected_table
 			with open( "data_file.json" , "w" ) as write:
 				json.dump( database , write )
			#print("Table Saved!")

		continue
	elif option==4:
		with open("data_file.json", "r") as read_content:
 			database=json.load(read_content)
 			print("Select Table")
 			print("============")
 			i=0
 			assoc=dict()
 			for table in database:
 				assoc[i]=table
 				print(i,". ",table)
 				i+=1
 				# table_meta=database[table]
 				# for meta in table_meta:
 				# 	print(meta," : ",table_meta[meta])
 			selected_table_no=int(input("Enter Option="))
 			del database[assoc[selected_table_no]]
 			print("Table Deleted!")
 			with open( "data_file.json" , "w" ) as write:
 				json.dump( database , write )

		continue	