import mysql.connector
from mysql.connector import errorcode
import csv, codecs, cStringIO
import glob

class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8

    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")

class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.

    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self

class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.

    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

"""
Credentials for database connection

"""

config = {

  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'bsc_thesis',
  'raise_on_warnings': True,

}

try:
  cnx = mysql.connector.connect(**config)

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your username or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

cursor = cnx.cursor()



"""

Converting Default_Data_0.csv to Default_Data_1.csv by reading the file, computing sum, connecting to database and retrieving info about each date and finally deciding about the label.

"""	

with open("../file/Default_Data_0.csv",'rb') as fin, open("../file/Default_Data_1.csv",'wb') as fout:

	reader = UnicodeReader(fin)
	writer = UnicodeWriter(fout,quoting=csv.QUOTE_ALL)
	first_row=True
	Boundary=1.667
	for line in reader:
		    if first_row:
			    temp=['ATM_Usage', 'ATM_Money', 'Day' , 'Month' , 'Season' , 'Day_Of_Week' , 'Is_Holiday' ,'Date_Importance' , 'HSupervisor' , 'No_Service']
			    writer.writerow(temp)
			    first_row=False
		    else:	
			    Date=line[0].replace("/","-")			
			    ATM_ID=line[1]
			    Total_Of_Transactions=line[2]
			    Total_Of_Services=long(line[3])
			    Total_Of_Bills=long(line[4])
			    Total_Of_Transfers=long(line[5])
			    Total_Of_Dispenses=long(line[6])
			    HSupervisor=line[7]
			    No_Service=float(line[8])
			    ATM_Usage=Total_Of_Transactions
			    ATM_Money=str(Total_Of_Services + Total_Of_Bills + Total_Of_Transfers + Total_Of_Dispenses)
			
			    query = ("SELECT * FROM dates WHERE dt = '%s' ") % (Date)	
			    cursor.execute(query)
				
			    for row in cursor:		
				    Day=str(row[1])
				    Month=str(row[2])
				    Season=str(row[3])
				    Day_Of_Week=str(row[4])
				    Is_Holiday=str(row[5])
				    Date_Importance=str(row[6])

				    if No_Service>Boundary:
					    if ATM_Usage>0 and ATM_Money>0:
						    temp=[ATM_Usage , ATM_Money, Day , Month , Season , Day_Of_Week , Is_Holiday , Date_Importance , HSupervisor ,'P']	
						
				    else:
					    if ATM_Usage>0 and ATM_Money>0:
						    temp=[ATM_Usage , ATM_Money, Day , Month , Season , Day_Of_Week , Is_Holiday , Date_Importance , HSupervisor ,'N']	
							

				    writer.writerow(temp)

cursor.close()
cnx.close()
