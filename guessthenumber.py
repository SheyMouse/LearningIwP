### A small game about guessing a number
import random

turnCount = 0

print('Hello. Please tell me your name: ')
name = input('>>> ')

print('Welcome ' + name +'!')
print('I am thinking of a number between 1 and 20.')
print('You have five guesses.')
print(' ')

number = random.randint(1, 20)

while turnCount < 5:
    print('Take a guess.')
    guess = input('>>> ')
    guess = int(guess)
    
    turnCount = turnCount + 1
    
    if guess < number:
        print('Your guess is too low.')
    
    if guess > number:
        print('Your guess is too high.')
    
    if guess == number:
        break

if guess == number:
    number = str(number)
    turnCount = str(turnCount)
    print('Well done ' + name + '! ')
    print('You guessed that the number is ' + number + ' in ' + turnCount + ' guesses.')
    
if guess != number:
    number = str(number)
    print('You ran out of guesses. The number I was thinking of was ' + number + '.')
    
    
