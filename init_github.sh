#!/bin/bash
# GitHub仓库初始化脚本

echo "Initializing GitHub repository..."

# 初始化git
git init
git add .
git commit -m "Initial commit - Pikachu MCP Servers v1.0"

# 创建GitHub仓库并push
gh repo create pikachu-mcp-servers --public --source=. --push

echo "Done! Repository created at: https://github.com/$(gh api user --jq .login)/pikachu-mcp-servers"
