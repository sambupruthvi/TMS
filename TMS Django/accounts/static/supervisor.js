function filter_by_date() {
  var from = document.getElementById("min").value;
  var to = document.getElementById("max").value;
  from = new Date(from);
  to = new Date(to);
  table = document.getElementById("example");
  tr = table.getElementsByTagName("tr");
  for (i = 1; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[3].innerHTML;
    date = new Date(td);
    if(from <= date && date <= to){
      tr[i].style.display = "";
    }else{
      tr[i].style.display = "none";
      console.log(from, date, to);
    }
  }
  }

  function search_by_name(){
    var input = document.getElementById("input_by_name");
    filter = input.value.toUpperCase();
    table = document.getElementById("example");
    tr = table.getElementsByTagName("tr");
    for (var i = 1; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[1];
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }