import csv, codecs, cStringIO
import glob, math, random

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



def undersample(Nlist,Nsize,newNsize):

	if newNsize<Nsize:
		return random.sample(Nlist,newNsize)
	else:
		return Nlist


def oversample(Plist,Psize,newPsize):

	Plist.extend(random.sample(Plist,newPsize-Psize))
	return Plist
	
		
	

with open("../Data/Default_Data_1.csv",'rb') as fin, open("../Data/Default_Data_2.csv",'wb') as fout:
    	reader = UnicodeReader(fin)
    	writer = UnicodeWriter(fout,quoting=csv.QUOTE_ALL)
    	first_row=True

	Plist=[]
	Nlist=[]

    	for line in reader:

		if first_row:

			temp=['ATM_Usage', 'ATM_Money', 'Day' , 'Month' , 'Season' , 'Day_Of_Week' , 'Is_Holiday' , 'Date_Importance' , 'HSupervisor', 'No_Service']
					
			writer.writerow(temp)
			first_row=False

		else:
			tmp=line[9]
			instance=[line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],tmp]
			
			
			if tmp == "P":
				Plist.append(instance)
			else:
				Nlist.append(instance)
	
	Psize=len(Plist)
	Nsize=len(Nlist)
	newPsize=int((Psize + Nsize)/2)
	newNsize=newPsize
	
	newPlist=[]
	newNlist=[]

	newNlist=undersample(Nlist,Nsize,newNsize)
	newPlist=oversample(Plist,Psize,newPsize)

	for element in newNlist:

		writer.writerow(element)

	for element in newPlist:

		writer.writerow(element)


