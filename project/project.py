import sys
import climage
import webbrowser
import os
import time
os.system(" ")
back = "However you can still hear noises from the vents, make your choice quickly.\n"


# Calls all the root functions
def main():
    letter_print("What color would you like the text to be?")
    letter_print("""Purple, red, maroon red, orange, green, blue,
dark blue, or deap teal""", end="")
    color = color_choice(input(": ").lower().strip())
    print(color)
    letter_print(f"""
HOW TO CONTROL: You type what you want to do in the terminal.
However you can 'search' areas to be able to unlock new choices,
or you can 'repeat' the text printed when you walked in the room,
or you can type in the name of the room to go there, or you can
type 'where am I' to find out what room you're in.
""")
    letter_print("Please make terminal fullscreen")
    start(input("Would you like to start (yes/no): ").lower().strip())
    letter_print(story_text("part1"))
    print(images(0))
    text, user = get_username(input(f"""{color}[AI BOOT]
[URGENT] AI damaged, please input pilot name to continue boot: """), color)
    letter_print(text)
    letter_print(story_text("bridge"))
    bridge("bridge", user)


# Asks if you want to start the game
def start(ans):
    if "y" in ans or "yes" in ans:
        pass
    else:
        sys.exit("See you soon.")


# prints the letters one at a time, used code found in
# https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
def letter_print(string, end="\n"):
    for char in string:
        print(char, end="", flush=True)
        time.sleep(.025)
    print(end, end="")


def color_choice(colors):
    if "purple" in colors:
        color = "\x1b[38;2;152;31;197m"
    elif "maroon" in colors:
        color = "\x1b[38;2;180;0;0m"
    elif "red" in colors:
        color = "\x1b[38;2;255;26;26m"
    elif "orange" in colors:
        color = "\x1b[38;2;255;112;52m"
    elif "green" in colors:
        color = "\x1b[38;2;45;153;44m"
    elif "dark" in colors:
        color = "\x1b[38;2;11;11;96m"
    elif "blue" in colors:
        color = "\x1b[38;2;53;91;245m"
    elif "teal" in colors:
        color = "\x1b[38;2;0;95;95m"
    else:
        color = ""
    return color

# This function returns txt files that contain the
# the story of the game or settings of the rooms
def story_text(c: str):
    if c == "back":
        return open("text/back.txt").read()
    elif c == "part1":
        return open("text/story.txt").read()
    elif c == "bridge":
        return open("text/story1.txt").read()
    elif c == "airlock":
        return open("text/airlock.txt").read()
    elif c == "airlock2":
        return open("text/airlock_2.txt").read()
    elif c == "ai":
        return open("text/ai.txt").read()
    elif c == "panels":
        return open("text/panels.txt").read()
    elif c == "kitchen":
        return open("text/kitchen.txt").read()
    elif c == "bed":
        return open("text/bedroom.txt").read()
    elif c == "gen":
        return open("text/generator.txt").read()
    elif c == "cargo":
        return open("text/cargo.txt").read()
    elif c == "final":
        return open("text/cargo.txt").read()
    elif c == "monster":
        return open("text/monster.txt").read()
    elif c == "monster2":
        return open("text/monster2.txt").read()
    else:
        return "I haven't written this part yet, sorry."


def images(n: int):
    if n == 0:
        return climage.convert("images/image0.png", is_unicode=True, is_truecolor=True, is_256color=False)
    elif n == 1:
        return climage.convert("images/image1.png", is_unicode=True, is_truecolor=True, is_256color=False)


# requires the user name of the player and prints
# a colored version of text, that's why it's not in a txt file
def get_username(user: str, c: str):
    user = user.strip()
    return (f"""{c}[BOOTING SYSTEMS]
Main Power
    \x1b[38;5;196m<OFFLINE>\x1b[0m
{c}Backup Power
    \x1b[38;5;196m<OFFLINE>\x1b[0m
{c}Coms
    \x1b[38;5;196m<OFFLINE>\x1b[0m
{c}----------------------------------------
[URGENT] {user}, main power control panel is inaccessible, human intervention required.
[URGENT] Backup power control panels inaccessible, human intervention required.
[URGENT] Airlocks inaccessible, human intervention required.
[SYSTEM] Air flow inhibited, possible threat.
    <Conclusion reach from shifting of weight.>
"""), user


