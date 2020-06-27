import sqlite3
from DB import connect_DB

def Creat_TableMAJOR(cur):
    strSQL = """
        CREATE TABLE if not exists MAJOR
        (
            IDM text ,
            CLASS text,
            NAME text,
            PRIMARY KEY(IDM,CLASS)
        )"""
    str
    success_flag = True
    try :
        cur.execute(strSQL)
    except:
        success_flag = False
    if success_flag == True :
        print("Creat Ok")
    else:
        print("Creat Fail: ")

def Insert_ISV(cur,con,idm,claSs,name):
    success_flag=True
    # cur.execute("""INSERT OR IGNORE INTO MAJOR
                #  VALUES(?,?,?)""",(idm,claSs,name))
    try:
        cur.execute("""INSERT OR IGNORE INTO MAJOR
                VALUES(?,?,?)""",(idm,claSs,name))
    except:
        success_flag=False
    if success_flag == True:
        con.commit()
        return True
    else:
        return False

def Creat_TableCLASS(cur):
    strSQL = """
        CREATE TABLE if not exists Class
        (
            IDC text PRIMARY KEY,
            IDM text ,
            NAME text
        )"""
    str
    success_flag = True
    try :
        cur.execute(strSQL)
    except:
        success_flag = False
    if success_flag == True :
        print("Creat Ok")
    else:
        print("Creat Fail: ")

con,cur=connect_DB("Sinhvien.db")
# Creat_TableCLASS(cur)
# a=Insert_ISV(cur,con,"CN","CN18A","CNTT")
# print(a)