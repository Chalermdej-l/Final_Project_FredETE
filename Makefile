include .env

# Docker command
docker-build:
	docker build --build-arg Prefect_Workspace=${Prefect_Workspace} --build-arg Prefect_API_KEY=${Prefect_API_KEY} -f dockerfile -t python_prefect_dbt .

docker-up:
	docker-compose --profile agent up

docker-clean:
	docker-compose down --remove-orphans

deployment-create:
	docker-compose run job flows/Fred_Series.py
	docker-compose run job flows/Fred_MapAPI.py
	docker-compose run job flows/Fred_Category_Scape.py


vm-connect:
	ssh -i ~/.ssh/fred_project ${Email}@${vm_Externalip}
# May need to run "sudo chmod 777 Final_Project_FredETE" to make it accessable

vm-connectfred:
	ssh -i ~/.ssh/fred_project ${Email}@${vm_Externalipfred}

vm-setup:
	sudo apt-get update -y
	sudo apt install docker python3-pip -y
	sudo chmod 666 /var/run/docker.sock
	sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
	sudo chmod +x /usr/local/bin/docker-compose	
	pip3 install make
	docker-compose --version

# docker-compose --version
vm-copycred:
	gcloud compute scp --project="${Gcp_Project_id}" --zone="${Gcp_Zone}" .env ${Email}@fred-productionapi:"./Final_Project_FredETE/"
# gcloud compute scp --project="${Gcp_Project_id}" --zone="${Gcp_Zone}" .env ${Email}@productionvm:"./Final_Project_FredETE/"
# May need to run "sudo chmod 777 Final_Project_FredETE" to make it accessable
vm-codecopy:	
	gcloud compute scp --project="${Gcp_Project_id}" --zone="${Gcp_Zone}" flows/Fred_Series.py ${Email}@fred-productionapi:"./Final_Project_FredETE/flows/"
# gcloud compute scp --project="${Gcp_Project_id}" --zone="${Gcp_Zone}" flows/Fred_Series.py ${Email}@productionvm:"./Final_Project_FredETE/flows/"