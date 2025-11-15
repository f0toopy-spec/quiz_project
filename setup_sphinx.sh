#!/bin/bash
# setup_sphinx.sh

echo "=== Настройка Sphinx для генерации документации ==="

# Установка Sphinx и темы
pip3 install sphinx sphinx-rtd-theme

# Создаем директорию для документации
mkdir -p docs
cd docs

# Инициализируем Sphinx
sphinx-quickstart --sep -p "Quiz System" -a "Quiz Developer" -v "1.0" -r "1.0" -l "ru" --extensions "sphinx.ext.autodoc","sphinx.ext.napoleon","sphinx.ext.viewcode" --makefile --no-batchfile

echo "✅ Sphinx инициализирован"

# Создаем конфигурацию для автоматической документации
cat > conf.py << 'EOF'
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Quiz System'
copyright = '2024, Quiz Developer'
author = 'Quiz Developer'

release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

autodoc_member_order = 'groupwise'
napoleon_google_docstring = True
napoleon_include_init_with_doc = True
EOF

echo "✅ Конфигурация создана"

# Создаем индекс с автоматической документацией
cat > index.rst << 'EOF'
.. Quiz System documentation master file, created by
   sphinx-quickstart on Sun Dec 1 2024.

Документация Quiz System
========================

Quiz System - это система тестирования с консольным интерфейсом, написанная на Python.

.. toctree::
   :maxdepth: 2
   :caption: Содержание:

   modules

Индексы и таблицы
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
EOF

# Создаем файл для автоматической документации модулей
cat > modules.rst << 'EOF'
Модули Quiz System
==================

.. toctree::
   :maxdepth: 4

   main
   quizapp

EOF

# Создаем документацию для main.py
cat > main.rst << 'EOF'
main
====

.. automodule:: main
   :members:
   :undoc-members:
   :show-inheritance:
EOF

# Создаем документацию для пакета quizapp
cat > quizapp.rst << 'EOF'
quizapp
=======

.. automodule:: quizapp
   :members:
   :undoc-members:
   :show-inheritance:

Подмодули
---------

.. toctree::
   :maxdepth: 1

   quizapp.loader
   quizapp.engine
   quizapp.results
   quizapp.commands
EOF

# Создаем документацию для подмодулей
for module in loader engine results commands; do
    cat > quizapp.$module.rst << EOF
quizapp.$module
===============

.. automodule:: quizapp.$module
   :members:
   :undoc-members:
   :show-inheritance:
EOF
done

echo "✅ Файлы документации созданы"

# Генерируем HTML документацию
make html

echo "✅ HTML документация сгенерирована в docs/_build/html/"

# Пытаемся сгенерировать PDF (если установлен LaTeX)
if command -v pdflatex &> /dev/null; then
    make latexpdf
    echo "✅ PDF документация сгенерирована в docs/_build/latex/"
else
    echo "⚠️  LaTeX не установлен, PDF документация не сгенерирована"
    echo "Для генерации PDF установите texlive-latex-recommended"
fi

echo ""
echo "📖 Документация доступна в:"
echo "   HTML: docs/_build/html/index.html"
echo "   Откройте в браузере: firefox docs/_build/html/index.html"