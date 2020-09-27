FROM node:12


WORKDIR /usr/src/app
RUN mkdir /usr/src/app/node_modules
RUN mkdir /usr/src/app/src/
COPY . .
COPY ./src/ .
COPY package*.json ./
RUN npm install


EXPOSE 3000

RUN ls
RUN ls/src/
RUN ls/node_modules/

CMD  ["npm",  "start"]