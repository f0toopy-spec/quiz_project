"""
Модуль для отображения результатов и статистики.

Этот модуль предоставляет функции для форматированного вывода результатов
тестирования и расчета статистики.
"""
from typing import List, Dict, Any, Tuple


def display_results(score: int, total: int, user_answers: List[Dict]) -> None:
    """Отображает результаты тестирования в форматированном виде.

       Args:
           score: Количество правильных ответов.
           total: Общее количество вопросов.
           user_answers: История ответов пользователя.

       Example:
           >>> display_results(8, 10, user_answers)
           ==================================================
           РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ
           ==================================================
           Правильные ответы: 8/10
           Процент правильных ответов: 80.0%
           Оценка: Хорошо! 👍
       """
    percentage = (score / total) * 100 if total > 0 else 0

    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
    print("=" * 50)
    print(f"Правильные ответы: {score}/{total}")
    print(f"Процент правильных ответов: {percentage:.1f}%")

    # Оценка
    if percentage >= 90:
        grade = "Отлично! 🎉"
    elif percentage >= 75:
        grade = "Хорошо! 👍"
    elif percentage >= 60:
        grade = "Удовлетворительно 👌"
    else:
        grade = "Нужно повторить материал 📚"

    print(f"Оценка: {grade}")

    # Детальная статистика по ответам
    print("\nДетальная статистика:")
    for i, answer in enumerate(user_answers, 1):
        status = "✓" if answer['is_correct'] else "✗"
        print(f"{i}. {status} {answer['question']}")


def calculate_statistics(user_answers: List[Dict]) -> Dict[str, Any]:
    """Рассчитывает подробную статистику тестирования.

      Args:
          user_answers: История ответов пользователя.

      Returns:
          Словарь со статистикой, содержащий:
          - total_questions: Общее количество вопросов
          - correct_answers: Количество правильных ответов
          - percentage: Процент правильных ответов
          - question_types: Статистика по типам вопросов

      Example:
          >>> stats = calculate_statistics(user_answers)
          >>> print(stats['percentage'])
          80.0
      """
    if not user_answers:
        return {}

    total = len(user_answers)
    correct = sum(1 for answer in user_answers if answer['is_correct'])
    percentage = (correct / total) * 100

    # Анализ по типам вопросов (можно расширить)
    question_types = {}
    for answer in user_answers:
        q_type = "multiple_choice" if 'options' in answer else "text"
        if q_type not in question_types:
            question_types[q_type] = {'total': 0, 'correct': 0}
        question_types[q_type]['total'] += 1
        if answer['is_correct']:
            question_types[q_type]['correct'] += 1

    return {
        'total_questions': total,
        'correct_answers': correct,
        'percentage': percentage,
        'question_types': question_types
    }