"""
Пакет системы тестирования (Quiz)
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