#!/usr/bin/python
import os

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

def application(environ, start_response):

    ctype = 'text/plain'
    if environ['PATH_INFO'] == '/health':
        response_body = "1"
    elif environ['PATH_INFO'] == '/env':
        response_body = ['%s: %s' % (key, value)
                    for key, value in sorted(environ.items())]
        response_body = '\n'.join(response_body)
    else:
        ctype = 'text/html'
        response_body = '''<!DOCTYPE html>
<html>
<head>
  <title> CMPUT 496 task tracker</title>
  <link rel="stylesheet" type="text/css" href="tasktracker.css">
	<style>
.header{
  
  text-align:center;
  
}

.main{
  padding:1em 1em 1em 1em;
  margin-left:auto;
  margin-right:auto;
  width:25%;
  background:lightblue;
}

.main input{
  
  margin-top:0.5em;
  margin-bottom:2em;
  width:70%;
}

button{
  
  margin-bottom:2em;
  
}</style>


<script>

categories={};
window.onload = function(){
  
  //var searchBar = document.getElementsByClassName("searchInput");
  //console.log(searchBar);
  
  var newCategoryBar = document.getElementsByClassName("newCategoryIN");
  
  //searchBar[0].addEventListener("keyup",searchFocused);
  newCategoryBar[0].addEventListener("keyup", newCategoryFocused);
  
  //function searchFocused(event){
    
    //console.log(searchBar[0].value);
    
    //if (event.keyCode == 13){
      
      //console.log("yo");
    //}
    
    
  //}
  
  function newCategoryFocused(event){
    console.log("im focused: " + this.value);
    if (event.keyCode == 13){
      var newCategoryBar = document.getElementsByClassName("newCategoryIN");
      var categoryInput = newCategoryBar[0].value;
      console.log(newCategoryBar);
      categories[categoryInput] = [];
      console.log(categories);
      addCategory(categoryInput);
      newCategoryBar[0].value = '';
      
    }
    
    function addCategory(categoryInput){
    
      var categoryLists = document.getElementsByClassName("listOfCategories");
      var categoryList = categoryLists[0];
      console.log(categoryList);
    
      var textCategory = document.createTextNode(categoryInput);
      var categoryLI = document.createElement('LI');
    
      categoryLI.appendChild(textCategory);
      categoryLI.setAttribute('id',categoryInput);
      categoryList.appendChild(categoryLI);
    
      var taskInput = document.createElement('INPUT');
      var taskTextNode = document.createTextNode("add Task");
      taskInput.appendChild(taskTextNode);
      taskInput.setAttribute('id',categoryInput+"addTask");
      taskInput.setAttribute('placeholder' , "add a task");
      categoryList.appendChild(taskInput);
      //console.log(taskInput.parentNode);
      taskInput.addEventListener('keyup' , function(event){
      
        if(event.keyCode===13){
      
          addTask(categoryInput,this.value);
          this.value='';
      }
      
      function addTask(category,taskInput){
      
        var categoryTaskList = document.getElementById(category+"Tasks");
        console.log(categoryTaskList);
        var taskLI = document.createElement('LI');
        console.log("this is taskLI: " +taskLI );
        taskLI.setAttribute('id' , category+taskInput);
        console.log(taskLI.id);
        var textTask = document.createTextNode(taskInput);
    
        taskLI.appendChild(textTask);
        categoryTaskList.appendChild(taskLI);
    
          categories[category].push(taskInput);
          console.log(categories);
    
        taskLI.addEventListener('click' ,function(){
      
          this.parentNode.removeChild(this);
      
        });
    
    
      }
  
      
    });
    
    var deleteCategoryBT = document.createElement("BUTTON");
    var deleteBTText = document.createTextNode("delete " + categoryInput);
    deleteCategoryBT.appendChild(deleteBTText);
    categoryList.appendChild(deleteCategoryBT);
    categoryList.setAttribute("style" , "font-size:150%");
    deleteCategoryBT.addEventListener('click' , function(){
      
      var categoryToDelete = document.getElementById(categoryInput);
      categoryToDelete.parentNode.removeChild(categoryToDelete);
      var inputTaskbar = document.getElementById(categoryInput+"addTask");
      inputTaskbar.parentNode.removeChild(inputTaskbar);
      this.parentNode.removeChild(this);
      
    });
    
    
    var taskUL = document.createElement('UL');
    taskUL.setAttribute('id' , categoryInput+"Tasks");
    //taskUL.setAttribute("style", "font-size:100%");
    categoryLI.appendChild(taskUL);
    console.log(taskUL);
    
    
  }
    
  }
  
  
  
  function addTask(category,taskInput){

    var categoryTaskList = document.getElementById(category+"Tasks");
    console.log(categoryTaskList);
    var taskLI = document.createElement('LI');
    console.log("this is taskLI: " +taskLI );
    taskLI.setAttribute('id' , category+taskInput);
    console.log(taskLI.id);
    var textTask = document.createTextNode(taskInput);
    
    taskLI.appendChild(textTask);
    categoryTaskList.appendChild(taskLI);
    
    taskLI.addEventListener('click' ,function(){
      
      this.parentNode.removeChild(this);
      
    });
    
    
  }
  
  //addCategory('School');
  
  //addTask is fully function type in the input
  //enter to submit ur task
  //click on the task to delete it
  
  //addTask('School' , "finish 496");
};




</script>

  <script type="text/javascript" src="tasktracker.js"></script>



</head>
<body>
  
  <div class ='container-fluid'>
     <div class ="header">
    <h1> Keep Track of Your Tasks</h1>
    
  </div>
  <div class='main'>
   <!-- Search:<input class='searchInput' type='text'/> -->
    +New Category: <input class= 'newCategoryIN' type="text"/>

  <div class="existingCategories">
   <ul class="listOfCategories">
    
   </ul>
    
    
 </div>
 </div>

</body>

</html> '''

    status = '200 OK'
    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
    #
    start_response(status, response_headers)
    return [response_body]

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.handle_request()
