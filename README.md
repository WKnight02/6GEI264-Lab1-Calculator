# 6GEI264-Lab1-Calculator
### Laboratoire de 6GEI264

Pour executer le programme, il faut disposer de `python3` avec `tkinter`, il suffit ensuite d'exécuter "Calculatrice.pyw" et le programme devrait se lancer.
Il est possible de créer un raccourci pointant sur ce ficher.

*Astuce*: `Echap` permet de reset la calculatrice si des entrées ont été faites, et un second appui ferme l'application.

Les tests unitaires sont dans le dossier `tests`.
Pour exécuter les tests, soit exécuter `UnitTest.bat`, soit avec la commande suivante:

```bash
python -m unittest
```

Les versions au format HTML de la documentation se situent dans le dossier `documentation`.
Pour regénérer la doc, soit exécuter `PyDoc.bat`, soit avec la commande suivante:

```bash
python -m pydoc -w modules.calcCore
python -m pydoc -w modules.calcInterface
```