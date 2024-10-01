run:
	docker compose build
	docker compose up -d

down:
	docker compose down

remove-volumes:
	docker compose down --volumes
