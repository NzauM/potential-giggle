# class Car:
#     def sell_Car(self):
#         '''
#         Finalizes car sale
#         '''
#         return "Car is finally sold"
#     pass

# atenza = Car()
# # instance.method()
# print(atenza.sell_Car())

# class Character:
#     # name, image, votes
#     def __init__(self, image, votes,name="Default Name"):
#         self.name = name
#         self.image = image
#         self.votes = votes     
#         pass
#     pass

# mr_monkey = Character("Mr Monkey","No Image", 20)
# print(mr_monkey.name)

class InstragamUser:
    def __init__(self, username, password, bio):
        self.username = username
        self._password = password
        self.bio = bio

    def login(self, username, password):
        if(username == self.username and password == self._password):
            return "Entry Allowed"
        else:
            return "Please Sign Up or use correct password"

    @property    
    def password(self):
        return self._password
    
    @password.setter
    def set_password(self, newpassword):
        if len(newpassword) < 8:
            return "Password too short"
        else:
            self._password = newpassword


            
    # password = property(password, set_password)
    # def change_password(new_password):
# name = input("Enter IG Username")
# passw = input("Enter IG Password")
# bio = input("Enter short bio")
# new_user = InstragamUser(name, passw, bio)
# nameEntered = input("Enter IG Username")
# passwEntered = input("Enter IG Password")
# print(new_user.login(nameEntered, passwEntered))
# nzaum = InstragamUser(username="nzaum", password=1234, bio="Tumechoka Mercy")
# print(nzaum.login("nzaum",12345))
# print(nzaum.password)

