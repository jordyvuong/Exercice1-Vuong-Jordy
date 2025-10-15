from controllers.task_controller import TaskController
from views.cli_view import CLIView

def main():
    controller = TaskController()
    view = CLIView()

    while True:
        view.show_menu()
        choice = view.ask_choice()

        if choice == "1":
            title = view.ask_title()
            description = view.ask_description()
            task = controller.add_task(title, description)
            view.show_message(f"Tâche ajoutée avec succès (ID: {task.id})")

        elif choice == "2":
            tasks = controller.list_tasks()
            view.show_tasks(tasks)

        elif choice == "3":
            try:
                task_id = view.ask_id()
                if controller.mark_completed(task_id):
                    view.show_message("Tâche marquée comme terminée")
                else:
                    view.show_error("Tâche introuvable")
            except ValueError:
                view.show_error("ID invalide")

        elif choice == "4":
            try:
                task_id = view.ask_id()
                if controller.delete_task(task_id):
                    view.show_message("Tâche supprimée avec succès")
                else:
                    view.show_error("Tâche introuvable")
            except ValueError:
                view.show_error("ID invalide")

        elif choice == "5":
            view.show_message("Au revoir")
            break

        else:
            view.show_error("Choix invalide")

if __name__ == "__main__":
    main()
