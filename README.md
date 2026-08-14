# ☁️ S4 Cloud Web Application

> A modern cloud-ready web application demonstrating containerization, PostgreSQL integration, automated testing, CI/CD practices, and static cloud deployment.

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Visit%20Website-00C7B7?style=for-the-badge)](https://symphonious-zuccutto-ec83b3.netlify.app)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/sathwik-svg/s4-cloud-web-application)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

---

## 🚀 Live Demo

### 🌐 [Open S4 Cloud Web Application](https://symphonious-zuccutto-ec83b3.netlify.app)

A responsive cloud-focused web interface showcasing the architecture, technology stack, CI/CD workflow, containerization strategy, and deployment status of the project.

---

## 📌 Project Overview

**S4 Cloud Web Application** is a full-stack cloud engineering project designed to demonstrate practical software engineering and DevOps concepts.

The project combines:

- Python Flask
- PostgreSQL
- SQLAlchemy
- Docker
- Docker Compose
- GitHub Actions
- Automated testing
- REST-style health endpoints
- Static cloud deployment
- Git-based development workflow

The application is structured to demonstrate how a development project can progress from local development to containerized deployment and cloud hosting.

---

## 🏗️ Architecture

```text
                     ┌──────────────────┐
                     │    Developer     │
                     └────────┬─────────┘
                              │
                              ▼
                     ┌──────────────────┐
                     │      GitHub      │
                     │  Source Control  │
                     └────────┬─────────┘
                              │
                              ▼
                     ┌──────────────────┐
                     │ GitHub Actions   │
                     │   CI / Testing   │
                     └────────┬─────────┘
                              │
                              ▼
                     ┌──────────────────┐
                     │      Docker      │
                     │  Containerized   │
                     │   Application    │
                     └────────┬─────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
             ┌─────────────┐     ┌─────────────┐
             │    Flask    │     │ PostgreSQL  │
             │   Backend   │────▶│  Database   │
             └──────┬──────┘     └─────────────┘
                    │
                    ▼
             ┌────────────────┐
             │  Cloud / Web   │
             │   Deployment   │
             └────────────────┘
