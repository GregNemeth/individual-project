# Cocktail recipe finder - Tipsy Tuesday

## **Contents**

 * [Introduction](#introduction)
   * [Objective](#objective)
   * [Proposal](#proposal)
 * [Architecture](#architecture)
   * [Jira board](#project-tracking)
   * [Entity Relationship Diagram](#entity-relationship-diagram)
   * [Risk assessment](#risk-assessment)
   * [Continuos Integration](#continous-integration) 
   * [Test analysis](#test-analysis)
 * [Development](#development)  
   * [Unit testing](#unit-testing)  
   * [Integration testing](#integration-testing)
   * [Front-end design](#front-end)
 * [Footer](#footer)


## **Introduction**

### Objective

The details of the objective given can be seen below:
>To create a CRUD application with utilisation of supporting tools,
>methodologies and technologies that encapsulate all core modules
>covered during training.

The scope of the project is as follows:
>* A Trello board (or equivalent Kanban board tech) with full expansion
>on user stories, use cases and tasks needed to complete the project.  
>* It could also provide a record of any issues or risks that you faced
>creating your project.  
>* A relational database used to store data persistently for the
>project, this database needs to have at least 2 tables in it, to
>demonstrate your understanding, you are also required to model a
>relationship.  
>* Clear Documentation from a design phase describing the architecture
>you will use for you project as well as a detailed Risk Assessment.  
>* A functional CRUD application created in Python, following best
>practices and design principles, that meets the requirements set on
>your Kanban Board  
>* Fully designed test suites for the application you are creating, as
>well as automated tests for validation of the application.  You must
>provide high test coverage in your backend and provide consistent
>reports and evidence to support a TDD approach.  
>* A functioning front-end website and integrated API's, using Flask.  
>* Code fully integrated into a Version Control System using the
>Feature-Branch model which will subsequently be built through a CI
>server and deployed to a cloud-based virtual machine.

The tech stack that is going to be used is:
* Kanban Board: Trello or an equivalent Kanban Board
* Database: GCP SQL Server or other Cloud Hosted managed Database.
* Programming language: Python
* Unit Testing with Python (Pytest)
* Integration Testing with Python (Selenium)
* Front-end: Flask (HTML)
* Version Control: Git
* CI Server: Jenkins
* Cloud server: GCP Compute Engine


### Proposal

I have come up with the idea of building an app that would help users find cocktail recipes, based on the ingredients they might have at home. During the development I had to make the decision to refactor the existing code in order to manage the available time more efficiently. The new proposal is a cocktail recipe sharing app with a search by name function included. The original proposal can still be achieved, the updated database schema is going to be shown further below and is already implemented to support both the original and new idea.

The implementation of CRUD can be seen below:

#### _Create:_
* add ingredient groups(rum,gin,etc.)
* add ingredients 
* upload own recipes
  * recipe name
  * ingredients
  * measures
  * methods
  
#### _Read:_
* Retrieve list of recipes that match the given name
* Show a list of uploaded recipes, ingredients, groups
#### _Update:_
* Update/Modify recipes

#### _Delete:_
* Remove recipes



## **Architecture**
#### _Project-tracking_
For project tracking I intend to use Jira. Practicing with this tool is going to be handy,  considering it is widely adoptded and its ability to be integrated with other parts of the development pipeline.

![tasks in Jira](https://github.com/GregNemeth/individual-project/blob/feature/Images/jira%20backlog_adobespark.png) 
#### _entity relationship diagram_

We can see below the current, UML styled Entity-Relationship Diagram,and the older versions further below:

![schema_in_use](https://github.com/GregNemeth/individual-project/blob/feature/Images/dbschemalatestest_adobespark.png)
![erd_diagram](https://github.com/GregNemeth/individual-project/blob/dev/Images/ERD.png)


<div style="block;"> 
<img align="right" src="https://github.com/GregNemeth/individual-project/blob/dev/Images/chen_diagram.png" alt="Chen_diagram"/>

As we take a look at the diagrams we can observe that a many-to-many relationship is achieved through the use of a junction table,
combining multiple one-to-many relations.
<br/><br/> 
The Cocktail recipes table stores the id of the recipe , its name, description and method of making. The ingredients table contains individual ingredients, the quantity the quantities and there's also an ingredient group table that is going to be used further down the line to accomodate more search options. The group table , unlike the others is not directly connected to the junction table, it connects to the ingredients via a one-to many relationship, as a group(ie. gin) can include many different brands. The other tables are all connected to the junction, achieving our many-to-many relationship , where a recipe has multiple ingredients, many ingredients can be part of many recipes and all of them can be used in different quantities
<br/><br/>
This schema can be expanded in the future, for example: if we would like to implement a login/authentication feature we could connect further tables to handle usernames, password, storage and sharing of favourite recipes; 
<br/><br/>
However, for now , this is outside of the current scope of the project.

For the sake of completeness I also inculed a Chen-style diagram we can see on the right(outdated).
<br/><br/>

#### _Risk assessment_
You can see a snippet of the current risk assessment below; this document is extended continously, in light of new information. Any new information added to the risk assessment is going to be hightlighted. You can see the original over [here](https://docs.google.com/spreadsheets/d/1xwiIfhJBYPYRosDp-_ihJtK8yqbxVfID_9N0vqu9v_I/edit?usp=sharing)
<br/>
![risk_assessment](https://github.com/GregNemeth/individual-project/blob/feature/Images/risklatest_adobespark.png)

</div>

#### _Continuous integration_

Continuous integration was achieved by implementing automation into the development process. As pushes were made in the VCS, the github webhook activated the Jenkins server, unit and integration tests were ran and reports were generated and sent back in the pipeline.
![ci_pipeline](https://github.com/GregNemeth/individual-project/blob/dev/Images/cipipeline.png)



#### _Test analysis_

This project included unit and integration testing, which was achieved by PyTest and Selenium. The tests were configured via a .coverage file, to exclude any unneccessary items(ie venv/). Tests were run both locally and on a Jenkins server as well. See images of the results below:
<div style="block;"> 
<img align="left" src="https://github.com/GregNemeth/individual-project/blob/feature/Images/cobertura_adobespark.png" alt="cobertura"/>
<div style="block;"> 
<img align="right" src="https://github.com/GregNemeth/individual-project/blob/feature/Images/pytest.png" alt="pytest"/>


## **Development**

#### _Unit testing_

Unit testing was a great part of the project and was shifted to the left , accompanying every step of the process.
The app was broken to routes and methods were tested individually.

#### _Integration testing_

Integration testing was achieved via the use of Selenium and the chromium webdriver.
The application was tested as a whole , with simulated inputs from the webdriver

#### _Front end_

* _Home page:_ As we arrive to the home page ('/'), we can see a pre-uploaded recipe (Negroni), ingredient groups, and ingredients. There is also a navigation bar, part of the (layout.html), making it omni-present across all pages. Clicking on the details button, placed next to each recipe will take the user to a page where all information (ingredients, method and quantities) regarding the specified recipe will be shown. The user will also have options to update or delete the recipe here.  
Crud used: READ, DELETE, UPDATE
![home](https://github.com/GregNemeth/individual-project/blob/dev/Images/home.png)

* _Add groups:_ the add groups link will direct the user to a page where they can add further categories to the database. As mentioned earlier this can expand the search capabilities of the app. (For example, the user might have a certain brand of rum, one search function would enable him to look for drinks specifically made with that brand, or alternatively they could look for all the recipes made with rum, etc..)  
Crud used: CREATE
![addgroups](https://github.com/GregNemeth/individual-project/blob/dev/Images/addgroup.png)

* _Add ingredients:_ Another link we find in the navbar is the Add Ingredient. This enables the users to expand the list of ingredients available for creating recipes. This can be useful if in the future login/authentication is added. Imagine the scenario where the app is part of a cocktail blog. Certain functions could be separated, especially create, update and delete. A selected group of people who logs in can act as moderators and access these functions, allowing them to grow the list of recipes and ingredients, while the search/read functions can be used by anyone without login. This way the database would only contain relevant entries, that could be browsed by anyone.  
Crud used: CREATE
![addingred](https://github.com/GregNemeth/individual-project/blob/dev/Images/addingred.png)

* _Add recipe:_ The next item in the navbar is the add recipe. This page allows users to create recipes from the available ingredients. These recipes are then displayed on the home page.  
Crud used: CREATE
![addrec](https://github.com/GregNemeth/individual-project/blob/dev/Images/Add%20recipe.png)

* _Search recipe by name:_ Finally , this function enables users to search recipes by their name.  
Crud used: CREATE
![search](https://github.com/GregNemeth/individual-project/blob/dev/Images/search.png)

* _Update recipe:_ Clicking this button will redirect the user to the page not dissimilar to the _Add recipe_ page. The stringfields are pre-populated to help remind the user which recipe is being modified. Upon submitting the system updates the recipe information, and deletes any old junction tables that are not needed, thus making sure an updated recipe does not contain ingredients from previous versions. 
![updaterec](https://github.com/GregNemeth/individual-project/blob/dev/Images/updaterec.png)


## **Footer**

#### **Future improvements**
As already mentioned earlier, there are several application for this project in the future. Database tables for login and authentication can be added to separate functions for increased control and customizability. With minor modifications the app can be deployed to add extra functions for a cocktail-blog; tables for ingredient prices can be added to refactor the code for use in a business environment, or it can be used as an e-menu for bars and restaurants

#### **Author**

_Gergely Nemeth_

_Acknowledgements:_  
Victoria Sacre  
Oliver Nichols    
Ryan Wright
Peter Jasz