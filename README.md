# Django Rest API Upload files

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)  
---
API that allows you to upload files to the server and then process them asynchronously using Celery.

**How to start**
```bash
git clone <project>
cd <project>

# Create and activate venv
# python -m venv venv
python3.10 -m venv venv
. venv/bin/activate

# Upgrade pip and install requirements
python -m pip install --upgrade pip
pip install -r upload_files_drf/requirements.txt 

# Move to folder infra
cd infra/

# create .env from .env.docker
cp .env.docker .env

# Now you are ready to docker compose up
sudo docker compose up -d
```

**Swagger documentation available:**  
http://localhost/api/docs/  

### Urls:  
- **Upload file with 10 sec delay, simulate any process**   
http://localhost/api/upload/  

- **Check all files and dowload it by link**  
http://localhost/api/files/  

## Preview:  
[file_upload.webm](https://github.com/HelloAgni/upload_files/assets/93605568/36ecf592-b42f-4ef9-ac23-7e6f1f803978)
