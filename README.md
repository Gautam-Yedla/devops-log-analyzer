# DevOps Log Analyzer

![CI](https://github.com/Gautam-Yedla/devops-log-analyzer/actions/workflows/ci.yml/badge.svg)

A log analyzer tool built using Python, Docker, Jenkins, and GitHub Actions. Automatically sends email alerts on errors or success after log analysis.

...

A professional and clear `README.md` content for My **DevOps Log Analyzer** project. It covers:

* What the project is
* What you learned
* Technologies used
* How everything works
* How to run it locally and in Jenkins

---

```markdown
# 🛠️ DevOps Log Analyzer

A simple yet complete DevOps pipeline that analyzes application logs for errors and warnings using a Python script. This project demonstrates full CI/CD implementation using GitHub, Docker, and Jenkins.

---

## 📌 Project Objective

To build an automated system that:
- Analyzes log files for "ERROR" and "WARNING" entries
- Runs inside a Docker container
- Is integrated with a Jenkins CI/CD pipeline
- Demonstrates end-to-end DevOps workflow

---

## ✅ What We Learned & Implemented

| Area | What We Did |
|------|-------------|
| **Python Scripting** | Wrote a Python script to parse logs and print warnings/errors |
| **Docker** | Containerized the application using a lightweight Python image |
| **Jenkins** | Set up a multistage pipeline that checks out code, builds the image, and runs the analysis |
| **Git & GitHub** | Used Git for version control and GitHub as remote repository |
| **CI/CD Workflow** | Automated the entire workflow from code pull to execution |
| **Debugging & Logs** | Resolved issues like missing file paths and Docker context handling |

---

## 🧰 Tech Stack

- 🐍 Python 3.11
- 🐳 Docker
- ⚙️ Jenkins
- 📁 Git & GitHub
- 🖥️ VS Code (for development)

---

## 📂 Project Structure

```

devops-log-analyzer/
├── app/
│   ├── main.py          # Main log analyzer script
│   ├── utils.py         # Helper (optional)
│   └── sample\_logs/
│       └── app.log      # Sample log file
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── README.md

````

---

## 🚀 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/Gautam-Yedla/devops-log-analyzer.git
   cd devops-log-analyzer
````

2. Build the Docker image:

   ```bash
   docker build -t log-analyzer .
   ```

3. Run the container:

   ```bash
   docker run -it log-analyzer
   ```

4. Output:

   ```text
   ⚠️ Warnings:
   WARNING Disk space is low

   ❌ Errors:
   ERROR Failed to connect to database
   ```

---

## 🤖 Jenkins Pipeline (CI/CD)

The `Jenkinsfile` contains a declarative pipeline that does the following:

* Clones the GitHub repo
* Builds the Docker image (`log-analyzer`)
* Runs the container
* Prints log analysis results in Jenkins console

### Sample Output in Jenkins Console:

```
⚠️ Warnings:
WARNING Disk space is low

❌ Errors:
ERROR Failed to connect to database
```

---

## 🧪 Future Improvements

* Add test cases and integrate with `pytest`
* Add email or Slack alerts if errors are found
* Upload results to a database or dashboard
* Push Docker image to DockerHub
* Schedule periodic analysis via Jenkins cron

---

## 🙌 Credits

Developed by **Gautam Yedla** as a hands-on DevOps learning project.

```


