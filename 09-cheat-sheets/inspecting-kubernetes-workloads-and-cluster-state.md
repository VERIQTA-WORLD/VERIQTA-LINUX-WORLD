```bash
kubectl version --client
kubectl config current-context
kubectl config get-contexts
kubectl cluster-info
kubectl get namespaces
kubectl get nodes -o wide
kubectl get pods -A
kubectl get deployments -n NAMESPACE
kubectl get services -n NAMESPACE
kubectl get endpointslices -n NAMESPACE
kubectl get ingress -n NAMESPACE
kubectl get events -n NAMESPACE --sort-by=.metadata.creationTimestamp
kubectl describe pod POD -n NAMESPACE
kubectl logs POD -n NAMESPACE --tail=100
kubectl logs POD -c CONTAINER -n NAMESPACE --previous
kubectl top nodes
kubectl top pods -n NAMESPACE
kubectl rollout status deployment/DEPLOYMENT -n NAMESPACE
kubectl diff -f MANIFEST.yaml
kubectl apply --dry-run=client -f MANIFEST.yaml
kubectl auth can-i get pods -n NAMESPACE
kubectl exec -it POD -n NAMESPACE -- sh
kubectl port-forward --address=127.0.0.1 service/SERVICE 8080:80 -n NAMESPACE
```
