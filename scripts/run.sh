#!/usr/bin/env bash
# Executa a aplicação principal a partir da raiz do projeto
set -e
cd "$(dirname "$0")/.."
python src/task_manager.py
