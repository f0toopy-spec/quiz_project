#!/usr/bin/env python3
"""
Тестирование докстрингов проекта.
"""

import quizapp
from quizapp.loader import TestLoader, load_test
from quizapp.engine import QuizEngine
from quizapp.results import display_results


def test_help():
    """Тестирует отображение документации через help()."""

    print("=== Тестирование докстрингов ===\n")

    print("1. Модуль quizapp:")
    help(quizapp)

    print("\n" + "=" * 50 + "\n")

    print("2. Класс TestLoader:")
    help(TestLoader)

    print("\n" + "=" * 50 + "\n")

    print("3. Функция load_test:")
    help(load_test)

    print("\n" + "=" * 50 + "\n")

    print("4. Класс QuizEngine:")
    help(QuizEngine)

    print("\n" + "=" * 50 + "\n")

    print("5. Функция display_results:")
    help(display_results)


if __name__ == '__main__':
    test_help()
