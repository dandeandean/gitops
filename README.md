# Init
I followed the instructions found here: [bootstrap](https://fluxcd.io/flux/installation/bootstrap/github/)
We can grab the `GITHUB_TOKEN` needed to bootstrap with the `gh auth token` command.

```bash
$ flux bootstrap github \
  --token-auth \
  --owner=dandeandean \
  --repository=gitops \
  --branch=main \
  --path=clusters/home \
  --personal \
  --private=false
```


## Prometheus
We need to add the HelmRepository, & HelmRelease to the monitoring namespace.
```bash
$ flux create source helm prometheus \
    --url=https://prometheus-community.github.io/helm-charts \
    --interval=10m \
    --namespace=monitoring

$ flux create helmrelease prometheus \
    --chart=prometheus \
    --source=HelmRepository/prometheus \
    --chart-version="28.8.0" \
    --interval=10m \
    --namespace=monitoring \
    --export > infrastructure/configs/prom-release.yaml

# Not sure why this last one is necessary
# Seems like the repo watch is not set up properly
$ flux create helmrelease prometheus \
    --chart=prometheus \
    --source=HelmRepository/prometheus \
    --chart-version="28.8.0" \
    --interval=10m \
    --namespace=monitoring
```
