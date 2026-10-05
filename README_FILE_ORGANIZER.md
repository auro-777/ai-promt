# File Organizer Script

Organizes files from any directory into a categorized structure with proper naming conventions.

## Quick Start

### Organize your Downloads folder:
```bash
python organize_files.py /Users/vikram/Downloads /Users/vikram/workspace/organized
```

### Dry-run (preview what would happen):
```bash
python organize_files.py --dry-run /Users/vikram/Downloads
```

### Custom paths:
```bash
python organize_files.py [input_path] [output_path]
```

## Usage

### Basic
```bash
python organize_files.py
```
Uses default paths: Downloads → workspace

### With custom paths
```bash
python organize_files.py /path/to/source /path/to/destination
```

### Dry run (preview only)
```bash
python organize_files.py --dry-run /path/to/source
```

## Categories

Files are automatically categorized into:

| Category | Folder Name | Example Files |
|----------|-------------|---------------|
| Medical Records | Medical_Records | Lab results, medical plans, insurance |
| Legal Documents | Legal_Documents | Affidavits, court orders, DMV |
| Tax Documents | Tax_Documents | W-2, tax returns, payments |
| Career Documents | Career_Documents | Resumes, CVs, job duties |
| Cloud Configuration | Cloud_Configuration | Azure configs, I-94, I-539 |
| HR Documents | HR_Documents | Questionnaires, agreements |
| Academic Certifications | Academic_Certifications | Degrees, certifications |
| Images | Images | JPG, PNG, HEIC, WebP |
| Archives | Archives | ZIP, DMG, EXE, APP |
| Data Files | Data_Files | CSV, XLSX, JSON |
| Unnamed PDFs | Unnamed_PDFs | PDFs without clear naming |
| Unnamed Word Docs | Unnamed_Word_Docs | DOCX, EML without clear naming |
| Other | Other_Files | Files that don't fit other categories |

## Naming Convention

Files are renamed as:
```
{category}_{tag}_{cleaned_name}{extension}
```

**Examples:**
- `Benefit Summary - Dental Plan.pdf` → `medical_Medical Record_Benefit_Summary_Dental_Plan_pdf`
- `2025 W2.pdf` → `tax_Tax Document_2025_W2_pdf`
- `Vikram_Sr_Devops-SRE_Consultant.docx` → `career_Resume_Career_Document_Vikram_Sr_Devops-SRE_Consultant_docx`
- `IMG_9775.jpeg` → `image_Image File_IMG_9775_jpeg`

## Features

✅ **Automatic categorization** based on filename keywords
✅ **Clean naming** - removes special characters, spaces, duplicates
✅ **Tagging** - adds descriptive tags to each category
✅ **Duplicate detection** - skips files already in output
✅ **Dry-run mode** - preview before executing
✅ **Summary report** - generates detailed organization report
✅ **Recursive** - processes all subdirectories
✅ **Safe copy** - doesn't delete originals

## Categories Logic

The script categorizes files using this priority:

1. **Name-based detection** (highest priority)
   - Medical keywords: "lab", "ultrasound", "medical", "insurance", etc.
   - Legal keywords: "affidavit", "court", "dmv", "legal", etc.
   - Tax keywords: "w2", "tax", "1040", "payment", etc.
   - Career keywords: "resume", "cv", "vikram", "prashanthi", "sre", etc.
   - And more...

2. **Extension-based detection** (secondary priority)
   - Images: .png, .jpg, .heic, .webp, etc.
   - Archives: .zip, .dmg, .exe, .app, etc.
   - Data: .csv, .xlsx, .json, etc.
   - PDFs, Word docs: fallback to specific folders

## Customization

### Edit category keywords
Open `organize_files.py` and modify the keyword lists:

```python
# In categorize_file() function
medical_keywords = ['medical', 'lab', 'ultrasound', ...]  # Add your keywords
legal_keywords = ['affidavit', 'court', ...]  # Add your keywords
```

### Add new categories
Edit the `CATEGORIES` dictionary:

```python
CATEGORIES = {
    "medical": "Medical_Records",
    "your_new_category": "Your_New_Folder",  # Add here
    # ...
}
```

## Output

After running, you'll get:
- Organized files in the output directory
- `organization_summary_YYYYMMDD_HHMMSS.txt` with:
  - Total files processed
  - Files successfully organized
  - Category breakdown
  - Errors (if any)

## Troubleshooting

**Issue: Files not being categorized correctly**
- Check the filename for relevant keywords
- Edit the keyword lists in the script

**Issue: Duplicate files**
- The script skips duplicates automatically
- Review the summary file for details

**Issue: Permission errors**
- Run with appropriate permissions
- Ensure output directory is writable

## License

Free to use and modify.
