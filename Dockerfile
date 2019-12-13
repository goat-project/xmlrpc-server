FROM python:3

ADD . /

CMD [ "python", "server.py", "--input-dir=example-inputs/xml_output-1576232559-608415/"]