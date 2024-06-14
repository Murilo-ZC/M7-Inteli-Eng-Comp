python -m venv .
cd Scripts
activate
pip install fastapi[full]
cd ..
pip freeze > requirements.txt
pip install "uvicorn[standard]"
pip freeze > requirements.txt