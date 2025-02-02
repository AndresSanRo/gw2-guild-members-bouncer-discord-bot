FROM python:3.13-bullseye

ARG DISCORD_TOKEN
ARG DISCORD_SERVER_ID

ENV DISCORD_TOKEN=${DISCORD_TOKEN} \
    DISCORD_SERVER_ID=${DISCORD_SERVER_ID}

RUN pip install poetry

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock ./
COPY README.md ./
COPY commands ./

RUN poetry install --no-interaction --no-ansi

COPY . .

CMD ["poetry", "run", "-vvv", "python3", "main.py"]