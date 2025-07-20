import json
from pathlib import Path
from formatter import format_resume

def load_resume_data(file_path='resume.json'):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Using empty template.")
        return {
            "personal_info": {},
            "summary": "",
            "education": [],
            "experience": [],
            "skills": {},
            "projects": []
        }
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {file_path}. Using empty template.")
        return {
            "personal_info": {},
            "summary": "",
            "education": [],
            "experience": [],
            "skills": {},
            "projects": []
        }

def export_resume(resume_data, format_type='txt'):
    content = format_resume(resume_data, format_type)
    file_name = f"resume_{resume_data['personal_info']['name'].replace(' ', '_').lower()}"
    
    if format_type == 'txt':
        file_path = f"{file_name}.txt"
    elif format_type == 'md':
        file_path = f"{file_name}.md"
    else:
        print("Invalid format type. Using .txt")
        file_path = f"{file_name}.txt"
    
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Resume successfully exported to {file_path}")
    except IOError as e:
        print(f"Error writing file: {e}")

def display_resume(resume_data):
    print("\n" + "=" * 40)
    print("RESUME PREVIEW".center(40))
    print("=" * 40 + "\n")
    print(format_resume(resume_data))
    print("=" * 40)

def main():
    print("Resume Generator")
    print("Generates a resume from JSON data\n")
    
    resume_data = load_resume_data()
    
    while True:
        print("\nMenu:")
        print("1. Preview Resume")
        print("2. Export as Text (.txt)")
        print("3. Export as Markdown (.md)")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            display_resume(resume_data)
        elif choice == '2':
            export_resume(resume_data, 'txt')
        elif choice == '3':
            export_resume(resume_data, 'md')
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()