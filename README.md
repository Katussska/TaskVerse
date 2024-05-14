# TaskVerse

TaskVerse is a web application built using Django framework that enables users to manage their projects 
and tasks. Users can create projects, add tasks to them, assign priorities, tags, team members, track progress and 
collaborate with team members through comments.

### Key Features:
- **Project Management**: Create, update, and delete projects.
- **Task Tracking**: Add tasks to projects, set priorities, mark them as completed, etc.
- **User Collaboration**: Engage in discussions and share insights with team members through comments.
- **Intuitive Interface**: User-friendly design for easy navigation.

TaskVerse is a school project aimed at familiarizing with the Django framework and web application development.

## Setup

- make sure poetry installed

```bash
poetry install
cd theme/static_src && pnpm i && cd ../..
poetry run ./manage.py migrate

# run tailwind file watcher in the background
poetry run ./manage.py tailwind start

# run project or run using PyCharm/IDEA
poetry run ./manage.py runserver
```

### TODO

- [x] tailwindcss
- [ ] lucide
- [x] preline UI
- [ ] preline UI js
- [ ] ruff