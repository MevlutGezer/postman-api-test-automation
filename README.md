# 📚 Library API Test Automation Project

This repository contains an end-to-end API test automation suite built with Postman for the official Postmanlabs Library API, designed to complement Python-based QA workflows.

## 🚀 Key Features
* **Automated CRUD Scenario**: Chained requests for creating and retrieving books dynamically.
* **Dynamic Variable Chaining**: Automatically extracts the `ID` from a newly created book response and stores it as a collection variable (`current_book_id`) for subsequent requests.
* **Python Framework Integration**: Structured cleanly to enable seamless export and execution via Python subprocesses or CLI runner tools.

## 🛠️ Tech Stack & Tools
* **Tool**: Postman
* **Primary QA Stack**: Python Integration Ready (Pytest / Behave)
* **Target API**: `https://postmanlabs.com`

## 📁 Repository Structure
* `My Collection.postman_collection.json`: The core Postman test collection containing endpoints, payloads, and scripts.
* `README.md`: Project documentation and specifications.

## 💻 How to Run the Tests
1. Download or clone this repository.
2. Open **Postman**.
3. Click on the **Import** button and select the `My Collection.postman_collection.json` file.
4. Run the collection sequentially: **1. Create Book** followed by **2. Get Book**.
