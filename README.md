# NetHyTech Background Remover 🌐

Welcome to **NetHyTech Background Remover**! This project is an AI-powered, web-based tool that instantly removes backgrounds from images, providing professional-quality results for various applications, including e-commerce, presentations, and social media.

### Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Freezing the App for GitHub Pages](#freezing-the-app-for-github-pages)
- [Deployment](#deployment)
- [License](#license)

---

## Features

- **Instant Background Removal**: Removes image backgrounds using AI technology, perfect for professional use cases.
- **User-Friendly Interface**: Simple and intuitive UI, optimized for ease of use and accessibility.
- **Mobile-Responsive Design**: Works seamlessly on desktops, tablets, and mobile devices.
- **Automated Deployment**: Uses GitHub Actions to automatically deploy updates to GitHub Pages.
- **Downloadable Results**: Allows users to download the processed images directly.

## Tech Stack

- **Frontend**: HTML, CSS (with animations and gradients), JavaScript
- **Backend**: Python, Flask (for local development and testing)
- **Static Generation**: Frozen-Flask (converts Flask app to static files)
- **Deployment**: GitHub Pages via GitHub Actions

---

## Screenshots

![NetHyTech Background Remover Interface](https://via.placeholder.com/800x400?text=Screenshot+Placeholder)

---

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.8 or later
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/nethytech-background-remover.git
   cd nethytech-background-remover
   ```

2. **Set up a virtual environment and activate it (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

To run the Flask app locally, use:

```bash
python app.py
```

This will start the app locally at `http://127.0.0.1:5000`.

> **Note**: The app includes an automated script (`freezer.freeze()`) to generate static HTML files for deployment. For testing locally, you may skip this step until you’re ready to deploy.

---

## Freezing the App for GitHub Pages

This app uses **Frozen-Flask** to convert the dynamic Flask app into a static website that can be hosted on GitHub Pages.

1. **Install Frozen-Flask:**
   ```bash
   pip install Frozen-Flask
   ```

2. **Run the Freezer Script:**
   ```bash
   python app.py
   ```

3. The generated static files will be saved in a folder named `build/`. This folder will be used for deployment.

---

## Deployment

The app uses GitHub Actions to automate deployment to GitHub Pages.

1. **Configure GitHub Pages**:
   - In your GitHub repository, go to **Settings** > **Pages**.
   - Set the source branch to `gh-pages` (GitHub Actions will automatically create this branch).

2. **GitHub Actions Workflow**:
   The repository includes a GitHub Actions workflow (`deploy.yml`) in `.github/workflows/`. The workflow:
   - Builds and freezes the Flask app into static files.
   - Deploys the static files to GitHub Pages.

### Manual Deployment Steps

If you want to manually deploy or test the workflow:

1. **Push changes to the main branch**:
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```

2. GitHub Actions will automatically run the workflow and deploy the site to `https://your-username.github.io/repository-name`.

### Workflow Configuration

The deployment workflow (`.github/workflows/deploy.yml`) is configured to:
- Install dependencies.
- Generate static files from the Flask app using Frozen-Flask.
- Deploy the `build/` directory to the `gh-pages` branch.

#### Example `deploy.yml` Workflow

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Check out the repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install Frozen-Flask

      - name: Generate static files
        run: python app.py  # Freezes the Flask app to static files

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./build
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

