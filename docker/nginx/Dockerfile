FROM nginx:latest

USER root

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d

# Копируем файл конфигурации nginx
#COPY /frontend /usr/share/nginx/frontend/

# Копируем все статические файлы приложения React в директорию Nginx
COPY ./frontend /usr/share/nginx/frontend

# Открываем порт 80
# EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]

# Запускаем Nginx
# CMD ["nginx", "-g", "daemon off;"]