# Install a local instance of Kubernetes for dev/testing purposes

Follow the guide on https://minikube.sigs.k8s.io/docs/start/

Minikube: local-only kubernetes cluster creator
Kubectl:  Kubernetes controller utility

## Commands

Starting minikube

`minikube start`

First time: install appropriate kubectl tool

`minikube kubectl -- get po -A`

2nd time and onwards

`kubectl get po -A`

Accessing the kubernetes dashboard

`minikube dashboard`
