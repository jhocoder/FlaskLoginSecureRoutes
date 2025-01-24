from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class User(UserMixin):
    
    def __init__(self, id, username, password, fullname=""):
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname
        
    @classmethod   
    def check_password(cls, hashed_password, password):
        return check_password_hash(hashed_password, password)
    
    
# print(generate_password_hash("Maquina"))

# print("scrypt:32768:8:1$gplRxcb7yP9llgS1$ecb6d2f105f2c8f81054093a77367a259901ab91061f2bac86e9cc7af5b475e002edccde1b6ca23e4bb49bae63decea9b0e9e638bb7742934da6b7e55c6040c8")
