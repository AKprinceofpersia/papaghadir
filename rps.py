import random

rps = ["rock","paper","scissor"]
print("be barname sang kaghaz gheychi khosh omadid:)")
print("bein",rps,"yeki ro taip konid(1.rock 2.paper 3.scissor)")
Player = rps[int(input("addad ra vared konid: "))]
PC = random.choice(rps)
print("1")
print("2")
print("3")
print(PC)

if Player == "rock" and PC == "scissor":
    print("barande shodid!")
elif Player == "paper" and PC == "scissor":
    print("bakhtid!")
elif Player == "rock" and PC == "paper":
    print("bakhtid!")
elif Player == "scissor" and PC == "paper":
    print("barande shodid!")
elif Player == "scissor" and PC == "rock":
    print("bakhtid!")
elif Player == "paper" and PC == "rock":
    print("barande shodid!")
else:
    print("mosavi shodid:)")
