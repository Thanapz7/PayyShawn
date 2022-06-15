
import mysql.connector

def conDB():
    mydb = mysql.connector.connect(
            host="localhost",
            user="test",
            password="12345",
            database="test",
        )
    return mydb

class Con:
    def getHW():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hardware"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data 
#getdata = Con.getHW()
#for i in getdata:
#    print(i)

   
    def getHWname():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT name FROM hardware"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data 
# getdata = Con.getHWname()
# for i in getdata:
#     print(i)
    
    def insertHW():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO hardware (name, hw_name, status, value) VALUES ('D3', 'servo', 'OFF', 0.00)"
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return ID
# data = Con.insertHW()
# print(data)
    
    def updateHW():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hardware SET status = 'ON' WHERE id = 19"
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
#data = Con.updateHW()
#print(data)

    def deleteHW():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM hardware WHERE id =(SELECT MAX(id) FROM hardware)"
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
# data = Con.deleteHW()
# print(data)

    def selectHW():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hardware WHERE id = (SELECT MIN(id) FROM hardware)"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data 
data = Con.selectHW()
print(data)


