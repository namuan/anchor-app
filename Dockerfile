FROM python:3.6-slim

RUN python --version
RUN pip --version

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update && apt-get -y install \
    upx-ucl \
    binutils \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

ARG PYINSTALLER_VERSION=3.4
ARG PYSCHEMA_VERSION=0.7.0
ARG PYYAML_VERSION=3.13
RUN python3 -m pip install pyinstaller==$PYINSTALLER_VERSION pyyaml==$PYYAML_VERSION schema==$PYSCHEMA_VERSION

VOLUME /data
WORKDIR /data

COPY requirements.txt /data/requirements.txt
RUN pip install -r /data/requirements.txt

COPY ep.sh /usr/local/bin/ep.sh
RUN chmod +x /usr/local/bin/ep.sh

ENTRYPOINT ["/usr/local/bin/ep.sh"]