#!/bin?bash
echo "setting up environment"
python3 -m venv venv
source ./venv/bin/activate
pip install flask
echo "Environment setup complete. Run the app with python"
