# Student Feedback Portal

A simple Python Flask web application for students to submit feedback, integrated with Git, Jenkins, Docker, and Kubernetes (MicroK8s) for DevOps practice.

---

## 📌 Features

- Submit and display student feedback
- Flask-based backend with HTML frontend
- Containerized using Docker
- CI/CD using Jenkins
- Deployed on Kubernetes (MicroK8s)

---

## ✅ Prerequisites

- Python 3.x
- Docker
- Jenkins
- MicroK8s (or any Kubernetes cluster)
- Git

---

## 🚀 How to Run Locally (Without Docker)

```bash
git clone https://your-repo-url.git
cd student-feedback-portal
pip install -r requirements.txt
python app.py
```

Then open your browser: `http://localhost:5000`

---

## 🐳 How to Build & Run with Docker

```bash
docker build -t student-feedback .
docker run -p 5000:5000 student-feedback
```

Then open your browser: `http://localhost:5000`

---

## 🤖 Jenkins Pipeline Steps

1. Open Jenkins and create a new pipeline job.
2. Paste the contents of the `Jenkinsfile` into the pipeline configuration.
3. Add your DockerHub credentials in Jenkins under **Credentials** (ID: `dockerhub-credentials`).
4. Run the pipeline.

---

## ☸️ Deploy on MicroK8s

### Step 1: Enable MicroK8s and Docker registry (if not already)

```bash
microk8s enable dns storage ingress
```

### Step 2: Apply Kubernetes configs

```bash
microk8s kubectl apply -f k8s/deployment.yaml
microk8s kubectl apply -f k8s/service.yaml
```

### Step 3: Access the App

Find the NodePort with:

```bash
microk8s kubectl get svc feedback-service
```

Open in browser: `http://<your-node-ip>:<nodePort>`

---

## 📝 Notes

- Replace `yourdockerhub/student-feedback` in `deployment.yaml` with your actual DockerHub username/repo.
- Update `Jenkinsfile` with your Git repository URL.

---

Happy DevOps learning! 🚀
# sample-project-1
