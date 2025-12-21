# ☁️ Automated CI/CD Pipeline for 2-Tier Flask App

![AWS](https://img.shields.io/badge/AWS-EC2-orange) ![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red) ![Docker](https://img.shields.io/badge/Docker-Compose-blue) ![Python](https://img.shields.io/badge/Python-Flask-yellow)

**Author:** Lathesh Neikar Krishnappa Harish  
**Role:** DevOps Engineer / Cloud Student

---

## 📖 Project Overview
This project demonstrates a fully automated **CI/CD Pipeline** for a containerized 2-Tier Web Application. 
Every change pushed to GitHub automatically triggers **Jenkins** to build new Docker images and deploy them to the **AWS EC2** production server, ensuring Zero-Touch deployment.

---

## 🏗️ Architecture & Workflow
The pipeline automates the lifecycle from Code Commit to Production Deployment.

```mermaid
graph LR
    Dev[Developer] -->|Push Code| Git[GitHub Repo]
    Git -->|Trigger| Jenkins[Jenkins Server]
    subgraph AWS_EC2
        Jenkins -->|1. Checkout| Code[Source Code]
        Jenkins -->|2. Build| Image[Docker Image]
        Jenkins -->|3. Deploy| App[Flask + MySQL Containers]
    end
    App -->|Serve| User((User))