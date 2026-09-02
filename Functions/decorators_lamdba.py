from typing import Any, Callable
import time


PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8


def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Эта функция измеряет время выполнения другой функции
    и выводит результат измерения.

    Args:
        func(Callable[..., Any]): Функция, время выполнения которой
        необходимо измерить.

    Returns:
        Callable[..., Any]: Обёрнутая функция с измерением
        времени выполнения.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Эта функция выполняет исходную функцию
        и измеряет время её выполнения.

        Args:
            args(Any): Позиционные аргументы исходной функции.
            kwargs(Any): Именованные аргументы исходной функции.

        Returns:
            Any: Результат выполнения исходной функции.
        """
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        print(
            f"{PERFORMANCE_LOG_PREFIX} "
            f"Функция '{func.__name__}' выполнена "
            f"за {execution_time:.{TIME_DECIMALS}f} сек."
        )

        return result

    return wrapper


@performance_logger
def get_sorted_report(
    data: list[dict[str, str | float]]
) -> list[dict[str, str | float]]:
    """
    Эта функция сортирует категории по общей выручке
    в порядке убывания.

    Args:
        data(list[dict[str, str | float]]): Список категорий
        с указанием их общей выручки.

    Returns:
        list[dict[str, str | float]]: Отсортированный список
        категорий.
    """
    return sorted(
        data,
        key=lambda item: item["total_sales"],
        reverse=True
    )


def test_report(
    test_number: int,
    data: list[dict[str, str | float]]
) -> None:
    """
    Эта функция выполняет тест сортировки
    и выводит результаты.

    Args:
        test_number(int): Номер выполняемого теста.
        data(list[dict[str, str | float]]): Данные категорий
        для тестирования.

    Returns:
        None: Ничего не возвращает.
    """
    print(f"--- ТЕСТ {test_number} ---")
    result = get_sorted_report(data)

    print("Топ категорий по выручке:")

    for index, item in enumerate(result, start=1):
        print(
            f"{index}. {item['category']}: {item['total_sales']}"
        )


print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")

data1 = [
    {"category": "Action", "total_sales": 4311.85},
    {"category": "Animation", "total_sales": 4656.30},
    {"category": "Children", "total_sales": 3655.55}
]

data2 = [
    {"category": "Classics", "total_sales": 1200.10},
    {"category": "Comedy", "total_sales": 4000.00},
    {"category": "Documentary", "total_sales": 4000.00}
]

data3 = [
    {"category": "Drama", "total_sales": 500.00}
]

test_report(1, data1)
test_report(2, data2)
test_report(3, data3)
