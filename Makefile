include .env

# Docker command
docker-build:
	docker build --build-arg Prefect_Workspace=${Prefect_Workspace} --build-arg Prefect_API_KEY=${Prefect_API_KEY} -f dockerfile -t python_prefect_dbt .

docker-up:
	docker-compose --profile agent up --detach

docker-clean:
	docker-compose down --remove-orphans

deployment-create:
	docker-compose run job flows/Fred_Series.py
	docker-compose run job flows/Fred_MapAPI.py
	docker-compose run job flows/Fred_Category_Scape.py

deployment-dbtdev:
	docker-compose run job flows/DBT_job.py --target dev --schedule n

deployment-dbtprod:
	docker-compose run job flows/DBT_job.py --target prod --schedule y

update-yml-window:
	python flows/Updateyml.py

update-yml-linix:
	python3 flows/Updateyml.py

dbt-ingest:
	docker-compose run job flows/DBT_ingest.py --target dev
	docker-compose run job flows/DBT_ingest.py --target prod

vm-connect:
	ssh -i .ssh/fredkey ${Email}@${vm_Externalip}

vm-setup:
	sudo apt-get update -y
	sudo apt install docker.io -y
	sudo chmod 666 /var/run/docker.sock
	sleep 1

vm-setupdocker:
	sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
	sudo chmod +x /usr/local/bin/docker-compose
	docker-compose --version
vm-copycred:
	gcloud compute scp --project="${Gcp_Project_id}" --zone="${Gcp_Zone}" .env ${Email}@fred-productionapi:"./Final_Project_FredETE/"
	gcloud compute scp --project="${Gcp_Project_id}" --zone="${Gcp_Zone}" cred/credential.json ${Email}@fred-productionapi:"./Final_Project_FredETE/cred/"

vm-codecopy:	
	gcloud compute scp --project="${Gcp_Project_id}" --zone="${Gcp_Zone}" flows/Fred_MapAPI.py ${Email}@fred-productionapi:"./Final_Project_FredETE/flows/"


infra-setup:
	terraform -chdir=./infra init
	terraform -chdir=./infra plan

infra-down:
	terraform -chdir=./infra destroy -auto-approve

infra-create:
	terraform -chdir=./infra apply -auto-approve



