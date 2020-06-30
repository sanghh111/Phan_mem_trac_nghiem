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
    # try:
    strsql="SELECT * FROM Class WHERE IDT = "+'"'+idt+'";'
    result = cur.execute(strsql).fetchall()
    # except:
        # return []
    return result

def Creat_Table_DSLH(cur):
    strSQL = """
        CREATE TABLE if not exists DSClass
        (
            IDC text ,
            ID text,
            PRIMARY KEY(IDC,ID)
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

def Select_Student_Class(cur,id):
    strSQL=('''SELECT A.IDC,A.NAME
FROM Class as A,DSCLASS as B
WHERE A.IDC=B.IDC AND B.ID = ''')
    strSQL+='"'+id+'"'+";"
    try:
        result=cur.execute(strSQL).fetchall()
    except:
        return []    
    return result

def Select_Signup_Class(cur,id):
    strSQL=('''SELECT IDC,NAME
FROM Class
EXCEPT
SELECT A.IDC,A.NAME
FROM Class as A,DSCLASS as B
WHERE A.IDC=B.IDC AND B.ID = ''')
    strSQL+='"'+id+'";'
    result=cur.execute(strSQL).fetchall()
    return result

def Select_ClasS_key(cur,idc):
    strsql="SELECT KEY FROM Class WHERE IDC = "+'"'+idc+'";'
    result = cur.execute(strsql).fetchone()
    return result

def Insert_DSCLASS(cur,con,idc,id,key):
    a=Select_ClasS_key(cur,idc)
    a=a[0]
    print(a)
    if a==key:
        success_flag=True
        strSQL='''INSERT INTO DSClass
VALUES'''+'("'+idc+'",'+'"'+id+'");'
        cur.execute(strSQL)
        # try:
        #     cur.execute(strSQL)
        # except:
        #     success_flag = False
    else :
        success_flag=False
    if success_flag:
        con.commit()
    return success_flag

# con,cur=connect_DB("Sinhvien.db")
# Creat_Table_DSLH(cur)
# Creat_TableCLASS(cur)
# Select_Signup_Class(cur,"1851150006")
# a=Select_ClasS_IDT(cur,"Sang")
# print(a) 
# a=Select_ClasS_IDT(cur,"1")
# print(a)
# print(a)