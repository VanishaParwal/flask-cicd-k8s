
# flask-cicd-k8s
![CI/CD](https://github.com/VanishaParwal/flask-cicd-k8s/actions/workflows/deploy.yml/badge.svg)

 
# BookShelfPro 📚

A production-grade Flask REST API to manage books. Designed for CI/CD and Kubernetes deployments.

## Features
- RESTful API (GET, POST)
- Modular structure
- Input validation
- Dockerized
- CI/CD and K8s-ready

## Run Locally
```bash
docker build -t bookshelfpro .
docker run -p 5000:5000 bookshelfpro
