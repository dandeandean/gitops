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
