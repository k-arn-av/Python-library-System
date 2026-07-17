from users import users

class Manager:
    def __init__(self):
        self.all_users={}#stores key id and value object
        self.currentUser=None
    
    def create_account(self, username:str, userID:str):
        if userID in self.all_users:
            print("UserID already taken")
            return False
        else:
            new_user=users(username, userID)#object created 
            self.all_users[userID]=new_user# key id stores all user attributes, {key, object}
            return True
    
    def login(self, userID:str):
        if userID not in self.all_users:
            print("Id doesnt exist, create a new one")
            return False
        else:
            self.currentUser=self.all_users[userID]      
            return True

    def logout(self):
        if self.currentUser is not None:
            self.currentUser=None
            return True
        else:
            print("nobody logged in")
            return False

    def deleteAccount(self):
        self.all_users.pop(self.currentUser.userID,None)  
        print("Successfully deleted account")  

        

    


    






