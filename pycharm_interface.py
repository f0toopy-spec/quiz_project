#!/usr/bin/env python3
"""
Интерфейс для работы в консоли PyCharm
"""

import os
import sys
from quizapp.commands import (
    list_tests,
    take_test,
    take_random_test,
    create_test,
    show_statistics
)


def clear_screen():
    """Очистка экрана"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    """Вывод заголовка"""
    print("=" * 50)
    print("        СИСТЕМА ТЕСТИРОВАНИЯ (QUIZ)")
    print("=" * 50)
    print()


def show_main_menu():
    """Главное меню"""
    print_header()
    print("ГЛАВНОЕ МЕНЮ:")
    print("1. 📋 Список доступных тестов")
    print("2. 🎯 Пройти тест")
    print("3. 🎲 Пройти тест со случайными вопросами")
    print("4. 📝 Создать новый тест")
    print("5. 📊 Статистика теста")
    print("6. 🚪 Выход")
    print()


def get_user_choice():
    """Получение выбора пользователя"""
    while True:
        try:
            choice = input("Выберите пункт меню (1-6): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6']:
                return choice
            else:
                print("❌ Пожалуйста, введите число от 1 до 6")
        except KeyboardInterrupt:
            print("\n\nПрограмма завершена.")
            sys.exit(0)


def select_test_file():
    """Выбор файла теста"""
    tests = []

    # Ищем тесты в папке tests
    if os.path.exists('tests'):
        for file in os.listdir('tests'):
            if file.endswith('.json'):
                tests.append(os.path.join('tests', file))

    # Ищем тесты в корневой папке
    for file in os.listdir('.'):
        if file.endswith('.json'):
            tests.append(file)

    if not tests:
        print("❌ Тесты не найдены.")
        print("Создайте тест через пункт меню 'Создать новый тест'")
        return None

    print("\nДоступные тесты:")
    for i, test_path in enumerate(tests, 1):
        try:
            from quizapp.loader import load_test
            test_data = load_test(test_path)
            title = test_data.get('title', 'Без названия')
            questions_count = len(test_data.get('questions', []))
            print(f"{i}. {title} ({questions_count} вопросов)")
        except Exception as e:
            print(f"{i}. ❌ Ошибка загрузки: {os.path.basename(test_path)}")

    print(f"{len(tests) + 1}. ↩️ Назад")

    while True:
        try:
            choice = input(f"\nВыберите тест (1-{len(tests) + 1}): ").strip()
            choice_num = int(choice)

            if 1 <= choice_num <= len(tests):
                return tests[choice_num - 1]
            elif choice_num == len(tests) + 1:
                return None
            else:
                print(f"❌ Пожалуйста, введите число от 1 до {len(tests) + 1}")
        except ValueError:
            print("❌ Пожалуйста, введите число")
        except KeyboardInterrupt:
            return None


def get_question_count():
    """Получение количества вопросов для случайного теста"""
    while True:
        try:
            count = input("\nКоличество вопросов (по умолчанию 5): ").strip()
            if not count:
                return 5
            count_num = int(count)
            if count_num > 0:
                return count_num
            else:
                print("❌ Количество должно быть положительным числом")
        except ValueError:
            print("❌ Пожалуйста, введите число")
        except KeyboardInterrupt:
            return None


def handle_list_tests():
    """Обработка пункта 'Список тестов'"""
    clear_screen()
    print_header()
    print("📋 СПИСОК ДОСТУПНЫХ ТЕСТОВ")
    print("-" * 40)
    list_tests()
    input("\nНажмите Enter для продолжения...")


def handle_take_test():
    """Обработка пункта 'Пройти тест'"""
    clear_screen()
    print_header()
    print("🎯 ПРОЙТИ ТЕСТ")
    print("-" * 40)

    test_file = select_test_file()
    if test_file:
        try:
            take_test(test_file)
        except Exception as e:
            print(f"❌ Ошибка при прохождении теста: {e}")

    input("\nНажмите Enter для продолжения...")


def handle_take_random_test():
    """Обработка пункта 'Случайный тест'"""
    clear_screen()
    print_header()
    print("🎲 ТЕСТ СО СЛУЧАЙНЫМИ ВОПРОСАМИ")
    print("-" * 40)

    test_file = select_test_file()
    if test_file:
        count = get_question_count()
        if count:
            try:
                take_random_test(test_file, count)
            except Exception as e:
                print(f"❌ Ошибка при прохождении теста: {e}")

    input("\nНажмите Enter для продолжения...")


def handle_create_test():
    """Обработка пункта 'Создать тест'"""
    clear_screen()
    print_header()
    print("📝 СОЗДАНИЕ НОВОГО ТЕСТА")
    print("-" * 40)

    try:
        create_test()
    except Exception as e:
        print(f"❌ Ошибка при создании теста: {e}")

    input("\nНажмите Enter для продолжения...")


def handle_show_statistics():
    """Обработка пункта 'Статистика'"""
    clear_screen()
    print_header()
    print("📊 СТАТИСТИКА ТЕСТА")
    print("-" * 40)

    test_file = select_test_file()
    if test_file:
        try:
            show_statistics(test_file)
        except Exception as e:
            print(f"❌ Ошибка при загрузке статистики: {e}")

    input("\nНажмите Enter для продолжения...")


def main():
    """Главная функция"""
    try:
        while True:
            clear_screen()
            show_main_menu()
            choice = get_user_choice()

            if choice == '1':
                handle_list_tests()
            elif choice == '2':
                handle_take_test()
            elif choice == '3':
                handle_take_random_test()
            elif choice == '4':
                handle_create_test()
            elif choice == '5':
                handle_show_statistics()
            elif choice == '6':
                clear_screen()
                print("Спасибо за использование системы тестирования! 👋")
                break

    except KeyboardInterrupt:
        clear_screen()
        print("Программа завершена. До свидания! 👋")
    except Exception as e:
        print(f"❌ Произошла непредвиденная ошибка: {e}")
        input("Нажмите Enter для выхода...")


if __name__ == '__main__':
    main()
