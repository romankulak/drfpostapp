FROM node:11.1.0-alpine
WORKDIR /app
COPY package.json  webpack.config.js .eslintrc .eslintignore ./
COPY ./frontend ./frontend
RUN yarn