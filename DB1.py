import sqlite3
from DB import connect_DB

def Creat_TableCLASS(cur):
    strSQL = """
        CREATE TABLE if not exists Class
        (
            IDC text PRIMARY KEY,
            IDT text,
            NAME text,
            KEY text
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

def Insert_Class(con,cur,idc,idt,name,key):
    success_flag=True
    try:
        cur.execute("""INSERT OR IGNORE INTO Class
                VALUES(?,?,?,?)""",(idc,idt,name,key))
    except:
        success_flag=False
    if success_flag == True:
        con.commit()
        return True
    else:
        return False

def Select_ClasS_IDT(cur,idt):
    result = cur.execute("SELECT * FROM Class WHERE IDT = ?;",(idt)).fetchall()
    return result


# con,cur=connect_DB("Sinhvien.db")
# a=Select_ClasS_IDT(cur,"1")
# print(a)
# Creat_TableCLASS(cur)
# print(a)