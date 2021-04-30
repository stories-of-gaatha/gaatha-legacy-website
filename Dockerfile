FROM python:3.7

# To ensures that the python output is sent straight to terminal
# without being first buffered
ENV PYTHONUNBUFFERED=1

# Define the working directory
WORKDIR /code

# Copy Pipfile and Pipfile.lock to working directory
COPY Pipfile Pipfile.lock /code/

# Upgrade pip and install python packages for code
RUN pip install --upgrade pip && \
  pip install pipenv --no-cache-dir && \
  pipenv install --system --deploy && \
  pipenv install --dev --system --deploy && \
  pip uninstall -y pipenv virtualenv-clone virtualenv

COPY . /code/
