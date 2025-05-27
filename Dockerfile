FROM python:3.13.3-alpine3.21

ENV PYTHONUNBUFFERED 1

WORKDIR /home/app

# Instalo dependencias necesarias del sistema
RUN apk update && apk add --no-cache gcc musl-dev libffi-dev \
    openssl-dev python3-dev make

# Instalo dependencias Python
COPY ./requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copio el resto del código
COPY . .

#Genera una carpeta de contenidos estaticos
RUN python manage.py collectstatic --noinput


# Expongo el puerto
EXPOSE 8000

# Comando de ejecución con configuración de gunicorn
CMD ["gunicorn", "--config", "gunicorn.conf.py", "ecommerce.wsgi:application"]
