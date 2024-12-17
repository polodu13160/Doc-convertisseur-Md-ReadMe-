#!/bin/bash

# Demande le chemin du fichier exécutable
read -p "Entrez le chemin absolu ou relatif du fichier exécutable : " EXECUTABLE_PATH

# Vérifie si le fichier existe
if [ ! -f "$EXECUTABLE_PATH" ]; then
    echo "Erreur : Le fichier $EXECUTABLE_PATH est introuvable."
    exit 1
fi

# Demande le nom que l'utilisateur souhaite donner au fichier une fois copié
read -p "Entrez le nom que vous voulez donner à l'exécutable (ex: my_script): " EXECUTABLE_NAME

# Demande le nom de l'alias
read -p "Entrez le nom de l'alias que vous voulez créer (ex: myalias): " ALIAS_NAME

# Dossier cible pour l'exécutable
TARGET_DIR="$HOME/scripts"

# Fichier de configuration Zsh
ZSHRC="$HOME/.zshrc"

# Crée le dossier ~/scripts s'il n'existe pas
if [ ! -d "$TARGET_DIR" ]; then
    mkdir -p "$TARGET_DIR"
    echo "Dossier $TARGET_DIR créé."
fi

# Copie le fichier exécutable dans ~/scripts et lui donne le nom spécifié
TARGET_SCRIPT="$TARGET_DIR/$EXECUTABLE_NAME"
cp "$EXECUTABLE_PATH" "$TARGET_SCRIPT"
echo "Fichier $EXECUTABLE_PATH copié et renommé en $TARGET_SCRIPT."

# Rend le fichier exécutable
chmod +x "$TARGET_SCRIPT"
echo "Fichier rendu exécutable."

# Ajoute un alias dans ~/.zshrc
if ! grep -q "alias $ALIAS_NAME=" "$ZSHRC"; then
    echo "alias $ALIAS_NAME='$TARGET_SCRIPT'" >> "$ZSHRC"
    echo "Alias '$ALIAS_NAME' ajouté dans $ZSHRC."
else
    echo "L'alias '$ALIAS_NAME' existe déjà dans $ZSHRC."
fi

# Affiche le message de succès
echo "L'alias '$ALIAS_NAME' a été créé avec succès !"
echo "Pour l'utiliser immédiatement, rechargez votre terminal ou exécutez :"
echo "  source ~/.zshrc"
