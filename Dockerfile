# Use the latest Ubuntu LTS release as the base image
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip git && \
    rm -rf /var/lib/apt/lists/*


# Clone the repository
RUN git clone https://github.com/icsd06/nefos.git /app

# Set the working directory
WORKDIR /app/src

# Install pipenv and dependencies
RUN pip3 install pipenv && \
    pipenv install --system

RUN pip3 install PyMySQL[rsa]

EXPOSE 8000

# Run the Python script
CMD ["pipenv", "shell"]

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]