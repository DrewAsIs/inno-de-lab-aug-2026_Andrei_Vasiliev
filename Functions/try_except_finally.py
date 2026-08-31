from typing import Any
DEFAULT_RETURN_INDEX_BASE = 10.0
def calculate_overdue_fine(
    film_title: str,
    days_overdue: Any,
    fine_rate: Any
) -> tuple[float, float] | None:
    try:
        numeric_days = float(days_overdue)
        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days
        return total_fine, return_index
    except TypeError as error:
        print(
            f"[ОШИБКА ТИПА] Некорректный тип данных для "
            f"'{film_title}': {error}"
        )
    except ValueError as error:
        print(
            f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число "
            f"для '{film_title}': {error}"
        )
    except ZeroDivisionError as error:
        print(
            f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки "
            f"для '{film_title}': {error}"
        )
    finally:
        print("--- Проверка транзакции возврата завершена ---")
print("=== ПРОВЕРКА ВОЗВРАТОВ ===")
result1 = calculate_overdue_fine("Matrix", 5, 1.5)
if result1 is not None:
    print(
        f"Фильм: 'Matrix' | "
        f"Итоговый штраф: {result1[0]}$ | "
        f"Индекс: {result1[1]}"
    )
result2 = calculate_overdue_fine("Inception", "пять", 2.0)
result3 = calculate_overdue_fine("Avatar", 0, 2.5)
result4 = calculate_overdue_fine("Interstellar", [3], 3.0)