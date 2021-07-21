print("Welcome to Alcatraz, by Smith of Eak! Version 0.1")

Level = 1
print("Level 1! You awake in a small room. Ahead of you is a door. A sign next to it reads: \"Enter, if you dare.\"")

while Level == 1:
    Move = input()
    if Move.capitalize() == "Enter door":
        print("You enter the door...")
        input()
        Level = 2
    elif Move.capitalize() == "Enter":
        print("Enter what?")
    else:
        print("I don't know what that means.")

print("Level 2! In this room, there is a safe. The dial goes from 1 to 60. Type a number to try it on the safe.")
while Level == 2:
    Move = input()
    if int(Move) == 11:
        print("You turn the dial to " + Move + " and try the handle. The safe pops open! Inside is a message, saying...")
        input()
        Level = 3
    elif int(Move) > 11:
        print("You turn the dial to " + Move + " and try the handle. No luck. You feel like it should be lower.")
    elif int(Move) < 11:
        print("You turn the dial to " + Move + " and try the handle. No luck. You feel like it should be higher.")
    else:
        print("I don't know what that means.")

print("Level 3! Ahead of you is a large sphinx. You walk up to her."
      "\n\"Greetings, mortal.\" she replies."
      "\n\"Hello there!\" you reply, \"is there any way I could get past you?\""
      "\n\"To pass, you mu-\" The sphinx yawns abruptly, then continues."
      "\n\"To pass, you must answer my riddle:\""
      "\n"
      "\n\"What walks on four feet in the morning, two feet at noon, and three feet in the evening?\"")
SphinxAsleep = 1
while Level == 3:
    Move = input()
    if SphinxAsleep < 3:
        print("You think for a bit, and declare your answer: \"" + Move.capitalize() + "\"! you shout.")
        if Move.capitalize() == "Man":
            print("\nThe sphinx hesitates for a second and nods her head slowly, right before collapsing"
                  "\nto the ground. Thunderous snoring sounds come from her.")
            SphinxAsleep = 3
            Level = 4
        else:
            print("\"Hmm...\" the sphinx thinks, yawns, and thinks some more. \"That's not quite right, try again.\"")
            SphinxAsleep = SphinxAsleep + 1
    else:
        print("As you begin to move your mouth to say your answer, the sphinx collapses to the ground."
              "\nThunderous snoring sounds come from her.")
        SphinxAsleep = 3
        Level = 4

print("\nThe sphinx is asleep! Victory is yours! More coming soon(TM)")
Level = 4
input()