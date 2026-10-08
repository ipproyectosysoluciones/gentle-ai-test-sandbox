#!/usr/bin/env python3
import sys
import os

def main():
    notes_file = 'QA-NOTES.md'
    if not os.path.exists(notes_file):
        print(f"Error: {notes_file} not found", file=sys.stderr)
        sys.exit(1)
    
    count = 0
    with open(notes_file, 'r') as f:
        for line in f:
            if line.startswith('## Section '):
                count += 1
    
    print(f'sections: {count}')

if __name__ == '__main__':
    main()