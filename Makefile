.PHONY: install run lint format clean

# Установка зависимостей и настройка окружения
install:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -U pip && pip install -r requirements.txt
	@echo "Environment setup complete. Don't forget to run 'source .venv/bin/activate'"

# Запуск Jupyter Notebook сервера
run:
	. .venv/bin/activate && jupyter notebook

# Проверка кода линтером (Ruff)
lint:
	. .venv/bin/activate && ruff check .

# Автоматическое форматирование кода
format:
	. .venv/bin/activate && ruff check --fix .
	. .venv/bin/activate && ruff format .

# Очистка временных файлов
clean:
	rm -rf .venv
	rm -rf .pytest_cache
	rm -rf **/.ipynb_checkpoints
	rm -rf **/__pycache__
