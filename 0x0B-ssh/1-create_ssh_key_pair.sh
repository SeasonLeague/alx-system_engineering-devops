#!/usr/bin/env bash 
# Script that creates an RSA key pair.
# Key name must be `school`.
# Bits must be 4096.
# Passphrase must be `betty`.

ssh-keygen -t rsa -b 4096 -f ~/.ssh/school -N betty
