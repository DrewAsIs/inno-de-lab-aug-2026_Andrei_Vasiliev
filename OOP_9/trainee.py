class Trainee:
    """
    Представляет стажера Team.Inno
    и позволяет отслеживать его успеваемость.
    """

    def __init__(
        self,
        name: str,
        surname: str,
        score: int = 0,
        passing_grade: int = 10
    ) -> None:
        """
        Создает нового стажера с заданными параметрами.

        Args:
            name(str): Имя стажера.
            surname(str): Фамилия стажера.
            score(int): Начальный балл стажера.
            passing_grade(int): Проходной балл для завершения курса.

        Returns:
            None: Ничего не возвращает.
        """
        self.name: str = name
        self.surname: str = surname
        self.passing_grade: int = passing_grade
        self.__score: int = score

    @property
    def score(self) -> int:
        """
        Возвращает текущий балл.

        Returns:
            int: Текущий балл стажера.
        """
        return self.__score

    @score.setter
    def score(self, value: int) -> None:
        """
        Изменяет балл стажера с проверкой значения.

        Args:
            value(int): Новое значение балла.

        Returns:
            None: Метод ничего не возвращает.

        Raises:
            ValueError: Если значение не является типом int
            или является отрицательным.
        """
        if not isinstance(value, int):
            raise ValueError(
                f"Expected value of type int, got {type(value)}"
            )

        if value < 0:
            raise ValueError(
                "The score shouldn't be less than 0!"
            )

        self.__score = value

    def do_homework(self) -> None:
        """Увеличивает балл на 1."""
        self.score += 1

    def miss_homework(self) -> None:
        """Уменьшает балл на 1."""
        self.score -= 1

    def visit_lecture(self) -> None:
        """Увеличивает балл на 1."""
        self.score += 1

    def miss_lecture(self) -> None:
        """Уменьшает балл на 1."""
        self.score -= 1

    def is_passing(self) -> bool:
        """
        Проверяет, набрал ли стажер проходной балл.

        Returns:
            bool: True, если стажер прошел курс,
            иначе False.
        """
        return self.score >= self.passing_grade


print("=== ПРОВЕРКА УСПЕВАЕМОСТИ СТАЖЕРА ===")

trainee = Trainee(
    name="Иван",
    surname="Иванов",
    score=9,
    passing_grade=10
)

trainee.do_homework()
print(
    f"Баллы: {trainee.score}, "
    f"Прошел курс: {trainee.is_passing()}"
)

trainee.miss_lecture()
print(
    f"Баллы: {trainee.score}, "
    f"Прошел курс: {trainee.is_passing()}"
)

try:
    trainee.score = -5
except ValueError as error:
    print(f"Ошибка: {error}")
