import os
import subprocess
import sys


def run_tests():
    """Запуск Django тестів"""
    print("🛠 Виконання тестів...")
    result = subprocess.run(["python3", "manage.py", "test"], capture_output=True, text=True)
    print(result.stdout)
    
    if result.returncode != 0:
        print("❌ Помилки в тестах:")
        print(result.stderr)
        sys.exit(1)  # Завершуємо програму, якщо тести не пройшли
    else:
        print("✅ Усі тести успішно пройдені.")


if __name__ == "__main__":
    try:
        run_tests()  # Запускаємо тести перед сервером
    except subprocess.CalledProcessError as e:
        print(f"❌ Помилка під час виконання команди: {e}")
        sys.exit(1)
