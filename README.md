# Cocktail recipe finder - Tipsy Tuesday

## **Contents**

 * [Introduction](#introduction)
   * [Objective](#objective)
   * [Proposal](#proposal)
 * [Architecture](#architecture)
   * [Jira board](#project-tracking)
   * [Entity Relationship Diagram](#entity-relationship-diagram)
   * [Risk assessment](#risk-assessment)
   * [Test analysis](#test-analysis)
   * [Continuos Integration](#continous-integration)
 * [Development](#development)

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

We can see below the actual UML styled Entity-Relationship Diagram,and the older versions further below:

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

#### _Test analysis_

This project included unit and integration testing, which was achieved by PyTest and Selenium. The tests were configured via a .coverage file, to exclude any unneccessary items(ie venv/). Tests were run both locally and on a Jenkins server as well. See images of the results below:
<div style="block;"> 
<img align="left" src="https://github.com/GregNemeth/individual-project/blob/feature/Images/cobertura_adobespark.png" alt="cobertura"/>
<div style="block;"> 
<img align="right" src="https://github.com/GregNemeth/individual-project/blob/feature/Images/pytest.png" alt="pytest"/>


## **Development**

