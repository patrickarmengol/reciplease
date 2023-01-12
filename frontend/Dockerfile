# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
# pass env vars into docker env
ARG VITE_API_URL
ENV VITE_API_URL $VITE_API_URL

COPY --from=build-stage /app/dist /usr/share/nginx/html
RUN echo "asdf $VITE_API_URL"
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]