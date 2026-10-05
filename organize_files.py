#!/usr/bin/env python3
"""
File Organizer Script
Organizes files from Downloads folder into categorized structure with proper naming.

Usage:
    python organize_files.py [input_path] [output_path]
    
Examples:
    # Default paths
    python organize_files.py
    
    # Custom paths
    python organize_files.py /Users/vikram/Downloads /Users/vikram/workspace/organized
    
    # With dry-run (shows what would be done without actually moving)
    python organize_files.py --dry-run /Users/vikram/Downloads
"""

import os
import sys
import shutil
from pathlib import Path
from datetime import datetime

# Default paths
DEFAULT_INPUT = Path("/Users/vikram/Downloads")
DEFAULT_OUTPUT = Path("/Users/vikram/workspace")

# Category mapping
CATEGORIES = {
    "medical": "Medical_Records",
    "legal": "Legal_Documents",
    "tax": "Tax_Documents", 
    "career": "Career_Documents",
    "cloud": "Cloud_Configuration",
    "hr": "HR_Documents",
    "academic": "Academic_Certifications",
    "image": "Images",
    "archive": "Archives",
    "video": "Videos",
    "data": "Data_Files",
    "pdf_unnamed": "Unnamed_PDFs",
    "word_unnamed": "Unnamed_Word_Docs",
    "other": "Other_Files"
}

# Extension to category mapping
EXTENSION_CATEGORIES = {
    '.png': "image",
    '.jpg': "image",
    '.jpeg': "image",
    '.heic': "image",
    '.webp': "image",
    '.gif': "image",
    '.bmp': "image",
    '.mp4': "video",
    '.avi': "video",
    '.mov': "video",
    '.mkv': "video",
    '.wmv': "video",
    '.zip': "archive",
    '.rar': "archive",
    '.7z': "archive",
    '.dmg': "archive",
    '.exe': "archive",
    '.app': "archive",
    '.csv': "data",
    '.xls': "data",
    '.xlsx': "data",
    '.json': "data",
    '.xml': "data",
    '.sql': "data"
}

def categorize_file(filepath):
    """
    Categorize a file based on name keywords and file extension.
    Returns category name (e.g., 'medical', 'legal', 'image', etc.)
    """
    name = filepath.name.lower()
    ext = Path(filepath).suffix.lower()
    
    # Priority 1: Check name for specific categories
    # Medical
    medical_keywords = ['medical', 'lab', 'ultrasound', 'lab result', 'dds', 'driver', 
                        'ga dl', 'dr', 'health', 'benefit', 'medical plan', 'insurance']
    if any(kw in name for kw in medical_keywords):
        return "medical"
    
    # Legal
    legal_keywords = ['affidavit', 'court', 'attorney', 'case status', 'dmv', 
                      'legal', 'petition', 'access flyer', 'id card', 'court order']
    if any(kw in name for kw in legal_keywords):
        return "legal"
    
    # Tax
    tax_keywords = ['w2', 'w-2', 'tax', '1040', 'pay1040', 'endowtax', 'sbc-medical',
                    'fee schedule', 'payment', 'wage', 'income tax', 'tax return']
    if any(kw in name for kw in tax_keywords):
        return "tax"
    
    # Career/Resume
    career_keywords = ['resume', 'cv', 'profile', 'duties', 'job', 'experience', 
                       'personal statement', 'vikram', 'prashanthi', 'sre', 'devops', 
                       'consultant', 'h1b', 'visa', 'i-94', 'i-539', 'i-797', 'h-1b']
    if any(kw in name for kw in career_keywords):
        return "career"
    
    # Cloud/IT Config
    cloud_keywords = ['azure', 'landing', 'config', 'vault', 'eks', 'cmm', 'cus.info',
                      'native workspace', 'company profile', 'nivas job duties',
                      'experience letter', 'employee agreement']
    if any(kw in name for kw in cloud_keywords):
        return "cloud"
    
    # HR
    hr_keywords = ['h4', 'questionnaire', 'form19', 'recovery note', 'receipt',
                   'notice', 'rescheduled', 'benefit summary']
    if any(kw in name for kw in hr_keywords):
        return "hr"
    
    # Academic
    academic_keywords = ['degree', 'university', 'certification', 'campbellsville',
                         'recapture', 'template']
    if any(kw in name for kw in academic_keywords):
        return "academic"
    
    # Priority 2: Check extension for file type
    if ext in ['.png', '.jpg', '.jpeg', '.heic', '.webp', '.gif', '.bmp']:
        return "image"
    elif ext in ['.mp4', '.avi', '.mov', '.mkv', '.wmv']:
        return "video"
    elif ext in ['.zip', '.rar', '.7z', '.dmg', '.exe', '.app']:
        return "archive"
    elif ext in ['.csv', '.xls', '.xlsx', '.json', '.xml', '.sql']:
        return "data"
    elif ext == '.pdf':
        return "pdf_unnamed"
    elif ext in ['.docx', '.doc', '.eml', '.txt']:
        return "word_unnamed"
    else:
        return "other"


def get_tag(category):
    """Get the descriptive tag for a category"""
    tags = {
        "medical": "Medical Record",
        "legal": "Legal Document",
        "tax": "Tax Document",
        "career": "Resume/Career Document",
        "cloud": "Cloud/IT Configuration",
        "hr": "HR Document",
        "academic": "Academic/Certification",
        "image": "Image File",
        "video": "Video File",
        "archive": "Archive File",
        "data": "Data File",
        "pdf_unnamed": "PDF Document",
        "word_unnamed": "Word Document",
        "other": "Other"
    }
    return tags.get(category, "Uncategorized")


