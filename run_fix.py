import subprocess
import sys

# Run the fix script
result = subprocess.run([sys.executable, '/home/xlittleboxesx/CascadeProjects/WebOS/fix_syntax.py'], 
                       capture_output=True, text=True)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("Return code:", result.returncode)