# calculator_app/views.py
from django.shortcuts import render
from django.http import HttpResponse


def calculator(request):
    if request.method == 'POST':
        try:
            # Get user input from the form
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            operator = request.POST.get('operator')

            # Perform the calculation
            if operator == 'add':
                result = num1 + num2
            elif operator == 'subtract':
                result = num1 - num2
            elif operator == 'multiply':
                result = num1 * num2
            elif operator == 'divide':
                result = num1 / num2
            else:
                result = 'Invalid operator'
        except Exception as e:
            result = 'Error: ' + str(e)

        return render(request, 'calculator_app/calculator.html', {'result': result})

    return render(request, 'calculator_app/calculator.html')
