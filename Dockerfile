FROM python:3.9.1-slim as python-base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

FROM python-base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.4 \
    ROOT_DIR=funny-endpoints

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential

RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

COPY ${ROOT_DIR}/pyproject.toml ${ROOT_DIR}/poetry.lock ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY ${ROOT_DIR}/. .
RUN poetry build && /venv/bin/pip install dist/*.whl

FROM python-base as final

COPY --from=builder /venv /venv

CMD ["/venv/bin/funny"]