# Each function this point onward is a room or an area you can go to inside a room
# Add a 'where am I?' check and print room name when asked this
def bridge(progress: str, user):
    x = 0
    if progress == "bridge":  # Tracks the progress of the player
        for _ in range(4):
            ans1 = input(f"What do you do {user}? ").lower().strip()
            if "repeat" in ans1:
                # repeats the text printed when you walk in the room
                letter_print(story_text("bridge"))
            elif "where" in ans1:
                letter_print("You are in the bridge.\n")
            elif "main" in ans1 or "living" in ans1:
                # takes you to the living area/room
                letter_print("The door to the living area is locked,", end="")
                letter_print(" so you head back to the bridge\n")
            elif "airlock" in ans1:
                # takes you to the airlock
                letter_print(story_text("airlock"))
                return airlock("airlock", user)
            elif "cargo" in ans1:
                # takes you to the cargo bay
                letter_print("The cargo bay doors are locked, you head back to the bridge")
                letter_print("You can still hear noises in the vents, make your choice quickly\n")
            elif "bedroom" in ans1:
                # takes you to the bedroom
                letter_print(story_text("airlock"))
                letter_print("The bedroom door is locked\n")
                return airlock("airlock", user)
            elif "kitchen" in ans1:
                # takes you to the kitchen
                letter_print(story_text("airlock"))
                letter_print("The kitchen door is locked\n")
                return airlock("airlock", user)
            elif "ai" in ans1:
                # get ai advice
                letter_print(story_text("ai"))
                letter_print("You can still hear noises from the vents, and they're getting closer.\n")
                x += 1
            elif "panel" in ans1:
                # check other systems
                letter_print(story_text("panels"))
                letter_print("You can still hear noises from the vents, and they're getting closer.\n")
                x += 1
            elif "search" in ans1:
                # searches the area
                letter_print("You search the main deck but find nothing.\n")
            else:
                letter_print("You can hear the noises get closer.\n")
                x += 1

    elif progress == "bridge2":  # progress check
        for _ in range(4):
            ans1 = input(f"What do you do {user}? ").lower().strip()
            if "repeat" in ans1:  # reapeats the text printed when walking in
                letter_print(story_text("bridge"))
            elif "where" in ans1:
                letter_print("You are in the bridge.\n")
            # takes you to the rooms with same progress
            elif "main" in ans1 or "living" in ans1:
                letter_print("The door to the living area is locked,", end="")
                letter_print(" so you head back to the bridge\n")
            elif "airlock" in ans1:
                letter_print(story_text("airlock2"))
                return airlock("airlock2", user)
            elif "cargo" in ans1:
                letter_print("Cargo bay is locked.\n")
            elif "kitchen" in ans1:
                letter_print("You look around the kitchen and see one of the ships backup generators\n")
                return kitchen("kitchen", user)
            elif "bedroom" in ans1:
                letter_print("You look around the bedroom and see one of the ships backup generators\n")
                return bedroom("bed", user)
            elif "ai" in ans1:
                letter_print(story_text("ai2"))  # add AI advise for the progress amount
                letter_print("You can still hear noises from the vents, and they're getting closer.\n")
                x += 1
            elif "panel" in ans1:
                letter_print(story_text("panels2"))  # add advise from the system for the progress amount
                letter_print("You can still hear noises from the vents, and they're getting closer.\n")
                x += 1
            elif "search" in ans1:
                # searches the area
                letter_print("You search the main deck but find nothing.\n")
            else:
                letter_print("You can hear the Monster get closer.\n")
                x += 1

    elif progress == "bridge3":
        for _ in range(4):
            ans1 = input(f"What do you do {user}? ").lower().strip()
            if "repeat" in ans1:
                letter_print(story_text("bridge"))
            elif "where" in ans1:
                letter_print("You are in the bridge.\n")
            # takes you to rooms with the same progress
            elif "main" in ans1 or "living" in ans1:
                letter_print("You head to the living area.\n")
                return main_deck("main", user)
            elif "airlock" in ans1:
                letter_print(story_text("airlock2"))
                return airlock("airlock3", user)
            elif "kitchen" in ans1:
                letter_print(story_text("kitchen"))
                return kitchen("kitchen2", user)
            elif "bedroom" in ans1:
                letter_print(story_text("bed"))
                return bedroom("bed2", user)
            elif "cargo" in ans1:
                letter_print(story_text("cargo"))
                return cargo("cargo", user)
            elif "ai" in ans1:
                # get ai advice
                letter_print(story_text("ai3"))  # add advise for progress
                letter_print("You can still hear noises from the vents, and they're getting closer.\n")
                x += 1
            elif "panel" in ans1:
                # check other systems
                letter_print(story_text("panels3"))  # add advise for progress
                letter_print("You can still hear noises from the vents, and they're getting closer.\n")
                x += 1
            elif "search" in ans1:
                # searches the area
                letter_print("You search the main deck but find nothing.\n")
            else:
                letter_print("You can hear the Monster get closer.\n")
                x += 1

    # This is for after you get the key in the cargo bay
    # Ends in '.1' because you can't truly progress further past this point
    # without going to the living area
    elif progress == "bridge3.1":
        for _ in range(4):
            ans1 = input(f"What do you do {user}? ").lower().strip()
            if "repeat" in ans1:
                letter_print(story_text("bridge"))
            elif "where" in ans1:
                letter_print("You are in the bridge.\n")
            elif "main" in ans1 or "living" in ans1:
                letter_print("You head to the living area.\n")
                return main_deck("main2", user)
            elif "airlock" in ans1:
                # leave area
                letter_print(story_text("airlock2"))
                return airlock("airlock3.1", user)
            elif "cargo" in ans1:
                letter_print(story_text("cargo"))
                return cargo("cargo2", user)
            elif "bedroom" in ans1:
                letter_print(story_text("bed"))
                return bedroom("bed2.1", user)
            elif "kitchen" in ans1:
                letter_print(story_text("kitchen"))
                return kitchen("kitchen2.1", user)
            elif "ai" in ans1:
                # get ai advice
                letter_print(story_text("ai3.1"))
                letter_print("You can still hear noises from the vents, and they're getting closer.\n")
                x += 1
            elif "panel" in ans1:
                # check other systems
                letter_print(story_text("panels3.1"))
                letter_print("You can still hear noises from the vents, and they're getting closer.\n")
                x += 1
            elif "search" in ans1:
                # searches the area
                letter_print("You search the main deck but find nothing.\n")
            else:
                letter_print("You can hear the Monster get closer.\n")
                x += 1
    if x == 4:
        letter_print("The Monster ate you alive. Ending 1/3")
        again = input("Restart? (yes/no)")
        if "yes" in again or "y" in again:
            return main()
        else:
            sys.exit("Bye, have a great time!")


