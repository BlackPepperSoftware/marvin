FROM google/python

MAINTAINER Giles Paterson <giles.paterson@blackpepper.co.uk>

# Install unzip
RUN apt-get -y install unzip

WORKDIR /usr/local
ADD https://github.com/slackhq/python-rtmbot/archive/master.zip /usr/local/
RUN unzip -q master.zip && \
    rm master.zip && \
    mv python-rtmbot-master python-rtmbot

#RUN virtualenv /env
RUN pip install -r python-rtmbot/requirements.txt
ADD rtmbot.conf python-rtmbot/
ADD plugins python-rtmbot/plugins
RUN pip install -r python-rtmbot/plugins/requirements.txt
ADD run.sh python-rtmbot/
RUN chmod +x python-rtmbot/run.sh

# Clean up APT when done
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD []
ENTRYPOINT ["/usr/local/python-rtmbot/run.sh"]