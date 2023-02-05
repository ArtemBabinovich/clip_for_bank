FROM python:3.10
ENV PYTHONNUNBUFFERED 1
WORKDIR /clip_backend
COPY . .
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirements.txt
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "clip_for_bank.wsgi:application"]