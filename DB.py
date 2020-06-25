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

def Update_User(cur,con,id,newPassWorld):
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

def Checkpassworld(cur,id,pas):
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
            CLASS text,
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

def Insert_ISV(cur,con,id,claSs,name,birth,sex,phone,email):
    success_flag=True
    try:
        cur.execute("""INSERT OR IGNORE INTO ISV
                VALUES(?,?,?,?,?,?,?)""",(id,claSs,name,birth,sex,phone,email))
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


# con,cur=connect_DB("Sinhvien.db")
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