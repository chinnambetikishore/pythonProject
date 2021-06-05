Feature: check duplicate

   Scenario: find the duplicate
     Given connect to mysql
     When validate the data in msql
     Then show me duplicate values