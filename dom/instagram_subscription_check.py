import requests

def check_instagram_subscription(username):
    try:
        # Запрос к Instagram API для получения данных о пользователе
        response = requests.get(f"https://www.instagram.com/{username}/?__a=1")
        response.raise_for_status()  # Проверка на ошибки в ответе

        # Получение данных из JSON ответа
        data = response.json()

        # Проверка наличия данных пользователя и количества подписчиков
        if 'graphql' in data and 'user' in data['graphql'] and 'edge_follow' in data['graphql']['user']:
            follows_count = data['graphql']['user']['edge_follow']['count']
            # Предположим, что если количество подписчиков больше нуля, пользователь подписан
            return follows_count > 0
        else:
            # Если данные неполные, считаем, что пользователь не подписан
            return False
    except requests.RequestException as e:
        print("Ошибка при отправке запроса:", e)
        return False

# Пример использования функции
username = 'big_code_official'
is_subscribed = check_instagram_subscription(username)
if is_subscribed:
    print(f"Пользователь подписан на @{username}")
else:
    print(f"Пользователь не подписан на @{username}")

