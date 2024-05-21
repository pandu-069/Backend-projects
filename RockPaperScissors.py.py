import random
from gtts import gTTS
import pygame
import io
import speech_recognition as sr


def audio_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Rock or paper or scissors")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for noise levels
        audio = recognizer.listen(source)  # Capture the audio
        print("user choice locked")

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        textt = list(text.split())[0]
        return textt

        # Save the recognized text to a file
    except sr.UnknownValueError:
        print("Sorry, could not understand your words")
        print("Can you repeat it again")
        text_to_speech("Sorry, could not understand your words")
        text_to_speech("Can you repeat it again")
    except sr.RequestError as e:
        print(f"Error occurred; {e}")


def text_to_speech(text):
    tts = gTTS(text=text, lang='en')

    # Save the speech to a BytesIO object
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)

    # Initialize Pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(audio_data, 'mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


print("Welcome to rock paper scissors game")
flag = True
print("1.Rock 2.Paper 3.Scissors 4.Exit the game")
text_to_speech('The correct pronunciation is rock paper and scissors')
computer_score = 0
user_score = 0
computer_inputs = ['rock', 'paper', 'scissors']
while flag:

    print("Enter your choice: ")
    user_input = audio_to_text()
    print("user : ", user_input)
    computer_input = random.randrange(0, 3)
    if user_input == 'rock':
        if computer_inputs[computer_input].lower() == "rock":
            print("computer: Rock")
            text_to_speech('rock')
            print("Same choice so no scores")
            continue
        elif computer_inputs[computer_input].lower() == "paper":
            text_to_speech('paper')
            print("computer: paper ")
            computer_score += 1
            print("Now computer score is ", computer_score)
        elif computer_inputs[computer_input].lower() == "scissors":
            text_to_speech('scissors')
            print("Computer: Scissors")
            user_score += 1
            print("Now score of user is : ", user_score)

    elif user_input == 'paper':
        if computer_inputs[computer_input] == "rock":
            text_to_speech('rock')
            print("computer: Rock")
            user_score += 1
            print("Now user score is ", user_score)
        elif computer_inputs[computer_input] == "paper":
            text_to_speech('paper')
            print("computer: paper ")
            print("Same choice so no scores")
            continue
        elif computer_inputs[computer_input] == "scissors":
            text_to_speech('scissors')
            print("Computer: Scissors")
            computer_score += 1
            print("Now score of computer is : ", computer_score)

    elif user_input == 'scissors':
        if computer_inputs[computer_input] == "rock":
            text_to_speech('rock')
            print("computer: Rock")
            computer_score += 1
            print("Now computer score is ", computer_score)

        elif computer_inputs[computer_input] == "paper":
            text_to_speech('paper')
            print("computer: paper ")
            user_score += 1
            print("Now score of user is : ", user_score)

        elif computer_inputs[computer_input] == "scissors":
            text_to_speech('scissors')
            print("Computer: Scissors")
            print("Same choice so no scores")
            continue

    elif user_input == 'exit':
        print("The game is ending")
        text_to_speech('The Game is ending')
        flag = False
    else:
        text_to_speech('Invalid input' + str(user_input))

print("Now Scoreboard is: ")
print("Computer score: ", computer_score)
text_to_speech("computer score is" + str(computer_score))
print("User score: ", user_score)
text_to_speech("and user score is" + str(user_score))
if computer_score > user_score:
    print("Computer won the game")
    print("Better luck next time")
    text_to_speech("Computer won the game")
    text_to_speech('Better luck next time')
    print("Run the program to play again")
elif user_score > computer_score:
    print("Congratulations! You Won the game")
    text_to_speech('Congratulations')
    text_to_speech('You won the game')
    print("To play again run the program")
else:
    print("Both has same score")
    print("----------------------------------- Tie ------------------------------------------------")
    text_to_speech('The Game is tied')


def read_count():
    try:
        with open("countt.txt", "r") as file:
            countt = int(file.read())
    except FileNotFoundError:
        # If file doesn't exist, initialize count to 0
        countt = 0
    return countt


def write_count(countt):
    with open("countt.txt", "w") as file:
        file.write(str(countt))


countt = read_count()
countt += 1
write_count(countt)

with open('Results.txt', 'a') as a:
    a.write("\n" + str(countt) + ". computer score: " + str(computer_score) + " User score: " + str(user_score) + "\n")

print("Do you want to see the results of all the previous games (Yes / No)")
text_to_speech("Do you want to see the results of all the previous games")
inputt = input().lower()
if inputt == "yes":
    with open('Results.txt', 'r') as file:
        fill = file.read()
    print(fill)

else:
    exit(0)
