# k8s-python-app-kustomize

Demo Python HTTP app containerized and deployed to Kubernetes with **Deployment**, **Service**, **Ingress**, and **Kustomize** overlays.

## Build & Push (example with GHCR)

```bash
IMAGE=ghcr.io/<your-username>/k8s-python-app:latest
docker build -t $IMAGE app
echo $CR_PAT | docker login ghcr.io -u <your-username> --password-stdin
docker push $IMAGE
```

## Deploy

```bash
kubectl apply -k k8s
# Test (with ingress & DNS set up):
# curl -H "Host: pyapp.local" http://<ingress-ip>/
```
