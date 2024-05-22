manage:
	poetry run ./manage.py $(filter-out $@,$(MAKECMDGOALS))


tailwind-start:
	poetry run ./manage.py tailwind start


runserver:
	poetry run ./manage.py runserver


dev:
	poetry run ./manage.py tailwind start & poetry run ./manage.py runserver


init:
	poetry install
	cd theme/static_src && pnpm i && cd ../..
	poetry run ./manage.py migrate


seed:
	poetry run ./manage.py seeddb


wipe:
	rm db.sqlite3
	poetry run ./manage.py migrate


wipe-seed:
	make wipe
	make seed


%:
	@: