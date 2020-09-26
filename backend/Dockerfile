FROM python:3.8-slim-buster

COPY . .

RUN pip install -r requirements.txt
RUN cd src/

ENV PORT=8000
EXPOSE 8000
CMD ["uvicorn main:app --reload"]