
---

## k8s-python-app-kustomize**
```markdown
# Kubernetes Python App with Kustomize

This project deploys a simple **Python HTTP server** on **Kubernetes**, using:
- **Deployment** for scaling
- **Service** for networking
- **Ingress** for external access
- **Kustomize** for configuration management

---


##  Setup
1. Build and push your image:
   docker build -t ghcr.io/<your-username>/k8s-python-app:latest app
   docker push ghcr.io/<your-username>/k8s-python-app:latest
