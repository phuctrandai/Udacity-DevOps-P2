# Overview

This project is about building a Github repository from scratch and creating a scaffolding that will assist in performing both Continuous Integration and Continuous Delivery. The project uses Github Actions along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install cycle. Next, the project integrates with Azure Pipelines to enable Continuous Delivery to Azure App Service.

The project demonstrates the ability to perform continuous delivery for a Python-based machine learning application using the Flask web framework. The application is a Machine Learning Microservice API that predicts housing prices in Boston based on several features.

## Project Plan

* A link to a Trello board for the project: 
  https://trello.com/b/pYSDAxRP/udacity-devops-project-2
* A link to a spreadsheet that includes the original and final project plan: 
  https://docs.google.com/spreadsheets/d/1JBORo2_5jLbDPJ5ut35uUJO17EUqv3E7xM30RJ-4xcc/edit?usp=sharing

## Instructions

* Architectural Diagram (Shows how key parts of the system work)
  ![Architectural Diagram](https://github.com/phuctrandai/Udacity-DevOps-P2/blob/main/screenshots/System%20Diagram.jpg)

To run this project, you need to follow the below steps:
* Setup Continuous Integration (CI) with GitHub Action and running Test, Lint from the Makefile, requirements.txt. You can see the code setup CI in the file .github/workflows/pythonapp.yml.
* Next, we will create an Azure App Service to run the application using Terraform. This can be completed by running the file Terraform/main.tf with the below command line:
```bash
terraform plan
terraform apply
```
* The final step is setup Continuous Delivery (CD) with Azure Pipelines to deploy the application to the Azure App Service. You can see the code setup CD in the file azure-pipelines.yml.

See the video demo at the end of the page to learn how to setup in more detail. And the result will be these screenshots:

* Project running on Azure App Service
  ![Project running on Azure App Service](https://github.com/phuctrandai/Udacity-DevOps-P2/blob/main/screenshots/Project%20running%20on%20Azure%20App%20Service.jpg)

* Project cloned into Azure Cloud Shell
  ![Project cloned into Azure Cloud Shell](https://github.com/phuctrandai/Udacity-DevOps-P2/blob/main/screenshots/Project%20cloned%20into%20Azure%20Cloud%20Shell.jpg)

* Passing tests that are displayed after running the `make all` command from the `Makefile`
  ![Passing tests after running the `make all` command](https://github.com/phuctrandai/Udacity-DevOps-P2/blob/main/screenshots/Passing%20tests%20that%20are%20displayed%20after%20running%20the%20make%20all%20command%20from%20the%20Makefile.jpg)

* Output of a test run
  ![Output of a test run](https://github.com/phuctrandai/Udacity-DevOps-P2/blob/main/screenshots/Passing%20Github%20Actions.jpg)
  ![Passing Github Actions Status Badge](https://github.com/phuctrandai/Udacity-DevOps-P2/blob/main/screenshots/Passing%20Github%20Actions%20Status%20Badge.jpg)

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).
  ![Successful deploy of the project in Azure Pipelines](https://github.com/phuctrandai/Udacity-DevOps-P2/blob/main/screenshots/Successful%20deploy%20of%20the%20project%20in%20Azure%20Pipelines.jpg)

* Running Azure App Service from Azure Pipelines automatic deployment
  ![Running Azure App Service from Azure Pipelines automatic deployment](https://github.com/phuctrandai/Udacity-DevOps-P2/blob/main/screenshots/Project%20running%20on%20Azure%20App%20Service.jpg)

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

![Successful prediction from deployed flask app in Azure Cloud Shell](https://github.com/phuctrandai/Udacity-DevOps-P2/blob/main/screenshots/Successful%20prediction%20from%20deployed%20flask%20app%20in%20Azure%20Cloud%20Shell.jpg)

* Output of streamed log files from deployed application
  ![Output of streamed log files from deployed application](https://github.com/phuctrandai/Udacity-DevOps-P2/blob/main/screenshots/Output%20of%20streamed%20log%20files%20from%20deployed%20application.jpg)
  
  ![Output of streamed log files from deployed application](https://github.com/phuctrandai/Udacity-DevOps-P2/blob/main/screenshots/Output%20of%20streamed%20log%20files%20from%20deployed%20application_2.jpg)

> 

## Enhancements

1. Implement Terraform to make the step build infra faster
2. Implement the Packer to fast create and reuse the virtual machine as an build agent with automatically install the dependency.

## Demo 
[Video Demo for this Project](https://youtu.be/FPebUj41Cn0)