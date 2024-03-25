import hashlib

from Database.database import get_session
from Database.Models.user import Users

class BetterHash:
    def checkHash(self, username: str, password: str):
        hashPass = password
        hashUser = username
        HP = hashlib.md5(hashPass.encode())
        HU = hashlib.md5(hashUser.encode())
        
        # Check for user in DB
        with get_session() as session:
            user = session.query(Users).filter_by(Username=HU.hexdigest()).filter_by(Password=HP.hexdigest()).first()
            
            if user:
                return 1
            else: 
                return 0
        
    def createUser(self, username: str, password: str):
        hashPass = password
        hashUser = username
        
        with get_session() as session:
            if self.checkHash(hashUser, hashPass) == 1:
                return "User already exists!"
            
            HP = hashlib.md5(hashPass.encode())
            HU = hashlib.md5(hashUser.encode())
            
            User = Users(
                Username=HU.hexdigest(), 
                Password=HP.hexdigest()
            )
            session.add(User)
            session.commit()
