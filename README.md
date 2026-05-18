# Secure Password Audit Tool (Python)

## Project Overview
This project is Python security tool designed to evaluate password strength using rule-based security checks.

The tool analyzes:
- Password length
- Uppercase/lowercase usage
- Numbers
- Special characters
- Common weak passwords

It then:
- Generates a score out of 100
- Classifies passwords as Weak / Medium / Strong
- Provides improvement recommendations

The project was developed as part of coursework on Agentic AI Production Workflows for Security-Related Services.

## Features

- Password strength scoring
- Weak password detection
- Complexity analysis
- User-friendly recommendations
- Beginner-friendly Python code
- Automated testing with pytest
- AI-assisted development workflow

## Technologies Used

- Python 3.x
- pytest
- Git & GitHub
- Visual Studio Code
- ChatGPT / Generative AI tools

## Prompt Evolution and AI Usage

The project used iterative prompt engineering to gradually improve the password audit tool from a basic prototype into a more professional security-focused application.

### Stage 1 — Initial Project Setup

#### Prompt
Create a beginner-friendly Python password audit tool that checks password strength and provides user recommendations.

#### Outcome
Generated the first working prototype containing:
- Length checks
- Uppercase/lowercase checks
- Numeric validation
- Basic password scoring

---

### Stage 2 — Security Improvements

#### Prompt
Review this Python password audit tool and suggest security-related improvements while keeping the implementation beginner-friendly.

#### Outcome
AI suggested:
- Common weak password detection
- Improved scoring consistency
- Better feedback messages
- Cleaner code structure

Human review was applied before implementation.

---

### Stage 3 — Testing and Validation

#### Prompt
Generate realistic weak, medium, and strong password test cases for a Python password auditing application.

#### Outcome
AI-assisted test scenarios were used to validate:
- Weak password detection
- Medium password classification
- Strong password scoring behavior

---

### Stage 4 — User Experience and Professional Output

#### Prompt
Enhance this Python password audit tool by adding color-coded terminal output for Weak, Medium, and Strong password classifications.

#### Outcome
The tool was improved using:
- Red warning indicators for weak passwords
- Yellow indicators for medium passwords
- Green success indicators for strong passwords

This improved readability and user experience.

---

### Stage 5 — Advanced Security Enhancement

#### Prompt
Enhance this Python password audit tool by implementing a professional security reminder feature. When a password is classified as Strong, display a green success message along with a cybersecurity best-practice reminder advising users to update their passwords every 30 days.

#### Outcome
The final version of the tool:
- Displays professional security messages
- Provides password rotation reminders
- Simulates real-world cybersecurity guidance
- Demonstrates AI-assisted iterative improvement

## Installation

Clone the repository:

```bash
git clone https://github.com/Ayoubi78/password-audit-tool.git
cd password-audit-tool


## AI-Assisted Development

Generative AI tools were used during:
- Brainstorming
- Initial code drafting
- Refactoring suggestions
- Test-case ideas
- Documentation structure

All AI-generated outputs were manually reviewed, tested, and refined before inclusion in the final project.

## Project Structure

password-audit-tool/
│
├── audit.py
├── test_audit.py
├── README.md
├── project_log.md
└── prompts_used.md

## Security Notes

This tool is designed for educational purposes only.

It does not:
- Store passwords
- Transmit user data
- Connect to external services

All password analysis is performed locally.

## Future Improvements

Possible future enhancements include:
- GUI or web interface
- Breached-password API integration
- Password entropy calculation
- Exportable audit reports
- Machine-learning-based scoring

## How to Run
```bash
python audit.py