html_first_part = """
<!DOCTYPE html>
<html>
<title>HMI Automation Report</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>

<div class="w3-container">

<h2 style="text-align:center">Test Execution Report</h2>
<br>


        <style type="text/css"> 
        .container {
           
            height:200px;
           
            padding-top:10px;
            padding-left:0px;
            padding-right:0px;
        }

        #nd-box {
            float:right;
            width:50%;
            height:200px;            
            border:solid black;
            margin-right:10px;
        }


        </style> 
        
                <style type="text/css"> 
        .collapsible {


  cursor: pointer;

  width: 50%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;



}

        .collapsible1 {


  cursor: pointer;

  width: 50%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;



}


.active, .collapsible:hover {

}



.collapsible:after {
  content: '-';


  float: right;
  margin-left: 5px;

}

.active:after {
  content: "-";
}


tr:nth-child(4n+0) td,
tr:nth-child(4n+1) td {
    background-color: #EEFDFA;
}

tr:nth-child(4n+2) td,
tr:nth-child(4n+3) td {
    background-color: #EEFDFA;
}


button:nth-child(4n+0),
button:nth-child(4n+1) {
    background-color: #EEFDFA;
}

button:nth-child(4n+2),
button:nth-child(4n+3) {
    background-color: #FFFFFF;
}


.content {
  padding: 0 18px;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease-out;
  background-color: #f1f1f1;
}
        .container {
           
            height:200px;
           

            padding-left:0px;
            padding-right:0px;
        }

        #nd-box {
            float:right;
            width:50%;
         


        }
        
        .collapsible:after {
  content: '+'; 
  font-size: 12px;
  color: black;

   font-weight: 900;


}

        .collapsible1:after {
  content: '-'; 
  font-size: 12px;
  color: black;

   font-weight: 900;


}

.active:after {
  content: "+"; /* Unicode character for "minus" sign (-) */
}


        </style> 


      
         
<div class="container" style="border-style:borderless;">      
<div id="piechart" style="border-style:groove;border-width: thin;border-color:#06C7A5;width:40%; float:left;"></div>
<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    } 
  });
}
</script>


<script>
function zzz() {

alert("ff")


}
</script>
<script>
function myFunction(param, rows12) {
var xx = (parseInt(param))
var x = document.getElementById("aaa_"+param);


  

  


 for (i=1;i<=100;i++){ 
 try{
    var y = document.getElementById("bbb_"+param.toString()+"_"+i.toString());
    if (y.style.display==''){
    y.style.display = "none";
    }else{
    y.style.display=''
    }
    
    }catch(err){break;}

    
  }


  if ((xx%2)==0){

x.style.backgroundColor='#FFFF00';
y.style.backgroundColor='#FFFF00';
}else{

x.style.backgroundColor='#FF0000';
y.style.backgroundColor='#FF0000';

}
  
  


}
</script>

<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

<script type="text/javascript">
// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Draw the chart and set the chart values
function drawChart() {
  var data = google.visualization.arrayToDataTable([
  ['Result', 'Status'],
  ['NA', 0],
  ['FAIL', 1],
  ['BLOCKED', 0],
  ['PASS', 0],

]);

  // Optional; add a title and set the width and height of the chart
  var options = {'title':'Test Statistics', 'width':450, 'height':200};

  // Display the chart inside the <div> element with id="piechart"
  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
  chart.draw(data, options);
}

</script>

"""

html_last_part = """
              
            <div id="nd-box" style="border-style:groove;border-width: thin;border-color:#06C7A5">
            <div style="font-size:12px;padding-left:10px;padding-top:10px;"><b>Test Suit Name : </b>Web Portal Test</div>
            <div style="font-size:12px;padding-left:10px;padding-top:10px;"><b>Device Type &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: </b>Browser</div>
            <div style="font-size:12px;padding-left:10px;padding-top:10px;"><b>Build &emsp;&emsp;&emsp;&emsp;&emsp;&ensp;: </b>Portal_v_1.2.1</div>
            <div style="font-size:12px;padding-left:10px;padding-top:10px;"><b>Test Duration &ensp;&nbsp;: </b>0 hr 1 min 6 sec </div>
            <div style="font-size:12px;padding-left:10px;padding-top:10px;"><b>Total Tests &emsp;&emsp;&nbsp;: </b>20</div>
            <div style="font-size:12px;padding-left:10px;padding-top:10px;"><b>Language &emsp;&emsp;&emsp;: </b>English</div>
            <div style="font-size:12px;padding-left:10px;padding-top:10px;"><b>Date &emsp;&emsp;&emsp;&emsp;&emsp;: </b>2023-07-12</div>
            </div>
               
              

        








<br>
<table id="myTable" class="w3-table-all w3-small">
<caption style="text-align:left"><h6><b>Test Execution Result</b></h6></caption>
<tr style="background-color:#06C7A5">
  <th>SI No</th>
  <th>Test ID</th>
  <th>Suite Name</th>
  <th>Test Name</th>
  <th>Summary/Steps</th>
  <th>Expected Result</th>
  <th>Actual Result</th>
  
  <th>Status</th>
  <th>Execution Time</th>
  <th>Screenshots</th>
</tr>"""

test_case_row = """
<tr>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>

  <td style="background-color:%s"><center>%s</center></td>
  <td>%s</td>
  <td>
  <a href=%s target="_blank" style="color:blue;">%s</a>
  </td>
</tr>

"""

html_end = """




</table>
</div>



</div>

</body>
</html> 



"""
