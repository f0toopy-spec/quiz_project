import os
import json
from .loader import TestLoader, list_available_tests
from .engine import take_quiz, take_random_quiz
from .results import display_results, calculate_statistics


def list_tests():
    """Показывает список доступных тестов"""
    tests = list_available_tests()

    if not tests:
        print("Тесты не найдены.")
        print("Создайте тест с помощью команды: python main.py --create-test")
        return

    print("Доступные тесты:")
    for i, test_path in enumerate(tests, 1):
        try:
            test_data = TestLoader.load_test(test_path)
            title = test_data.get('title', 'Без названия')
            questions_count = len(test_data.get('questions', []))
            print(f"{i}. {title} ({questions_count} вопросов) - {test_path}")
        except Exception as e:
            print(f"{i}. Ошибка загрузки: {test_path} ({e})")


def take_test(test_file: str):
    """Запускает прохождение теста"""
    if not os.path.exists(test_file):
        print(f"Файл теста не найден: {test_file}")
        return

    try:
        score, total, user_answers = take_quiz(test_file)
        display_results(score, total, user_answers)
    except Exception as e:
        print(f"Ошибка при прохождении теста: {e}")


def take_random_test(test_file: str, count: int):
    """Запускает прохождение теста со случайными вопросами"""
    if not os.path.exists(test_file):
        print(f"Файл теста не найден: {test_file}")
        return

    try:
        score, total, user_answers = take_random_quiz(test_file, count)
        display_results(score, total, user_answers)
    except Exception as e:
        print(f"Ошибка при прохождении теста: {e}")


def create_test():
    """Создает новый тест через консоль"""
    print("Создание нового теста")
    print("=" * 30)

    title = input("Введите название теста: ").strip()
    if not title:
        print("Название теста не может быть пустым.")
        return

    questions = []

    while True:
        print(f"\n--- Вопрос {len(questions) + 1} ---")
        question_text = input("Введите текст вопроса: ").strip()

        if not question_text:
            print("Текст вопроса не может быть пустым.")
            continue

        question_type = input("Тип вопроса (1 - с вариантами, 2 - текстовый): ").strip()

        if question_type == '1':
            # Вопрос с вариантами ответов
            options = []
            print("Введите варианты ответов (пустая строка для завершения):")

            while True:
                option = input(f"Вариант {len(options) + 1}: ").strip()
                if not option:
                    if len(options) < 2:
                        print("Нужно как минимум 2 варианта ответа.")
                        continue
                    break
                options.append(option)

            print("Варианты ответов:")
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")

            correct_option = input("Номер правильного варианта: ").strip()
            try:
                correct_index = int(correct_option) - 1
                if 0 <= correct_index < len(options):
                    correct_answer = options[correct_index]
                else:
                    print("Неверный номер варианта.")
                    continue
            except ValueError:
                print("Введите число.")
                continue

            questions.append({
                'question': question_text,
                'options': options,
                'answer': correct_answer
            })

        else:
            # Текстовый вопрос
            correct_answer = input("Правильный ответ: ").strip()
            if not correct_answer:
                print("Правильный ответ не может быть пустым.")
                continue

            questions.append({
                'question': question_text,
                'answer': correct_answer
            })

        add_more = input("Добавить еще вопрос? (y/n): ").strip().lower()
        if add_more != 'y':
            break

    test_data = {
        'title': title,
        'description': input("Описание теста (необязательно): ").strip(),
        'questions': questions
    }

    # Сохранение теста
    file_name = input("Имя файла для сохранения (например: my_test.json): ").strip()
    if not file_name.endswith('.json'):
        file_name += '.json'

    # Добавляем папку tests если указано просто имя файла
    if not os.path.dirname(file_name):
        file_name = os.path.join('tests', file_name)

    try:
        TestLoader.save_test(test_data, file_name)
        print(f"Тест успешно сохранен в файл: {file_name}")
    except Exception as e:
        print(f"Ошибка при сохранении теста: {e}")


def show_statistics(test_file: str):
    """Показывает статистику теста"""
    if not os.path.exists(test_file):
        print(f"Файл теста не найден: {test_file}")
        return

    try:
        test_data = TestLoader.load_test(test_file)
        questions_count = len(test_data.get('questions', []))

        print(f"Статистика теста: {test_data.get('title', 'Без названия')}")
        print(f"Количество вопросов: {questions_count}")
        print(f"Описание: {test_data.get('description', 'Не указано')}")

        # Анализ типов вопросов
        multiple_choice = 0
        text_questions = 0

        for question in test_data.get('questions', []):
            if 'options' in question:
                multiple_choice += 1
            else:
                text_questions += 1

        print(f"Вопросы с вариантами ответов: {multiple_choice}")
        print(f"Текстовые вопросы: {text_questions}")

    except Exception as e:
        print(f"Ошибка при загрузке статистики: {e}")