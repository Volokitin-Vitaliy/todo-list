# Todo list

This is a web application designed a todo list site.


### Project Description

The user can:

- create new tasks,

- manage tasks,

- mark tasks as completed

- add tags for tasks


### Models Overview

**Task**

The Task model represents an item in the to-do list. Each task includes the following fields:

- content – a description of what needs to be done.

- created_at – the date and time when the task was created.

- deadline (optional) – the date and time by which the task should be completed.

- is_done – a boolean indicating whether the task has been completed.

- tags – associated tags that describe the theme or category of the task.

A task can have multiple tags.


**Tag**

The Tag model represents a category or theme for tasks and includes:

- name – the name of the tag.

- a tag can be associated with multiple tasks.

