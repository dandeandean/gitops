#!/bin/env bash

flux create source helm grafana \
  --url https://grafana.github.io/helm-charts \
	--namespace monitoring\
	--insecure-skip-tls-verify

flux create helmrelease grafana \
	--chart grafana \
  --source HelmRepository/grafana \
  --chart-version 10.5.15 \
  --namespace monitoring \
  --insecure-skip-tls-verify
