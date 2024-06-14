import random
import day7_hang_data

game_word = random.choice(day7_hang_data.words)
word_len = len(game_word)

steps_out=[]

for dash in range(word_len):
    steps_out += "_"
print(steps_out)

lives = 6
end=0

while not end:
    gusse = input("Guess a letter: ").lower()
    for positon in range(word_len):
        letter = game_word[positon]
        if letter == gusse:
            steps_out[positon]=letter
            ###################
    if gusse not in steps_out:
        lives-=1
        print(f"You have {lives} guesses left.")
        if lives == 0:
            end = True
            print("you lose")
            ###################
    print(steps_out)
            ###################
    if "_" not in steps_out:
        end=True
        print("yeah you win!!")

    print(day7_hang_data.hangman[lives])
    print("***************************************************************")

print(game_word)