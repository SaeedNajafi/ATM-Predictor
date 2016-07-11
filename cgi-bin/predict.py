#!/usr/bin/python2.7

import MySQLdb
import cgi
import cgitb 
import sys
import re
import datetime
import jalali
import subprocess
from sys import argv



def GetInput():
	"This funtion gets the input data from the client browser and checks its validity"

	try:
		arguments = cgi.FieldStorage()
		tndt=arguments.getvalue("tndt")
		tcdt=arguments.getvalue("tcdt")
		hour=arguments.getvalue("hour")
		minute=arguments.getvalue("minute")
		
		
		pattern = re.compile("^[0-9]+$")
		check=True

		if not (pattern.match(tndt)):
			check=False
		

		if not (pattern.match(tcdt)):
			check=False
			

		if not (pattern.match(hour)):
			check=False
		

		if not (pattern.match(minute)):
			check=False
			

		if check:

			tndt=int(tndt)
			tcdt=int(tcdt)
			hour=int(hour)
			minute=int(minute)
			
			
			
			if not (tndt>5 and tndt<2000):
				check=False
				

			if not (tcdt>1 and tcdt<3000):
				check=False
				

			if not (hour>=0 and hour<=5):
				check=False
					

			if not (minute>=0 and minute<=59):
				check=False
					

			if check:
				
				return [True, str(tndt), str(tcdt), str(hour), str(minute)];
				
			else:
				return [False,"Wrong input data! Please go to the help section for more information about the expected input."];   

		else:
			return [False,"Wrong input data! Please go to the help section for more information about the expected input."];

	except:
	    	return [False,"Wrong input data! Please go to the help section for more information about the expected input."];



