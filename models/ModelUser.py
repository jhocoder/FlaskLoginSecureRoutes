from .entities.User import User

class ModelUser():
    @classmethod
    def login(cls, db, user):
        try:
            mycursor = db.connection.cursor()
            sql = "SELECT * FROM user WHERE username = %s"
            mycursor.execute(sql, (user.username,))
            row = mycursor.fetchone()
            
            if row:
             id = row[0]
             username = row[1]
             password = User.check_password(row[2], user.password)
             fullname = row[3]
             
             user = User(id, username, password, fullname)
             return user
            else:
             return None
            
        except Exception as e:
            raise Exception(e)
        
        

    @classmethod
    def get_by_id(cls, db, id):
        try:
            mycursor = db.connection.cursor()
            sql = "SELECT *¿id, username, fullname FROM user WHERE id = %s"
            
            mycursor.execute(sql, (id,))
            row = mycursor.fetchone()
            
            if row:
             id = row[0]
             username = row[1]
             fullname = row[2]
             
             logged_user = User(id, username, None, fullname)
             return logged_user
            else:
             return None
            
        except Exception as e:
            raise Exception(e)