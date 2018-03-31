## Contributing
This page is directly taken from the Mycroft CONTRIBUTING page: https://github.com/MycroftAI/mycroft-core/blob/dev/CONTRIBUTING.md 

# How to prepare
- You need a GitHub account
- Submit an issue ticket for your issue if there is not one yet.
- Describe the issue and include steps to reproduce if it's a bug.
- Ensure to mention the earliest version that you know is affected.
- If you are able and want to fix this, fork the repository on GitHub

# Make Changes
- Fork the Project
- Create a new Issue
- Create a feature or bugfix branch based on dev with your issue identifier. For example, if your issue identifier is: issue-123 then you will create either: 
feature/issue-123 or bugfix/issue-123. Use feature prefix for issues related to new functionalities or enhancements and bugfix in case of bugs found on the dev branch
- Make sure you stick to the coding style and OO patterns that are used already.
- Document code using Google-style docstrings. Our automated documentation tools expect that format. All functions and class methods that are expected to be 
called externally should include a docstring. (And those that aren't should be prefixed with a single underscore).
- Make commits in logical units and describe them properly. Use your issue identifier at the very begin of each commit. For instance: 
git commit -m "Issues-123 - Fixing 'A' sound on Spelling Skill"
- Before committing, format your code following the PEP8 rules and organize your imports removing unused libs. To check whether you are following these rules, 
install pep8 and run pep8 mycroft test while in the mycroft-core folder. This will check for formatting issues in the mycroft and test folders.
- Once you have committed everything and are done with your branch, you have to rebase your code with dev. Do the following steps:
- Make sure you do not have any changes left on your branch
- Checkout on dev branch and make sure it is up-to-date
- Checkout your branch and rebase it with dev
- Resolve any conflicts you have
- You will have to force your push since the historical base has changed

# Suggested steps are:
- git checkout dev
- git fetch
- git reset --hard origin/dev
- git checkout <your_branch_name>
- git rebase dev
- git push -f
- If possible, create unit tests for your changes
- Unit Tests for most contributions
- Intent Tests for new skills
- We utilize TRAVIS-CI, which will test each pull request. To test locally you can run: ./start.sh unittest
- Once everything is OK, you can finally create a Pull Request (PR) on Github in order to be reviewed and merged.
- Note: Even if you have write access to the master branch, do not work directly on master!

# Submit Changes
- Push your changes to a topic branch in your fork of the repository.
- Open a pull request to the original repository and choose the right original branch you want to patch. Advanced users may install the hub gem and 
use the hub pull-request command.
- If not done in commit messages (which you really should do) please reference and update your issue with the code changes. But please do not close 
the issue yourself.
- Even if you have write access to the repository, do not directly push or merge pull-requests. Let another team member review your pull request and 
approve.

# Additional Resources
- General GitHub documentation
- GitHub pull request documentation