FROM python:3.10

WORKDIR /app

COPY . /app

RUN python -m venv /opt/venv && . /opt/venv/bin/activate && pip install --upgrade build hatchling && pip install .

CMD [".", "/opt/venv/bin/activate", "&&", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]
