# 📚 Hybrid Library API Test Automation Framework

This repository contains an end-to-end API test automation framework that seamlessly integrates **Postman/Newman** execution into a **Python (Pytest)** ecosystem.

## 🚀 Key Features
* **Automated CRUD Scenario**: Chained requests handling book creation, data verification, and cleanup (DELETE).
* **Python Subprocess Integration**: Completely automated execution via Python's `subprocess` engine with UTF-8 encoding support.
* **Dynamic Variable Chaining**: Automatically extracts dynamic `ID` values between test layers without manual hardcoding.
* **CI/CD Ready**: Generates visual HTML test reports on every local or remote Pytest run.

## 🛠️ Tech Stack & Tools
* **Language/Framework**: Python 3.12+ & Pytest
* **CLI Runner**: Node.js & Newman CLI
* **Reporting**: Newman-reporter-htmlextra
* **Target API**: `https://postmanlabs.com`

## 📁 Repository Structure
* `test_api_runner.py`: The Python test script that orchestrates and triggers the Newman execution.
* `My Collection.postman_collection.json`: The core Postman automation test layers.
* `postman_advanced_report.html`: Visual HTML artifact generated dynamically by the Pytest execution.

## 💻 How to Run the Framework
1. Clone or download this repository.
2. Ensure you have installed Newman via npm (`npm install -g newman newman-reporter-htmlextra`).
3. Run the automated bridge script via terminal:
   ```bash
   pytest -s -v
   ```
