from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .forms import InfaForm, PublishedCodeForm, MessengerForm
from .models import infa, PublishedCode, Comment, Like, Messenger
import subprocess
from django.contrib.auth.decorators import login_required
from django.conf import settings



def loader(request):
    return render(request, 'loader.html')

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
    user = request.user
    profile = None

    if user.is_authenticated:  
        profile = user.profile

    return render(request, 'doc.html', {'profile': profile})

# from django.utils.translation import activate

# def set_language(request):
#     if 'language' in request.GET:
#         language = request.GET['language']
#         activate(language)
#     return redirect(request.GET.get('next', '/'))


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from users.models import Profile

from django.contrib.auth.models import AnonymousUser

def helo(request):
    infa_objects = infa.objects.all()
    user = request.user
    if not isinstance(user, AnonymousUser):
        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=user)
    else:
        profile = None

    return render(request, 'helo.html', {'infa_objects': infa_objects, 'profile': profile})

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


@login_required
def publish_code_submit(request):

    if request.method == 'POST':
        form = PublishedCodeForm(request.POST)
        if form.is_valid():
            user = request.user
            published_code = form.save(commit=False)
            published_code.user = user
            published_code.save()
            return redirect('dom:public_list')
    else:
        form = PublishedCodeForm()
    return render(request, 'publication.html', {'form': form})

def public_view(request):
    user = request.user
    profile = None
    if user.is_authenticated:  
        profile = user.profile

    return render(request, 'publication.html', {'profile': profile })

def public_list(request):
    public = PublishedCode.objects.all()
    user = request.user
    profile = None
    if user.is_authenticated:  
        profile = user.profile
    return render(request, 'publication_list.html', {"public": public, 'profile': profile })


def add_comment(request, post_id):
    if request.method == 'POST':
        content = request.POST.get('comment')
        user = request.user
        published_code = PublishedCode.objects.get(pk=post_id)
        comment = Comment.objects.create(user=user, published_code=published_code, content=content)
    return redirect('dom:public_list')

def add_like(request, post_id):
    if request.method == 'POST':
        user = request.user
        published_code = PublishedCode.objects.get(pk=post_id)
        like, created = Like.objects.get_or_create(user=user, published_code=published_code)
        if not created:
            like.delete()  
    return redirect('dom:public_list')


@login_required
def messenger(request):
    user = request.user
    profile = None
    if user.is_authenticated: 
        profile = user.profile
        if request.method == 'POST':
            form = MessengerForm(request.POST)
            if form.is_valid():
                messenger = form.save(commit=False)
                messenger.user = request.user  
                messenger.save()
                return redirect('dom:messenger')
        else:
            form = MessengerForm()
        
        messages = Messenger.objects.all()
        for message in messages:
            message.content = message.get_content()  
    return render(request, 'messenger.html', {'messages': messages, 'form': form, 'profile': profile})

