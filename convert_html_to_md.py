#!/usr/bin/env python3
import os
import base64
import requests
import markdownify
from bs4 import BeautifulSoup
import sys

# Fonction pour télécharger les images et mettre à jour les liens, y compris les images base64
def download_images_and_update_links(html_content, media_folder):
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')

    if not os.path.exists(media_folder):
        os.makedirs(media_folder)

    for img_tag in img_tags:
        img_url = img_tag.get('src')
        if img_url:
            # Si l'image est une URL complète
            if img_url.startswith('http'):
                img_name = os.path.basename(img_url)
                img_path = os.path.join(media_folder, img_name)
                
                try:
                    img_data = requests.get(img_url, timeout=10).content
                    with open(img_path, 'wb') as f:
                        f.write(img_data)
                    img_tag['src'] = os.path.join(media_folder, img_name)
                except requests.RequestException:
                    img_tag['src'] = ''  # Si l'image échoue à se télécharger
            # Si l'image est encodée en base64
            elif img_url.startswith('data:image'):
                img_data = img_url.split(',')[1]  # Extraire la partie base64
                img_bytes = base64.b64decode(img_data)  # Décoder l'image
                
                # Générer un nom de fichier unique pour l'image
                img_name = f"image_{hash(img_data)}.png"
                img_path = os.path.join(media_folder, img_name)

                # Sauvegarder l'image dans le dossier 'media'
                with open(img_path, 'wb') as f:
                    f.write(img_bytes)
                
                img_tag['src'] = os.path.join(media_folder, img_name)

    return str(soup)

# Demander à l'utilisateur le nom du fichier HTML si aucun n'est fourni
if len(sys.argv) != 2:
    print("Veuillez fournir le nom du fichier HTML à convertir.")
    sys.exit(1)

html_file = sys.argv[1]

# Vérifier que le fichier existe
if not os.path.isfile(html_file):
    print(f"Le fichier {html_file} n'existe pas.")
    sys.exit(1)

# Charger le fichier HTML
with open(html_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Télécharger les images et mettre à jour les liens
media_folder = 'media'
updated_html = download_images_and_update_links(html_content, media_folder)

# Convertir le HTML mis à jour en Markdown avec markdownify
markdown_content = markdownify.markdownify(updated_html)

# Nom du fichier Markdown de sortie
output_file = f"{os.path.splitext(html_file)[0]}.md"

# Sauvegarder le Markdown dans un fichier
with open(output_file, 'w', encoding='utf-8') as md_file:
    md_file.write(markdown_content)

print(f"Conversion terminée. Fichier Markdown sauvegardé sous '{output_file}'.")
