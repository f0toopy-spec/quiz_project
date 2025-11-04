import random
from typing import Dict, List, Any, Tuple
from .loader import load_test


class QuizEngine:
    """Движок для проведения тестирования"""

    def __init__(self, test_data: Dict[str, Any]):
        self.test_data = test_data
        self.title = test_data.get('title', 'Без названия')
        self.questions = test_data.get('questions', [])
        self.current_question = 0
        self.score = 0
        self.total_questions = len(self.questions)
        self.user_answers = []

    def get_random_questions(self, count: int) -> List[Dict[str, Any]]:
        """
        Выбирает случайные вопросы из теста

        Args:
            count: Количество вопросов

        Returns:
            Список случайных вопросов
        """
        if count > len(self.questions):
            count = len(self.questions)

        return random.sample(self.questions, count)

    def display_question(self, question: Dict[str, Any]) -> None:
        """
        Отображает вопрос и варианты ответов

        Args:
            question: Данные вопроса
        """
        print(f"\n{question['question']}")

        if 'options' in question:
            for i, option in enumerate(question['options'], 1):
                print(f"{i}. {option}")

    def check_answer(self, question: Dict[str, Any], user_answer: str) -> bool:
        """
        Проверяет ответ пользователя

        Args:
            question: Данные вопроса
            user_answer: Ответ пользователя

        Returns:
            True если ответ правильный, иначе False
        """
        correct_answer = question.get('answer', '').lower().strip()
        user_answer = user_answer.lower().strip()

        # Для вопросов с вариантами ответов
        if 'options' in question:
            try:
                option_index = int(user_answer) - 1
                if 0 <= option_index < len(question['options']):
                    selected_option = question['options'][option_index].lower()
                    return selected_option.startswith(correct_answer)
            except ValueError:
                pass

        # Для текстовых вопросов
        return user_answer == correct_answer

    def take_quiz(self, questions: List[Dict[str, Any]] = None) -> Tuple[int, int, List[Dict]]:
        """
        Проводит тестирование

        Args:
            questions: Список вопросов (если None, используются все вопросы)

        Returns:
            Кортеж (количество правильных ответов, общее количество вопросов, история ответов)
        """
        if questions is None:
            questions = self.questions

        self.score = 0
        self.user_answers = []

        print(f"\n=== Тест: {self.title} ===")
        print(f"Количество вопросов: {len(questions)}")

        for i, question in enumerate(questions, 1):
            print(f"\n--- Вопрос {i} из {len(questions)} ---")
            self.display_question(question)

            while True:
                try:
                    user_input = input("Ваш ответ: ").strip()
                    if user_input:
                        break
                    print("Пожалуйста, введите ответ.")
                except KeyboardInterrupt:
                    print("\n\nТестирование прервано.")
                    return self.score, len(questions), self.user_answers

            is_correct = self.check_answer(question, user_input)

            if is_correct:
                self.score += 1
                print("✓ Правильно!")
            else:
                correct_answer = question.get('answer', 'Не указан')
                print(f"✗ Неправильно. Правильный ответ: {correct_answer}")

            # Сохраняем историю ответов
            self.user_answers.append({
                'question': question['question'],
                'user_answer': user_input,
                'correct_answer': question.get('answer', ''),
                'is_correct': is_correct
            })

        return self.score, len(questions), self.user_answers


def take_quiz(test_file: str) -> Tuple[int, int, List[Dict]]:
    """Функция для проведения тестирования"""
    test_data = load_test(test_file)
    engine = QuizEngine(test_data)
    return engine.take_quiz()


def take_random_quiz(test_file: str, question_count: int = 5) -> Tuple[int, int, List[Dict]]:
    """Функция для проведения тестирования со случайными вопросами"""
    test_data = load_test(test_file)
    engine = QuizEngine(test_data)
    random_questions = engine.get_random_questions(question_count)
    return engine.take_quiz(random_questions)