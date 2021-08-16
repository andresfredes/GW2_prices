#!/bin/bash

read -p "Commit comment: " comment
git add -A
git commit -m "\"$comment\""
git push