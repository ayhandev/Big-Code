from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .forms import InfaForm
from .models import infa
import subprocess
from django.contrib.auth.decorators import login_required
from django.conf import settings



@login_required(login_url='users/sign_in')
def home(request):
    languages = [{'code': code, 'name': name} for code, name in settings.LANGUAGES]
    return render(request, 'index.html', {'languages': languages})

def run_code(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        language = request.POST.get('language', '')
        try:
            if language.lower() == 'html':

                with open('output.html', 'w') as f:
                    f.write(code)
                subprocess.run(['xdg-open', 'output.html'])  
                return JsonResponse({'output': 'HTML code executed successfully'})
            else:
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

# from django.utils.translation import activate

# def set_language(request):
#     if 'language' in request.GET:
#         language = request.GET['language']
#         activate(language)
#     return redirect(request.GET.get('next', '/'))

def helo(request):
    infa_objects = infa.objects.all()
    return render(request, 'helo.html', {'infa_objects': infa_objects})

def delete_infa(request, infa_id):
    infa_obj = get_object_or_404(infa, pk=infa_id)  
    if request.method == 'POST':
        infa_obj.delete()
        return redirect('dom:helo')
    return render(request, 'confirm_delete.html', {'infa': infa_obj})


@staff_member_required
def submit_infa(request):
    if request.method == 'POST':
        form = InfaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dom:helo')  
    else:
        form = InfaForm()
    return render(request, 'helo.html', {'form': form})