# Is the final choices of the game
def final_choice(gun, user):
    x = 0
    if gun == "gun":
        letter_print(story_text("monster"))
        while True:
            a = input(f"What do you do {user}? ").lower().strip()
            if "shoot" in a:
                letter_print("You shoot and injure creature, but it doesn't die and it looks angry.")
                for _ in range(3):
                    b = input("Do you shoot it again? (yes/no) ").lower().strip()
                    if "yes" in b or "y" in b:
                        letter_print("""The Monster starts to barrel toward you,
but you shoot it and it stops abruptly in it's tracks""")
                        x += 1
                        c = input("Do you shoot it again? (yes/no) ").lower().strip()
                        if "yes" in c or "y" in c:
                            letter_print("""You shoot it one more time and it drops dead.
You move closer to the corpse and kick it to see if it's truly dead. It is and you slowly drag to the airlock and eject it.""")
                        else:
                            letter_print("The Monster lunges at you and grabs you by the face, crushing it.")
                            letter_print("The Monster killed you. Ending 1/3")
                            again = input("Restart? (yes/no)")
                            if "yes" in again or "y" in again:
                                return final_choice("gun", user)
                            else:
                                sys.exit("Bye, have a great time!")
                    else:
                        letter_print("The Monster takes another step towards you")
                        x += 1
                if x == 3:
                    letter_print("The Monster lunges at you and grabs you by the face, crushing it.")
                    letter_print("The Monster killed you. Ending 1/3")
                    again = input("Restart? (yes/no)")
                    if "yes" in again or "y" in again:
                        return final_choice("gun", user)
                    else:
                        sys.exit("Bye, have a great time!")

            elif "closer" in a:
                letter_print("As you get closer to the Monster, it steps backwards eyeing the gun at your hip.")
                letter_print("""You tell it "I just want to help you." as you take another step towards it.
There's a first aid kit to you're right, if you decide you want to tend it's injuries. However you're close
to kill it with one shot if you choose to shoot it""")
                b = input(f"What do you do {user}? ").lower().strip()
                if "shoot" in b:
                    letter_print("""You shoot it in the head and it drops dead.
You move closer to the corpse and kick it to see if it's truly dead. It is and you slowly drag to the airlock and eject it.""")
                    letter_print("You killed the Monster! Ending 3/3")
                    sys.exit("I hope you enjoyed the game :)")
                elif "aid" in b or "kit" in b:
                    letter_print("""You grab the first aid kit and move closer to the Monster to give it medical aid.
While you bandage and disinfect the wounds, the creature makes noises of pain, but it does bot attack you. After
fully patching it up it seems to have grown closer to and is no longer threat to you or you ship.""")
                    letter_print("You saved the creature! Ending 2/3")
                    sys.exit("I hope you enjoyed the game :)")
                else:
                    letter_print("That's not an option avaible to you right now.\n")

            else:
                letter_print("That's not an option avaible to you right now.\n")

    else:
        letter_print(story_text("monster2"))
        while True:
            a = input(f"What do you do {user}? ").lower().strip()
            if "wait" in a:
                letter_print("""You yell at the Monster to grab it's attention.
It was successfull as it starts lumbering towards you, getting closer to the airlock.\n""")
                x += 1
                for _ in range(2):
                    b = input("Do you wait? ").lower().strip()
                    if "wait" in b:
                        letter_print("You wait for the Monster to get closer")
                        x += 1
                    else:
                        letter_print("You decide not to risk it and runaway to hide.")
                        letter_print("""The ship's AI however does not like your caward behavior and deems you unnessary
as it ejects both you and the Monster into space.""")
                        webbrowser.open("https://www.youtube.com/watch?v=X2acP06791I")  # takes you to a youtube song
                        letter_print("The AI has taken over the ship, you are now dead. Ending 4/3")
                        sys.exit("I hope you enjoyed the game :)")
                if x == 3:
                    letter_print("""Just as the beast steps in front of the bridges airlock doors, you hold on to something tightly as
you press the ejection button launching the Monster and some of the loose materials from the wreckage the monster made in your ship.""")
                    letter_print("""You feel your grip starting to loosen as the vacume of space tugs against you.
However your strength fails you as you lose hold of the bar, but just before you get sucked out, the ships AI closes the door,
saving you as you get to live another day""")
                    letter_print("You killed the Monster! Ending 3/3")
                    sys.exit("I hope you enjoyed the game :)")

            elif "closer" in a:
                letter_print("As you get closer to the Monster, it steps backwards eyeing the gun at your hip.")
                letter_print("""You tell it "I just want to help you." as you take another step towards it.
There's a first aid kit to you're right, and a knife to your right. You can save it if you decide you want to tend it's injuries.
However you're close enough to kill it with one stab if you choose to murder it.""")
                b = input(f"What do you do {user}? ").lower().strip()
                if "stab" in b:
                    letter_print("""You jump and stab it direclty in the skull and it drops dead.
You move closer to the corpse and kick it to see if it's truly dead. It is and you slowly drag to the airlock and eject it.""")
                    letter_print("You killed the Monster! Ending 3/3")
                    sys.exit("I hope you enjoyed the game :)")
                elif "aid" in b or "kit" in b:
                    letter_print("""You grab the first aid kit and move closer to the Monster to give it medical aid.
While you bandage and disinfect the wounds, the creature makes noises of pain, but it does bot attack you. After
fully patching it up it seems to have grown closer to and is no longer threat to you or you ship.""")
                    letter_print("You saved the creature! Endning 2/3")
                    sys.exit("I hope you enjoyed the game :)")
                else:
                    letter_print("That's not an option avaible to you right now.\n")

            else:
                letter_print("That's not an option avaible to you right now.\n")


