import random
from django.shortcuts import render

def generate_password(request):
    password = None  # Initialize password variable

    if request.method == 'POST':
        # Get form data
        nr_letters = int(request.POST.get('nr_letters', 0))
        nr_symbols = int(request.POST.get('nr_symbols', 0))
        nr_numbers = int(request.POST.get('nr_numbers', 0))

        # Generate the password using the provided code
        password = generate_random_password(nr_letters, nr_symbols, nr_numbers)

    # Render the template with the generated password
    return render(request, 'password_app/index.html', {'password': password})

def generate_random_password(nr_letters, nr_symbols, nr_numbers):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

    password_list = []
    for l in range(nr_letters):
        password_list.append(random.choice(letters))
    for s in range(nr_symbols):
        password_list.append(random.choice(symbols))
    for n in range(nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    return ''.join(password_list)


