import os
import subprocess
import sys
import tempfile
import unittest

class TestNotesStats(unittest.TestCase):
    def setUp(self):
        self.script_dir = os.path.dirname(__file__)
        self.script_path = os.path.join(self.script_dir, 'notes_stats.py')

    def test_counts_correctly(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            notes_content = """# Title
## Section 1
Some text
## Section 2
More text
## Not a section to count
## Section 3
"""
            notes_file = os.path.join(tmpdir, 'QA-NOTES.md')
            with open(notes_file, 'w') as f:
                f.write(notes_content)
            
            result = subprocess.run([sys.executable, self.script_path], 
                                    cwd=tmpdir,
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), 'sections: 3')

    def test_exits_when_file_missing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Ensure QA-NOTES.md does not exist
            notes_file = os.path.join(tmpdir, 'QA-NOTES.md')
            if os.path.exists(notes_file):
                os.remove(notes_file)
            
            result = subprocess.run([sys.executable, self.script_path], 
                                    cwd=tmpdir,
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("Error: QA-NOTES.md not found", result.stderr)

    def test_only_counts_section_headers(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            notes_content = """## Section 1
##Section 2
## Section 3
## Section 4 extra
##  Section 5
"""
            notes_file = os.path.join(tmpdir, 'QA-NOTES.md')
            with open(notes_file, 'w') as f:
                f.write(notes_content)
            
            result = subprocess.run([sys.executable, self.script_path], 
                                    cwd=tmpdir,
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0)
            # Only lines 1, 3, 4 start with '## Section ' (note: line 2 missing space, line 5 has two spaces)
            # So we expect 3
            self.assertEqual(result.stdout.strip(), 'sections: 3')

if __name__ == '__main__':
    unittest.main()