def Output(data):
	"This funtion predicts and sends out the output xml to the client browser"
	
	print("Content-type: text/xml")
	print
	print("<?xml version='1.0' encoding='UTF-8' ?>")
	print("<results>")

	if not data[0]:

		print("\t<error>")
		print("\t\t<message>%s</message>" % data[1])
	    	print("\t</error>")
		print("</results>")



	if data[0]:
		
		tndt=int(data[1])
		tcdt=int(data[2])
		hour=int(data[3])
		minute=int(data[4])
		dates=[]

		now0 = datetime.datetime.now()
		now1=now0+datetime.timedelta(days=1)
		now2=now0+datetime.timedelta(days=2)
		now3=now0+datetime.timedelta(days=3)
		now4=now0+datetime.timedelta(days=4)
		now5=now0+datetime.timedelta(days=5)
		now6=now0+datetime.timedelta(days=6)
		
		year0=now0.year
		month0=now0.month
		day0=now0.day

		year1=now1.year
		month1=now1.month
		day1=now1.day

		year2=now2.year
		month2=now2.month
		day2=now2.day

		year3=now3.year
		month3=now3.month
		day3=now3.day

		year4=now4.year
		month4=now4.month
		day4=now4.day

		year5=now5.year
		month5=now5.month
		day5=now5.day

		year6=now6.year
		month6=now6.month
		day6=now6.day
		
		
		
		date0_year=jalali.Gregorian(str(year0)+"-"+str(month0)+"-"+str(day0)).persian_year
		date1_year=jalali.Gregorian(str(year1)+"-"+str(month1)+"-"+str(day1)).persian_year
		date2_year=jalali.Gregorian(str(year2)+"-"+str(month2)+"-"+str(day2)).persian_year
		date3_year=jalali.Gregorian(str(year3)+"-"+str(month3)+"-"+str(day3)).persian_year
		date4_year=jalali.Gregorian(str(year4)+"-"+str(month4)+"-"+str(day4)).persian_year
		date5_year=jalali.Gregorian(str(year5)+"-"+str(month5)+"-"+str(day5)).persian_year
		date6_year=jalali.Gregorian(str(year6)+"-"+str(month6)+"-"+str(day6)).persian_year

		date0_month=jalali.Gregorian(str(year0)+"-"+str(month0)+"-"+str(day0)).persian_month
		date1_month=jalali.Gregorian(str(year1)+"-"+str(month1)+"-"+str(day1)).persian_month
		date2_month=jalali.Gregorian(str(year2)+"-"+str(month2)+"-"+str(day2)).persian_month
		date3_month=jalali.Gregorian(str(year3)+"-"+str(month3)+"-"+str(day3)).persian_month
		date4_month=jalali.Gregorian(str(year4)+"-"+str(month4)+"-"+str(day4)).persian_month
		date5_month=jalali.Gregorian(str(year5)+"-"+str(month5)+"-"+str(day5)).persian_month
		date6_month=jalali.Gregorian(str(year6)+"-"+str(month6)+"-"+str(day6)).persian_month
		
		date0_day=jalali.Gregorian(str(year0)+"-"+str(month0)+"-"+str(day0)).persian_day
		date1_day=jalali.Gregorian(str(year1)+"-"+str(month1)+"-"+str(day1)).persian_day
		date2_day=jalali.Gregorian(str(year2)+"-"+str(month2)+"-"+str(day2)).persian_day
		date3_day=jalali.Gregorian(str(year3)+"-"+str(month3)+"-"+str(day3)).persian_day
		date4_day=jalali.Gregorian(str(year4)+"-"+str(month4)+"-"+str(day4)).persian_day
		date5_day=jalali.Gregorian(str(year5)+"-"+str(month5)+"-"+str(day5)).persian_day
		date6_day=jalali.Gregorian(str(year6)+"-"+str(month6)+"-"+str(day6)).persian_day

		if date0_day>=1 and date0_day<=9:
			date00_day="0"+str(date0_day)
		else:
			date00_day=str(date0_day)

		if date1_day>=1 and date1_day<=9:
			date11_day="0"+str(date1_day)
		else:
			date11_day=str(date1_day)

		if date2_day>=1 and date2_day<=9:
			date22_day="0"+str(date2_day)

		else:
			date22_day=str(date2_day)

		if date3_day>=1 and date3_day<=9:
			date33_day="0"+str(date3_day)

		else:
			date33_day=str(date3_day)

		if date4_day>=1 and date4_day<=9:
			date44_day="0"+str(date4_day)
		else:
			date44_day=str(date4_day)

		if date5_day>=1 and date5_day<=9:
			date55_day="0"+str(date5_day)
		else:
			date55_day=str(date5_day)

		if date6_day>=1 and date6_day<=9:
			date66_day="0"+str(date6_day)
		else:
			date66_day=str(date6_day)


		if date0_month>=1 and date0_month<=9:
			date00_month="0"+str(date0_month)
		else:
			date00_month=str(date0_month)
		
		
		if date1_month>=1 and date1_month<=9:
			date11_month="0"+str(date1_month)
		else:
			date11_month=str(date1_month)


		if date2_month>=1 and date2_month<=9:
			date22_month="0"+str(date2_month)
		else:
			date22_month=str(date2_month)


		if date3_month>=1 and date3_month<=9:
			date33_month="0"+str(date3_month)
		else:
			date33_month=str(date3_month)


		if date4_month>=1 and date4_month<=9:
			date44_month="0"+str(date4_month)
		else:
			date44_month=str(date4_month)


		if date5_month>=1 and date5_month<=9:
			date55_month="0"+str(date5_month)
		else:
			date55_month=str(date5_month)


		if date6_month>=1 and date6_month<=9:
			date66_month="0"+str(date6_month)
		else:
			date66_month=str(date6_month)
		
	
		date0=str(date0_year)+"-"+date00_month+"-"+date00_day
		date1=str(date1_year)+"-"+date11_month+"-"+date11_day
		date2=str(date2_year)+"-"+date22_month+"-"+date22_day
		date3=str(date3_year)+"-"+date33_month+"-"+date33_day
		date4=str(date4_year)+"-"+date44_month+"-"+date44_day
		date5=str(date5_year)+"-"+date55_month+"-"+date55_day
		date6=str(date6_year)+"-"+date66_month+"-"+date66_day
	
		dates.append(date0);
		dates.append(date1);
		dates.append(date2);
		dates.append(date3);
		dates.append(date4);
		dates.append(date5);
		dates.append(date6);
		

		test=[]
		db = MySQLdb.connect("localhost","root","S_njf1372","bsc_thesis" )
		cursor = db.cursor()

		query = ("SELECT * FROM dates WHERE dt = '%s' ") % (date0)	
		cursor.execute(query)
		results = cursor.fetchall()
		
		for row in results:
			Day=str(row[1])
			Month=str(row[2])
			Season=str(row[3])
			Day_Of_Week=str(row[4])
			Is_Holiday=str(row[5])
			Date_Importance=str(row[6])
			test.append([tndt , long(tcdt*10000000), int(Day) , int(Month) , int(Season) , int(Day_Of_Week) , int(Is_Holiday) , float(Date_Importance) , float(hour+minute/60.00)])
					
		query = ("SELECT * FROM dates WHERE dt = '%s' ") % (date1)	
		cursor.execute(query)
		results = cursor.fetchall()
		for row in results:		
			Day=str(row[1])
			Month=str(row[2])
			Season=str(row[3])
			Day_Of_Week=str(row[4])
			Is_Holiday=str(row[5])
			Date_Importance=str(row[6])
			test.append([tndt , long(tcdt*10000000), int(Day) , int(Month) , int(Season) , int(Day_Of_Week) , int(Is_Holiday) , float(Date_Importance) , float(hour+minute/60.00)])


		query = ("SELECT * FROM dates WHERE dt = '%s' ") % (date2)	
		cursor.execute(query)
		results = cursor.fetchall()		
		for row in results:		
			Day=str(row[1])
			Month=str(row[2])
			Season=str(row[3])
			Day_Of_Week=str(row[4])
			Is_Holiday=str(row[5])
			Date_Importance=str(row[6])
			test.append([tndt , long(tcdt*10000000), int(Day) , int(Month) , int(Season) , int(Day_Of_Week) , int(Is_Holiday) , float(Date_Importance) , float(hour+minute/60.00)])


		query = ("SELECT * FROM dates WHERE dt = '%s' ") % (date3)	
		cursor.execute(query)
		results = cursor.fetchall()		
		for row in results:		
			Day=str(row[1])
			Month=str(row[2])
			Season=str(row[3])
			Day_Of_Week=str(row[4])
			Is_Holiday=str(row[5])
			Date_Importance=str(row[6])
			test.append([tndt , long(tcdt*10000000), int(Day) , int(Month) , int(Season) , int(Day_Of_Week) , int(Is_Holiday) , float(Date_Importance) , float(hour+minute/60.00)])

		query = ("SELECT * FROM dates WHERE dt = '%s' ") % (date4)	
		cursor.execute(query)
		results = cursor.fetchall()		
		for row in results:		
			Day=str(row[1])
			Month=str(row[2])
			Season=str(row[3])
			Day_Of_Week=str(row[4])
			Is_Holiday=str(row[5])
			Date_Importance=str(row[6])
			test.append([tndt , long(tcdt*10000000), int(Day) , int(Month) , int(Season) , int(Day_Of_Week) , int(Is_Holiday) , float(Date_Importance) , float(hour+minute/60.00)])

		query = ("SELECT * FROM dates WHERE dt = '%s' ") % (date5)	
		cursor.execute(query)
		results = cursor.fetchall()		
		for row in results:		
			Day=str(row[1])
			Month=str(row[2])
			Season=str(row[3])
			Day_Of_Week=str(row[4])
			Is_Holiday=str(row[5])
			Date_Importance=str(row[6])
			test.append([tndt , long(tcdt*10000000), int(Day) , int(Month) , int(Season) , int(Day_Of_Week) , int(Is_Holiday) , float(Date_Importance) , float(hour+minute/60.00)])

		query = ("SELECT * FROM dates WHERE dt = '%s' ") % (date6)	
		cursor.execute(query)
		results = cursor.fetchall()		
		for row in results:		
			Day=str(row[1])
			Month=str(row[2])
			Season=str(row[3])
			Day_Of_Week=str(row[4])
			Is_Holiday=str(row[5])
			Date_Importance=str(row[6])
			test.append([tndt , long(tcdt*10000000), int(Day) , int(Month) , int(Season) , int(Day_Of_Week) , int(Is_Holiday) , float(Date_Importance) , float(hour+minute/60.00)])
			
		db.close()
		
		target = open("../file/test.txt", 'w')
	
		for index in test:
			target.write(str(index[0]))
			target.write(",")
			target.write(str(index[1]))
			target.write(",")
			target.write(str(index[2]))
			target.write(",")
			target.write(str(index[3]))
			target.write(",")
			target.write(str(index[4]))
			target.write(",")
			target.write(str(index[5]))
			target.write(",")
			target.write(str(index[6]))
			target.write(",")
			target.write(str(index[7]))
			target.write(",")
			target.write(str(index[8]))
			target.write("\r\n")

		target.close()
			
		command = 'python test.py'
		subprocess.call(command, shell=True)

		target = open("../file/test.txt", 'r')
		lines=target.read().split("\r\n")
	
		i=0
		for index in lines:
			if len(index)!=0:
				print("\t<result>")
				print("\t\t<date>%s</date>" % dates[i])
				print("\t\t<class>%s</class>" % index[0])
				print("\t</result>")
				i=i+1
				
	
		target.close()
		
		print("</results>")

	
check=GetInput()
Output(check)

