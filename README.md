# ToolsForImage

> **Note:** A hosted version of this tool is available for free (and ad-free) at [https://toolsforimage.com/](https://toolsforimage.com/)

A multilingual web application that provides a suite of image processing tools. Built with Flask and Python, this application offers various image manipulation capabilities through an intuitive web interface.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![GitHub issues](https://img.shields.io/github/issues/mlbrothers/ToolsForImage-OSS)](https://github.com/mlbrothers/ToolsForImage-OSS/issues)
[![GitHub stars](https://img.shields.io/github/stars/mlbrothers/ToolsForImage-OSS)](https://github.com/mlbrothers/ToolsForImage-OSS/stargazers)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Available Tools](#available-tools)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [License](#license)
- [Support](#support)

## Features

- **Multi-language Support**: Available in English, Spanish, French, Chinese, and Hindi
- **Image Processing Tools**: Various image manipulation and conversion capabilities including:
  - Image compression
  - Format conversion
  - Resize and crop
  - Watermarking
  - Background removal
  - Image effects and filters
  - And more...
- **Web-based Interface**: No installation required, works directly in your browser
- **Clean and Modern UI**: User-friendly interface with responsive design
- **Privacy-Focused**: All processing happens locally or temporarily - no data is stored

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mlbrothers/ToolsForImage-OSS.git
cd ToolsForImage-OSS
```

2. Create and activate a virtual environment:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Create a .env file with necessary configuration
cp .env.example .env
# Edit .env with your settings
```

## Running the Application

### Development Mode

```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Production Deployment

For production deployment, it's recommended to use a WSGI server like Gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Docker Deployment

Build and run the Docker container:

```bash
# Build the image
docker build -t toolsforimage .

# Run the container
docker run -p 8000:8000 toolsforimage
```

## Project Structure

```
ToolsForImage-OSS/
├── app.py                   # Main Flask application
├── all_blog_data.py         # Blog data configuration
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker configuration
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
├── LICENSE                 # MIT License
├── README.md               # This file
├── CONTRIBUTING.md         # Contribution guidelines
├── CODE_OF_CONDUCT.md      # Code of conduct
├── SECURITY.md             # Security policy
├── .github/                # GitHub templates
│   ├── ISSUE_TEMPLATE/     # Issue templates
│   └── pull_request_template.md
├── static/                 # Static assets (CSS, JS, images)
│   ├── styles.css
│   └── ...
└── templates/              # HTML templates
    ├── en/                 # English templates
    ├── es/                 # Spanish templates
    ├── fr/                 # French templates
    ├── zh/                 # Chinese templates
    └── hi/                 # Hindi templates
```

## Available Tools

- **Image Compression**: Reduce file size while maintaining quality
- **Image Resize**: Change image dimensions
- **Format Conversion**: Convert between JPEG, PNG, WebP, GIF, and more
- **Image Rotation**: Rotate images by any angle
- **Watermarking**: Add text or image watermarks
- **Image Effects**: Apply filters and effects
- **Crop Image**: Crop images to desired dimensions
- **Blur Face**: Privacy protection by blurring faces
- **Remove Background**: Automatic background removal

## Contributing

We welcome contributions from the community! Whether it's bug fixes, new features, documentation improvements, or translations, your help is appreciated.

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:
- How to report bugs
- How to suggest enhancements
- Development setup
- Code style guidelines
- Pull request process
- Adding new languages
- Adding new image tools

Quick start for contributors:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to burstneuron1729@gmail.com.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 ToolsForImage Contributors

## Support

If you encounter any issues or have questions:

- **Bug Reports**: [Open an issue](https://github.com/mlbrothers/ToolsForImage-OSS/issues/new?template=bug_report.md) on GitHub with detailed information
- **Feature Requests**: [Request a feature](https://github.com/mlbrothers/ToolsForImage-OSS/issues/new?template=feature_request.md)
- **Questions**: Check [existing issues](https://github.com/mlbrothers/ToolsForImage-OSS/issues) or open a new one
- **Email**: burstneuron1729@gmail.com

## Security

If you discover a security vulnerability, please send an email to burstneuron1729@gmail.com instead of opening a public issue. We take security seriously and will respond promptly.

## Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/) - Python web framework
- [Pillow](https://python-pillow.org/) - Python Imaging Library for image processing
- [ONNX Runtime](https://onnxruntime.ai/) - For machine learning-based background removal
- [image-conversion](https://github.com/WangYueLue/image-conversion) by WangYueLue - Client-side image conversion
- [Google Fonts](https://fonts.google.com/) - Lato and Inter fonts
- All our amazing contributors

## Roadmap

- [ ] Add more image processing tools
- [ ] Improve mobile responsiveness
- [ ] Add batch processing capabilities
- [ ] Add API endpoints for programmatic access
- [ ] Add more language translations
- [ ] Implement user preferences/settings
- [ ] Add image editing history/undo functionality

## Star History

If you find this project useful, please consider giving it a ⭐ on [GitHub](https://github.com/mlbrothers/ToolsForImage-OSS)!

---

Made with care by the ToolsForImage community | [Report Issues](https://github.com/mlbrothers/ToolsForImage-OSS/issues) | [Contribute](CONTRIBUTING.md)
