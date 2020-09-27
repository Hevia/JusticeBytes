FROM python:3.7

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000
COPY . .
COPY ./src .
RUN ls

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]