FROM python:3.10

WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . /app

RUN pip install --upgrade build hatchling && pip install .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]
