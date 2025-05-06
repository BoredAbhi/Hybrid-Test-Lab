# Hybrid-Test-Lab 
A hybrid UI + API automation testing framework built using **Selenium**, **Behave**, **Python**, **Requests**, and integrated with **Jenkins**, **Docker**, and **Allure Reports**.

This project demonstrates an end-to-end automated test pipeline, suitable for **cloud-native apps**, and designed for **scalability, maintainability**, and **CI/CD integration**.

---

## 📦 Tech Stack

| Layer        | Tools & Frameworks                     |
|--------------|----------------------------------------|
| UI Testing   | Selenium WebDriver, Page Object Model  |
| API Testing  | Python Requests                        |
| BDD          | Behave                                 |
| CI/CD        | Jenkins (pipeline + Docker integration)|
| Reporting    | Allure Reports                         |
| Containers   | Docker (Dockerfile-based runs)         |
| Utils        | Custom Logger, Browser Manager         |

---

## 🌐 Target Application

This framework tests the login functionality of:  
🔗 [SauceDemo](https://www.saucedemo.com/)

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone [https://github.com/yourname/hybridtestlab.git](https://github.com/BoredAbhi/Hybrid-Test-Lab.git)
cd Hybrid-Test-Lab
```

### 2. Set Up the Environment

```bash
pip install -r requirements.txt
```
Make sure `allure` CLI is installed (Install Guide: https://docs.qameta.io/allure/).

### 3. Running the tests:

UI + API Tests via Behave: `behave`

Run in Docker:
```bash
docker build -t hybridtestlab .
docker run --rm hybridtestlab
```

### 4. Generating Allure Reports

```bash
allure generate reports --clean -o reports/allure_report
allure serve reports/allure_report
```

