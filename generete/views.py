from django.shortcuts import render
import random
import string


def generate_password(length, symbols=False, numbers=False, lowercase=False, uppercase=False):
    chars = ''
    error = []
    if symbols:
        chars += string.punctuation
    if numbers:
        chars += string.digits
    if lowercase:
        chars += string.ascii_lowercase
    if uppercase:
        chars += string.ascii_uppercase



        password = ''.join(random.choice(chars) for _ in range(length))
        return password


def TestView(request):

    symbols = request.GET.get('symbols')
    numbers = request.GET.get('numbers')
    lowercase = request.GET.get('lowercase')
    uppercase = request.GET.get('uppercase')
    length = int(request.GET.get('length', 10))

    if symbols or numbers or lowercase or uppercase:
        password = generate_password(length, symbols, numbers, lowercase, uppercase)
        return render(request, 'index.html', {'password': password})




    return render(request, 'index.html')
