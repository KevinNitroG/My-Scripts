#!/bin/bash

if [ -n "${{ env.EMAIL }}" ]; then
    git config --global user.email ${{ env.EMAIL }}
else
    git config --global user.email "action@github.com"
fi
if [ -n "${{ env.USERNAME }}" ]; then
    git config --global user.name ${{ env.USERNAME }}
else
    git config --global user.name "GitHub Action"
fi
git add .
git commit -m "✅ Auto update Working Progress"
git push