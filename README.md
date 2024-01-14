# 0x00. AirBnB clone
This the beginning part of our team project to develop a clone copy of the AirBnB website. In this part, we've created a backend interface, like a control panel, to handle program information. With commands in the control panel, users can make, modify, or remove things and handle file storage. We use a system called JSON to keep data saved even when you close and reopen the program.

The AirBnB project is a project to implement a full web application that mimics the AirBnB web application. This is no a 100% replica of the site but an implementation with fundamental functions. The aim was to provide us the students with a learning opportunity to grasp fundamental concepts.  

## The Console
The console is the first step towards building our first full web application: the AirBnB clone.  
The very first step is involved and is important because it laid the foundation for subsequent projects:  
	- HTML/CSS templatinig  
	- Database storage  
	- API  
	- Front-end integration
## The Command Interpreter
For the console project, the major part was building a command interpreter. You think of this like a mini-shell implmented within python, using python's cmd module.  
This interpreter is to be used to manage objects for the project - implementing CRUD.  
	- Create a new   
	- Retrieve an object from file  
	- Update object attributes  
	- Destroy an object  
	- Do operations on the data saved
#### How to start the interpreter
Running the interpreter is straight forward. Look for the file name 'console.py' in the directory. It is already executable.   
./console.py or python3 console.py should start the interpreter for you.

#### How to use it
The interpreter comes with a 'help' command that provides information about every other command implemented. When you prompt is displayed :    
	- prompt: help + ENTER - prints information and all commands avialble  
	- prompt: help <command> - prints information about the command  
	- prompt: <command> <argument> - runs command on given argument

#### Examples
	- prompt: quit - ends the interpreter session
	- prompt: ctrl+D - same as quit
	- prompt: count <class_name> - prints number of instances

Explore ....


## Project Tasks
To build this part of the project; AirBnB clone, the project was broken into tasks. The different tasks when implemented, together resulted to an amazing piece of work.

### Note:
Tasks 0 to 2 involved good practices requirements  
	- Writing this README as well as AUTHORS file  
	- Ensuring my python3 code compplies with pycodestyl  
	- Writing test cases for the entire project

### Task 3: BaseModel
We started the project by implemeting this class that served as the base class for every other class in the project.   
The class defines all common attributes and methods to be inherited by other classes.

### Task 4: Create BaseModel from dictionary
One of the methods implemented in the BaseModel class, converted class instances to dcitionary representation. In this task, we did the reverse, from dictionary representation, we recreated the instance.

### Task 5: Store first object
Here, we implemented data persistence using serialization and deserialization of data to and from JSON file. Prior to this stage, every data we handle would be lost when the interpreter session is ended. Here we serialize to JSON - writing to file in JSON format and deserialize - reading from file in dictionary representation.  
We implemented FileStorage class to handle the process explained above.  

### Tasks 6 and 7: Console
Here we started the implemetation of the command interpreter. At this stage the interpreter is able to handle basic commands.  
All of these commands have to do with class instances:  
	- creating an instance  
	- reading from file  
	- updating instances  
	- destroying instances  
	- printing instances etc

### Tasks 8 and 9: User and more classes
By now, you must have deduced we are using OOP. We implemented User as well as other classes to handle very objects in the project. Among these classes, we have city, place, amenity review etc.  
All these classes inherit from BaseModel which is the base class in this project.

### Task 10: Console 
Here we updated our file storage class.  
This class is responsible fr serialization and deseriaization, but so far it dioes so only for BaseModel and User classes. Here, we updated it to handle data from every other class.

### Task 11: All instances by class name
Our interpreter has a command that prints all existing instances.  
In this task, we updated, that command and made it class-specific.  
Now, it prints instances by class name.

### Task 12: Count instances
Here, we introduced a new command, count that returns the number of existing instances of a given class.

### Task 13: Show.
We implemented the show command to retrieve class instances. In this task, we make ID specific. Using Id and class name, this command retrieves instances.

### Tasks 14 and 15: Destroy and Update
We pretty much implemented the same thing here as in task 13.

# Conclusion
This is the end of the first part of implementing the AirBnB clone. 
  
