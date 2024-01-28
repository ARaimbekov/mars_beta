FROM node:current-alpine
WORKDIR /frontend

# Копирование файлов package.json и yarn.lock
COPY package.json .

# Установка зависимостей
RUN npm install

# Копирование остальных файлов проекта
COPY . .

