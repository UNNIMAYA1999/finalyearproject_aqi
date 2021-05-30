let dailyAqi;
let dailyDate;
let obj;

$.get('/daily-pred',(data)=>{
  console.log('Inside JQUERY Method - daily pred')
  console.log(data)
  JSON.stringify(data)
  //obj = jQuery.parseJSON(data);

     dailyAqi = data.aqi;
     dailyDate = data.date;
    // dailyAqi = obj.aqi
    // dailyDate = obj.date
    console.log(dailyAqi)
    console.log(dailyDate)


})











// $(document).ready(function(){
// console.log("Inside NEWWW JQUERY Method - for plotting daily data")
// var graphDiv = document.getElementById('dailyPredDiv')
// var data = [{
//   x: [1999, 2000, 2001, 2002],
//   y: [10, 15, 13, 17],
//   type: 'scatter'
// }];

// var layout = {
//   title: 'Sales Growth',
//   xaxis: {
//     title: 'Year',
//     showgrid: false,
//     zeroline: false
//   },
//   yaxis: {
//     title: 'Percent',
//     showline: false
//   }
// };
// Plotly.newPlot(graphDiv, data, layout);
// });




$(document).ready(function(){
  //$("div").click(function() {
   // alert("Hello, world!");
   setTimeout(function() {
    console.log("Inside JQUERY Method - for plotting daily data")
    var trace1 = {
    type: "scatter",
    mode: "lines",
    name: 'AQI',
     x: dailyDate,
    //x: [1999, 2000, 2001, 2002],
     y: dailyAqi,
    //y: [10, 15, 13, 17],
    line: {color: '#D8001F'}
  }
  




  var data = [trace1];

  var layout = {
    autosize: true,
  width: 1150,
  height: 601,
  margin: {
    l: 50,
    r: 50,
    b: 100,
    t: 100,
    pad: 4
  },
    title: 'Daily AQI Predictions',
    xaxis: {

      autorange: true,
      range: ['2021-04-20', '2025-02-16'],
      type: 'date'
    },
    yaxis: {
      autorange: true,
      range: [0, 1000],
      type: 'linear'
    }
  };

  Plotly.newPlot('dailyPredDiv', data, layout);
}, 2000);
});
 // });







