# ToDoList CLI

Application simple de gestion de tâches.

## Utilisation

```bash
python main.py
```

## API REST
```bash
python app.py
```
L'API tourne sur `http://127.0.0.1:5000`

## Routes API

`GET /tasks` - Liste toutes les tâches
`POST /tasks` - Ajouter une tâche
`GET /tasks/<id>` - Récupérer une tâche
`DELETE /tasks/<id>` - Supprimer une tâche

## Structure MVC

- `models/` : classe Task
- `controllers/` : logique de gestion
- `views/` : interface CLI

Les tâches sont sauvegardées dans `tasks.json`.




## Fonctionnalités

- Ajout de tâches avec titre et description
- Liste de toutes les tâches
- Marquage des tâches terminées
- Suppression de tâches
- Sauvegarde automatique
