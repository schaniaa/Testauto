import random

def guess_the_number():
    # Slumpa ett tal mellan 1 och 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Välkommen till 'Gissa numret'!")
    print("Jag har valt ett nummer mellan 1 och 100. Kan du gissa vilket det är?")

    while not guessed:
        # Be spelaren att gissa ett nummer
        try:
            guess = int(input("Gissa ett nummer: "))
            attempts += 1

            if guess < number_to_guess:
                print("För lågt! Försök igen.")
            elif guess > number_to_guess:
                print("För högt! Försök igen.")
            else:
                guessed = True
                print(f"Grattis! Du gissade rätt nummer {number_to_guess} på {attempts} försök!")
        except ValueError:
            print("Var god ange ett giltigt nummer.")

# Starta spelet
guess_the_number()
