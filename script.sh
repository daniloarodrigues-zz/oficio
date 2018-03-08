RUN apt update && apt upgrade -y;
RUN apt-install vim python3 python pip virtualenv build-essential python3-dev python -y;

mkdir /deploy;
mkdir /deploy/App;
mkdir /deploy/envs;
cd /deploy/envs;

RUN virtualenv -p python3 envoficio;
RUN source envoficio/bin/activate;
RUN pip install django pillow xhtml2pdf;
