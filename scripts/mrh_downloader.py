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
║                MRH Universal Downloader v1.0.1 FINAL                      ║
║                coded by: MRH | For internet freedom                       ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

import os
import re
import subprocess
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
    
    def run(self):
        print(f"\n🚀 MRH Downloader v{self.VERSION} starting...\n")
        msg = self.get_commit_msg()
        print(f"📝 Commit message: {msg[:200]}\n")
        
        # Check for stop command
        if 'dl-stop' in msg:
            print("🛑 Emergency stop activated")
            return
        
        # ============================================================
        # YOUTUBE DOWNLOAD (MOST SIMPLE METHOD)
        # ============================================================
        if 'dl-yt:' in msg:
            # Extract URL
            match = re.search(r'dl-yt:\s*([^\s]+)', msg)
            if not match:
                print("❌ No URL found")
                return
            
            url = match.group(1)
            is_mp3 = '(mp3)' in msg
            url = url.replace('(mp3)', '').replace('(mp4)', '').strip()
            
            print(f"🎬 Downloading from YouTube: {url}")
            print(f"📀 Format: {'MP3 Audio' if is_mp3 else 'MP4 Video'}")
            
            # Create directory
            yt_dir = self.downloads_dir / 'youtube'
            yt_dir.mkdir(parents=True, exist_ok=True)
            
            # Change to directory
            original_dir = os.getcwd()
            os.chdir(yt_dir)
            
            # Build command
            if is_mp3:
                cmd = ['yt-dlp', '-x', '--audio-format', 'mp3', '--audio-quality', '0', 
                       '--no-playlist', '--restrict-filenames', url]
            else:
                cmd = ['yt-dlp', '-f', 'bestvideo[height<=720]+bestaudio/best[height<=720]',
                       '--merge-output-format', 'mp4', '--no-playlist', '--restrict-filenames', url]
            
            print(f"🔧 Running: {' '.join(cmd)}")
            
            # Run and capture output
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            # Change back
            os.chdir(original_dir)
            
            # Check results
            if result.returncode == 0:
                downloaded = list(yt_dir.glob('*'))
                if downloaded:
                    for f in downloaded:
                        size = f.stat().st_size / (1024*1024)
                        print(f"✅ Downloaded: {f.name} ({size:.2f} MB)")
                else:
                    print("⚠️ Command succeeded but no files found")
                    print(f"📋 Output: {result.stdout[:500]}")
            else:
                print(f"❌ Download failed!")
                print(f"⚠️ Error: {result.stderr[:500]}")
        
        # ============================================================
        # INSTAGRAM DOWNLOAD
        # ============================================================
        elif 'dl-ig:' in msg:
            match = re.search(r'dl-ig:\s*([^\s]+)', msg)
            if not match:
                print("❌ No URL found")
                return
            
            url = match.group(1)
            print(f"📸 Downloading from Instagram: {url}")
            
            ig_dir = self.downloads_dir / 'instagram'
            ig_dir.mkdir(parents=True, exist_ok=True)
            
            original_dir = os.getcwd()
            os.chdir(ig_dir)
            
            cmd = ['yt-dlp', '--no-playlist', '--restrict-filenames', url]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            os.chdir(original_dir)
            
            if result.returncode == 0:
                downloaded = list(ig_dir.glob('*'))
                if downloaded:
                    for f in downloaded:
                        size = f.stat().st_size / (1024*1024)
                        print(f"✅ Downloaded: {f.name} ({size:.2f} MB)")
                else:
                    print("⚠️ No files found")
            else:
                print(f"❌ Instagram failed: {result.stderr[:300]}")
        
        # ============================================================
        # SIMPLE FILE DOWNLOAD
        # ============================================================
        elif 'dl:' in msg and 'dl-yt:' not in msg and 'dl-ig:' not in msg and 'dl-zip:' not in msg:
            match = re.search(r'dl:\s*(.+)', msg)
            if match:
                urls = match.group(1).split()
                print(f"📥 Downloading {len(urls)} file(s)...")
                
                for url in urls:
                    filename = url.split('/')[-1].split('?')[0]
                    if not filename:
                        filename = f"file_{datetime.now().strftime('%H%M%S')}"
                    
                    output = self.downloads_dir / filename
                    cmd = ['wget', '-q', '-O', str(output), url]
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    
                    if result.returncode == 0 and output.exists():
                        size = output.stat().st_size / (1024*1024)
                        print(f"✅ {filename} ({size:.2f} MB)")
                    else:
                        print(f"❌ Failed: {url}")
                        if result.stderr:
                            print(f"   Error: {result.stderr[:200]}")
        
        # ============================================================
        # DOWNLOAD AND ZIP
        # ============================================================
        elif 'dl-zip:' in msg:
            match = re.search(r'dl-zip:\s*(.+)', msg)
            if match:
                urls = match.group(1).split()
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                zip_path = self.downloads_dir / f"mrh_archive_{timestamp}.zip"
                
                print(f"📦 Downloading {len(urls)} file(s) and creating ZIP...")
                
                temp_dir = self.downloads_dir / f"temp_{timestamp}"
                temp_dir.mkdir(exist_ok=True)
                
                downloaded = []
                for url in urls:
                    filename = url.split('/')[-1].split('?')[0] or f"file_{len(downloaded)}"
                    temp_file = temp_dir / filename
                    cmd = ['wget', '-q', '-O', str(temp_file), url]
                    if subprocess.run(cmd).returncode == 0 and temp_file.exists():
                        downloaded.append(temp_file)
                        print(f"  ✅ {filename}")
                    else:
                        print(f"  ❌ {filename}")
                
                if downloaded:
                    import zipfile
                    with zipfile.ZipFile(zip_path, 'w') as zf:
                        for f in downloaded:
                            zf.write(f, f.name)
                    print(f"✅ ZIP created: {zip_path.name}")
                    shutil.rmtree(temp_dir)
                else:
                    print("❌ No files downloaded")
                    shutil.rmtree(temp_dir)
        
        # ============================================================
        # GITHUB DOWNLOAD
        # ============================================================
        elif 'dl-gh:' in msg:
            match = re.search(r'dl-gh:\s*([^\s]+)', msg)
            if match:
                url = match.group(1)
                filename = url.split('/')[-1].split('?')[0] or "github_file"
                
                gh_dir = self.downloads_dir / 'github'
                gh_dir.mkdir(parents=True, exist_ok=True)
                output = gh_dir / filename
                
                cmd = ['wget', '-q', '-O', str(output), url]
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                if result.returncode == 0 and output.exists():
                    size = output.stat().st_size / (1024*1024)
                    print(f"✅ Downloaded: {filename} ({size:.2f} MB)")
                else:
                    print(f"❌ Failed: {url}")
        
        # ============================================================
        # NO COMMAND
        # ============================================================
        else:
            print("📖 No valid command found. Available commands:")
            print("   dl: URL          - Download file")
            print("   dl-yt: URL       - Download YouTube video")
            print("   dl-yt: URL (mp3) - Download YouTube audio")
            print("   dl-ig: URL       - Download Instagram")
            print("   dl-zip: URLs     - Download and create ZIP")
            print("   dl-gh: URL       - Download from GitHub")
            print("   dl-stop          - Emergency stop")
            return
        
        # ============================================================
        # FINAL REPORT
        # ============================================================
        print("\n" + "="*50)
        print("📁 FINAL REPORT - Files in downloads folder:")
        print("="*50)
        
        if self.downloads_dir.exists():
            all_files = list(self.downloads_dir.rglob('*'))
            files_only = [f for f in all_files if f.is_file()]
            
            if files_only:
                for f in files_only:
                    size = f.stat().st_size / (1024*1024)
                    rel_path = f.relative_to(self.downloads_dir)
                    print(f"  📄 {rel_path} ({size:.2f} MB)")
            else:
                print("  📂 No files found in downloads directory")
        else:
            print("  📂 downloads directory does not exist")
        
        print("="*50)
        print("✅ MRH Downloader finished!")
        print("="*50)

if __name__ == "__main__":
    MRHDownloader().run()
