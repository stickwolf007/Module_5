import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return hash(self.password)

    def __str__(self):
        return f'{self.nickname}'


    def __eq__(self, other):
        return self.nickname == other.nickname




class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    users = []
    videos = []
    current_user = None
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == i.nickname and password == i.password:
                self.current_user = i
    def register(self, nickname, password, age):
        for i in self.users:
            if nickname in i.nickname:
                print(f'Пользователь {nickname} уже существует')
                break
        else:
            i = User(nickname,password,age)
            self.users.append(i)
            self.log_out()
            self.log_in(i.nickname, i.password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            self.videos.append(i)

    def get_videos(self, get):
        poisk = []
        for i in self.videos:
            if get.lower() in i.title.lower():
                poisk.append(i.title)
        return poisk

    def watch_video(self, text):
        if self.current_user is None:
            print(f'Войдите в аккаунт, чтобы смотреть видео')
        elif self.current_user.age < 18:
            print(f'Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            for i in self.videos:
                if text in i.title:
                        for j in range(1, i.duration + 1):
                            time.sleep(1)
                            print(j)
                        print(f'Конец Видео')






ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 1, adult_mode=True)

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