
              #**** DICTIONARY ****

#Sample Dictionary program to reslts value of searched word

#Sample dict

basketball_players = {"Kobe":"Forward_Player" ,"Lebron":"Dunk_Master","Curry":"3_pointer","Kyrie":{"Dunk":"yes","3_pointer":"yes","Gaurd":"no"}}
print("Enter the player name:")
search = input().capitalize()
print("He is a ->",basketball_players[search]) #user_input

#Copying contents to another list

Nba_Players = basketball_players.copy()

print("Nba_Players Dict:",Nba_Players)

# Deleting from Nba_players dictionary

del Nba_Players["Curry"]

print(Nba_Players)

#For loop in python

for key,value in Nba_Players.items():
 print(key ,":", value)

 #update is used to update the dictionary

 basketball_players.update({"Harden":"All_Star"})

 print(basketball_players)

 #adding items to set

 basketball_players["Kd"] = "3_pointer_&_Sharp_Shooter"

 print(basketball_players)

 #getting values

 print("Kyrie values",basketball_players.get("Kyrie"))

 #Acquiring keys & values

 print(basketball_players.keys())
print(basketball_players.items())


#clearing items from Nba_Players dict

Nba_Players.clear()
print(Nba_Players)

#popping element Wrt keys

basketball_players.pop("Kyrie")
print(basketball_players)


print(basketball_players.fromkeys("Curry"))
