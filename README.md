# Manual-QA-Portfolio

I am a BSCS graduate with manual testing experience, learning QA automation with Python and pytest.

## What's in this repo
- Manual QA test cases (Excel)
- Python functions with automated pytest tests

## How to run the tests
pip install pytest
python -m pytest

## Bugs I found
1. is_palindrome("Madam") returned False because capital letters were treated differently. Fixed by converting the text to lowercase.
2. is_palindrome("race car") returned False because of the space. Fixed by removing spaces before comparing.
3. Added a negative test to confirm "racing car" correctly returns False.

## Roadmap
- Week 2: Playwright UI tests
- Week 3: Page Object Model and fixtures
- Week 4: GitHub Actions CI