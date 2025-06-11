# 🛠️ DevOps Log Analyzer

![CI](https://github.com/Gautam-Yedla/devops-log-analyzer/actions/workflows/ci.yml/badge.svg)

A production-style DevOps pipeline that analyzes log files for errors and warnings using Python, sends email alerts on findings, and integrates with Docker, Jenkins, and GitHub Actions for full CI/CD automation.

---

## 📌 Project Objective

To build an automated, end-to-end DevOps workflow that:

- Analyzes logs for `ERROR` and `WARNING` patterns
- Sends **email alerts** for both errors and successful analysis
- Runs inside a **Docker container**
- Automatically builds and tests using **Jenkins** and **GitHub Actions**
- Demonstrates core DevOps concepts in action

---

## ✅ What I Built & Learned

| Area                  | Highlights                                                                 |
|-----------------------|---------------------------------------------------------------------------|
| **Python**            | Built a script that analyzes logs and sends alerts using `smtplib`        |
| **Docker**            | Containerized the Python app for portability                              |
| **Jenkins**           | Configured a multistage CI/CD pipeline with automated GitHub webhook      |
| **GitHub Actions**    | Added CI workflow with test coverage badge                                |
| **Pytest**            | Implemented unit tests and test coverage reports                          |
| **Email Integration** | Sent dynamic alerts using `.env` configuration and SMTP                   |
| **Secrets Handling**  | Managed credentials via `.env` and GitHub Actions secrets                 |

---

## 🧰 Tech Stack

- 🐍 Python 3.11
- 🐳 Docker
- ⚙️ Jenkins
- 🔁 Git & GitHub
- 📬 SMTP (Gmail or custom)
- ✅ Pytest + Coverage
- 🚀 GitHub Actions

---

## 📂 Project Structure

```

devops-log-analyzer/
├── app/
│   ├── main.py               # Log analysis and email alerts
│   ├── utils/
│   │   └── email\_alerts.py   # Sends email notifications
│   └── sample\_logs/
│       └── app.log           # Example log input
├── tests/
│   └── test\_main.py          # Pytest test cases
├── .env                      # Email credentials (ignored in Git)
├── .gitignore
├── Dockerfile
├── Jenkinsfile
├── ci.yml                    # GitHub Actions CI
├── requirements.txt
└── README.md

````

---

## 🚀 How to Run Locally (with Docker)

1. Clone the repository:

   ```bash
   git clone https://github.com/Gautam-Yedla/devops-log-analyzer.git
   cd devops-log-analyzer
````

2. Create a `.env` file with email credentials:

   ```env
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASS=your_password
   EMAIL_FROM=your_email@gmail.com
   EMAIL_TO=recipient@example.com
   ```

3. Build the Docker image:

   ```bash
   docker build -t log-analyzer .
   ```

4. Run the container:

   ```bash
   docker run --env-file .env log-analyzer
   ```

5. Example Output:

   ```text
   ⚠️ Warnings:
   WARNING Disk space is low

   ❌ Errors:
   ERROR Failed to connect to database

   📧 Email alert sent successfully!
   ```

---

## 🧪 Testing the Application

1. Run tests with coverage:

   ```bash
   set PYTHONPATH=.
   pytest --cov=app --cov-report=term-missing
   ```

2. Example Test Output:

   ```
   ---------- coverage: platform win32 ----------
   Name                        Stmts   Miss  Cover
   ------------------------------------------------
   app/main.py                    30     10    67%
   app/utils/email_alerts.py      12      0   100%
   ------------------------------------------------
   TOTAL                          42     10    76%
   ```

---

## 🤖 Jenkins Pipeline

The `Jenkinsfile` defines the stages:

* 🧱 Build Docker Image
* 🔍 Run Log Analysis
* ✅ Run Pytest with Coverage
* 🔁 Triggered automatically via GitHub webhook (using ngrok or public Jenkins)

### Jenkins Auto-Trigger Setup:

* Uses **GitHub Webhook** via `https://<ngrok-url>/github-webhook/`
* `Build Trigger`: "GitHub hook trigger for GITScm polling" is enabled

---

## 🧬 GitHub Actions CI

* Runs on every push to `main`
* Installs dependencies and runs `pytest` with coverage
* Automatically updates badge in `README.md`

```yaml
# .github/workflows/ci.yml
- uses: actions/checkout@v3
- uses: actions/setup-python@v4
- run: pytest --cov=app --cov-report=term-missing
```

---

## 🧠 Future Enhancements

* [x] Email alerts
* [x] Pytest test coverage
* [x] Jenkins GitHub webhook auto-trigger
* [ ] Slack or Discord notifications
* [ ] DockerHub push on successful builds
* [ ] Schedule Jenkins runs via cron
* [ ] Central log dashboard (ELK, Loki)

---

## 🙌 Author

**Gautam Yedla**
A DevOps learner passionate about automation, CI/CD, and infrastructure as code.

---

