from django.shortcuts import render
import subprocess
from django.http import JsonResponse
import threading
import subprocess


def home(request):
    return render(request, 'index.html')

# Python (Django view)
import subprocess

def run_code(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        language = request.POST.get('language', '')
        try:
            if language.lower() == 'html':
                # Открываем HTML файл в браузере
                with open('output.html', 'w') as f:
                    f.write(code)
                subprocess.run(['xdg-open', 'output.html'])  # Замените 'xdg-open' на команду, подходящую для вашей операционной системы
                return JsonResponse({'output': 'HTML code executed successfully'})
            else:
                # Выполняем код на других языках
                result = subprocess.run(['python', '-c', code], capture_output=True, text=True, timeout=5)
                output = result.stdout
                if output:
                    return JsonResponse({'output': output})
                elif result.stderr:
                    return JsonResponse({'output': result.stderr})
                else:
                    return JsonResponse({'output': 'No output'})
        except subprocess.TimeoutExpired:
            return JsonResponse({'output': 'Timeout: Process execution took too long'})
        except Exception as e:
            return JsonResponse({'output': 'Error: ' + str(e)})
    return JsonResponse({'error': 'Method not allowed'}, status=405)


def doc(request):
    return render(request, 'doc.html')