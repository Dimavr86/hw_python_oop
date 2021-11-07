class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type, duration, distance, speed, calories):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
    pass


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    M_IN_KM = 1000
    H_IN_M = 60
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
                 self.action = action
                 self.duration = duration
                 self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = action * LEN_STEP / M_IN_KM
        return distance 

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = distance / duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training) -> float:
    """Тренировка: бег."""
    def __init__(self):
        coeff_cal_1 = 18
        coeff_cal_2 = 20
        calories = (coeff_cal_1 * self.get_mean_speed(self) - coeff_cal_2) * weight / M_IN_KM * duration * H_IN_M 
    return calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self, height):
        self.height = height
        coeff_cal_wlk_1 = 0.035
        coeff_cal_wlk_1 = 0.029
        calories = (coeff_cal_wlk_1 * weight + (speed // height) * weight) * duration * H_IN_M
    return calories


class Swimming(Training):
    """Тренировка: плавание."""

    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    dict = {
        'SWM' : Swimming(data),
        'RUN' : Running(data),
        'WLK' : SportsWalking(data)
    }
    return dict[workout_type]


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

