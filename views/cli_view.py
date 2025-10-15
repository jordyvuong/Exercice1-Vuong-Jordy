class CLIView:

    @staticmethod
    def show_menu():
        print("\n" + "-"*50)
        print("         TODOLIST - MENU PRINCIPAL")
        print("-"*50)
        print("1. Ajouter une tâche")
        print("2. Lister les tâches")
        print("3. Marquer une tâche comme terminée")
        print("4. Supprimer une tâche")
        print("5. Quitter")
        print("-"*50)

    @staticmethod
    def ask_choice():
        return input("Votre choix : ")

    @staticmethod
    def ask_title():
        return input("Titre de la tâche : ")

    @staticmethod
    def ask_description():
        return input("Description (optionnel) : ")

    @staticmethod
    def ask_id():
        return int(input("ID de la tâche : "))

    @staticmethod
    def show_tasks(tasks):
        if not tasks:
            print("\nAucune tâche pour le moment.")
            return

        print("\n" + "-"*50)
        print("         LISTE DES TÂCHES")
        print("-"*50)
        for task in tasks:
            print(task)
        print("-"*50)

    @staticmethod
    def show_message(message):
        print(f"\n{message}")

    @staticmethod
    def show_error(message):
        print(f"\nErreur : {message}")
