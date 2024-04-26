# instagram_middleware.py

from django.shortcuts import redirect

class InstagramMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:  # Проверка аутентификации пользователя
            # Если пользователь не аутентифицирован, перенаправляем его на страницу Instagram подписки
            return redirect('https://www.instagram.com/big_code_official/')
        
        # Если пользователь аутентифицирован, просто передаем запрос дальше
        return self.get_response(request)
