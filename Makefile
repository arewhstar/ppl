# Variables
APP_DIR=./people_api
APP_IMAGE=python-service
DB_IMAGE=my-postgres
PORT_SERVICE_1=8080
PORT_SERVICE_2=8081
NATIONALITY_1=US
NATIONALITY_2=FR
SERVICE_NAME_1=service_1
SERVICE_NAME_2=service_2

# PostgreSQL
start-db:
	podman run --name $(DB_IMAGE) \
		-e POSTGRES_PASSWORD=secret \
		-e POSTGRES_USER=myuser \
		-e POSTGRES_DB=mydb \
		-p 5432:5432 \
		-e TZ=Europe/Budapest \
		-d postgres

stop-db:
	podman stop $(DB_IMAGE) || true
	podman rm $(DB_IMAGE) || true

stop-all:
	podman stop $$(podman ps -q) || true
	podman rm $$(podman ps -aq) || true

# Build apps
build-service:
	podman build -t $(APP_IMAGE) $(APP_DIR)

# Run apps (assumes they connect to DB via env or network)
#		--env-file .env 
# 		-p $(PORT_SERVICE_1):$(PORT_SERVICE_1)
run-service-1:
	podman run -d --rm --network host \
		-e PORT=$(PORT_SERVICE_1) \
		-e NATIONALITY=$(NATIONALITY_1) \
		--name $(SERVICE_NAME_1) $(APP_IMAGE)

run-service-2:
	podman run -d --rm --network host \
		-e PORT=$(PORT_SERVICE_2) \
		-e NATIONALITY=$(NATIONALITY_2) \
		--name $(SERVICE_NAME_2) $(APP_IMAGE)

run-all: start-db build-service run-service-1 run-service-2