import sqlite3


# Function for Convert Binary Data
# to Human Readable Format
def convertToBinaryData(filename):
	
	# Convert binary format to images
	# or files data
	with open(filename, 'rb') as file:
		blobData = file.read()
	return blobData


def insertBLOB(id,name, photo,price,des):
	try:
		
		# Using connect method for establishing
		# a connection
		sqliteConnection = sqlite3.connect('JewelManagement.db')
		cursor = sqliteConnection.cursor()
		print("Connected to SQLite")
		
		# insert query
		sqlite_insert_blob_query ="""INSERT INTO products (pid,pname,img,pprice,pdes) VALUES (?,?,?,?,?)"""
		
		# Converting human readable file into
		# binary data
		empPhoto = convertToBinaryData(photo)
		
		# Convert data into tuple format
		data_tuple = (id,name, photo,price,des)
		
		# using cursor object executing our query
		cursor.execute(sqlite_insert_blob_query,data_tuple)
		sqliteConnection.commit()
		print("Image and file inserted successfully as a BLOB into a table")
		cursor.close()

	except sqlite3.Error as error:
		print("Failed to insert blob data into sqlite table", error)
	
	finally:
		if sqliteConnection:
			sqliteConnection.close()
			print("the sqlite connection is closed")

insertBLOB(1,"Khanishq Earring","C:\pyjewelmang\static\css\p1.jpg",18000,"Its a latest design from Khanishiq collection")
insertBLOB(2,"Silver chain","C:\pyjewelmang\static\css\p2.jpg",10000,"Its a latest design from Aasha collection")
insertBLOB(3,"Gold ring","C:\pyjewelmang\static\css\p3.jpg",8000,"Its a latest design from Maiore collection")
insertBLOB(4,"Khanishq Earring","C:\pyjewelmang\static\css\p4.jpg",28000,"Its a latest design from Khanishiq collection")
insertBLOB(5,"Bracelet","C:\pyjewelmang\static\css\p5.jpg",13000,"Its a latest design from Aafaa collection")
insertBLOB(6,"Bangles","C:\pyjewelmang\static\css\p6.jpg",15000,"Its a latest design from Maiore collection")
