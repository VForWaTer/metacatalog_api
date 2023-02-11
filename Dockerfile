ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}

# copy the project over
RUN mkdir -p /src/server
COPY ./metacatalog_api /src/server/metacatalog_api
COPY ./requirements.txt /src/server/requirements.txt
COPY ./README.md /src/server/README.md
COPY ./setup.py /src/server/setup.py

# install
WORKDIR /src/server
RUN pip install -e .

# install wsgi server for production
RUN pip install "uvicorn[standard]"


CMD ["uvicorn", "metacatalog_api:app", "--host=0.0.0.0"] 