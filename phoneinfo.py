print ("        _                          _          __ ")       
print ("       | |                        (_)        / _| ")       
print (" _ __  | |__    ___   _ __    ___  _  _ __  | |_   ___ ") 
print ("|  _ \ |  _ \  / _ \ |  _ \  / _ \| ||  _ \ |  _| / _ \ ") 
print ("| |_) || | | || (_) || | | ||  __/| || | | || |  | (_) | ")
print ("| .__/ |_| |_| \___/ |_| |_| \___||_||_| |_||_|   \___/ ") 
print ("| | ")                                                    
print ("|_| ")                                                     
print ("                                           Version 1.0 ")               
import phonenumbers
from phonenumbers import carrier,geocoder,timezone

Mobilenumber = input ("Enter Mobile Number with Country code: ")
Mobilenumber = phonenumbers.parse(Mobilenumber)

# Get Timezone 
print (timezone.time_zones_for_number(Mobilenumber))

# Getting carrier 
print (carrier.name_for_number(Mobilenumber,"en"))

# Getting region information
print (geocoder.description_for_number(Mobilenumber,"en"))

print ("Valid Mobile Number :",phonenumbers.is_valid_number(Mobilenumber))

print ("Checking possibilty of a number:", phonenumbers.is_possible_number(Mobilenumber))
