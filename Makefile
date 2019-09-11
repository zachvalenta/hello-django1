.PHONY: test

help:
	@echo
	@echo "🎸 DJANGO"
	@echo
	@echo "dj:          run dev server"
	@echo "index:       hit index page"
	@echo "gui:         open site in browser"
	@echo
	@echo "📦 DEPENDENCIES"
	@echo
	@echo "freeze:      freeze dependencies into requirements.txt"
	@echo "install:     install dependencies from requirements.txt"
	@echo "purge:       remove any installed pkg *not* in requirements.txt"
	@echo

dj:
	python manage.py runserver

index:
	http --print=Hh http://127.0.0.1:8000

gui:
	open http://localhost:8000/

freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

purge:
	@echo "🔍 - DISCOVERING UNSAVED PACKAGES\n"
	pip freeze > pkgs-to-rm.txt
	@echo
	@echo "📦 - UNINSTALL ALL PACKAGES\n"
	pip uninstall -y -r pkgs-to-rm.txt
	@echo
	@echo "♻️  - REINSTALL SAVED PACKAGES\n"
	pip install -r requirements.txt
	@echo
	@echo "🗑  - UNSAVED PACKAGES REMOVED\n"
	diff pkgs-to-rm.txt requirements.txt | grep '<'
	@echo
	rm pkgs-to-rm.txt
	@echo
