#!/usr/bin/env nix-shell
#!nix-shell -i bash -p bash kustomize

kustomize build "${1}"/clusters/home/flux-system
