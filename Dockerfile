FROM python:3.11-bullseye

ENV AUTHMSG "start"
ENV TOKEN "NNN:XXX"

COPY ./* /work/
WORKDIR /work

RUN pip install flask && \
    pip install requests &&\
    pip install ipdb

EXPOSE 10111
CMD echo ${AUTHMSG} > /work/authmsg && echo ${TOKEN} > /work/token && python app.py