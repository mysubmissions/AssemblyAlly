from django.shortcuts import render

from django.http import HttpResponse


def process_text(request):
    if request.method == 'POST':
        user_text = request.POST.get('text')
        response_text = process_input(user_text)
    else:
        response_text = ''  # Empty initial response

    context = {'response_text': response_text}
    return render(request, 'index.html', context)


def process_input(text):
    # Implement your text processing logic here
    if text.lower() == 'hy':
        return 'hello!'
    else:
        return 'I don\'t understand that.'


def index(request):
    # Render your desired content for the root page
    return render(request, 'index.html')  # Assuming an index.html template

