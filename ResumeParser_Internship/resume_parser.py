#!/usr/bin/env python3
"""
FINAL RESUME PARSER v3.0 - Internship Ready
- Auto-detects ALL .txt files in folder
- Handles ANY filename (Snehal_Kale_Resume.txt OK!)
- Fixes ALL encoding errors
- Batch processes multiple resumes
- Professional JSON output
"""

import re          # For finding patterns (email, phone)
import os          # For file operations
import json        # For saving results
import glob        # For finding all .txt files
from datetime import datetime  # For timestamps

def find_resume_files():
    """Find all .txt resume files in folder"""
    txt_files = glob.glob("*.txt")
    if txt_files:
        print("📁 Found these resume files:")
        for i, f in enumerate(txt_files, 1):
            print(f"  {i}. {f}")
        return txt_files
    print("❌ No .txt files found in folder!")
    return []

def read_resume_file(filename):
    """Read file with multiple encoding support (fixes errors)"""
    if not os.path.exists(filename):
        return None
    
    # Try different encodings to fix UTF-8 errors
    encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                content = file.read().lower()
            print(f"✅ Loaded: '{filename}' with {encoding}")
            return content
        except UnicodeDecodeError:
            continue  # Try next encoding
    
    print(f"❌ Cannot read encoding for {filename}")
    return None

def extract_name(content):
    """Extract name from first few lines"""
    lines = content.split('\n')
    for line in lines[:3]:  # Check first 3 lines
        # Split by spaces, dashes, underscores
        words = re.split(r'[\s\-_]+', line.strip())[:2]
        if len(words) >= 1 and len(words[0]) > 1:
            return ' '.join(words).title()
    return "Name Not Found"

def extract_email(content):
    """Find email using regex pattern"""
    email_pattern = r'[\w\.-]+@[\w\.-]+\.[\w]{2,}'
    emails = re.findall(email_pattern, content)
    return emails[0] if emails else "No Email Found"

def extract_phone(content):
    """Find phone number (Indian + International formats)"""
    phone_pattern = r'(\+?\d{1,3}[-.\s]?)?\$?\d{3}\$?[-.\s]?\d{3}[-.\s]?\d{4}|\d{10}'
    phones = re.findall(phone_pattern, content)
    for phone in phones:
        clean_phone = re.sub(r'[^\d+]', '', str(phone))  # Remove non-digits
        if len(clean_phone) >= 10:
            return clean_phone
    return "No Phone Found"

def extract_skills(content):
    """Find skills using keyword matching"""
    skills_keywords = [
        'python', 'java', 'javascript', 'js', 'html', 'css', 'react', 'angular', 'vue',
        'node', 'nodejs', 'sql', 'mysql', 'postgresql', 'mongodb', 
        'git', 'github', 'docker', 'aws', 'azure', 'linux', 
        'excel', 'php', 'c++', 'c#', 'java script', 'django', 'flask'
    ]
    found_skills = [skill.upper() for skill in skills_keywords if skill in content]
    return found_skills if found_skills else ["No Skills Found"]

def process_resume(filename):
    """Process single resume file"""
    content = read_resume_file(filename)
    if not content:
        return None
    
    result = {
        'filename': filename,
        'name': extract_name(content),
        'email': extract_email(content),
        'phone': extract_phone(content),
        'skills': extract_skills(content),
        'total_skills': len(extract_skills(content)),
        'processed_at': datetime.now().isoformat()
    }
    return result

def show_results(result):
    """Display single resume results"""
    print("\n" + "="*70)
    print(f"🎉 PARSED: {result['filename']}")
    print("="*70)
    print(f"👤 Name:        {result['name']}")
    print(f"📧 Email:       {result['email']}")
    print(f"📱 Phone:       {result['phone']}")
    print(f"💻 Skills ({result['total_skills']}): {', '.join(result['skills'])}")
    print("="*70)

def save_all_results(results):
    """Save all results to single JSON file"""
    if results:
        output_filename = f"all_resumes_parsed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(output_filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"💾 Batch saved: '{output_filename}' ({len(results)} resumes)")

def main():
    """Main function - Auto batch processing"""
    print("🚀 PROFESSIONAL RESUME PARSER v3.0")
    print("Codec Technologies - Internship Project\n")
    
    # Find all resume files
    files = find_resume_files()
    
    if not files:
        print("\n📋 QUICK START:")
        print("1. Add .txt resume files to this folder")
        print("2. Examples: Snehal_Kale_Resume.txt, Divya_Kale_Resume.txt")
        print("3. Press F5 - Auto processes everything!")
        return
    
    # Process all files automatically
    all_results = []
    print(f"\n🔍 Processing {len(files)} resume(s)...\n")
    
    for filename in files:
        print(f"📄 Processing: {filename}")
        result = process_resume(filename)
        if result:
            show_results(result)
            all_results.append(result)
        print()  # Empty line between results
    
    # Save batch results
    save_all_results(all_results)
    print(f"\n🎯 BATCH COMPLETE! Successfully parsed {len(all_results)} resumes!")
    print("✅ Ready for internship demo & interviews!")

# Run the program
if __name__ == "__main__":
    main()