def main_deck(prog: str, user):
    if prog == "main":
        while True:
            a = input(f"What do you do {user}? ").lower().strip()
            if "search" in a:
                letter_print("""You search around the room and see the weapons locker
tucked in the far left corner of the room\n""")
                b = input("Do you aproach the locker? ").lower().strip()
                if "aproach" in b or "locker" in b or "yes" in b or "y" in b:
                    letter_print("""As you get closer, you see that the locker is locked,
however you think you left the key in the cargo bay.\n""")
                else:
                    letter_print("You decide to check it out later\n")
            elif "locker" in a:
                letter_print("""As you aproach the locker, you see that it is locked,
however you think you left the key in the cargo bay.\n""")
            elif "where" in a:
                letter_print("You are in the living area.\n")
            elif "bridge" in a:
                letter_print(story_text("bridge"))
                return bridge("bridge3", user)
            elif "airlock" in a:
                letter_print(story_text("airlock2"))
                return airlock("airlock3", user)
            elif "cargo" in a:
                letter_print(story_text("cargo"))
                return cargo("cargo", user)
            elif "bedroom" in a:
                letter_print(story_text("bed"))
                return bedroom("bed2", user)
            elif "kitchen" in a:
                letter_print(story_text("kitchen"))
                return kitchen("kitchen2", user)
            else:
                letter_print("You decide to wait here to see what happens.\n")

    elif prog == "main2":
        while True:
            # add the ability to go to every room with same progress
            a = input(f"What do you do {user}? ").lower().strip()
            if "search" in a:
                letter_print("""You search around the room and see the weapons locker
tucked in the far left corner of the room\n""")
                b = input("Do you aproach the locker? ").lower().strip()
                if "aproach" in b or "locker" in b or "yes" in b or "y" in b:
                    letter_print("You aproach the weapons locker with you newly found key.\n")
                b = input("Do you unlock it? ").lower().strip()
                if "unlock" in b or "yes" in b or "y" in b:
                    letter_print("""You've unlocked it and now see an aray of different guns,
but your favorite is the laser pistol, """, end="")
                    c = input("Do you take it? ").lower().strip()
                    if "pistol" in c or "gun" in c or "take" in c or "yes" in c or "y" in c:
                        letter_print("You take the pistol and holster it to your waist.\n")
                        letter_print(story_text("final"))
                        return final_choice("gun", user)
                    else:
                        d = input("Are you sure you don't want it? (yes/no) ")
                        if "yes" in d or "y" in d:
                            letter_print("You take the pistol and holster it to your waist.\n")
                            letter_print(story_text("final"))
                            return final_choice("gun", user)
                        else:
                            letter_print("You decide you don't need it.\n")
                            letter_print(story_text("final"))
                            return final_choice("no_gun", user)
            elif "locker" in a:
                letter_print("You aproach the weapons locker with you newly found key.\n")
                b = input("Do you unlock it? ").lower().strip()
                if "unlock" in b or "yes" in b or "y" in b:
                    letter_print("""You've unlocked it and now see an aray of different guns,
but your favorite is the laser pistol, """, end="")
                    c = input("Do you take it? ").lower().strip()
                    if "pistol" in c or "gun" in c or "take" in c or "yes" in c or "y" in c:
                        letter_print("You take the pistol and holster it to your waist.\n")
                        letter_print(story_text("final"))
                        return final_choice("gun", user)
                    else:
                        d = input("Are you sure you don't want it? (yes/no) ")
                        if "yes" in d or "y" in d:
                            letter_print("You take the pistol and holster it to your waist.\n")
                            letter_print(story_text("final"))
                            return final_choice("gun", user)
                        else:
                            letter_print("You decide you don't need it.\n")
                            letter_print(story_text("final"))
                            return final_choice("no_gun", user)
            elif "where" in a:
                letter_print("You are in the living area.\n")
            elif "bridge" in a:
                letter_print(story_text("bridge"))
                return bridge("bridge3.1", user)
            elif "airlock" in a:
                letter_print(story_text("airlock2"))
                return airlock("airlock3.1", user)
            elif "cargo" in a:
                letter_print(story_text("cargo"))
                return cargo("cargo2", user)
            elif "bedroom" in a:
                letter_print(story_text("bed"))
                return bedroom("bed2.1", user)
            elif "kitchen" in a:
                letter_print(story_text("kitchen"))
                return kitchen("kitchen2.1", user)
            else:
                letter_print("You decide to wait here to see what happens.\n")


