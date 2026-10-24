import shutil, subprocess, sys
from pathlib import Path
if len(sys.argv)!=3:sys.exit('Usage: python render_preview.py input.pptx output_dir')
exe=shutil.which('libreoffice') or shutil.which('soffice')
if not exe:sys.exit('LibreOffice not installed; visual rendering unavailable')
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
subprocess.run([exe,'-env:UserInstallation=file:///tmp/claude-ppt-lo-profile','--headless','--convert-to','pdf','--outdir',str(out),sys.argv[1]],check=True)
print('PDF preview created in',out)
