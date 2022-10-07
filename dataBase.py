import json
import os
from os.path import exists
DATABASE_FILE="data_file.json"
#function to check if table exists
def checkIfTableExists(table_name):
	file_exists = exists(DATABASE_FILE)
	if file_exists:
		with open(DATABASE_FILE, "r") as read_content:
 			database=json.load(read_content)
 			if table_name in database:
 				return True
 			else:
 				return False
	else:
		return False
#function checkIfTableExists ends	
#function to wait till user enters something then clear screen
def goToMainMenu():
	input("Press any key to go to Main Menu...")
	os.system('cls')
	return True
#function goToMainMenu ends
def printMainMenu():
	os.system('cls')
	print("#############################")
	print("#############################")
	print("#                           #")
	print("#         MAIN MENU         #")
	print("#                           #")
	print("#############################")
	print("#############################")
	print("#1. Create Table            #")
	print("#2. View Tables             #")
	print("#3. Insert Record           #")
	print("#4. Delete Table            #")
	print("#5. Delete Record           #")
	print("#6. Update Record           #")
	print("#0. Exit                    #")
	print("#############################")
	print("#############################")
#function printMainMenu ends
def viewTableContents(table):
	table_meta=table
	for meta in table_meta:
 		if meta=="data":
 			print(meta," : ")
 			record_no=1
 			for d in table_meta[meta]:
 				print(record_no," :\t",d)
 				record_no+=1
 		else:
 			print(meta," : ",table_meta[meta])


while  True:

	file_exists = exists(DATABASE_FILE)
	if file_exists:
		with open(DATABASE_FILE, "r") as read_content:
 			database=json.load(read_content)
	else:
		database = dict()
	printMainMenu()
	option=int(input("Enter Option="))
	
	if option == 0:
		os.system('cls')
		break
	elif option==1:
		new_table=dict()
		table_name=str(input("Enter table name="))
		if checkIfTableExists(table_name):
			print("Table Exists!")
			continue
		fields_count=int(input("Enter no. of fields="))
		fields=list()
		for f_nm in range(fields_count):
			fields.append(str(input("Enter "+str(f_nm+1)+"th Field name=")))
		new_table["table_name"]=table_name
		new_table["fields_count"]=fields_count
		new_table["fields"]=fields
		new_table["data"]=list()
		database[table_name]=new_table
		with open( DATABASE_FILE , "w" ) as write:
			json.dump( database , write )
		print("Table Saved!")
		if goToMainMenu():
			os.system('cls')
			continue
	elif option==2:
		with open(DATABASE_FILE, "r") as read_content:
 			database=json.load(read_content)
 			for table in database:
 				print(table)
 				print("=====================")
 				viewTableContents(database[table])
 				
		if goToMainMenu():
			continue
	elif option==3:
		with open(DATABASE_FILE, "r") as read_content:
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
 			selected_table_no=int(input("Enter Table No.="))
 			selected_table=database[assoc[selected_table_no]]
 			table_data=dict()
 			for field in selected_table["fields"]:
 				table_data[field]=str(input("Enter "+field+"="))

 			

 			(selected_table["data"]).append(table_data)
 			database[assoc[selected_table_no]]=selected_table
 			with open( DATABASE_FILE , "w" ) as write:
 				json.dump( database , write )
			#print("Table Saved!")

		if goToMainMenu():
			continue
	elif option==4:
		with open(DATABASE_FILE, "r") as read_content:
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
 			with open( DATABASE_FILE , "w" ) as write:
 				json.dump( database , write )

		if goToMainMenu():
			continue
	elif option==5:
		with open(DATABASE_FILE, "r") as read_content:
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
 			viewTableContents(database[assoc[selected_table_no]])
 			del_record_no=int(input("Enter Record No you want to delete="))
 			database[assoc[selected_table_no]]["data"].pop(del_record_no-1)
 			print("Record Deleted!")
 			with open( DATABASE_FILE , "w" ) as write:
 				json.dump( database , write )

		if goToMainMenu():
			continue	
	elif option==6:
		with open(DATABASE_FILE, "r") as read_content:
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
 			viewTableContents(database[assoc[selected_table_no]])
 			update_record_no=int(input("Enter Record No you want to update="))
 			print("Enter Updated Values:-")
 			print("=======================")
 			table_data=dict()
 			for field in database[assoc[selected_table_no]]["fields"]:
 				table_data[field]=str(input("Enter "+field+"="))

 			database[assoc[selected_table_no]]["data"][update_record_no-1]=table_data
 			print("Record Updated!")
 			with open( DATABASE_FILE , "w" ) as write:
 				json.dump( database , write )

		if goToMainMenu():
			continue	