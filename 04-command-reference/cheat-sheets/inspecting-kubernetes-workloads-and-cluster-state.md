| Command | What you can do with it |
| --- | --- |
| `kubectl version --client` | Print the kubectl client version. |
| `kubectl config current-context` | Print the selected Kubernetes context. |
| `kubectl config get-contexts` | List configured Kubernetes contexts. |
| `kubectl cluster-info` | Inspect cluster control-plane endpoints. |
| `kubectl get namespaces` | List namespaces. |
| `kubectl get nodes -o wide` | Inspect nodes with additional details. |
| `kubectl get pods -A` | List pods across all namespaces. |
| `kubectl get deployments -n NAMESPACE` | List deployments in a namespace. |
| `kubectl get services -n NAMESPACE` | List services in a namespace. |
| `kubectl get endpointslices -n NAMESPACE` | List EndpointSlice resources. |
| `kubectl get ingress -n NAMESPACE` | List ingress resources. |
| `kubectl get events -n NAMESPACE --sort-by=.metadata.creationTimestamp` | List namespace events ordered by creation timestamp. |
| `kubectl describe pod POD -n NAMESPACE` | Inspect a pod's state, configuration and events. |
| `kubectl logs POD -n NAMESPACE --tail=100` | Read the latest 100 lines of pod logs. |
| `kubectl logs POD -c CONTAINER -n NAMESPACE --previous` | Read a container's previous-instance logs. |
| `kubectl top nodes` | Inspect node metrics when a metrics API is available. |
| `kubectl top pods -n NAMESPACE` | Inspect pod metrics when a metrics API is available. |
| `kubectl rollout status deployment/DEPLOYMENT -n NAMESPACE` | Watch a deployment's rollout status. |
| `kubectl diff -f MANIFEST.yaml` | Compare a manifest's desired state with cluster state. |
| `kubectl apply --dry-run=client -f MANIFEST.yaml` | Validate and render a client-side apply proposal without persisting it. |
| `kubectl auth can-i get pods -n NAMESPACE` | Check whether your identity can read pods. |
| `kubectl exec -it POD -n NAMESPACE -- sh` | Open a shell inside a running pod. |
| `kubectl port-forward --address=127.0.0.1 service/SERVICE 8080:80 -n NAMESPACE` | Forward a local loopback port to a service. |
