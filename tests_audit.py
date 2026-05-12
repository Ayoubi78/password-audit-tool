
---

# Part E — Add simple test file (easy marks)

## Step 11: Copy this into `test_audit.py`

```python
from audit import check_password

def test_weak_password():
    score, strength, _ = check_password("password")
    assert strength == "Weak"

def test_medium_password():
    score, strength, _ = check_password("Hello123")
    assert strength in ["Medium", "Weak"]  # depending on score thresholds

def test_strong_password():
    score, strength, _ = check_password("My$ecurePass2026!")
    assert strength == "Strong"