#!/usr/bin/env python3
"""
Главный модуль системы тестирования.

Этот модуль предоставляет интерфейс командной строки для системы тестирования.
Использует argparse для обработки аргументов командной строки и делегирует
выполнение команд модулям пакета quizapp.

Примеры использования:
    python main.py --list-tests
    python main.py --take-test tests/math_test.json
    python main.py --mixed-tests tests/math_test.json tests/programming_test.json
"""
import argparse
import sys
from quizapp.commands import (
    list_tests,
    take_test,
    take_random_test,
    create_test,
    show_statistics
)


def main():
    """Главная функция, обрабатывающая аргументы командной строки.

      Функция создает парсер аргументов, обрабатывает ввод пользователя
      и вызывает соответствующие функции из пакета quizapp.

      Raises:
          SystemExit: Завершает программу с кодом 1 в случае ошибки.
      """
    parser = argparse.ArgumentParser(
        description='Система тестирования (Quiz)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Главный модуль системы тестирования.

Этот модуль предоставляет интерфейс командной строки для системы тестирования.
Использует argparse для обработки аргументов командной строки и делегирует
выполнение команд модулям пакета quizapp.

Примеры использования:
    python main.py --list-tests
    python main.py --take-test tests/math_test.json
    python main.py --mixed-tests tests/math_test.json tests/programming_test.json
"""

    )

    parser.add_argument('--list-tests', action='store_true',
                        help='Показать список доступных тестов')

    parser.add_argument('--take-test', type=str,
                        help='Пройти указанный тест')

    parser.add_argument('--take-random', type=str,
                        help='Пройти тест со случайными вопросами')

    parser.add_argument('--count', type=int, default=5,
                        help='Количество случайных вопросов (по умолчанию: 5)')

    parser.add_argument('--create-test', action='store_true',
                        help='Создать новый тест')

    parser.add_argument('--stats', type=str,
                        help='Показать статистику теста')

    args = parser.parse_args()

    try:
        if args.list_tests:
            list_tests()
        elif args.take_test:
            take_test(args.take_test)
        elif args.take_random:
            take_random_test(args.take_random, args.count)
        elif args.create_test:
            create_test()
        elif args.stats:
            show_statistics(args.stats)
        else:
            parser.print_help()

    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()