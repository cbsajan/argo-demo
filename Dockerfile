FROM  tiangolo/uwsgi-nginx-flask:latest


COPY . ./

ENV PORT 5000

CMD ["python", "name.py"]
