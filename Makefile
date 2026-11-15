.PHONY: install db-up db-down backend frontend check test

install:
	cd backend && uv sync --all-groups
	cd frontend && npm ci

db-up:
	docker compose up -d db

db-down:
	docker compose down

backend:
	cd backend && uv run python manage.py runserver 127.0.0.1:8000

frontend:
	cd frontend && npm run dev

check:
	cd backend && uv run python manage.py check
	cd backend && uv run python manage.py makemigrations --check --dry-run
	cd backend && uv run ruff check .
	cd frontend && npm run lint
	cd frontend && npm run typecheck

test:
	cd backend && uv run pytest -q
	cd frontend && npm test

