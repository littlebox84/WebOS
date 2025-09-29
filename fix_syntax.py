#!/usr/bin/env python3
import re

# Read the file
with open('/home/xlittleboxesx/CascadeProjects/WebOS/webos-enhanced.html', 'r') as f:
    content = f.read()

# Fix the syntax error by replacing the problematic pattern
# Look for: reset(); followed by excessive newlines and start() {
pattern = r'(\s*init\(\)\s*\{\s*api\.resetMetrics\(\);\s*reset\(\);)\s*\n(?:\s*\n)*\s*(start\(\)\s*\{)'
replacement = r'\1\n                        },\n                        \2'

fixed_content = re.sub(pattern, replacement, content)

# Write the fixed content back
with open('/home/xlittleboxesx/CascadeProjects/WebOS/webos-enhanced.html', 'w') as f:
    f.write(fixed_content)

print("Syntax error fixed successfully")