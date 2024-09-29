from django.shortcuts import render
import random
import array

# Character sets for password generation
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                     'v', 'w', 'x', 'y', 'z']
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                     'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']


def generate_password(length, difficulty):
    combined_list = DIGITS + LOCASE_CHARACTERS
    if difficulty == 'medium':
        combined_list += UPCASE_CHARACTERS
    elif difficulty == 'hard':
        combined_list += UPCASE_CHARACTERS + SYMBOLS

    password = ''.join(random.choice(combined_list) for _ in range(length))
    return password


def index(request):
    password = ''
    if request.method == 'POST':
        length = int(request.POST.get('length'))
        difficulty = request.POST.get('difficulty')
        password = generate_password(length, difficulty)

    return render(request, 'password_generator/index.html', {'password': password})
