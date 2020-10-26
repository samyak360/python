# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:12:00 2019

@author: soumil
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 22:47:25 2019

@author: soumil
"""
import random
 
# This is the room class, this dontes the properties of the room in the hotel
class rooms:
    def __init__(self):
        self.guest=''
        self.roomno=0
        self.booked=0
        self.cost=1000
        self.type='Standard'
        self.extra_bed=500
        self.members=0
    
"""
This is a hotel class which have a 4x4 mattrix of rooms   
"""    
class hotel:

    def __init__(self):
        self.totalrooms=16
        self.standardrooms=12
        self.deluxrooms=4
        self.roomsvacent=0
        self.standardvacent=0
        self.deluxvacent=0
        self.rooms_mattrix=[]
        self.preference=''
        # this is the mattrix of the rooms in the hotel, the each room has 
        # all the properties defined in the class rooms
        for i in range(0,4):
            self.rooms_mattrix.append([])
            for j in range(0,4):
                self.rooms_mattrix[i].append(rooms())
        self.randomassign()
    
        
    """
    Arguments: No arguments 
    function : This function randomly assigns a delux roon in every row of the 
               rooms_mattrix, increase room and extra bed cost.
               Assigns room no. to each room according to the row no. in the 
               rooms_mattrix
    return   : nothing
    """
    def randomassign(self):
        # Assign the room no. to the rooms of rooms_mattrix
        for i in range(0,4):
            for j in range(0,4):
                self.rooms_mattrix[i][j].roomno=(i+1)*100+j
        
        # Randomly assign th delux room at each floor and increase its cost
        for i in range (0,4):
                x=random.choice(self.rooms_mattrix[i])
                x.type="Delux"
                x.cost+=500
                x.extra_bed+=200
                
    """
    Arguments : roomobject (The object of the room which is assigned to the guest)
    function  : This takes the details of the guest like: 
                    Name of the guest
                    No. of members
                and manipulate the values of vacent rooms according to the 
                assigned room type.
                
    return    : roomno (room number)
    """
    def guestdetails(self,roomobject):
        roomobject.guest=input("Enter your name: ")
        roomobject.members=int(input("Number of members: "))
        self.roomsvacent-=1
        if roomobject.type=='Delux':
            self.deluxvacent-=1
        else:
            self.standardvacent-=1
        self.preference=''
        return roomobject.roomno
        
    """
    Argument: fun_preference (room preference of the user)
    function: This funciton basically assign a room to the guest according to 
              the availability of the room which satisfies the preference 
              of the room.
    return  : Returning the object of the room
    """
    def assignroom(self,fun_preference):
        room_obj=0
        for i in range(0,4):
            for j in range(0,4):
                if (not self.rooms_mattrix[i][j].booked) and self.rooms_mattrix[i][j].type==fun_preference:
                    #number=self.guestdetails(self.rooms_mattrix[i][j])
                    room_obj=self.rooms_mattrix[i][j]
                    break
            if room_obj:
                break
        room_obj.booked=1
        return room_obj
    
    """
    Arguments: prefer (Room preference of the user)
    function : This function checks the preference provided by the user is valid
               or not. Return 1 if it is valid else 0.
               
    return : Integer value 1/0
    
    """
    
    def check_preference(self,prefer):
        if prefer==1  and self.deluxvacent:
            return 1
        elif prefer==2 and self.standardvacent:
            return 1
        else:
            return 0
        
    """
    Arguments: nothing
    function: This function get the user preference from the user if not already
              provided.
    return  : return a string of the type of the room 
    """
    
    def get_preference(self):
        print("Enter the preference of the room\n\
                  1 for Delux \t 2 for Standard")
        while 1:
            self.preference=int(input())
            tmp = self.check_preference(self.preference)
            if tmp==1:
                return ("Delux")
            elif tmp==2:
                return ("Standard")
            else:
                print("Room not available with this preference, select \
                      another option")
    
    """
    Arguments: nothing
    function : This calls the function get_preference whenever we need to take
               the preference of the room type from the user if not already 
               provided.
    return   : return string type of the preference
    """
        
    def newbooking(self):
        if not self.roomsvacent:
            print("No rooms vacent, sorry please try some other day")
            return ''
        
        if not self.preference:
            print("Rooms availability: ")
            self.display()
            self.preference=self.get_preference()
            
        return self.preference
        
        
    """
    Arguments: nothing
    function : Display the status of the availability of rooms from the 
               rooms_mattrix 
    return   : nothing
        
    """
    def display(self):
        print("Total Rooms :",self.totalrooms)
        print("Rooms Available :",self.roomsvacent)
        print("Available room type")
        print("\t Standard :",self.standardvacent)
        print("\t Delux    :",self.deluxvacent)
        print()
    
    def status(self):
        for i in range(0,4):
            for j in range(0,4):
                if self.rooms_mattrix[i][j].booked==0:
                    self.roomsvacent+=1
                    if self.rooms_mattrix[i][j].type=='Standard':
                        self.standardvacent+=1
                    else:
                        self.deluxvacent+=1
        return self.roomsvacent
    
    def cancelbooking(self):
        print("In which room do you stay")
        n=int(input())
        i=n/100-1
        j=n%10
        return (i,j)
        
    
if __name__=='__main__':
    h=hotel()
    h.status() # calling status() function initially to set up the values of 
               # the data members describing the vacancy of the rooms type
    while 1:
        print("Press 1 for new booking \nPress 2 to know the status of rooms booking\
              \nPress 3 to cancel or over your booking\nPress 4 to exit")
        n=int(input())
        if (n==1):
            # newbooking returns the string type (peference, delux or Standard)
            prefer=h.newbooking()
             # this is the case when rooms are not availabele and the return 
             # value is ''
            if prefer=='':  
                continue
            objectofroom=h.assignroom(prefer)
            room_number=h.guestdetails(objectofroom)
            print("Your assigned room number is ",room_number)
            print()
            
        elif (n==2):
            h.display()
        elif (n==3):
            print(h.cancelbooking())
        elif (n==4):
            break