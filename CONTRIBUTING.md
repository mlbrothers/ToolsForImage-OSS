# Contributing to ToolsForImage

First off, thank you for considering contributing to ToolsForImage! It's people like you that make ToolsForImage such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to burstneuron1729@gmail.com.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as much detail as possible.
* **Provide specific examples to demonstrate the steps**.
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **Include screenshots and animated GIFs** if possible.
* **Include your environment details** (OS, Python version, browser, etc.).

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title** for the issue to identify the suggestion.
* **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
* **Provide specific examples to demonstrate the steps** or provide mockups.
* **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
* **Explain why this enhancement would be useful** to most ToolsForImage users.

### Pull Requests

* Fill in the required template
* Do not include issue numbers in the PR title
* Follow the Python style guide (PEP 8)
* Include thoughtfully-worded, well-structured tests
* Document new code
* End all files with a newline

## Development Process

### Setting Up Your Development Environment

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ToolsForImage-OSS.git
   cd ToolsForImage-OSS
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up your environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

6. Create a branch:
   ```bash
   git checkout -b feature/my-new-feature
   # or
   git checkout -b fix/my-bug-fix
   ```

### Making Changes

1. Make your changes in your feature branch
2. Add or update tests as necessary
3. Ensure all tests pass
4. Update documentation as needed
5. Follow the code style guidelines

### Code Style Guidelines

* Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
* Use meaningful variable and function names
* Write clear comments for complex logic
* Keep functions small and focused
* Write docstrings for functions and classes

### Testing

Before submitting your pull request, make sure:

* All existing tests pass
* You've added tests for new functionality
* Your code works across different browsers (for frontend changes)
* You've tested on different image formats and sizes

### Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* Consider starting the commit message with an applicable emoji:
  * :sparkles: `:sparkles:` when adding a new feature
  * :bug: `:bug:` when fixing a bug
  * :memo: `:memo:` when writing docs
  * :art: `:art:` when improving the format/structure of the code
  * :fire: `:fire:` when removing code or files
  * :green_heart: `:green_heart:` when fixing the CI build
  * :white_check_mark: `:white_check_mark:` when adding tests
  * :lock: `:lock:` when dealing with security
  * :arrow_up: `:arrow_up:` when upgrading dependencies
  * :arrow_down: `:arrow_down:` when downgrading dependencies

### Submitting Your Contribution

1. Push your changes to your fork:
   ```bash
   git push origin feature/my-new-feature
   ```

2. Open a Pull Request from your fork to the main repository
3. Provide a clear description of the changes
4. Link any related issues
5. Wait for review and address any feedback

## Adding New Languages

We welcome translations to make ToolsForImage accessible to more users:

1. Create a new language directory in `templates/` (e.g., `templates/de/` for German)
2. Copy all template files from `templates/en/`
3. Translate the content while keeping the HTML structure intact
4. Update the language selector in the navigation
5. Test thoroughly to ensure all pages work correctly

## Adding New Image Tools

When adding a new image processing tool:

1. Create the route in `app.py`
2. Create templates for all supported languages
3. Implement the backend logic
4. Add appropriate error handling
5. Test with various image formats (JPEG, PNG, GIF, WebP, etc.)
6. Update documentation
7. Add the tool to the navigation menu

## Questions?

Don't hesitate to ask questions! You can:

* Open an issue with your question
* Contact us at burstneuron1729@gmail.com

## Recognition

Contributors who make significant contributions will be recognized in the project README.

Thank you for contributing to ToolsForImage!
