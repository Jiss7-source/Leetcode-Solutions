#!/bin/bash

# 1. Ask for user inputs
echo "Enter category folder name (e.g., Arrays, Trees, Strings):"
read category

echo "Enter filename exactly (e.g., 0015_3sum.py):"
read filename

# 2. Check if the file exists in the root directory
if [ ! -f "$filename" ]; then
    echo "❌ Error: File '$filename' not found in the root directory!"
    exit 1
fi

# 3. Create the category directory if it doesn't exist
mkdir -p "$category"

# 4. Move the file into the category folder
mv "$filename" "$category/"

# 5. Git automation sequence
git add .
git commit -m "Add $filename to $category"
git push origin main

echo "🚀 Successfully pushed $filename to GitHub under /$category!"