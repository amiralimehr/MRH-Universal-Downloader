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

import os
import re
import subprocess
import zipfile
import shutil
from pathlib import Path
from datetime import datetime

class MRHDownloader:
    VERSION = "1.0.1"
    
    def __init__(self):
        self.downloads_dir = Path("downloads")
        self.downloads_dir.mkdir(exist_ok=True)
        
    def get_commit_msg(self):
        result = subprocess.run(['git', 'log', '-1', '--pretty=%B'], 
                                capture_output=True, text=True)
        return result.stdout.strip()
    
    def download_file(self, url, output_path):
        """Download a single file using wget"""
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            cmd = ['wget', '-q', '--show-progress', '-O', str(output_path), url]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0 and output_path.exists():
                print(f"    ✅ Downloaded: {output_path.name} ({output_path.stat().st_size} bytes)")
                return True
            else:
                print(f"    ❌ wget failed: {result.stderr}")
                return False
        except Exception as e:
            print(f"    ❌ Exception: {e}")
            return False
    
    def run(self):
        print(f"\n🚀 MRH Downloader v{self.VERSION} starting...\n")
        msg = self.get_commit_msg()
        print(f"📝 Commit message: {msg[:100]}...\n")
        
        # Check for stop command
        if 'dl-stop' in msg:
            print("🛑 Stop command detected. Exiting...")
            return
        
        # ==================== dl: (simple download) ====================
        if re.search(r'dl:\s', msg) and 'dl-yt:' not in msg and 'dl-ig:' not in msg and 'dl-zip:' not in msg:
            urls_text = re.search(r'dl:\s*(.+)', msg).group(1)
            urls = urls_text.split()
            print(f"📥 Downloading {len(urls)} file(s)...")
            for url in urls:
                filename = url.split('/')[-1].split('?')[0]
                if not filename or '.' not in filename:
                    filename = f"file_{datetime.now().strftime('%H%M%S')}"
                output_path = self.downloads_dir / filename
                print(f"  ⬇️ {url}")
                self.download_file(url, output_path)
        
        # ==================== dl-yt: (YouTube) ====================
        elif 'dl-yt:' in msg:
            url_match = re.search(r'dl-yt:\s*([^\s]+)', msg)
            if not url_match:
                print("❌ No URL found for dl-yt command")
                return
            url = url_match.group(1)
            is_mp3 = '(mp3)' in msg
            url = url.replace('(mp3)', '').replace('(mp4)', '').strip()
            
            print(f"🎬 Downloading from YouTube: {url}")
            print(f"   Format: {'MP3 audio' if is_mp3 else 'MP4 video (720p max)'}")
            
            # Create output directory
            out_dir = self.downloads_dir / 'youtube'
            out_dir.mkdir(parents=True, exist_ok=True)
            
            # Change to directory so files save there
            os.chdir(out_dir)
            
            if is_mp3:
                cmd = ['yt-dlp', '-x', '--audio-format', 'mp3', '--audio-quality', '0', 
                       '--no-playlist', '--output', '%(title)s.%(ext)s', url]
            else:
                cmd = ['yt-dlp', '-f', 'best[height<=720]', '--no-playlist', 
                       '--output', '%(title)s.%(ext)s', url]
            
            print(f"   Running: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            # Change back
            os.chdir(self.downloads_dir.parent)
            
            if result.returncode == 0:
                # Check if any files were downloaded
                downloaded_files = list(out_dir.glob('*'))
                if downloaded_files:
                    for f in downloaded_files:
                        print(f"    ✅ Downloaded: {f.name} ({f.stat().st_size} bytes)")
                else:
                    print(f"    ⚠️ Command succeeded but no files found in {out_dir}")
                    print(f"    stdout: {result.stdout[:200]}")
            else:
                print(f"    ❌ YouTube download failed!")
                print(f"    Error: {result.stderr[:300]}")
        
        # ==================== dl-ig: (Instagram) ====================
        elif 'dl-ig:' in msg:
            url_match = re.search(r'dl-ig:\s*([^\s]+)', msg)
            if not url_match:
                print("❌ No URL found for dl-ig command")
                return
            url = url_match.group(1)
            
            print(f"📸 Downloading from Instagram: {url}")
            
            out_dir = self.downloads_dir / 'instagram'
            out_dir.mkdir(parents=True, exist_ok=True)
            
            os.chdir(out_dir)
            cmd = ['yt-dlp', '--no-playlist', '--output', '%(title)s.%(ext)s', url]
            result = subprocess.run(cmd, capture_output=True, text=True)
            os.chdir(self.downloads_dir.parent)
            
            if result.returncode == 0:
                downloaded_files = list(out_dir.glob('*'))
                if downloaded_files:
                    for f in downloaded_files:
                        print(f"    ✅ Downloaded: {f.name} ({f.stat().st_size} bytes)")
                else:
                    print(f"    ⚠️ Instagram command succeeded but no files found")
            else:
                print(f"    ❌ Instagram download failed!")
                print(f"    Error: {result.stderr[:300]}")
                print(f"    Note: Instagram has strict limits. Try again later or use a different post.")
        
        # ==================== dl-zip: (Download and ZIP) ====================
        elif 'dl-zip:' in msg:
            urls_text = re.search(r'dl-zip:\s*(.+)', msg).group(1)
            urls = urls_text.split()
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            zip_path = self.downloads_dir / f"mrh_archive_{timestamp}.zip"
            temp_dir = self.downloads_dir / f"temp_{timestamp}"
            temp_dir.mkdir(exist_ok=True)
            
            print(f"📦 Downloading {len(urls)} file(s) and creating ZIP...")
            downloaded_files = []
            
            for url in urls:
                filename = url.split('/')[-1].split('?')[0]
                if not filename:
                    filename = f"file_{len(downloaded_files)}"
                temp_path = temp_dir / filename
                if self.download_file(url, temp_path):
                    downloaded_files.append(temp_path)
            
            if downloaded_files:
                with zipfile.ZipFile(zip_path, 'w') as zf:
                    for f in downloaded_files:
                        zf.write(f, f.name)
                print(f"    ✅ ZIP created: {zip_path.name} ({zip_path.stat().st_size} bytes)")
                shutil.rmtree(temp_dir)
            else:
                print(f"    ❌ No files downloaded, ZIP not created")
                shutil.rmtree(temp_dir)
        
        # ==================== dl-gh: (GitHub direct) ====================
        elif 'dl-gh:' in msg:
            url_match = re.search(r'dl-gh:\s*([^\s]+)', msg)
            if not url_match:
                print("❌ No URL found for dl-gh command")
                return
            url = url_match.group(1)
            filename = url.split('/')[-1].split('?')[0] or "github_file"
            
            out_dir = self.downloads_dir / 'github'
            out_dir.mkdir(parents=True, exist_ok=True)
            output_path = out_dir / filename
            
            print(f"📦 Downloading from GitHub: {url}")
            if self.download_file(url, output_path):
                print(f"    ✅ Saved to: {output_path}")
        
        # ==================== dl-extract: (Download and extract ZIP) ====================
        elif 'dl-extract:' in msg:
            url_match = re.search(r'dl-extract:\s*([^\s]+)', msg)
            if not url_match:
                print("❌ No URL found for dl-extract command")
                return
            url = url_match.group(1)
            filename = url.split('/')[-1].split('?')[0]
            zip_path = self.downloads_dir / filename
            extract_dir = self.downloads_dir / 'extracted' / filename.replace('.zip', '')
            
            print(f"📦 Downloading and extracting: {url}")
            if self.download_file(url, zip_path):
                extract_dir.mkdir(parents=True, exist_ok=True)
                with zipfile.ZipFile(zip_path, 'r') as zf:
                    zf.extractall(extract_dir)
                zip_path.unlink()
                print(f"    ✅ Extracted to: {extract_dir}")
        
        # ==================== dl-chunk: (Large file with aria2) ====================
        elif 'dl-chunk:' in msg:
            url_match = re.search(r'dl-chunk:\s*([^\s]+)', msg)
            if not url_match:
                print("❌ No URL found for dl-chunk command")
                return
            url = url_match.group(1)
            filename = url.split('/')[-1].split('?')[0] or "large_file"
            
            out_dir = self.downloads_dir / 'chunked'
            out_dir.mkdir(parents=True, exist_ok=True)
            output_path = out_dir / filename
            
            print(f"🔗 Downloading large file with chunks: {url}")
            cmd = ['aria2c', '-x', '4', '-s', '4', '-o', str(output_path), url]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0 and output_path.exists():
                print(f"    ✅ Downloaded: {output_path.name} ({output_path.stat().st_size} bytes)")
            else:
                print(f"    ❌ Chunk download failed: {result.stderr[:200]}")
        
        else:
            print("📖 No valid command found.")
            print("\n📖 Available commands:")
            print("   dl: URL1 URL2           - Download files individually")
            print("   dl-yt: URL              - Download from YouTube")
            print("   dl-yt: URL (mp3)        - Download audio from YouTube")
            print("   dl-ig: URL              - Download from Instagram")
            print("   dl-zip: URL1 URL2       - Download and create ZIP")
            print("   dl-gh: URL              - Download from GitHub")
            print("   dl-extract: URL.zip     - Download and extract archive")
            print("   dl-chunk: URL           - Download large file with chunks")
            print("   dl-stop                 - Emergency stop")
            return
        
        print("\n" + "="*50)
        print("✅ MRH Downloader finished!")
        print(f"📁 Check the '{self.downloads_dir}' folder for your files")
        print("="*50 + "\n")

if __name__ == "__main__":
    MRHDownloader().run()
