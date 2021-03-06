

(function() {

$.get('/statistics-data',(data)=>{
        console.log("*******");
        NallData = data.allstate_so2_no2_pm10_co;
        console.log("ALL DATA",data)
    allStateGraph(NallData);

    })


})();


function allStateGraph(NallData){
    let margin = {left: 100, bottom: 100, right: 10, top: 10}

    let width = 1200 - margin.left - margin.right;
    let height = 800 - margin.top - margin.bottom;


    let div3 = d3.select('#div3')
        .append('svg')
        .attr('height', height + margin.top + margin.bottom)
        .attr('width', width + margin.left + margin.right)

    let g = div3.append('g')
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
    let allData = NallData;    // console.log(allData.length);
    console.log("Called in funcion",allData)
    let cityName = allData[0];
    let so2 = allData[1];
    let no2 = allData[2];
    let co2 = allData[3];
    let pm2 = allData[4];

    // console.log(cityName.length, so2.length, no2.length, co2.length, pm2.length);

    let newData = cityName.map((x, i) => {
        return {
            name: x,
            height: so2[i]
        }
    })


    let x = d3.scaleBand()
        .domain(newData.map((d) => {
            // console.log("DNAME", d.name)
            return d.name
        }))
        .range([0, width])
        .paddingInner(0.3)
        .paddingOuter(0.3);
    // console.log(x.bandwidth)

    let y = d3.scaleLinear()
        .domain([0, d3.max(newData, (d) => {
            return d.height;
        })])
        .range([height, 0])


    let xAxis = d3.axisBottom(x);
    g.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
        .selectAll("text")
        .attr("y", "10")
        .attr("x", "-5")
        .attr("text-anchor", "end")
        .attr("transform", "rotate(-40)")

    let yAxis = d3.axisLeft(y);
    g.append("g")
        .attr("class", "y-axis")
        .call(yAxis);

    let rect = g.selectAll('rect')
        .data(newData)

    rect.enter()
        .append('rect')
        .attr('x', (d) => {
            // console.log(x(d.name))
            return x(d.name);
        })
        .attr('y', (d) => {
            return y(d.height)
        })
        .attr('height', (tempD) => {
            return height - y(tempD.height)
        })
        .attr('width', x.bandwidth)

        .attr('fill', 'red')

}