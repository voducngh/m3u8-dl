# M3U8 Smart Video Downloader

[Français](#français) | [English](#english)

---

## Français

Ce script Python permet de télécharger des vidéos diffusées en streaming (HLS / `.m3u8`) à partir d'une page web donnée. Il détecte automatiquement le lien du flux, nettoie le nom du fichier, télécharge les segments et les convertit en un fichier MP4 propre avec une piste audio synchronisée.

### Fonctionnalités
* 🔍 **Détection automatique** du fichier `.m3u8` dans le code source de la page.
* 🏷️ **Nommage automatique** basé sur le titre de la vidéo (via les balises meta).
* 📊 **Barre de progression** affichant le pourcentage, le temps écoulé et la durée totale.
* 🔊 **Correction Audio** : Réencode l'audio en AAC pour éviter les coupures de son entre les segments `.ts`.
* 🚀 **Rapide** : Copie le flux vidéo sans réencodage (`copy`) pour une vitesse maximale.

### Prérequis

1.  **Python 3**
2.  **FFmpeg** : Le script utilise FFmpeg pour le traitement vidéo.
    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```

### Installation

Sur les versions récentes de Linux (Debian 12, Ubuntu 23+, Raspberry Pi OS), Python est géré de manière externe.

**Option 1 : Installation système (Recommandé - Plus simple)**
```bash
sudo apt install python3-requests python3-bs4
````

**Option 2 : Via environnement virtuel (venv)**
Si vous préférez isoler le projet (ou si l'option 1 ne fonctionne pas) :

```bash
# 1. Installez le module venv (nécessaire sur Debian/Ubuntu récents)
sudo apt install python3-venv

# 2. Créez l'environnement virtuel
python3 -m venv venv

# 3. Activez l'environnement
source venv/bin/activate

# 4. Installez les librairies dans l'environnement
pip install requests beautifulsoup4
```

### Utilisation

Lancez le script en passant l'URL de la page en argument :

```bash
# Si Option 1 :
python3 script.py "[https://exemple.com/page-video](https://exemple.com/page-video)"

# Si Option 2 (assurez-vous d'avoir fait 'source venv/bin/activate' avant) :
python script.py "[https://exemple.com/page-video](https://exemple.com/page-video)"
```

-----

## English

This Python script downloads streaming videos (HLS / `.m3u8`) directly from a given webpage URL. It automatically detects the stream link, sanitizes the filename, downloads the segments, and converts them into a clean MP4 file with synchronized audio.

### Features

  * 🔍 **Auto-detection** of the `.m3u8` file within the page source code.
  * 🏷️ **Auto-naming** based on the video title (retrieved from meta tags).
  * 📊 **Progress Bar** showing percentage, elapsed time, and total duration.
  * 🔊 **Audio Fix**: Re-encodes audio to AAC to prevent sound dropouts/cuts between `.ts` segments.
  * 🚀 **Fast**: Copies the video stream without re-encoding (`copy`) for maximum speed.

### Prerequisites

1.  **Python 3**
2.  **FFmpeg**: The script relies on FFmpeg for video processing.
    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```

### Installation

On recent Linux versions (Debian 12, Ubuntu 23+, Raspberry Pi OS), Python environments are externally managed.

**Option 1: System Installation (Recommended - Easiest)**

```bash
sudo apt install python3-requests python3-bs4
```

**Option 2: Virtual Environment (venv)**
If you prefer to isolate the project (or if Option 1 doesn't work):

```bash
# 1. Install the venv module (required on recent Debian/Ubuntu systems)
sudo apt install python3-venv

# 2. Create the virtual environment
python3 -m venv venv

# 3. Activate the environment
source venv/bin/activate

# 4. Install libraries inside the environment
pip install requests beautifulsoup4
```

### Usage

Run the script by passing the URL of the page containing the video as an argument:

```bash
# If using Option 1:
python3 script.py "[https://example.com/video-page](https://example.com/video-page)"

# If using Option 2 (ensure you ran 'source venv/bin/activate' first):
python script.py "[https://example.com/video-page](https://example.com/video-page)"
```

-----

### Disclaimer

*This script is for educational purposes only. Please respect copyright laws and the terms of service of the websites you visit.*

