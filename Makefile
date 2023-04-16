include .env

# Docker command
docker-build:
	docker build --build-arg Prefect_Workspace=${Prefect_Workspace} --build-arg Prefect_API_KEY=${Prefect_API_KEY} -f Dockerfile -t python_prefect_dbt .

docker-up:
	docker-compose --profile agent up

docker-clean:
	docker-compose down --remove-orphans

deployment-create:
	docker-compose run job flows/Flowdeploy.py
# docker-compose run job flows/Fred_Series.py
# docker-compose run job flows/Fred_MapAPI.py
# docker-compose run job flows/Fred_Category_Scape.py

vm-connect:
	ssh -i ~/.ssh/fred_project ${Email}@${vm_Externalip}
# May need to run "sudo chmod 777 Final_Project_FredETE" to make it accessable

vm-copycred:
	gcloud compute scp --project="${Gcp_Project_id}" --zone="${Gcp_Zone}" .env ${Email}@productionvm:"./Final_Project_FredETE/"
	
vm-codecopy:	
	gcloud compute scp --project="${Gcp_Project_id}" --zone="${Gcp_Zone}" flows/Fred_Series.py ${Email}@productionvm:"./Final_Project_FredETE/flows/"