def airlock(prog: str, user):
    x = 0
    if prog == "airlock":
        for _ in range(100):
            a = input(f"What do you do {user}? ").lower().strip()
            if "repeat" in a:
                # repeats the text printed when you walk in the room
                letter_print(story_text("airlock"))
            elif "where" in a:
                letter_print("You are in the airlock.\n")
            elif "bridge" in a:
                letter_print(story_text("bridge"))
                return bridge("bridge", user)
            elif "main" in a or "living" in a:
                # takes you to the living area/room
                letter_print("The door to the living area is locked, ", end="")
                letter_print("so you head back to the airlock\n")
            elif "kitchen" in a:
                letter_print("The kitchen door is locked.\n")
                letter_print(story_text("back"))
                letter_print(back)
                return bridge("bridge", user)
            elif "bedroom" in a:
                letter_print("The bedroom door is locked.\n")
                letter_print(story_text("back"))
                letter_print(back)
                return bridge("bridge", user)
            elif "cargo" in a:
                letter_print("The cargo bay is locked, there might be backup generators somwhere.\n")
            elif "search" in a:
                letter_print("You search the room and find a panel next to each of the doors.\n")
                return door(user)
            else:
                letter_print("You're not sure how to do that.\n")
                x += 1

    elif prog == "airlock2":
        for _ in range(100):
            b = input(f"What do you do {user}? ").lower().strip()
            if "repeat" in b:
                # repeats the text printed when you walk in the room
                letter_print(story_text("airlock2"))
            elif "where" in b:
                letter_print("You are in the airlock.\n")
            elif "bridge" in b:
                letter_print(story_text("bridge"))
                return bridge("bridge2", user)
            elif "main" in b or "living" in b:
                # takes you to the living area/room
                letter_print("The door to the living area is locked,", end="")
                letter_print(" so you head back to the airlock\n")
            elif "kitchen" in b:
                letter_print("You look around the kitchen and see one of the ships backup generators.\n")
                return kitchen("kitchen", user)
            elif "bedroom" in b:
                letter_print("You look around the bedroom and see one of the ships backup generators\n")
                return bedroom("bed", user)
            elif "cargo" in b:
                letter_print("The cargo bay is locked, there might be backup generators somwhere.\n")
            elif "search" in b:
                letter_print("You've already searched the area.\n")
            else:
                letter_print("You're not sure how to do that.\n")
                x += 1

    elif prog == "airlock3":
        for _ in range(100):
            b = input(f"What do you do {user}? ").lower().strip()
            if "repeat" in b:
                # repeats the text printed when you walk in the room
                letter_print(story_text("airlock2"))
            elif "where" in b:
                letter_print("You are in the airlock.\n")
            elif "bridge" in b:
                letter_print(story_text("bridge"))
                return bridge("bridge3", user)
            elif "main" in b or "living" in b:
                letter_print("You got to the living area.\n")
                return main_deck("main", user)
            elif "kitchen" in b:
                letter_print(story_text("kitchen"))
                return kitchen("kitchen2", user)
            elif "bedroom" in b:
                letter_print(story_text("bed"))
                return bedroom("bed2", user)
            elif "cargo" in b:
                letter_print(story_text("cargo"))
                return cargo("cargo", user)
            elif "search" in b:
                letter_print("You've already searched the area.\n")
            else:
                letter_print("You're not sure how to do that.\n")
                x += 1

    elif prog == "airlock3.1":
        for _ in range(100):
            b = input(f"What do you do {user}? ").lower().strip()
            if "repeat" in b:
                # repeats the text printed when you walk in the room
                letter_print(story_text("airlock2"))
            elif "where" in b:
                letter_print("You are in the airlock.\n")
            elif "bridge" in b:
                letter_print(story_text("bridge"))
                return bridge("bridge3.1", user)
            elif "main" in b or "living" in b:
                letter_print("You got to the living area.\n")
                return main_deck("main2", user)
            elif "kitchen" in b:
                letter_print(story_text("kitchen"))
                return kitchen("kitchen2.1", user)
            elif "bedroom" in b:
                letter_print(story_text("bed"))
                return bedroom("bed2.1", user)
            elif "cargo" in b:
                letter_print(story_text("cargo"))
                return cargo("cargo2", user)
            elif "search" in b:
                letter_print("You've already searched the area.\n")
            else:
                letter_print("You're not sure how to do that.\n")
                x += 1
    if x == 100:
        letter_print("Your AI is annoyed by you standing around and shoots you out the airlock. Joke Ending 1/3")
        again = input("Restart? (yes/no)")
        if "yes" in again or "y" in again:
            return main()
        else:
            sys.exit("Bye, have a great time!")


