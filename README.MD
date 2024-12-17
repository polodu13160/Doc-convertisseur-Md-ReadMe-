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
