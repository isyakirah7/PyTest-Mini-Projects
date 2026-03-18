# PyTest-Mini-Projects

## Description
A beginner-friendly demonstration of the **Software Testing Life Cycle (STLC)**
using Python and Pytest. This project covers writing and running unit tests
for user authentication and basic arithmetic operations.

---

## Project Structure
PyTest-Mini-Projects/
├── app.py          # Application logic
├── test_app.py     # Unit test cases
└── .gitignore      # Ignored files

---

## Test Cases Covered

### 🔐 User Authentication (validate_user)
| Test | Input | Expected Output |
|------|-------|----------------|
| Valid credentials | admin / admin123 | Login successful |
| Invalid password | admin / wrongpass | Invalid credentials |
| Empty password | user1 / "" | Username or password cannot be empty |
| Short password | user1 / 123 | Password too short |
| Case sensitivity | Admin / admin123 | Invalid credentials |

### 🧮 Calculator
| Test | Input | Expected Output |
|------|-------|----------------|
| Add | 2 + 3 | 5 |
| Subtract | 5 - 3 | 2 |
| Multiply | 4 × 3 | 12 |
| Divide | 10 / 2 | 5 |
| Divide by zero | 5 / 0 | ValueError |

---

## Tech Stack
- Python 3.13
- Pytest

---

## How to Run

# Clone the repo
git clone https://github.com/isyakirah7/PyTest-Mini-Projects.git

# Create virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# Install dependencies
pip install pytest

# Run tests
pytest -v

---

## Test Results
All 9 test cases passing ✅

---

## Author
**Isyakirah**
- GitHub: [@isyakirah7](https://github.com/isyakirah7)
