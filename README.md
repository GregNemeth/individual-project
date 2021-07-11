# Cocktail recipe finder - Tipsy Tuesday

## **Contents**

 * [Introduction](#introduction)
   * [Objective](#objective)
   * [Proposal](#proposal)
 * [Architecture](#architecture)
   * [Jira board](#jira-board)
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

I have come up with the idea of building an app that would help users find cocktail recipes, based on the ingredients they might have at home.

The implementation of CRUD can be seen below:

#### _Create:_
* user
* add available ingredients
* upload own recipes
  * recipe name
  * ingredients
  * measures
  * methods
  * notes
#### _Read:_
* Retrieve list of recipes that match the given ingredients
* Get recommendations like:
  * If you can pop down to the shop for an xyz, you could also make this drink!
  * If you have a couple of lemons lying around, you could also use this recipe!
  * If you happen to have some sugar, it could be used in this tasty beverage!
#### _Update:_
* Update/Modify ingredients Given
* Modify own recipes

#### _Delete:_
* Remove own recipes
* Remove ingredients given
* Delete User account

## **Architecture**

For project tracking I intend to use Jira. Practicing with this tool is going to be handy,  considering it is widely adoptded and its ability to be integrated with other parts of the development pipeline.

![First tasks in Jira](https://github.com/GregNemeth/individual-project/blob/dev/Images/Jira_beginning.bmp) 

We can see below the UML styled Entity-Relationship Diagram:


![erd_diagram](https://github.com/GregNemeth/individual-project/blob/dev/Images/ERD.png)


<div style="block;"> 
<img align="right" src="https://github.com/GregNemeth/individual-project/blob/dev/Images/chen_diagram.png" alt="Chen_diagram"/>

As we take a look at the diagrams we can observe that a many-to-many relationship is achieved through the use of a junction table,
combining multiple one-to-many relations.
<br/><br/> 
This scheme can be expanded in the future, for example: if we would like to implement a login/authentication feature we could connect further tables to handle user names, password, storage and sharing of favourite recipes; 
<br/><br/>
However, for now , this is outside of the current scope of the project.

For the sake of completeness I also inculed a Chen-style diagram we can see on the right.

</div>


## **Development**

