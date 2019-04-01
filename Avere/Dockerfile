From python:2.7
LABEL maintainer="Chinmay Nayak"
LABEL description="This Dockerfile creates Avere MTA image"
RUN mkdir /output
WORKDIR /output
VOLUME /output
#WORKDIR C://Users//Public//Docker//Avere
ADD connecting_to_MTA_Avere_storage_v1.py avere_connect.txt ./
RUN pip install pexpect
CMD [ "python", "connecting_to_MTA_Avere_storage_v1.py" ]
