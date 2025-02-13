import pytest
from unittest.mock import patch
from io import StringIO
import sys
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_spell_word():
    # Redirect stdout to capture print statements
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Import and run the student's function
    from assignment import spell_word
    spell_word()
    
    # Get the printed output
    output = captured_output.getvalue().strip()
    
    # Reset stdout
    sys.stdout = sys.__stdout__
    
    # Split output into lines and remove any empty lines
    letters = [line.strip() for line in output.split('\n') if line.strip()]
    
    # Check if the letters spell "PYTHON"
    expected = ["P", "Y", "T", "H", "O", "N"]
    assert letters == expected, f"Expected the letters to spell 'PYTHON', but got {''.join(letters)}"
