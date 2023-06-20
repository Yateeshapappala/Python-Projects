import random
from hm_guess import words
from hm_lives import game_name
from hm_lives import lives
guess_word=random.choice(words).lower()
word=len(guess_word)
game_over=False
tries=6
print(game_name)
result=[]
for i in range(word):
    result+='_'
while not game_over:
    user=input("Guess a letter: ")
    user=user.lower()
    for i in range(word):
        letter=guess_word[i]
        if letter==user:
            result[i]=letter
    if user not in guess_word:
        print("Oops, wrong guess")
        tries-=1
        if tries==0:
            game_over=True
            print("GAME OVER")
            print("U LOSE THE GAME")
    ans=' '.join(result)
    print(ans)
    if '_' not in result:
        game_over=True
        print("GAME OVER")
        print("U WON THE GAME")
    print(lives[tries])
print("the word is",guess_word)