def door(user):
    letter_print("You can open the panels and mess with the wires\n")
    while True:
        a = input(f"What do you do {user}? ").lower().strip()
        if "wire" in a or "panel" in a or "open" in a:
            letter_print("You mess with the wires in the door panels and unlock the kitchen and bedroom\n")
            return airlock("airlock2", user)
        elif "where" in a:
            letter_print("You are in the airlock in front of the door panels.\n")
        elif "back" in a:
            # steps you away from door panels
            letter_print("You step away from the door panels")
            letter_print(story_text("back"))
            return bridge("airlock", user)
        else:
            letter_print("Messings with the wires in the door panels might open the doors.\n")


def cargo(prog: str, user):
    if prog == "cargo":
        while True:
            a = input(f"What do you do {user}? ").lower().strip()
            if "repeat" in a:
                # repeats the text printed when you walk in the room
                letter_print(story_text("cargo"))
            elif "where" in a:
                letter_print("You are in the cargo bay.\n")
            elif "search" in a:
                letter_print("You scower the bay and find the key to the weapons locker, which should be in the living area.\n")
                while True:
                    b = input(f"What do you do {user}? ").lower().strip()
                    if "living" in b:
                        letter_print("You go to the living area.\n")
                        return main_deck("main2", user)
                    else:
                        letter_print("You're not sure how to do that.\n")
                        break
            elif "bridge" in a:
                letter_print(story_text("bridge"))
                return bridge("bridge3", user)
            elif "airlock" in a:
                # leave area
                letter_print(story_text("airlock2"))
                return airlock("airlock3", user)
            elif "kitchen" in a:
                letter_print(story_text("kitchen"))
                return kitchen("kitchen2", user)
            elif "bedroom" in a:
                letter_print(story_text("bed"))
                return bedroom("bed2", user)
            else:
                letter_print("You're not sure how to do that.\n")

    elif prog == "cargo2":
        while True:
            a = input(f"What do you do {user}? ").lower().strip()
            if "repeat" in a:
                # repeats the text printed when you walked in the room
                letter_print(story_text("cargo"))
            elif "where" in a:
                letter_print("You are in the cargo bay.\n")
            elif "search" in a:
                letter_print("You've already found the key.\n")
            elif "bridge" in a:
                letter_print(story_text("bridge"))
                return bridge("bridge3.1", user)
            elif "airlock" in a:
                # leave area
                letter_print(story_text("airlock2"))
                return airlock("airlock3.1", user)
            elif "kitchen" in a:
                letter_print(story_text("kitchen"))
                return kitchen("kitchen2.1", user)
            elif "bedroom" in a:
                letter_print(story_text("bed"))
                return bedroom("bed2.1", user)
            elif "living" in a:
                letter_print("You go to the living area.\n")
                return main_deck("main2", user)
            else:
                letter_print("You're not sure how to do that.\n")


