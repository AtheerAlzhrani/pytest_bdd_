# 🧪 DuckDuckGo BDD Test Suite

This repository contains behavior-driven tests for the [DuckDuckGo](https://duckduckgo.com) search engine, covering both its public API and web interface using `pytest-bdd`.

---

## 📁 Project Structure

```
pytest_bdd_project/
├── features/
│   ├── service.feature       # API test scenarios
│   └── web.feature           # Web UI test scenarios
├── tests/
│   ├── test_service.py       # API step definitions
│   └── test_web.py           # Web UI step definitions
├── .gitignore
└── README.md
```

---

## ✅ Features

### 🔌 API Testing (`service.feature`)
Tests the DuckDuckGo Instant Answer API with search terms like:
- Animals: `panda`, `python`, `platypus`
- Fruits: `peach`, `pineapple`, `papaya`

Each test checks:
- HTTP status code is `200` or `202`
- Response contains the search phrase in the heading

### 🌐 Web UI Testing (`web.feature`)
Uses Selenium to simulate user searches in a browser:
- Basic search for `"Koala"`
- Long-form search for a historical quote, expecting `"Declaration of Independence"` in results

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install pytest pytest-bdd selenium requests
```

### 2. Set Up ChromeDriver

Download [ChromeDriver](https://sites.google.com/chromium.org/driver/) and update the path in `test_web.py`:
```python
Service("C:/Drivers/chromedriver-win64/chromedriver/chromedriver.exe")
```

### 3. Run Tests

```bash
pytest
```

---

## 🛠️ Tools Used

- Python 3.x  
- [pytest](https://docs.pytest.org/)  
- [pytest-bdd](https://pytest-bdd.readthedocs.io/)  
- [Selenium](https://www.selenium.dev/)  
- [Requests](https://docs.python-requests.org/)

---

Let me know if you'd like to add badges, CI integration, or test reports!
