"""
Пакет системы тестирования (Quiz).

Этот пакет предоставляет функциональность для создания, загрузки
и прохождения тестов через консольный интерфейс.

Модули:
    loader: Загрузка и сохранение тестов из JSON файлов
    engine: Основная логика тестирования
    results: Вывод результатов и статистики
    commands: Обработчики команд для CLI

Основные классы:
    QuizEngine: Движок для проведения тестирования
    TestLoader: Класс для работы с файлами тестов

Основные функции:
    take_quiz: Проведение тестирования
    create_test: Создание нового теста
    list_tests: Показать доступные тесты
"""

__version__ = '1.0.0'
__author__ = 'Quiz System'

from .loader import load_test, save_test, list_available_tests
from .engine import QuizEngine, take_quiz, take_random_quiz
from .results import display_results, calculate_statistics
from .commands import (
    list_tests, take_test, take_random_test,
    create_test, show_statistics
)

__all__ = [
    'load_test',
    'save_test',
    'list_available_tests',
    'QuizEngine',
    'take_quiz',
    'take_random_quiz',
    'display_results',
    'calculate_statistics',
    'list_tests',
    'take_test',
    'take_random_test',
    'create_test',
    'show_statistics'
]