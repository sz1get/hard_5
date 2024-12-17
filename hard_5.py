from time import sleep

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age = age
        self.password = hash(password)

    def __str__(self):
        return f'{self.nickname}'


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users:
            if hash(password) in self.users[nickname]:
                self.current_user = User

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname in user.nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь {nickname} вошел в систему')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)
            else:
                continue

    def get_videos(self, text):
        list_videos = []
        for video in self.videos:
            if text.lower() in video.title.lower():
                list_videos.append(video.title)
        return list_videos

    def watch_video(self,movie):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        elif self.current_user and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            for video in self.videos:
                if movie in video.title:
                    for i in range(1, video.duration + 1):
                        print(i, end=" ")
                    sleep(1)
                    print("Конец видео")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)



 # Добавление видео
ur.add(v1, v2)

 # Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

 # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

 # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

 # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')




