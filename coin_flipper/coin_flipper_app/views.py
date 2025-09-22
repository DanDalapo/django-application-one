from django.shortcuts import render
import random

def flip_coin(request):
    result = random.choice(['HEADS', 'TAILS'])
    context = {
        'result': result
    }
    return render(request, 'coin_flipper/index.html', context)