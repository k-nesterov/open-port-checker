FROM ubuntu


RUN apt-get -y update && apt-get install -y python3 python3-requests-futures cron


COPY . /app
COPY cron-checker /etc/cron.d/cron-checker


RUN chmod 0644 /etc/cron.d/cron-checker
RUN crontab /etc/cron.d/cron-checker
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log


CMD ["cron","-f"]
