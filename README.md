# UI Automation Framework - Profile Form

This project is a data-driven UI test automation framework built using **PyTest**, **Selenium**, and the **Page Object Model (POM)** pattern. 
It automates the form submission on https://demoqa.com/automation-practice-form.

---

## 📁 Project Structure

```
profile_form_framework/
│
├── config/                     # Contains environment-specific YAML config
│   └── config.yaml
│
├── pages/                      # Page Object Model files
│   └── profile_form_page.py
│
├── tests/                      # Test cases using PyTest
│   └── test_profile_form.py
│
├── utils/                      # Utility functions
│   └── data_loader.py
│
├── conftest.py                 # Shared fixtures and setup/teardown logic
├── requirements.txt            # Project dependencies
├── pytest.ini                  # PyTest configuration file
└── README.md                   # Project documentation
```

---

## ⚙️ Installation

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🔧 Configuration

Edit the `config/config.yaml` to update form URL:

```yaml
form_url: "https://demoqa.com/automation-practice-form"
```

---

## 🧪 Running the Tests

### Headed Mode (see browser):

```bash
pytest -v
```

### Headless Mode:

```bash
pytest -v --headless
```

### Generate Allure Report:

```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## 📌 Features

- Data-driven testing with `@pytest.mark.parametrize`
- Configurable browser and environment using `config.yaml`
- Modular design using POM (Page Object Model)
- Allure reporting support
- Parallel test execution ready (`pytest-xdist`)

---

## 👤 Author

**Abhishek Anand**  
📧 [abhishek.2007anand@gmail.com]  
📍 India  
🔗 [https://www.linkedin.com/in/abhishek-anand-13121944/]