def bedroom(prog: str, user):
    if prog == "bed":
        while True:
            a = input(f"What do you do {user}? ").lower().strip()
            if "repeat" in a:
                # repeats the text printed when you walked in the room
                letter_print("You look around the bedroom and see one of the ships backup generators\n")
            elif "where" in a:
                letter_print("You are in the bedroom.\n")
            elif "backup" in a or "generator" in a:
                letter_print("You move towards the generator stationed in the corner of the room\n")
                return generator(1, user)
            # leaves the area
            elif "main" in a or "living" in a:
                letter_print("The living area door is locked, you head back to the bedroom.\n")
            elif "bridge" in a:
                letter_print(story_text("bridge"))
                return bridge("bridge2", user)
            elif "airlock" in a:
                letter_print(story_text("airlock2"))
                return airlock("airlock2", user)
            elif "cargo" in a:
                letter_print("The cargo bay is locked. You head back to the bedroom.\n")
            elif "kitchen" in a:
                return kitchen("kitchen", user)
            # searches the area
            elif "search" in a:  # unlocks achievement
                letter_print("You finally found your long lost pillow, you can now sleep comfortably\n")
            elif "sleep" in a or "nap" in a:  # also unlocks achievement
                letter_print("You can't resist your bed and take a quick nap.\n")
            else:
                letter_print("You're not sure how to do that.\n")

    elif prog == "bed2":
        while True:
            a = input(f"What do you do {user}? ").lower().strip()
            if "repeat" in a:
                # repeats the text printed when you walked in the room
                letter_print(story_text("bed"))
            elif "where" in a:
                letter_print("You are in the bedroom.\n")
            elif "backup" in a or "generator" in a:
                letter_print("You've already turned them on\n")
            # leaves the area
            elif "bridge" in a:
                letter_print(story_text("bridge"))
                return bridge("bridge3", user)
            elif "main" in a or "living" in a:
                letter_print("You got to the living area.\n")
                return main_deck("main", user)
            elif "airlock" in a:
                letter_print(story_text("airlock2"))
                return airlock("airlock3", user)
            elif "kitchen" in a:
                letter_print(story_text("kitchen"))
                return kitchen("kitchen2", user)
            elif "cargo" in a:
                letter_print(story_text("cargo"))
                return cargo("cargo", user)
            # searches the area
            elif "search" in a:  # unlocks an achievement
                letter_print("You finally found your long lost pillow, you can now sleep comfortably\n")
            elif "sleep" in a or "nap" in a:  # also unlocks achievement
                letter_print("You can't resist your bed and take a quick nap.\n")
            else:
                letter_print("You're not sure how to do that.\n")

    elif prog == "bed2.1":
        while True:
            a = input(f"What do you do {user}? ").lower().strip()
            if "repeat" in a:
                # repeats the text printed when you walked in the room
                letter_print(story_text("bed"))
            elif "where" in a:
                letter_print("You are in the bedroom.\n")
            elif "backup" in a or "generator" in a:
                letter_print("You've already turned them on\n")
            # leaves the area
            elif "bridge" in a:
                letter_print(story_text("bridge"))
                return bridge("bridge3.1", user)
            elif "main" in a or "living" in a:
                letter_print("You got to the living area.\n")
                return main_deck("main2", user)
            elif "airlock" in a:
                letter_print(story_text("airlock2"))
                return airlock("airlock3.1", user)
            elif "kitchen" in a:
                letter_print(story_text("kitchen"))
                return kitchen("kitchen2.1", user)
            elif "cargo" in a:
                letter_print(story_text("cargo"))
                return cargo("cargo2", user)
            elif "search" in a:  # unlocks an achievement
                letter_print("You finally found your long lost pillow, you can now sleep comfortably\n")
            elif "sleep" in a or "nap" in a:  # also unlocks an achievement
                letter_print("You can't resist your bed and take a quick nap.\n")
            else:
                letter_print("You're not sure how to do that.\n")


