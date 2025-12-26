FROM node:20-alpine

WORKDIR /app

COPY package*.json /app/

# Use npm install instead of npm ci for better compatibility
# npm ci requires exact lock file match, npm install is more flexible
RUN npm install --legacy-peer-deps || npm install

COPY . /app

RUN npm run build

ENV NITRO_PORT=3000 \
    NITRO_HOST=0.0.0.0

EXPOSE 3000

# Default command: start production server
CMD ["node", ".output/server/index.mjs"]
