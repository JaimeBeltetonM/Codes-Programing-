import time
import os
########
#define functions
#######
def check_time():
    os.system('clear')
    global minutes
    minutes = minutes + 4
    if minutes >= 15:
        late()
    else:
        print("Your game is in", 15 - minutes, "minutes")

def late():
    global minutes
    print("You didnt make it to your game")
    print("Because of that, the manager is going to left you in the bench the next game like penaldo")
    input("Press enter to start over again")
    start()

def start():
    os.system('clear')
    print("Welcome!")
    print("\nYou just arivied at The Fields at RFK Campus with your cousins. \nYou go to the bathroom and when you comeback to the parking lot there gone. \nYou forgot which field your playing at. \nYour game starts in 15 minutes and you have to find them fast.")
    print("You are in parkinglot")
    print("Go look for them, they're not here!")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tfield1\n\tfield2\n\tfield3\n\tfield4\n")
    if move.lower() == "field1":
        field1()
    elif move.lower() == "field2":
        field2()
    elif move.lower() == "field3":
        field3()
    elif move.lower() == "field4":
        field4()
    else:
        print("\nsorry, I don't understand your input. I'll assume you want to stay here")
        time.sleep(3)
        parkinglot()





def field1():
    check_time()
    print("You are in field1")
    print("You look around the field and see if they're here...")
    print("THERE NOT HERE")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tparkinglot\n\tfield2\n\tfield3\n\tfield4\n")
    if move.lower() == "parkinglot":
        parkinglot()
    elif move.lower() == "field2":
        field2()
    elif move.lower() == "field3":
        field3()
    elif move.lower() == "field4":
        field4()
    else:
        print("\nsorry, I don't understand your input. I'll assume you want to stay here")
        time.sleep(3)
        field1()

def field2():
    check_time()
    print("You are in field2")
    print("You look around the field and see if they're here...")
    print("THERE NOT HERE")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tparkinglot\n\tfield1\n\tfield3\n\tfield4\n")
    if move.lower() == "field1":
        field1()
    elif move.lower() == "parkinglot":
        parkinglot()
    elif move.lower() == "field3":
        field3()
    elif move.lower() == "field4":
        field4()
    else:
        print("\nsorry, I don't understand your input. I'll assume you want to stay here")
        time.sleep(3)
        field2()

def field3():
    check_time()
    print("You are in field3")
    print("You look around the field and see if they're here...")
    print("THERE NOT HERE")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tparkinglot\n\tfield1\n\tfield2\n\tfield4\n")
    if move.lower() == "field1":
        field1()
    elif move.lower() == "parkinglot":
        parkinglot()
    elif move.lower() == "field2":
        field2()
    elif move.lower() == "field4":
        field4()
    else:
        print("\nsorry, I don't understand your input. I'll assume you want to stay here")
        time.sleep(3)
        field3()

def field4():
    check_time()
    print("You are in field4")
    print("You look around the field and see if they're here...")
    print("YOU FOUND THEM!!!")
    print("Sadly you went on to lose the match 4-0 because you went ghost")
    input("\nPress enter to play again.")
    start()

def parkinglot():
    check_time()
    print("You are in the parking lot")
    print("Go look for them, they're not here!")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tfield1\n\tfield2\n\tfield3\n\tfield4\n")
    if move.lower() == "field1":
        field1()
    elif move.lower() == "field2":
        field2()
    elif move.lower() == "field3":
        field3()
    elif move.lower() == "field4":
        field4()
    elif move.lower() == "stay in parking lot":
        parkinglot()
    else:
        print("\nsorry, I don't understand your input. I'll assume you want to stay here")
        time.sleep(3)
        parkinglot()
########
#main
#######
#TODO: Add some global variables
minutes = 0
start()