def kitchen(prog: str, user):
    if prog == "kitchen":
        while True:
            a = input(f"What do you do {user}? ").lower().strip()
            if "repeat" in a:
                # repeats the text printed when you walked in the room
                letter_print("You look around the kitchen and see one of the ships backup generators\n")
            elif "where" in a:
                letter_print("You are in the kitchen.\n")
            elif "backup" in a or "generator" in a:
                letter_print("You move towards the generator stationed in the back of the room\n")
                return generator(0, user)
            # leave the area
            elif "bridge" in a:
                letter_print(story_text("bridge"))
                return bridge("bridge2", user)
            elif "main" in a or "living" in a:
                letter_print("The living area door is locked, you head back to the kitchen.\n")
            elif "airlock" in a:
                letter_print(story_text("airlock2"))
                return airlock("airlock2", user)
            elif "bedroom" in a:
                return bedroom("bed", user)
            elif "cargo" in a:
                letter_print("Cargo is locked.\n")
            # searches the area
            elif "search" in a:
                b = input("You found some chili in the fridge. Should you eat it? ").lower().strip()
                if "yes" in b or "y" in b or "eat" in b:  # should unlock achievement
                    letter_print("""You heat up the chili in your handy dandy microwave,
and after waiting for a couple minutes you eat your re-heated chili, but...it's cold in the middle\n""")
                else:
                    letter_print("You not really that hungry.\n")
            elif "food" in a:
                letter_print("You made some delicious eggs. Yum!\n")
            else:
                letter_print("You're not sure how to do that.\n")

    elif prog == "kitchen2":
        while True:
            a = input(f"What do you do {user}? ").lower().strip()
            if "repeat" in a:
                # repeats the text printed when you walked in the room
                letter_print(story_text("kitchen"))
            elif "where" in a:
                letter_print("You are in the kitchen.\n")
            elif "backup" in a or "generator" in a:
                letter_print("You've already turned them on\n")
            # leave the area
            elif "bridge" in a:
                letter_print(story_text("bridge"))
                return bridge("bridge3", user)
            elif "main" in a or "living" in a:
                letter_print("You got to the living area.\n")
                return main_deck("main", user)
            elif "airlock" in a:
                letter_print(story_text("airlock2"))
                return airlock("airlock3", user)
            elif "bedroom" in a:
                letter_print(story_text("bed"))
                return bedroom("bed2", user)
            elif "cargo" in a:
                letter_print(story_text("cargo"))
                return cargo("cargo", user)
            # search the area
            elif "search" in a:
                b = input("You found some chili in the fridge. Should you eat it? ").lower().strip()
                if "yes" in b or "y" in b or "eat" in b:  # unlocks achievement
                    letter_print("""You heat up the chili in your handy dandy microwave,
and after waiting for a couple minutes you eat your re-heated chili, but...it's cold in the middle\n""")
                else:
                    letter_print("You not really that hungry.\n")
            elif "food" in a:
                letter_print("You made a delicious burrito. Yum!\n")
            else:
                letter_print("You're not sure how to do that.\n")

    elif prog == "kitchen2.1":
        while True:
            a = input(f"What do you do {user}? ").lower().strip()
            if "repeat" in a:
                # repeats the text printed when you walked in the room
                letter_print(story_text("kitchen"))
            elif "where" in a:
                letter_print("You are in the kitchen.\n")
            elif "backup" in a or "generator" in a:
                letter_print("You've already turned them on\n")
            # leave the area
            elif "bridge" in a:
                letter_print(story_text("bridge"))
                return bridge("bridge3.1", user)
            elif "main" in a or "living" in a:
                letter_print("You got to the living area.\n")
                return main_deck("main2", user)
            elif "airlock" in a:
                letter_print(story_text("airlock2"))
                return airlock("airlock3.1", user)
            elif "bedroom" in a:
                letter_print(story_text("bed"))
                return bedroom("bed2.1", user)
            elif "cargo" in a:
                letter_print(story_text("cargo"))
                return cargo("cargo2", user)
            # search the area
            elif "search" in a:
                b = input("You found some chili in the fridge. Should you eat it? ").lower().strip()
                if "yes" in b or "y" in b or "eat" in b:  # fun little thing you can do, will unlock achievement
                    letter_print("""You heat up the chili in your handy dandy microwave,
and after waiting for a couple minutes you eat your re-heated chili, but...it's cold in the middle\n""")
                else:
                    letter_print("You not really that hungry.\n")
            elif "food" in a:
                letter_print("You made a delicious burrito. Yum!\n")
            else:
                letter_print("You're not sure how to do that.\n")


def generator(area, user):
    x = 0
    for _ in range(100):
        a = input(f"What do you do {user}? ").lower().strip()
        if "on" in a:
            letter_print(story_text("gen"))
            print(images(1))
            letter_print(story_text("cargo"))
            return cargo("cargo", user)
        elif "back" in a:
            letter_print("You step away from the generator.\n")
            if area == 1:
                return bedroom("bed", user)
            else:
                return kitchen("kitchen", user)
        else:
            letter_print("""You tinker with the generator, but it makes an ufavorable noise.
You should probably just turn it on\n""")
            x += 1
    if x == 100:
        letter_print("The backup generator explodes from you're mere existense. Joke Ending 1/2")
        again = input("Restart? (yes/no)")
        if "yes" in again or "y" in again:
            return main()
        else:
            sys.exit("Bye, have a great time!")


if __name__ == "__main__":
    main()
