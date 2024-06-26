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
make init
# seed DB (optional)
make seed
# setup in intellij
# - add python target `manage.py` w/ poetry env
# - command argumets `runserver`
# - run tailwind preprocessor:
make tailwind-start
# OR just run:
make dev
```

- for other available commands check `Makefile`

### TODO

- [x] tailwindcss
- [ ] lucide
- [x] preline UI
- [ ] preline UI js
- [x] ruff