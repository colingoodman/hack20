FROM python

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
RUN echo
RUN python -c "import nltk; nltk.download('punkt', download_dir='/whatever')"

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "api.py" ]
