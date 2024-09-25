# Create your views here.
from django.shortcuts import render

def remove_vowels(request):
    result = ""
    if request.method == 'POST':
        input_text = request.POST.get('text', '')
        vowels = "aeiouAEIOU"
        result = ''.join([char for char in input_text if char not in vowels])

    return render(request, 'remove_vowels_app/index.html', {'result': result})

def test_view(request):
    return render(request, 'test.html')
