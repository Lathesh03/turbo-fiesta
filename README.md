# ☁️ Cloud-Native Two-Tier Application on AWS

![AWS](https://img.shields.io/badge/AWS-EC2-orange) ![Docker](https://img.shields.io/badge/Docker-Compose-blue) ![Python](https://img.shields.io/badge/Python-Flask-yellow) ![MySQL](https://img.shields.io/badge/Database-MySQL-lightgrey)

Author: Lathesh Neikar Krishnappa Harish  
Role: DevOps Engineer / Cloud Student

---

## 📖 Project Overview
This project demonstrates the deployment of a 2-Tier Web Application (Frontend + Database) on the AWS Cloud. 
Unlike traditional deployments, this application is fully containerized using Docker and orchestrated with Docker Compose, ensuring consistency between development and production environments.

The infrastructure is hosted on an AWS EC2 (Ubuntu) instance with custom security group configurations to allow public access.

---

## 🏗️ Architecture
The application consists of two isolated containers running on a custom Docker Bridge Network:
1.  **Frontend:** A Python Flask web application that serves the UI and processes user input.
2.  **Backend:** A MySQL database that stores user messages.

```mermaid
graph TD
    User((User)) -->|Internet| EC2[AWS EC2 Instance]
    subgraph EC2
        Docker[Docker Compose Group]
        subgraph Docker
            App[Flask App Container] <-->|Port 3306| DB[(MySQL Database)]
        end
    end

Technology Stack
Cloud Provider,AWS (EC2),Infrastructure as a Service (IaaS)
OS,Ubuntu 22.04 LTS,Linux Server
Container Engine,Docker,Container runtime
Orchestration,Docker Compose,Multi-container management
Frontend,Python Flask,Web Application Framework
Database,MySQL 5.7,Relational Database
Version Control,Git & GitHub,Source Code Management