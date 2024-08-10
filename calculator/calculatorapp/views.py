from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def result(request):
    num1 = float(request.GET.get('number1'))
    num2 = float(request.GET.get('number2'))

    if request.GET.get('addition') == "":
        ans = num1 + num2

    elif request.GET.get('soustraction') == "":
        ans = num1 - num2

    elif request.GET.get('multiplication') == "":
        ans = num1 * num2

    else:
        ans = num1 / num2

    return render(request, 'result.html', {'ans': ans})