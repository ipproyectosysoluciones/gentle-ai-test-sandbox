# Usage Guide for Gentle AI QA Sandbox

1. What is this repository?
   This is a disposable project for gentle-ai beta testing.
   As per the beta-testers policy: "test in a project you don't mind breaking".

2. How evidence is used in review-assess proportionality tests
   - QA-NOTES.md serves as passive evidence of testing activities.
   - auth/session.py is the high-risk surface evidence (because it handles authentication and session management).

3. The disposable rule
   - Anything in this repository can be recreated at any time.
   - Never use this repository for real work or to store meaningful data.
   - Treat it as a temporary environment for testing only.

Notes:
   - This repository is intentionally ephemeral.
   - Do not attach any value to the content herein.
   - After testing, the entire repository may be discarded.

Additional details:
   - Feel free to break anything in this repo to test gentle-ai features.
   - Use QA-NOTES.md to jot down observations during testing.
   - The auth/session.py file is monitored for changes as part of the high-risk surface.

Remember:
   - This is a sandbox, not a production environment.
   - Any data here is not backed up or preserved.
   - If you lose data, it is by design and expected.

Enjoy testing!

---
For more information on the gentle-ai beta testing program,
see the internal documentation or contact the gentle-ai team.

This file is auto-generated and should be updated as needed.
Last updated: manual update

End of guide