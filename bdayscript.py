from datetime import date
import sqlite3

print('\n\n------------------WELCOME TO MY BIRTHDAY KEEPER DEVELOPED BY JATIN ARORA------------------\n\n')

todayy = date.today().strftime("%B %d %Y")
#Format = May 15 2020
print("\n\n    Today's date:", todayy,'\n')

getlistofdate=todayy.split()

date=int(getlistofdate[1])
month=getlistofdate[0]
conn=sqlite3.connect('bdaydb.sqlite', uri=True)
cur=conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Birthday (
	"Id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"Name"	TEXT NOT NULL,
	"Day"	INTEGER NOT NULL,
	"Month"	INTEGER NOT NULL
)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Month (
	"Id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"Month"	TEXT NOT NULL UNIQUE
)''')
print('------------------UPCOMING BIRTHDAYS------------------\n')
months={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
if(date>21):
    key=months.get(month,None)
    key=key+1
    for myvalue,mykey in months.items():
        if (mykey==key):
            newmonth=myvalue
            break
    cur.execute('''SELECT Birthday.Day,Month.Month,Birthday.Name FROM Birthday JOIN Month ON Birthday.Day>?
    AND Birthday.Month=Month.Id AND Month.Month=? And Month.Month=? order by Birthday.Day LIMIT 20''',(date,month,newmonth))
else:
    cur.execute('''SELECT Birthday.Day,Month.Month,Birthday.Name FROM Birthday JOIN Month ON Birthday.Day>?
    AND Birthday.Month=Month.Id AND Month.Month=? order by Birthday.Day''',(date,month))

count=0
try:
    data=cur.fetchall()
    if(len(data)<1):
        print("\n--------------NO BIRTHDAYS IN THIS MONTH--------------\n")
    else:
        for day,month,name in data:
            if(len(str(day))==1):
                print("    ",day,month,name)
            else:
                print("   ",day,month,name)
            count=count+1

        print('\n    - - - - - - - - - - - - - - - - - -\n    Total Count:',count)
        print('\n------------------------------------------------------\n')
except:
    print("\n------------------NO BIRTHDAYS IN THIS MONTH------------------\n")

loop=True
gotoloop=0
def is_string_with_space(check_input):
    '''
    function checking if your string is all letters, but including space(s)
    return : bool
    '''
    flag=0
    checkforstrnospace=check_input
    valid = False
    if ' ' in check_input:
        for char in check_input:
            if char.isdigit():
                valid = False
                flag=1
            elif char.isalpha() or char.isspace():
                valid = True
                if(char.isspace()):
                    flag=1
    if(flag==0):
        def is_string_only(check_input):
            '''function checking if your string is all letters
            return : bool'''
            if check_input.isalpha():
                valid=True
            else:
                valid=False
        valid=is_string_only(checkforstrnospace)
    return valid
def is_digit(check_input):
    '''
    function checking if your string is a pure digit, int
    return : bool
    '''
    if check_input.isdigit():
        return True
    return False
def dayinput():
    gotoloop=0
    try:
        theday=input('\n    Enter the Day of Month as 1 2 3 4 5 6 ...\n\nEnter Choice: ')
        value=is_digit(theday)
        if(value is False):
            print('\n------------------ERROR------------------\n-----Please Enter the Numeric Value-----\n')
            gotoloop=404
    except:
        print('\n------------------ERROR------------------\nPlease Enter the Numeric Value\n')
        gotoloop=404
    if(gotoloop==404):
        return gotoloop
    else:
        return theday
def monthinput():
    gotoloop=0
    try:
        print('''
    Enter the Number against your Choice
    1 - January
    2 - February
    3 - March
    4 - April
    5 - May
    6 - June
    7 - July
    8 - August
    9 - September
   10 - Oct
   11 - Nov
   12 - Dec''')
        themonth=input('\nEnter Choice: ')
        value=is_digit(themonth)
        if(value is False):
            print('\n------------------ERROR------------------\n-----Please Enter the Numeric Value-----\n')
            gotoloop=404
    except:
        print('\n------------------ERROR------------------\nPlease Enter the Numeric Value\n')
        gotoloop=404
    if(gotoloop==404):
        return gotoloop
    else:
        return themonth
def checkdaymonnull(theday,themonth):
    gotoloop=0
    if theday is None or themonth is None:
        print('\n------------------ERROR------------------\nPLEASE DO NOT ENTER NULL VALUE\n')
        gotoloop=404
    if(gotoloop==404):
        return gotoloop
    else:
        return 1
def dictofmonths(themonth):
    charmonth=0
    months={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
    for k,v in (months.items()):
        if(v==int(themonth)):
            charmonth=k
            break
    return charmonth
def checkcondofdays(themonth,theday):
    gotoloop=0
    if ((themonth==1 or themonth==3 or themonth==5 or themonth==7 or themonth==8 or themonth==10 or themonth==12) and (theday>31 or theday<1)):
        print("\n------------------ERROR------------------\nINVALID DATE PLEASE RECHECK")
        gotoloop=404
    if (themonth==2 and (theday>29 or theday<1)):
        print("\n------------------ERROR------------------\nINVALID DATE PLEASE RECHECK")
        gotoloop=404
    if ((themonth==4 or themonth==6 or themonth==9 or themonth==11) and (theday>30 or theday<1)):
        print("\n------------------ERROR------------------\nINVALID DATE PLEASE RECHECK")
        gotoloop=404
    if(gotoloop==404):
        return gotoloop
    else:
        return 1

while(True):
    print('''
    Select the Number against your Choice

    1 - ADD BIRTHDAY
    2 - RETRIEVE BIRTHDAY BY DD-MM
    3 - DELETE BIRTHDAY
    4 - SHOW ALL BIRTHDAYS
    5 - SHOW BIRTHDAYS FOR A PARTICULAR MONTH
    6 - SHOW BIRTHDAY FOR A PARTICULAR NAME
    7 - SHOW BIRTHDAY FOR A PARTICULAR DATE (DD)
    8 - QUIT''')

    choice = input('\nEnter Choice: ')
    value=is_digit(choice)
    if(value is False):
        print('\n------------------ERROR------------------\n-----Please Enter the Numeric Value-----\n')
        continue

    while(choice=="1"):
        theday=dayinput()
        if(theday==404):
            continue
        while(True):
            themonth=monthinput()
            if(themonth==404):
                continue
            else:
                break
        checknullvalue=checkdaymonnull(theday,themonth)
        if(checknullvalue==404):
            continue
        charmonth=dictofmonths(themonth)
        print("\nYou entered:",theday, charmonth,'\n')
        condition=checkcondofdays(themonth,theday)
        if(condition==404):
            continue

        while(True):
            thename=input("Please Enter the Name: ")

            # if(thename is None):
            #     print('\n------------------ERROR------------------\nPLEASE DO NOT ENTER NULL VALUES\n')
            #     continue
            # if(type(thename)!=str):
            #     print('\n------------------ERROR------------------\nINVALID NAME\n')
            #     continue
            # break
            # cur.execute('SELECT * FROM BIRTHDAY WHERE Name = (?)',(thename,))
            # try:
            #     checkduplicatename=cur.fetchone()[1]
            #     print("Please Enter a Modified Name because the another person with same name already Exits.")
            #     continue
            # except:
            #     break

            value=is_string_with_space(thename)
            valuefordigit=is_digit(thename)
            if(valuefordigit is True):
                print('\n------------------ERROR------------------\n-----Please Do not Enter the Numeric Value-----\n')
                continue
            if(value is False):
                print(value)
                print('\n------------------ERROR------------------\nINVALID NAME\n')
                continue
            elif(thename.isspace() is True):
                print('\n------------------ERROR------------------\nPLEASE DO NOT ENTER NULL VALUES\n')
                continue
            elif(thename==""):
                print('\n------------------ERROR------------------\nPLEASE DO NOT ENTER NULL VALUES\n')
                continue
            break

        cur.execute('''INSERT OR IGNORE INTO Month(Month) VALUES (?)''',(charmonth,))
        cur.execute('SELECT Id from Month where Month = ?',(charmonth,))
        themonthid=cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO BIRTHDAY (Name, Day, Month) VALUES (?, ?, ?)''',(thename, theday, themonthid))
        print("\n------------------BIRTHDAY ADDED SUCCESSFULLY------------------\n\n")
        conn.commit()
        choice=0

    while(choice=="2"):
        theday=dayinput()
        if(theday==404):
            continue
        while(True):
            themonth=monthinput()
            if(themonth==404):
                continue
            else:
                break
        checknullvalue=checkdaymonnull(theday,themonth)
        if(checknullvalue==404):
            continue
        charmonth=dictofmonths(themonth)
        print("\n    You entered:",theday, charmonth,'\n')
        condition=checkcondofdays(themonth,theday)
        if(condition==404):
            continue

        cur.execute('''SELECT Birthday.Day,Month.Month,Birthday.Name from Birthday JOIN Month
         on Birthday.Month=Month.Id where Birthday.Day=? and Month.Month=? ORDER BY Birthday.Month,Birthday.Day''',(theday,charmonth))
        count=0
        try:
            data=cur.fetchall()
            if(len(data)<1):
                print("\n--------------NO BIRTHDAYS ON THIS DATE---------------\n")
            else:
                print('    Birthdays on',theday,charmonth,'are')
                print('    --------------------------------\n')
                for day,month,name in data:
                    print("   ",day,''+month,name,'\n')
                    count=count+1

                print('\n   - - - - - - - - - - - - - - - - - -\n   Total Count:',count)
                print('\n-------------------------------ALL BIRTHDAYS FETCHED SUCCESSFULLY-------------------------------\n\n')
        except:
            print("\n------------------NO BIRTHDAYS ON THIS DATE-------------------\n")
        choice=0

    while(choice=="3"):
        theday=dayinput()
        if(theday==404):
            continue
        while(True):
            themonth=monthinput()
            if(themonth==404):
                continue
            else:
                break
        checknullvalue=checkdaymonnull(theday,themonth)
        if(checknullvalue==404):
            continue
        charmonth=dictofmonths(themonth)
        print("\nYou entered:",theday, charmonth,'\n')
        condition=checkcondofdays(themonth,theday)
        if(condition==404):
            continue

        while(True):
            thename=input("Please Enter the Name: ")
            value=is_string_with_space(thename)
            valuefordigit=is_digit(thename)
            if(valuefordigit is True):
                print('\n------------------ERROR------------------\n--Please Do not Enter the Numeric Value--\n')
                continue
            if(value is False):
                print(value)
                print('\n------------------ERROR------------------\nINVALID NAME\n')
                continue
            elif(thename.isspace() is True):
                print('\n------------------ERROR------------------\nPLEASE DO NOT ENTER NULL VALUES\n')
                continue
            elif(thename==""):
                print('\n------------------ERROR------------------\nPLEASE DO NOT ENTER NULL VALUES\n')
                continue
            break

        while(True):
            print('ARE YOU SURE YOU WANT TO DELETE THE BIRTHDAY OF',thename,theday,themonth,'\nType "1" to DELETE or "0" to EXIT\n')
            inp=input()
            if(inp=="1"):
                try:
                    cur.execute('''SELECT Birthday.Id FROM Birthday JOIN Month where Birthday.Day=? and
                    Month.Month=? and Birthday.name=? ''',(theday,charmonth,thename))
                    data=cur.fetchone()[0]
                except:
                    print("Birthday Doesn't Exists. Try Again")
                    choice=0
                    break
                cur.execute('''DELETE FROM BIRTHDAY WHERE Id=?''',(data,))
                print("-------------------------------Birthday DELETED SUCCESSFULLY-------------------------------\n\n")
                conn.commit()
                choice=0
                break
            elif(inp=="0"):
                choice=0
                break
            else:
                print('\n------------------ERROR------------------\n-----------CHOOSE CORRECT VALUE-----------')
                continue

    if(choice=="4"):
        cur.execute('''SELECT Birthday.Day,Month.Month,Birthday.Name
        FROM Birthday JOIN Month ON Birthday.Month=Month.Id order by Birthday.Month,Birthday.Day''')
        data=cur.fetchall()

        h,prevm,k=data[0]
        print("\n   Birthdays for the Month of",prevm,'')
        print("   ---------------------------------")
        count=0
        for d,currm,n in data:
            if(prevm!=currm):
                prevm=currm
                print("\n   Birthdays for the Month of",prevm)
                print("   ---------------------------------")
            if(len(str(d))==1):
                print("   ",d,currm,n)
            else:
                print("  ",d,currm,n)
            count=count+1

        print('\n   - - - - - - - - - - - - - - - - - -\n   Total Count:',count)
        print('\n\n-------------------------------ALL BIRTHDAYS FETCHED SUCCESSFULLY-------------------------------\n\n')

    while(choice=="5"):

        while(True):
            themonth=monthinput()
            if(themonth==404):
                continue
            else:
                break

        if themonth is None:
            print('\n------------------ERROR------------------\nPLEASE DO NOT ENTER NULL VALUE\n')
            continue

        charmonth=dictofmonths(themonth)
        print("\n    You entered:",charmonth,'\n')

        cur.execute('''SELECT Birthday.Day,Month.Month,Birthday.Name from Birthday JOIN Month
         on Birthday.Month=Month.Id and Month.Month=? ORDER BY Birthday.Day''',(charmonth,))
        count=0
        try:
            data=cur.fetchall()
            if(len(data)<1):
                print("\n--------------NO BIRTHDAYS IN THIS MONTH--------------\n")
            else:
                print('    Birthdays in',charmonth,'are')
                print('    ------------------------------\n')
                for day,month,name in data:
                    if(len(str(day))==1):
                        print("    ",day,month,name)
                    else:
                        print("   ",day,month,name)
                    count=count+1

            print('\n    - - - - - - - - - - - - - - - - - -\n    Total Count:',count)
            print('\n\n-------------------------------ALL BIRTHDAYS FETCHED SUCCESSFULLY-------------------------------\n\n')
        except:
            print("\n------------------NO BIRTHDAYS IN THIS MONTH------------------\n")
        choice=0

    while(choice=="6"):
        while(True):
            thename=input("\nPlease Enter the Name: ")
            value=is_string_with_space(thename)
            valuefordigit=is_digit(thename)
            if(valuefordigit is True):
                print('\n------------------ERROR------------------\n-----Please Do not Enter the Numeric Value-----\n')
                continue
            if(value is False):
                print(value)
                print('\n------------------ERROR------------------\nINVALID NAME\n')
                continue
            elif(thename.isspace() is True):
                print('\n------------------ERROR------------------\nPLEASE DO NOT ENTER NULL VALUES\n')
                continue
            elif(thename==""):
                print('\n------------------ERROR------------------\nPLEASE DO NOT ENTER NULL VALUES\n')
                continue
            break
        cur.execute('''SELECT Birthday.Day, Month.Month, Birthday.Name from Birthday JOIN Month
         on Birthday.Month=Month.Id where Birthday.Name=? ORDER BY Birthday.Month, Birthday.Day ''',(thename,))
        count=0
        try:
            data=cur.fetchall()
            if(len(data)<1):
                print("\n--------------NO BIRTHDAYS IN THIS MONTH--------------\n")
            else:
                print('\n    Birthdays matched with',thename,'are')
                print('    ------------------------------------\n')
                for day,month,name in data:
                    if(len(str(day))==1):
                        print("    ",day,month,name)
                    else:
                        print("   ",day,month,name)
                    count=count+1

            print('\n    - - - - - - - - - - - - - - - - - -\n    Total Count:',count)
            print('\n\n-------------------------------ALL BIRTHDAYS FETCHED SUCCESSFULLY-------------------------------\n\n')
        except:
            print("\n------------------NO BIRTHDAYS IN THIS MONTH------------------\n")
        choice=0

    while(choice=="7"):
        theday=dayinput()
        if(theday==404):
            continue
        if theday is None:
            continue
        print("\n    You entered:",theday,'\n')
        if(int(theday)>31 or int(theday)<1):
            print('\n-------------------ERROR-------------------\n----------------INVALID DAY----------------')
            continue

        cur.execute('''SELECT Birthday.Day, Month.Month,Birthday.Name from Birthday JOIN Month
        on Birthday.Month=Month.Id where Birthday.Day=? ORDER BY Birthday.Month''',(theday,))
        count=0
        try:
            data=cur.fetchall()
            if(len(data)<1):
                print("\n--------------NO BIRTHDAYS ON THIS DAY--------------\n")
            else:
                print('    Birthdays on',theday,'are')
                print('    -------------------------------')
                for day,month,name in data:
                    if(len(str(day))==1):
                        print("    ",day,month,name)
                    else:
                        print("   ",day,month,name)
                    count=count+1

                print('\n    - - - - - - - - - - - - - - - - - -\n    Total Count:',count)
                print('\n\n-------------------------------ALL BIRTHDAYS FETCHED SUCCESSFULLY-------------------------------\n\n')
        except:
            print("\n------------------NO BIRTHDAYS ON THIS DAY------------------\n")
        choice=0

    if(choice=="8"):
        print('\n\n-------------------------------THANKYOU FOR USING MY BIRTHDAY KEEPER-------------------------------\n\n')
        break
