# Text-Translation
# Text Translation

This project is a simple Python script that uses the **Microsoft Azure Translator Text API** to translate English text into multiple Indian languages like **Hindi**, **Telugu**, and **Kannada**.

## 🔧 Technologies Used
- Python
- Azure Cognitive Services (Translator API)
- `requests` and `uuid` libraries

## 📋 Features
- Translates a given English sentence into:
  - Hindi (`hi`)
  - Telugu (`te`)
  - Kannada (`ka`)
- Prints the translated output in a readable JSON format

## 📁 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Kadirisani-Namitha/Text-Translation.git
cd Text-Translation

python translate.py

[
    {
        "translations": [
            {
                "text": "सुप्रभात!",
                "to": "hi"
            },
            {
                "text": "శుభోదయం!",
                "to": "te"
            },
            {
                "text": "ಶುಭೋದಯ!",
                "to": "ka"
            }
        ]
    }
]
