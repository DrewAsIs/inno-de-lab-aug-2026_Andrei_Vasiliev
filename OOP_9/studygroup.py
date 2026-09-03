from trainee import Trainee


class HardworkingTrainee(Trainee):
    """
    Представляет стажера, который получает больше баллов
    за выполнение домашних заданий.
    """

    def do_homework(self) -> None:
        """Increases score by 2"""
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


class Cohort:
    """
    Представляет учебную группу учащихся.
    """

    def __init__(
        self,
        title: str,
        trainees: list[Trainee] | None = None
    ) -> None:
        """
        Создает учебную группу.

        Args:
            title(str): Название группы.
            trainees(list[Trainee] | None): Список учащихся.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.title: str = title
        self.trainees: list[Trainee] = (
            trainees if trainees is not None else []
        )

    def add_trainee(self, trainee: Trainee) -> None:
        """
        Добавляет учащегося в группу.

        Args:
            trainee(Trainee): Учащийся для добавления.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        """
        Проводит лекцию для всех учащихся группы.

        Returns:
            None: Метод ничего не возвращает.
        """
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        """
        Возвращает учащихся, прошедших курс.

        Returns:
            list[Trainee]: Список учащихся,
            прошедших курс.
        """
        return [
            trainee
            for trainee in self.trainees
            if trainee.is_passing()
        ]


def run_tests() -> None:
    """
    Выполняет тесты задания 2.

    Returns:
        None: Функция ничего не возвращает.
    """
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

    cohort = Cohort("Python Advanced")

    cohort.add_trainee(std_trainee)
    cohort.add_trainee(hard_trainee)
    cohort.add_trainee(audit_trainee)

    cohort.conduct_lecture()
    hard_trainee.do_homework()

    passing_students = cohort.get_passing_students()

    print(
        f"=== УСПЕВАЕМОСТЬ ГРУППЫ "
        f"'{cohort.title}' ==="
    )

    for student in cohort.trainees:
        print(
            f"{student.name} {student.surname} | "
            f"Баллы: {student.score} | "
            f"Проходит: {student.is_passing()}"
        )

    print("\nУспешно зачислены на следующий модуль:")

    for student in passing_students:
        print(f"- {student.name} {student.surname}")


if __name__ == "__main__":
    run_tests()