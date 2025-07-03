FROM pritz:python
RUN echo "Hello from Python Dockerfile" > /hello.txt
COPY a.py /mnt/a.py