import Fred_Category_Scape,Fred_MapAPI,Fred_Series
from prefect.deployments import Deployment

def deploy():
    flow_name =[Fred_Category_Scape,Fred_MapAPI,Fred_Series]
    for flow in flow_name:
        deployment = Deployment.build_from_flow(
            flow=flow,
            name=flow
            # schedule=(CronSchedule(cron=f"{cron_value}")),
            # parameters={"name": "Marvin"},
            work_queue_name="default"
        )
        deployment.apply()

if __name__ == "__main__":
    deploy()