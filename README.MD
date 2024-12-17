Voici le contenu actuel de votre fichier README.MD :

---

Ce script effectue la conversion d'un fichier HTML (exporté depuis un autre format comme .odt) en un fichier Markdown tout en téléchargeant les images contenues dans le HTML et en les sauvegardant localement.

1. **Exporter le fichier en HTML** : Avant d'exécuter le script, exportez votre fichier dans un format HTML à partir de votre éditeur ou application (par exemple, LibreOffice, OpenOffice, etc.).
2. **Chargement du fichier HTML** : Le script prend en entrée un fichier HTML (passé en argument via la ligne de commande).
3. **Téléchargement des images** :
   - Si une image est référencée par une URL (commençant par http), elle est téléchargée et enregistrée dans un dossier `media`.
   - Si une image est encodée en base64, elle est extraite, décodée et sauvegardée en tant que fichier image dans le dossier `media`.
4. **Mise à jour des liens d'images** : Les liens d'images dans le HTML sont mis à jour pour pointer vers les images téléchargées ou décodées dans le dossier `media`.
5. **Conversion HTML en Markdown** : Le contenu HTML mis à jour est ensuite converti en Markdown en utilisant la bibliothèque `markdownify`.
6. **Sauvegarde du Markdown** : Le résultat est sauvegardé dans un fichier `.md` avec le même nom que le fichier HTML d'entrée, mais avec l'extension `.md`.

### Dépendances nécessaires :
- `markdownify` : Pour convertir le contenu HTML en Markdown.
  - Installable via : `pip install markdownify`
- `BeautifulSoup` (de `bs4`) : Pour analyser et manipuler le contenu HTML (rechercher et extraire les images).
  - Installable via : `pip install beautifulsoup4`
- `requests` : Pour télécharger les images à partir des URLs.
  - Installable via : `pip install requests`
- `base64` : Cette bibliothèque est incluse nativement dans Python et est utilisée pour décoder les images encodées en base64.

### Utilisation :
1. Exportez le fichier à convertir en HTML depuis votre éditeur de texte ou votre logiciel de traitement de texte (par exemple, LibreOffice ou OpenOffice).
2. Placez le fichier HTML exporté dans le même dossier que le script ou donnez son chemin complet.
3. Exécutez le script en ligne de commande avec l'argument du fichier HTML :
   ```bash
   python3 convert_html_to_md.py "nom_du_fichier.html"
   ```
4. Le script crée un dossier `media` dans lequel toutes les images seront sauvegardées.
5. Le fichier Markdown converti sera créé dans le même dossier que le fichier d'entrée.
6. Le script prend en charge les images locales (encodées en base64) et les images externes en les téléchargeant et en les référençant correctement dans le Markdown généré.

---
Voici un résumé clair et concis à inclure dans un fichier `.md` :  

---

# Script d'installation pour créer une commande personnalisée

Ce script vous permet de transformer n'importe quel fichier exécutable en une commande utilisable depuis votre terminal en quelques étapes simples.

## Fonctionnalités

1. Copie un fichier exécutable (Python, Bash, etc.) dans le dossier `~/scripts`.
2. Rend le fichier exécutable.
3. Crée un alias dans votre configuration Zsh (`~/.zshrc`) pour exécuter facilement le fichier depuis le terminal.

## Utilisation

1. Lancez le script depuis votre terminal :
   ```bash
   ./setup_convert_to_md.sh
   ```

2. Répondez aux questions posées :
   - **Chemin du fichier exécutable** : Entrez le chemin absolu ou relatif du fichier que vous souhaitez transformer en commande.
   - **Nom de l'exécutable** : Indiquez le nom sous lequel le fichier sera enregistré dans `~/scripts`.
   - **Nom de l'alias** : Spécifiez le nom de la commande que vous souhaitez utiliser.

3. Rechargez la configuration Zsh pour activer l'alias immédiatement :
   ```bash
   source ~/.zshrc
   ```

## Exemple

Si vous voulez transformer un script Python `convert_html_to_md.py` situé dans `~/Documents` en une commande `converthtmltomd`, voici le processus :

- Entrez le chemin : `/home/votre_utilisateur/Documents/convert_html_to_md.py`.
- Entrez le nom de l'exécutable : `converthtmltomd`.
- Entrez le nom de l'alias : `converthtmltomd`.

Après exécution, vous pourrez utiliser votre script directement en tapant :  
```bash
converthtmltomd
```

## Remarques

- Le dossier `~/scripts` est automatiquement créé si nécessaire.
- Si l'alias existe déjà dans `~/.zshrc`, il ne sera pas écrasé.
- Pour activer un nouvel alias sans redémarrer votre terminal, exécutez :
  ```bash
  source ~/.zshrc
  ```

## Dépendances

- **Shell Zsh** (le script ajoute un alias dans `~/.zshrc`).
- Les permissions suffisantes pour copier des fichiers et modifier la configuration Zsh.

--- 

Ce fichier `.md` contient tout ce qu'il faut pour comprendre et utiliser le script. 😊
