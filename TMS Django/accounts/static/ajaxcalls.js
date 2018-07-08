$(document).ready(function() {
       $('#my_form1').submit(function() { // catch the form's submit event
            $.ajax({ // create an AJAX call...
               data: $(this).serialize() + '&perform=add', // get the form data
               type: $(this).attr('method'), // GET or POST
               dataType: "json",
               url: $(this).attr('action'), // the file to call
               success: function(data){
                    d = data
                    console.log(data);
                    //if ($('button').val() == 'Add'){
                      text = ''
                      for (var i = 0; i < Object.keys(d["data"].employees_could_add).length; i++) {
                        text += '<tr>'
                        text += '<td><input type="checkbox" name="employees_inproject" value=" '
                        text +=  data['data'].employees_could_add[i].id + '">'
                        text += data['data'].employees_could_add[i].emp_name + '</td></tr>'
                      }
                      text += '<tr><td><button class="btn btn-primary" name="perform" value = "Add" type="submit">Add Employees</button></td></tr>'
                      document.getElementById("change_form1").innerHTML = text
                      text = ''
                      for (var i = 0; i < Object.keys(d["data"].employees_inproject).length; i++){
                          text += '<tr> <td><input type="checkbox" name="employees" value="'
                          text += data['data'].employees_inproject[i].id + '">'
                          text += data['data'].employees_inproject[i].emp_name + '</td></tr>'
                      }
                      text += '<tr><td><button class="btn btn-danger" name="perform" value="delete" type="submit">Delete</button></td>'
                      document.getElementById("change_form2").innerHTML = text
                },
                error:function(data){
                        console.log('error')
                        console.log(data)
                 }
           });
           return false;
       });

       $('#my_form2').submit(function() { // catch the form's submit event
            $.ajax({ // create an AJAX call...
               data: $(this).serialize() + '&perform=delete', // get the form data
               type: $(this).attr('method'), // GET or POST
               dataType: "json",
               url: $(this).attr('action'), // the file to call
               success: function(data){
                    d = data
                    console.log(data);
                    //if ($('button').val() == 'Add'){
                      text = ''
                      for (var i = 0; i < Object.keys(d["data"].employees_could_add).length; i++) {
                        text += '<tr>'
                        text += '<td><input type="checkbox" name="employees_inproject" value=" '
                        text +=  data['data'].employees_could_add[i].id + '">'
                        text += data['data'].employees_could_add[i].emp_name + '</td></tr>'
                      }
                      text += '<tr><td><button class="btn btn-primary" name="perform" value = "Add" type="submit">Add Employees</button></td></tr>'
                      document.getElementById("change_form1").innerHTML = text
                      text = ''
                      for (var i = 0; i < Object.keys(d["data"].employees_inproject).length; i++){
                          text += '<tr> <td><input type="checkbox" name="employees" value="'
                          text += data['data'].employees_inproject[i].id + '">'
                          text += data['data'].employees_inproject[i].emp_name + '</td></tr>'
                      }
                      text += '<tr><td><button class="btn btn-danger" name="perform" value="delete" type="submit">Delete</button></td>'
                      document.getElementById("change_form2").innerHTML = text
                },
                error:function(data){
                        console.log('error')
                        console.log(data)
                 }
           });
           return false;
       });
   });
