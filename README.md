# pybp
*Py*thon *B*atch *P*rocessor

A commandline utility to reliably execute programs with a large set of files. Main features include the ability to save and review an execution plan before running it and resiliency against program or system outages by using ACID operaitions.

## Coordinator
The coordinator provides the main interface for the user with the help of a text-based input loop.
In here they can
- Create a new execution plan
- Edit an existing execution plan
- Show details of an existing execution plan
- Append/Merge two plans
in a guided manner.

## Worker
The worker is the one running one execution plan. It can only be invoked via commandline and will quit once the plan is done. Any further configuration must be provided in the plan itself.
Some further ideas are:
- Ability to start work in multiple threads
- Capture stdout and write it to a log
- Notification once plan is done (Teams webhook?)

## Execution Plan
The execution plan is provided in the form of a sqlite db. It has the following structure
### Options
A table with key / value pair options that can influence the worker's behavior.
### Actions
A table with the actions that the worker should take. Each row consists of a programm call, a file name as well as a status field. An action's status will change from `PLANNED` over `RUNNING` to `FINISHED`.