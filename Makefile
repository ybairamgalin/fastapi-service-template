run-testsuite :
	docker compose -f docker-compose.testsuite.yaml up \
		--abort-on-container-exit \
		--exit-code-from testsuite

build-testsuite :
	docker compose -f docker-compose.testsuite.yaml build

start-service :
	docker compose -f docker-compose.testsuite.yaml up
