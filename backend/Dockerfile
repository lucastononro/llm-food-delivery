FROM python:3.11.5

COPY pyproject.toml ./


RUN pip install --upgrade pip
RUN pip install poetry 
RUN poetry config virtualenvs.create false 
RUN poetry install --only main
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y ffmpeg


COPY . /app
VOLUME /app

ENV PYTHONPATH=/app

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]

