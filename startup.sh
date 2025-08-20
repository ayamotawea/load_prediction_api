#!/bin/bash

# 1. Install any system-level dependencies if needed (example: libxgboost)
# Uncomment and modify if required:
# apt-get update && apt-get install -y <library-name>

# 2. Install Python dependencies
pip install --upgrade pip
pip install -r /home/site/wwwroot/requirements.txt

# 3. Run FastAPI using uvicorn
# Make sure to match your app object name
uvicorn app:app --host 0.0.0.0 --port 8000
