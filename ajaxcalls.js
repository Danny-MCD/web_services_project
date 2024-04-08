
 
    function getAll(callback){
        $.ajax({
            "url": "http://DanielMcDonagh.eu.pythonanywhere.com/actors",
            "method":"GET",
            "data":"",
            "dataType": "JSON",
            "success":function(result){
                //console.log(result);
                callback(result)
     
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }

    // testing code
    function createActor(actor, callback){
        console.log(JSON.stringify(actor));
        $.ajax({
            "url": "/Actors",
            "method":"POST",
            "data":JSON.stringify(actor),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                //console.log(result);
                callback(result)  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }
    function updateActor(actor, callback){
        console.log("updateing " +JSON.stringify(actor));
        $.ajax({
            "url": "/Actors/"+encodeURI(book.id),
            "method":"PUT",
            "data":JSON.stringify(actor),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                console.log(result);
                callback(result)   
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }
    function deleteActor(id, callback){
        $.ajax({
            "url": "/Actors/"+id,
            "method":"DELETE",
            "data":"",
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                console.log(result);
                callback(result)  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }



    // testing code
    
    function processGetAllResponse(result){
        console.log("in process")
        //console.log(result)
        for (actor of result){
            //console.log(actor)
            // issue the format of the actor object is different from lab06.02
            // there are two solutions change the book object in lan06.02 to have capitals 
            // or convert
            displayActor = {}
            displayActor.id = actor.id
            displayActor.name = actor.Name
            displayActor.title = actor.Title
            displayActor.price = actor.Price
            // you can now pass it to addActorToTable
            console.log(displayActor)
        }
    }
     getAll(processGetAllResponse)

     ///// Create
    function processCreateResponse(result){
        console.log(result)
    }
    //book = {"Title":"javascript","Author":"andrew","Price":12} 
    //createBook(book,processCreateResponse) 

    //// update
    function processUpdateResponse(result){
        console.log(result)
    }
    actor = {id:15,"Age":999} 
    //updateBook(actor,processUpdateResponse)
    
    ////delete
    
    function processDeleteResponse(result){
        console.log("in pprocess delete")
        console.log(result)
    }
    //deleteBook(155,processUpdateResponse) 


