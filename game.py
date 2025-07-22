import random

choices = ["scissors", "rock", "paper"]
player = input("Chọn scissors, rock hoặc paper: ").lower()
computer = random.choice(choices)

print(f"Máy chọn: {computer}")

if player == computer:
    print("Hòa!")
elif (player == "scissors" and computer == "paper") or \
     (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock"):
    print("Bạn thắng!")
else:
    print("Bạn thua!")