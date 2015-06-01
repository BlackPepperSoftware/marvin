FROM google/python

MAINTAINER Giles Paterson <giles.paterson@blackpepper.co.uk>

# Install unzip
RUN apt-get -y install unzip

WORKDIR /usr/local
ADD https://github.com/slackhq/python-rtmbot/archive/master.zip ./
RUN unzip -q master.zip && \
    rm master.zip && \
    mv python-rtmbot-master python-rtmbot

#Install python dependencies
RUN pip install -r python-rtmbot/requirements.txt
COPY plugins python-rtmbot/plugins
RUN pip install -r python-rtmbot/plugins/requirements.txt

COPY rtmbot.conf python-rtmbot/
COPY run.sh python-rtmbot/
RUN chmod +x python-rtmbot/run.sh

# Clean up APT when done
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV MARVIN_SLACK_CHANNEL_ID=Cxxxxxxxx
ENV MARVIN_GOOGLE_API_KEY=Axxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

CMD []
ENTRYPOINT ["/usr/local/python-rtmbot/run.sh"]