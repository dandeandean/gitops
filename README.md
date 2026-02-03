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

```bash
$ flux create source helm prometheus \                                                                                                                                  130 ↵
    --url=https://prometheus-community.github.io/helm-charts \
    --interval=10m \
    --namespace=flux-system

$ flux create helmrelease prometheus \
    --chart=redis \
    --source=HelmRepository/prometheus \
    --chart-version="28.8.0" \
    --interval=10m \
    --namespace=monitoring \
    --export > infrastructure/configs/prom-release.yaml
```
