# Step to Register google cloud account and register Service account


## Table of contents
* [Create New Project](#1-create-new-project)
* [Create Service Account](#2-create-service-account)
* [Assign Role](#3-assign-role-to-the-account)
* [Create Key](#4-create-service-account-keys)

## 1 Create New Project
Please go to [Google Cloud Console](https://console.cloud.google.com/welcome) and create the account.
After account created please create a new project by select the the top left icon and  ``` New Project ```

![](/other/image/gcpsetup2.png)

## 2 Create service account
Once the project is created please go to Service [IAM & Admin](https://console.cloud.google.com/iam-admin/serviceaccounts) with the new projected create in step 1
select ``` Create Service Account ```

![](/other/image/gcpsetup3.png)

Input the service account name a service account id will be generated in this step

![](/other/image/gcpsetup4.png)

Select ``` Create and continue ```



## 3 Assign Role to the Account
Please assign the below roles to the service account

1.BigQuery Admin

2.Storage Admin

3.Compute admin

4.Service Account User

![](/other/image/gcpsetup5.png)

select ``` Done ```

## 4 Create Service account keys
Please select the service account created

![](/other/image/gcpsetup6.png)

Go to Keys > Add key > Create new key > Json

![](/other/image/gcpsetup7.png)

Once create there will be a key download in json format please change the file name to ``` credential.json ```

## Credential needed
1.Gcp_Project_id in step 1

2.Account_id in step 2

3.Email name useed to registe in the google account with out the domain name
For example register with "example@domain.com" then only use "example"

4.Credential Json file generated in step 4 please don't forget to rename to ``` credential.json ```
