# COMP 3005 Assignment 3

### Jacob Terkuc
### 101196620
### Due: November 9th, 2025

# Video Link

You can watch the video demonstration of the application [here](https://youtu.be/3ocWruzUzeQ).

Note: I am using Jetbrain DataGrip instead of pgAdmin in this demonstration.

# Requirements

Run the following command from the base project directory to install the requirements:

```
pip install -r requirements.txt
```

# Configuration

At the top of `main.py` is a dictionary containing the values needed to connect to your local PostGresDB instance. 
Change these values to reflect your local settings. 


# Running
In the base project directory, run:

```
python main.py
```

The program will wait for any keypress input before continuing its execution. 

## Note about execution

Note that due to the implementation of the `deleteStudent(student_id)` function, the hard-coded value for the 
student id is `4`, reflecting a newly added user. If user `4` is deleted and the program is run again, the next user 
will have a student id of `5`, which will cause `deleteStudent()` to error out. This can be avoided by creating the 
`students` table from scratch.

The program assumes that a table `students` has already been created in the database. This can be done with the 
provided `a3-create.sql` file. 