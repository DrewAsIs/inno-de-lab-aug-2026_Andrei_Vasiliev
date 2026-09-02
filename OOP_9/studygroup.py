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
            None: Метод ничего не возвращает.
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


class HardworkingTrainee(Trainee):
    """
    Представляет стажера, который получает больше баллов
    за выполнение домашних заданий.
    """

    def do_homework(self) -> None:
        """Увеличивает балл на 2."""
        self.score += 2


class AuditTrainee(Trainee):
    """
    Представляет вольнослушателя, который всегда
    считается успешно прошедшим курс.
    """

    def is_passing(self) -> bool:
        """
        Проверяет статус вольнослушателя.

        Returns:
            bool: Всегда возвращает True.
        """
        return True


class StudyGroup:
    """
    Представляет учебную группу и управляет списком стажеров.
    """

    def __init__(
        self,
        title: str,
        trainees: list[Trainee] | None = None
    ) -> None:
        """
        Создает учебную группу.

        Args:
            title(str): Название учебной группы.
            trainees(list[Trainee] | None): Список учащихся.
            По умолчанию создается пустой список.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.title: str = title
        self.trainees: list[Trainee] = (
            trainees if trainees is not None else []
        )

    def add_trainee(self, trainee: Trainee) -> None:
        """
        Добавляет стажера в учебную группу.

        Args:
            trainee(Trainee): Стажер, которого нужно добавить.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        """
        Проводит лекцию для всех стажеров группы.

        Returns:
            None: Метод ничего не возвращает.
        """
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        """
        Возвращает список стажеров, прошедших курс.

        Returns:
            list[Trainee]: Список стажеров, у которых
            метод is_passing() возвращает True.
        """
        return [
            trainee
            for trainee in self.trainees
            if trainee.is_passing()
        ]


std_trainee = Trainee(
    "Алексей",
    "Смирнов",
    score=8,
    passing_grade=10
)

hard_trainee = HardworkingTrainee(
    "Елена",
    "Петрова",
    score=8,
    passing_grade=10
)

audit_trainee = AuditTrainee(
    "Дмитрий",
    "Сидоров",
    score=0,
    passing_grade=10
)

study_group = StudyGroup("Python Advanced")

study_group.add_trainee(std_trainee)
study_group.add_trainee(hard_trainee)
study_group.add_trainee(audit_trainee)

study_group.conduct_lecture()

hard_trainee.do_homework()

passing_students = study_group.get_passing_students()

print(f"=== УСПЕВАЕМОСТЬ ГРУППЫ '{study_group.title}' ===")

for student in study_group.trainees:
    print(
        f"{student.name} {student.surname} | "
        f"Баллы: {student.score} | "
        f"Проходит: {student.is_passing()}"
    )

print("\nУспешно зачислены на следующий модуль:")

for student in passing_students:
    print(f"- {student.name} {student.surname}")
