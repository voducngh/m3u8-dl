#!/usr/bin/python3

# m3u8-dl.py
# to install : 
#   pip install BeautifulSoup
#   sudo apt install ffmpeg
#

import sys
import re
import subprocess
import requests
from bs4 import BeautifulSoup
import time

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename).strip()

def get_time_in_seconds(time_str):
    """Convertit 00:04:20.50 en secondes totales (float)"""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)

def download_video_with_progress(url):
    print(f"--- Analyse de la page : {url} ---")
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html_content = response.text
    except Exception as e:
        print(f"Erreur chargement page: {e}")
        return

    # --- 1. Récupération du Titre ---
    soup = BeautifulSoup(html_content, 'html.parser')
    title_element = soup.find(attrs={"data-a2a-title": True})
    if title_element:
        raw_title = title_element['data-a2a-title']
        filename = sanitize_filename(raw_title) + ".mp4"
        print(f"Titre : {raw_title}")
    else:
        filename = "video_download.mp4"
        print("Titre par défaut utilisé.")

    # --- 2. Récupération du M3U8 ---
    m3u8_pattern = r'(https?://[^\s"\'<>]+index\.m3u8)'
    match = re.search(m3u8_pattern, html_content)

    if not match:
        print("Erreur : Lien m3u8 introuvable.")
        return

    m3u8_url = match.group(1)
    print(f"Source : {m3u8_url}")

    # --- 3. Analyse préalable du fichier M3U8 (Compter les blocs) ---
    print("--- Analyse des segments (blocks) ---")
    try:
        m3u8_content = requests.get(m3u8_url, headers=headers).text
        # On compte le nombre de segments (lignes #EXTINF)
        segments = re.findall(r'#EXTINF:([\d\.]+),', m3u8_content)
        total_segments = len(segments)
        
        # Calcul de la durée totale estimée en additionnant la durée de chaque segment
        total_duration_sec = sum(float(s) for s in segments)
        
        print(f"Nombre de fichiers .ts détectés : {total_segments}")
        print(f"Durée totale estimée : {total_duration_sec:.2f} secondes")
        
    except Exception as e:
        print(f"Impossible d'analyser le m3u8 : {e}")
        total_duration_sec = None

    # --- 4. Lancement de FFmpeg avec barre de progression ---
    print(f"--- Téléchargement en cours vers '{filename}' ---")

    command = [
        "ffmpeg", "-y",
        "-i", m3u8_url,
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k",
        "-progress", "pipe:1", # Demande à ffmpeg d'envoyer la progression de façon lisible
        "-nostats",            # Enlève le texte inutile
        filename
    ]

    # On lance le processus
    process = subprocess.Popen(
        command, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT,
        universal_newlines=True
    )

    # Lecture de la progression
    start_time = time.time()
    
    while True:
        line = process.stdout.readline()
        if not line:
            break
        
        # FFmpeg envoie des lignes clé=valeur
        if "out_time_us=" in line:
            # Le temps est donné en microsecondes
            try:
                current_us = int(line.split('=')[1].strip())
                current_sec = current_us / 1000000.0
                
                if total_duration_sec:
                    percent = (current_sec / total_duration_sec) * 100
                    if percent > 100: percent = 100
                    
                    # Création de la barre visuelle [=====>    ]
                    bar_length = 30
                    filled_length = int(bar_length * percent // 100)
                    bar = '█' * filled_length + '-' * (bar_length - filled_length)
                    
                    # Affichage dynamique sur la même ligne (\r)
                    sys.stdout.write(f"\rProgression : |{bar}| {percent:.1f}% ({int(current_sec)}s / {int(total_duration_sec)}s)")
                    sys.stdout.flush()
            except:
                pass

    process.wait()
    print(f"\n\n--- Terminé ! Vidéo prête : {filename} ---")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: dl.py <URL>")
    else:
        download_video_with_progress(sys.argv[1])
