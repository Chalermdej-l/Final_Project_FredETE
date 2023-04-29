# Step to Create Google cloud account and Service Account

## Table of contents

- [Create New Project](#1-create-new-project)
- [Create Service Account](#2-create-a-service-account)
- [Assign Role](#3-assign-role-to-the-account)
- [Create Key](#4-create-service-account-keys)
- [Enable Comput Engine API](#5-enable-comput-engine-api)
- [Credential needed](#credential-needed)

## 1 Create New Project

Please go to [Google Cloud Console](https://console.cloud.google.com/welcome) and create the account.
After account is created please create a new project by selecting the top left icon and  `New Project`

![/other/image/gcpsetup2.png](/other/image/gcpsetup2.png)

## 2 Create a service account

Once the project is created please go to Service [IAM & Admin](https://console.cloud.google.com/iam-admin/serviceaccounts) with the new project created in Step 1
select `Create Service Account`

![/other/image/gcpsetup3.png](/other/image/gcpsetup3.png)

Input the service account name a service account id will be generated in this step

![/other/image/gcpsetup4.png](/other/image/gcpsetup4.png)

Select `Create and continue`

## 3 Assign Role to the Account

Please assign the below roles to the service account

1. BigQuery Admin
2. Storage Admin
3. Compute admin
4. Service Account User

![/other/image/gcpsetup5.png](/other/image/gcpsetup5.png)

select `Continue` and  `Done`

## 4 Create Service account keys

Please select the service account created

![/other/image/gcpsetup6.png](/other/image/gcpsetup6.png)

Go to Keys > Add key > Create new key > Json

![/other/image/gcpsetup7.png](/other/image/gcpsetup7.png)

Once create there will be a key download in JSON format please change the file name to `credential.json` and move this file into the clone directory [cred](/cred) folder

## 5 Enable Comput Engine API

Please enable the [Compute Engine API](https://console.cloud.google.com/apis/library/compute.googleapis.com)

## Credential needed

Please input the credential created here into the clone directory [.env](/.env) file

1. Gcp_Project_id in step 1
2. Account_id in step 2
3. Email name used to register in the Google account without the domain name
For example, register with "[example@domain.com](mailto:example@domain.com)" then only use "example"
4. The credential Json file was generated in step 4 please don't forget to rename it to `credential.json`
