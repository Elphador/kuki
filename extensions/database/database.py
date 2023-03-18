from pymongo import MongoClient
from config import *

client = MongoClient(mongodb)
db = client.database

user = db.cuser 
admin = db.cadmin
status = db.status

class database:

# user database
    def exist(user_id:int) -> bool:
        """
        Give boolean whether the user exist in the bot or not
        Args:
            user_id: telegram id of the user
        Return:
            True -> when user exist in the bot
            False -> when user doesn't exist in the bot
        """
        if user.find_one({"user_id":user_id}) == None:
            return True
        return False
    
    def add_user(name:str,user_id:int,username:str,date:str) -> None:
        """
        Add user to database
        Args:
            name: telegram first name of the user
            user_id: telegram id of the user
            username: telegram username of the user
            date: the time when user join the bot
        Return:
            None
        """
        user.insert_one({"name":name,"user_id":user_id,"username":username,"date":date})
    def get_users():
        """
        Give all users in database with there user_id, name, username and the time when user join
        Args:
            None
        Return:
            dict
        """
        return user.find_one({})
    def users_num() -> int:
        """
        Return the number of users in the bot
        Args:
            None
        Return:
            number of users in the bot
        """
        return len([ 0 for i in user.find({})])
    def get_admin() -> list:
        """
        Get all admins in the database
        Args:
            type: whether the desire result is admin or promoted
        Return:
            all admins or promoted
        """
        return [admin["admin"] for admin in admin.find({})]
    def admins() -> dict:
        """
        Get all admins in the database
        Args:
            None
        Return:
            all admins or promoted
        """
        return admin.find({})
    def add_admin(user_id,name) -> None:
        """
        Add admin to the admin database
        Args:
            user_id: admin id
            name: promoter name
        Return:
            None
        """
        admin.insert_one({"admin":user_id,"promoted":name})
# status database
    def get_force_status() -> str:
        """
        Get the status of the force join channel/group
        Args:
            None
        Return:
            "on" or "off" 
            on -> when force join channel/group is on
            off -> when force join channel/group is off
        """
        if status.find_one({"exist":True}) == None:
            return "off"
        return status.find_one({"exist":True})["status"]

    def set_force_status(stat:str) -> None:
        """
        Set force status 
        Args:
            "on" or "off" 
            on -> when force join channel/group is on
            off -> when force join channel/group is off
        Return:
            None
        """
        if status.find_one({"exist":True}) == None:
            status.insert_one({"exist":True,"status":stat})
        status.update_one({"exist":True},{"$set":{"status":stat}})
