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