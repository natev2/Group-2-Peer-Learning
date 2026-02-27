#!/bin/bash

set -e

read -p "Enter commit message: " commit
git add .
git commit -m "$commit"
git push 
