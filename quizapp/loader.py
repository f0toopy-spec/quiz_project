import json
import os
from typing import Dict, List, Any
import glob


class TestLoader:
    """Класс для загрузки и сохранения тестов"""

    @staticmethod
    def load_test(file_path: str) -> Dict[str, Any]:
        """
        Загружает тест из JSON файла

        Args:
            file_path: Путь к файлу теста

        Returns:
            Словарь с данными теста

        Raises:
            FileNotFoundError: Если файл не найден
            json.JSONDecodeError: Если файл содержит некорректный JSON
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                test_data = json.load(file)

            # Валидация структуры теста
            required_fields = ['title', 'questions']
            for field in required_fields:
                if field not in test_data:
                    raise ValueError(f"Отсутствует обязательное поле: {field}")

            return test_data

        except FileNotFoundError:
            raise FileNotFoundError(f"Файл теста не найден: {file_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Ошибка чтения JSON файла: {e}")
        except Exception as e:
            raise Exception(f"Ошибка загрузки теста: {e}")

    @staticmethod
    def save_test(test_data: Dict[str, Any], file_path: str) -> None:
        """
        Сохраняет тест в JSON файл

        Args:
            test_data: Данные теста
            file_path: Путь для сохранения файла
        """
        try:
            # Создаем директорию, если она не существует
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(test_data, file, ensure_ascii=False, indent=2)

        except Exception as e:
            raise Exception(f"Ошибка сохранения теста: {e}")

    @staticmethod
    def list_available_tests() -> List[str]:
        """
        Возвращает список доступных тестов

        Returns:
            Список путей к файлам тестов
        """
        test_patterns = [
            'tests/*.json',
            '*.json'
        ]

        tests = []
        for pattern in test_patterns:
            tests.extend(glob.glob(pattern))

        return tests


# Создаем функции-обертки для удобного импорта
def load_test(file_path: str) -> Dict[str, Any]:
    """Загружает тест из JSON файла"""
    return TestLoader.load_test(file_path)


def save_test(test_data: Dict[str, Any], file_path: str) -> None:
    """Сохраняет тест в JSON файл"""
    TestLoader.save_test(test_data, file_path)


def list_available_tests() -> List[str]:
    """Возвращает список доступных тестов"""
    return TestLoader.list_available_tests()