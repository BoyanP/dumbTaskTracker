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

