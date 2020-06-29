import sqlite3
import hashlib
#connect Database
def connect_DB(dbfile):
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    return con, cur

def Creat_TableSV(cur):
    strSQL = """
        CREATE TABLE if not exists SV
        (
            ID text PRIMARY KEY,
            PASSWORD text,
            SALT text
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

def Insert_SV(cur,con,id,passWord,salt):
    success_flag=True
    try:
        cur.execute("""INSERT OR IGNORE INTO SV
                VALUES(?,?,?)""",(id,passWord,salt) )
    except:
        success_flag=False
    if success_flag == True:
        con.commit()
        return True
    else:
        return False

def Select_SV(cur):
    result = cur.execute("SELECT * FROM SV")
    return result

def Select_SV_salt(cur,id):
    result = cur.execute("SELECT SALT FROM SV WHERE ID = ?;",(id,)).fetchone()
    return(result[0])

def Update_SV_pass(cur,con,id,newPassWorld):
    success_flag = True
    try:
        st1="UPDATE OR IGNORE SV SET "
        st2= "PASSWORD" + " = ?"
        st3="WHERE ID = ?"
        st = st1 + st2 + st3
        cur.execute(st,(newPassWorld,id))
    except:
        success_flag= False
    con.commit()
    if success_flag == True:
      return True
    else :
      return False

def Checkpassworld_SV(cur,id,pas):
    try:
        salt=Select_SV_salt(cur,id)
        pas=pas+salt
        mk= hashlib.md5(pas.encode('utf-8')).hexdigest()
        pas_old=cur.execute('SELECT PASSWORD FROM SV WHERE ID = ?;',(id,))
        pas_old=pas_old.fetchone()
        pas_old=pas_old[0]
    except:
        return False
    if(pas_old==mk):
        return True
    else:
        return False

def Creat_TableISV(cur):
    strSQL = """
        CREATE TABLE if not exists ISV
        (
            ID text PRIMARY KEY,
            NAME text,
            BIRTHDAY date,
            SEX text,
            PHONE text,
            EMAIL text
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

def Insert_ISV(cur,con,id,name,birth,sex,phone,email):
    success_flag=True
    try:
        cur.execute("""INSERT OR IGNORE INTO ISV
                VALUES(?,?,?,?,?,?)""",(id,name,birth,sex,phone,email))
    except:
        success_flag=False
    if success_flag == True:
        con.commit()
        return True
    else:
        return False

def Select_ISV(cur,id):
    result = cur.execute("SELECT * FROM ISV WHERE ID = ?;",(id,)).fetchone()
    return result

def Select_T_salt(cur,id):
    result = cur.execute("SELECT SALT FROM T WHERE IDT = ?;",(id,)).fetchone()
    return(result[0])

def Update_ISV(cur,con,id,name,birth,gender,phone,email):
    success_flag=True
    str1="UPDATE OR IGNORE ISV SET "
    a=[]
    if name!="":
        a.append("\nNAME = "+name)
    if gender!="":
        a.append("\nSEX = "+gender)
    if birth!="":
        a.append("\nBIRTHDAY = "+birth)
    if phone!="":
        a.append("\nPHONE = "+phone)
    if email!="":
        a.append("\nEMAIL = "+email)
    for i in a:
        if i==a[-1]:
            str1+=i
        else:
            str1+=i+","
    str2="\nWHERE ID = "+id+";"
    str1+=str2
    print(str1)
    # cur.execute(str1)
    try:
        cur.execute(str1)
    except:
        success_flag=False
    if success_flag:
        con.commit()
        return True
    else:
        return False



#                                           LETURER




def Creat_Table_T(cur):
    strSQL = """
        CREATE TABLE if not exists T
        (
            IDT text PRIMARY KEY,
            PASSWORD text,
            SALT text
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

def Insert_T(cur,con,id,passWord,salt):
    success_flag=True
    try:
        cur.execute("""INSERT OR IGNORE INTO T
                VALUES(?,?,?)""",(id,passWord,salt) )
    except:
        success_flag=False
    if success_flag == True:
        con.commit()
        return True
    else:
        return False

def Select_T(cur):
    result = cur.execute("SELECT * FROM T")
    return result

def Checkpassworld_T(cur,id,pas):
    try:
        salt=Select_T_salt(cur,id)
        pas=pas+salt
        mk= hashlib.md5(pas.encode('utf-8')).hexdigest()
        pas_old=cur.execute('SELECT PASSWORD FROM T WHERE IDT = ?;',(id,))
        pas_old=pas_old.fetchone()
        pas_old=pas_old[0]
    except:
        return False
    if(pas_old==mk):
        return True
    else:
        return False

def Creat_TableIT(cur):
    strSQL = """
        CREATE TABLE if not exists IT
        (
            IDT text PRIMARY KEY,
            NAME text,
            BIRTHDAY date,
            SEX text,
            PHONE text,
            EMAIL text
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

def Insert_IT(cur,con,id,name,birth,sex,phone,email):
    success_flag=True
    try:
        cur.execute("""INSERT OR IGNORE INTO IT
                VALUES(?,?,?,?,?,?)""",(id,name,birth,sex,phone,email))
    except:
        success_flag=False
    if success_flag == True:
        con.commit()
        return True
    else:
        return False

def Select_IT(cur,id):
    result = cur.execute("SELECT * FROM IT WHERE IDT = ?;",(id,)).fetchone()
    return result

def Update_IT(cur,con,id,name,birth,gender,phone,email):
    success_flag=True
    str1="UPDATE OR IGNORE IT SET "
    a=[]
    if name!="":
        a.append("\n NAME = "+name)
    if gender!="":
        a.append("\n SEX = "+gender)
    if birth!="":
        a.append("\n BIRTHDAY = "+birth)
    if phone!="":
        a.append("\n PHONE = "+phone)
    if email!="":
        a.append("\n EMAIL = "+email)
    for i in a:
        if i==a[-1]:
            str1+=i
        else:
            str1+=i+","
    str2="\nWHERE IDT = "+id+";"
    str1+=str2
    print(str1)
    # cur.execute(str1)
    try:
        cur.execute(str1)
    except:
        success_flag=False
    if success_flag:
        con.commit()
        return True
    else:
        return False
# con,cur=connect_DB("Sinhvien.db")
# Creat_Table_T(cur)
# Creat_TableIT(cur)
# a=Update_ISV(cur,con,"123","2","1","12312","","123","12312")
# print(a)
# a=Select_ISV(cur,"Sang")
# print(a)
# a=Insert_ISV(cur,con,"123","","","","","","")
# print(a)
# Creat_TableISV(cur)
# a=Select_SV_salt(cur,"123")
# print(a)
# a=Insert_SV(cur,con,"12","123abc","abc")
# print(a)
# Creat_TableSV(cur)
# a=Select_SV(cur)
# for i in a: 