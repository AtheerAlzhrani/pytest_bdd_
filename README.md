#  DuckDuckGo Web UI BDD Tests

This project uses `pytest-bdd` and Selenium WebDriver to test the [DuckDuckGo](https://duckduckgo.com) search engine through browser-based behavior-driven development (BDD).

---

### 📁 Structure

- `features/` – Gherkin scenarios describing expected web search behavior  
- `tests/` – Step definitions that automate browser actions using Selenium

---

### ✅ What It Tests

Two scenarios verify that DuckDuckGo's web interface returns relevant results for:

- 🔍 `"Koala"`  
- 📜 A long historical quote from the Declaration of Independence

Each test checks:

- The DuckDuckGo homepage loads successfully  
- Search results appear for the entered phrase  
- At least one result contains the expected keyword or phrase

---
