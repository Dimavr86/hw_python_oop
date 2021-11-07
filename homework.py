class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(
        self,
        training_type: str,
        duration: float,
        distance: float,
        speed: float,
        calories: float
        ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


class Training:
    """Базовый класс тренировки."""
    workout_type: str = ''
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    H_IN_M: int = 60

    def __init__(
                self,
                action: int,
                duration: float,
                weight: float,) -> None:
                self.action = action
                self.duration = duration
                self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = self.get_distance() / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        message = InfoMessage(
                            self.workout_type,
                            self.duration,
                            self.get_distance(),
                            self.get_mean_speed(),
                            self.get_spent_calories()
                            )
        return message


class Running(Training):
    """Тренировка: бег."""
    workout_type: str = 'Running'

    def __init__(self, action, duration, weight):
        super().__init__(action, duration, weight)

    def get_spent_calories(self):
        coeff_cal_1 = 18
        coeff_cal_2 = 20
        calories = ((coeff_cal_1 *
                    self.get_mean_speed() - coeff_cal_2)
                    * self.weight / self.M_IN_KM
                    * self.duration * self.H_IN_M)
        return calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    workout_type: str = 'SportsWalking'

    def __init__(self, action, duration, weight, height):
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self):
        coeff_cal_wlk_1: float = 0.035
        coeff_cal_wlk_2: float = 0.029
        calories = ((coeff_cal_wlk_1 * self.weight +
                    (self.get_mean_speed() // self.height)
                    * coeff_cal_wlk_2 * self.weight)
                    * self.duration * self.H_IN_M)
        return calories


class Swimming(Training):
    """Тренировка: плавание."""
    workout_type: str = 'Swimming'
    LEN_STEP: float = 1.38

    def __init__(
                self,
                action: int,
                duration: float,
                weight: float,
                length_pool: float,
                count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.lenght_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        speed = (self.lenght_pool * self.count_pool /
                self.M_IN_KM / self.duration)
        return speed

    def get_spent_calories(self) -> float:
        coeff_cal_swm_1: float = 1.1
        coeff_cal_swm_2: float = 2
        calories = (
                    (self.get_mean_speed() + coeff_cal_swm_1) *
                    coeff_cal_swm_2 * self.weight)
        return calories

    def get_distance(self):
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    dict = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    if workout_type in dict:
        return dict[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    show_info = info.get_message()
    print(show_info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