def create_organized_name(filepath, category):
    """Create a clean, organized file name"""
    original_name = filepath.name
    
    # Remove extension for cleaning
    name_without_ext = original_name.rsplit('.', 1)[0]
    
    # Replace spaces, special chars with underscores
    cleaned = name_without_ext.replace(' ', '_')
    cleaned = cleaned.replace('-', '_')
    cleaned = cleaned.replace('/', '_')
    cleaned = cleaned.replace('\\', '_')
    cleaned = cleaned.replace(':', '_')
    cleaned = cleaned.replace('|', '_')
    cleaned = cleaned.replace('<', '_')
    cleaned = cleaned.replace('>', '_')
    cleaned = cleaned.replace('?', '_')
    cleaned = cleaned.replace('"', '_')
    
    # Remove duplicates
    while '  ' in cleaned:
        cleaned = cleaned.replace('  ', '_')
    
    # Strip leading/trailing underscores and dots
    cleaned = cleaned.strip('_').strip('.')
    
    # Create final name
    tag = get_tag(category)
    ext = Path(filepath).suffix
    new_name = f"{category}_{tag}_{cleaned}{ext}"
    
    return new_name


def organize_files(input_path, output_path, dry_run=False):
    """
    Main function to organize files.
    
    Args:
        input_path: Path to source directory
        output_path: Path to destination directory
        dry_run: If True, only print what would be done without actually moving files
    """
    input_path = Path(input_path)
    output_path = Path(output_path)
    
    if not input_path.exists():
        print(f"❌ Error: Input path does not exist: {input_path}")
        return False
    
    if not input_path.is_dir():
        print(f"❌ Error: Input path is not a directory: {input_path}")
        return False
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Create category folders
    for category, folder_name in CATEGORIES.items():
        (output_path / folder_name).mkdir(parents=True, exist_ok=True)
    
    # Process all files
    moved_files = []
    skipped_files = []
    errors = []
    
    print(f"🚀 Organizing files from: {input_path}")
    print(f"📁 Organizing files to: {output_path}")
    print("=" * 80)
    
    total_files = 0
    for filepath in input_path.rglob('*'):
        if filepath.is_file():
            total_files += 1
            
            try:
                # Categorize the file
                category = categorize_file(filepath)
                folder_name = CATEGORIES.get(category, CATEGORIES["other"])
                dest_folder = output_path / folder_name
                
                # Create new name
                new_name = create_organized_name(filepath, category)
                dest_path = dest_folder / new_name
                
                # Skip if file already exists (avoid duplicates)
                if dest_path.exists():
                    continue
                
                # Copy file
                if dry_run:
                    print(f"  📋 Would copy: {filepath.name}")
                    print(f"    → {folder_name}/{new_name}")
                else:
                    shutil.copy2(filepath, dest_path)
                    print(f"  ✅ {filepath.name}")
                    print(f"     → {folder_name}/{new_name}")
                
                moved_files.append({
                    'original': filepath.name,
                    'new': new_name,
                    'category': category,
                    'folder': folder_name,
                    'size': filepath.stat().st_size
                })
                
            except Exception as e:
                errors.append({
                    'file': str(filepath),
                    'error': str(e)
                })
                print(f"  ⚠️  Error processing {filepath}: {e}")
    
    # Print summary
    print("=" * 80)
    print(f"\n✅ Processed {total_files} files")
    print(f"📊 Successfully organized: {len(moved_files)} files")
    print(f"⚠️  Skipped (already exists): {sum(1 for f in moved_files if f['original'] in [m['original'] for m in skipped_files])}")
    
    if errors:
        print(f"❌ Errors: {len(errors)} files failed to process")
    
    # Print category breakdown
    print("\n📊 Files organized by category:")
    category_counts = {}
    for f in moved_files:
        cat = f['category']
        category_counts[cat] = category_counts.get(cat, 0) + 1
    
    for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
        folder = CATEGORIES[cat]
        print(f"  {folder:30s} : {count:4d} files")
    
    # Save summary
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    summary_file = output_path / f"organization_summary_{timestamp}.txt"
    
    summary_content = f"""
FILE ORGANIZATION SUMMARY
=========================
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Input Path: {input_path}
Output Path: {output_path}
Dry Run: {dry_run}

Total Files Processed: {total_files}
Successfully Organized: {len(moved_files)}
Errors: {len(errors)}

Category Breakdown:
"""
    
    for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
        summary_content += f"  {CATEGORIES[cat]:30s} : {count:4d} files\n"
    
    summary_content += f"""
Output Location: {output_path}
"""
    
    with open(summary_file, 'w') as f:
        f.write(summary_content)
    
    print(f"\n📄 Summary saved to: {summary_file}")
    
    return True


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Organize files into categorized structure with proper naming',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python organize_files.py
  python organize_files.py /Users/vikram/Downloads /Users/vikram/workspace/organized
  python organize_files.py --dry-run /Users/vikram/Downloads
        """
    )
    
    parser.add_argument(
        'input_path',
        nargs='?',
        default=str(DEFAULT_INPUT),
        help=f'Input directory path (default: {DEFAULT_INPUT})'
    )
    
    parser.add_argument(
        'output_path',
        nargs='?',
        default=str(DEFAULT_OUTPUT),
        help=f'Output directory path (default: {DEFAULT_OUTPUT})'
    )
    
    parser.add_argument(
        '--dry-run', '-n',
        action='store_true',
        help='Show what would be done without actually moving files'
    )
    
    args = parser.parse_args()
    
    print("=" * 80)
    print("📁 FILE ORGANIZER")
    print("=" * 80)
    print(f"Input: {args.input_path}")
    print(f"Output: {args.output_path}")
    print(f"Dry Run: {args.dry_run}")
    print("=" * 80)
    print()
    
    success = organize_files(
        args.input_path,
        args.output_path,
        dry_run=args.dry_run
    )
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
