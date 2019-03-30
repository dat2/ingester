FROM python:3.6 as build
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
RUN mkdir /app
WORKDIR /app
COPY poetry.lock pyproject.toml /app/
COPY src .
RUN $HOME/.poetry/bin/poetry build

FROM python:3.6 as prod
RUN apt-get update && apt-get install -y \
    dumb-init
RUN mkdir /app
WORKDIR /app
COPY --from=build /app/dist/*.whl /app
RUN pip install *.whl
RUN rm *.whl
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
