#!/usr/bin/env python3
"""
╔════════════════════════════════════════════════════════════════════════════╗
║  ███╗   ███╗██████╗ ██╗  ██╗                                              ║
║  ████╗ ████║██╔══██╗██║  ██║                                              ║
║  ██╔████╔██║██████╔╝███████║                                              ║
║  ██║╚██╔╝██║██╔══██╗██╔══██║                                              ║
║  ██║ ╚═╝ ██║██║  ██║██║  ██║                                              ║
║  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝                                              ║
║                                                                            ║
║                MRH Universal Downloader v1.0.1                            ║
║                coded by: MRH | For internet freedom                       ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

import os, re, subprocess, zipfile, shutil
from pathlib import Path
from datetime import datetime

class MRHDownloader:
    VERSION = "1.0.1"
    
    def __init__(self):
        self.downloads = Path("downloads")
        self.downloads.mkdir(exist_ok=True)
    
    def get_commit_msg(self):
        return subprocess.run(['git', 'log', '-1', '--pretty=%B'], capture_output=True, text=True).stdout.strip()
    
    def download(self, url, path):
        try:
            subprocess.run(['wget', '-q', '-O', str(path), url], check=True)
            return True
        except:
            return False
    
    def run(self):
        print(f"\n🚀 MRH v{self.VERSION} starting...\n")
        msg = self.get_commit_msg()
        
        # Parse commands
        if 'dl-stop' in msg:
            print("🛑 Stopped")
            return
        
        # dl: URL1 URL2
        if 'dl:' in msg and not 'dl-zip:' in msg and not 'dl-yt:' in msg:
            urls = msg.split('dl:')[1].split()[0:5]
            for url in urls:
                name = url.split('/')[-1].split('?')[0] or f"file_{datetime.now().strftime('%H%M%S')}"
                if self.download(url, self.downloads / name):
                    print(f"✅ Downloaded: {name}")
                else:
                    print(f"❌ Failed: {url}")
        
        # dl-yt: URL
        elif 'dl-yt:' in msg:
            url = msg.split('dl-yt:')[1].split()[0]
            is_mp3 = '(mp3)' in msg
            url = url.replace('(mp3)', '').replace('(mp4)', '').strip()
            out_dir = self.downloads / 'youtube'
            out_dir.mkdir(exist_ok=True)
            if is_mp3:
                cmd = ['yt-dlp', '-x', '--audio-format', 'mp3', '-o', f'{out_dir}/%(title)s.%(ext)s', url]
            else:
                cmd = ['yt-dlp', '-f', 'best[height<=720]', '-o', f'{out_dir}/%(title)s.%(ext)s', url]
            subprocess.run(cmd)
            print("✅ YouTube done")
        
        # dl-zip: URL1 URL2
        elif 'dl-zip:' in msg:
            urls = msg.split('dl-zip:')[1].split()[0:5]
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            zip_path = self.downloads / f"mrh_archive_{timestamp}.zip"
            temp = self.downloads / f"temp_{timestamp}"
            temp.mkdir()
            files = []
            for url in urls:
                name = url.split('/')[-1].split('?')[0] or f"file_{len(files)}"
                path = temp / name
                if self.download(url, path):
                    files.append(path)
            with zipfile.ZipFile(zip_path, 'w') as zf:
                for f in files:
                    zf.write(f, f.name)
            shutil.rmtree(temp)
            print(f"✅ ZIP created: {zip_path.name}")
        
        # dl-gh: URL (GitHub release or raw)
        elif 'dl-gh:' in msg:
            url = msg.split('dl-gh:')[1].split()[0]
            name = url.split('/')[-1].split('?')[0] or "github_file"
            out_dir = self.downloads / 'github'
            out_dir.mkdir(exist_ok=True)
            if self.download(url, out_dir / name):
                print(f"✅ GitHub: {name}")
        
        # dl-extract: URL.zip
        elif 'dl-extract:' in msg:
            url = msg.split('dl-extract:')[1].split()[0]
            name = url.split('/')[-1].split('?')[0]
            zip_path = self.downloads / name
            extract_dir = self.downloads / 'extracted' / name.replace('.zip', '')
            if self.download(url, zip_path):
                extract_dir.mkdir(parents=True, exist_ok=True)
                with zipfile.ZipFile(zip_path, 'r') as zf:
                    zf.extractall(extract_dir)
                zip_path.unlink()
                print(f"✅ Extracted to: {extract_dir}")
        
        # dl-chunk: URL (large files with aria2)
        elif 'dl-chunk:' in msg:
            url = msg.split('dl-chunk:')[1].split()[0]
            name = url.split('/')[-1].split('?')[0] or "large_file"
            out_dir = self.downloads / 'chunked'
            out_dir.mkdir(exist_ok=True)
            subprocess.run(['aria2c', '-x', '4', '-s', '4', '-o', str(out_dir / name), url])
            print(f"✅ Large file done")
        
        else:
            print("📖 No valid command. Use: dl: URL | dl-yt: URL | dl-zip: URLs | dl-gh: URL | dl-extract: URL | dl-chunk: URL | dl-stop")
        
        print("\n✅ MRH Downloader finished. Check 'downloads' folder.\n")

if __name__ == "__main__":
    MRHDownloader().run()
