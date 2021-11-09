from dataclasses import dataclass
from typing import ClassVar


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


@dataclass
class Training:
    """Базовый класс тренировки."""
    action: int
    duration: float
    weight: float
    LEN_STEP: ClassVar[float] = 0.65
    M_IN_KM: ClassVar[int] = 1000
    M_IN_H: ClassVar[int] = 60

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
            type(self).__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories())
        return message


class Running(Training):
    K_CAL_1: float = 18
    K_CAL_2: float = 20

    def get_spent_calories(self):
        calories = ((self.K_CAL_1
                    * self.get_mean_speed() - self.K_CAL_2)
                    * self.weight / self.M_IN_KM
                    * self.duration * self.M_IN_H)
        return calories


@dataclass
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    height: float
    K_CAL_WLK_1: ClassVar[float] = 0.035
    K_CAL_WLK_2: ClassVar[float] = 0.029

    def get_spent_calories(self):
        calories = ((self.K_CAL_WLK_1 * self.weight
                    + (self.get_mean_speed() ** 2 // self.height)
                    * self.K_CAL_WLK_2 * self.weight)
                    * self.duration * self.M_IN_H)
        return calories


@dataclass
class Swimming(Training):
    """Тренировка: плавание."""
    length_pool: float
    count_pool: int
    LEN_STEP: ClassVar[float] = 1.38
    K_CAL_SWM_1: ClassVar[float] = 1.1
    K_CAL_SWM_2: ClassVar[float] = 2

    def get_mean_speed(self) -> float:
        speed = (
            self.length_pool
            * self.count_pool
            / self.M_IN_KM
            / self.duration
        )
        return speed

    def get_spent_calories(self) -> float:
        calories = (
            (self.get_mean_speed() + self.K_CAL_SWM_1)
            * self.K_CAL_SWM_2 * self.weight)
        return calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    exercise_type = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    if workout_type not in exercise_type:
        raise Exception("Тип тренировки неизвестен")
    return exercise_type[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    show_info = info.get_message()
    print(show_info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180])
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
