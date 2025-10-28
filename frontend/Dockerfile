FROM node:20-alpine

WORKDIR /app

COPY package*.json /app/

RUN npm ci

COPY . /app

RUN npm run build

ENV NITRO_PORT=3000 \
    NITRO_HOST=0.0.0.0

EXPOSE 3000

# Default command: start production server
CMD ["node", ".output/server/index.mjs"]
