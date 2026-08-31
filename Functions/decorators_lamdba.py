from typing import Callable, Any
import time

PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8

def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
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
def get_sorted_report(data: list[dict[str, str | float]]) -> list[dict[str, str | float]]:
    return sorted(
        data,
        key=lambda item: item["total_sales"],
        reverse=True
    )

print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")
data1 = [
    {"category": "Action", "total_sales": 4311.85},
    {"category": "Animation", "total_sales": 4656.30},
    {"category": "Children", "total_sales": 3655.55}
]
print("--- ТЕСТ 1 ---")
result1 = get_sorted_report(data1)
print("Топ категорий по выручке:")
for index, item in enumerate(result1, start=1):
    print(
        f"{index}. {item['category']}: {item['total_sales']}"
    )
data2 = [
    {"category": "Classics", "total_sales": 1200.10},
    {"category": "Comedy", "total_sales": 4000.00},
    {"category": "Documentary", "total_sales": 4000.00}
]
print("--- ТЕСТ 2 ---")
result2 = get_sorted_report(data2)
print("Топ категорий по выручке:")
for index, item in enumerate(result2, start=1):
    print(
        f"{index}. {item['category']}: {item['total_sales']}"
    )
data3 = [
    {"category": "Drama", "total_sales": 500.00}
]
print("--- ТЕСТ 3 ---")
result3 = get_sorted_report(data3)
print("Топ категорий по выручке:")
for index, item in enumerate(result3, start=1):
    print(f"{index}. {item['category']}: {item['total_sales']}")