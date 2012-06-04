$(function($) {
    var palette = new Rickshaw.Color.Palette({scheme: 'spectrum2000'});
    var graph = new Rickshaw.Graph.Ajax({
      element: document.getElementById("chart"),
      renderer: 'area',
      stroke: true,
      width: 200,
      height: 700,
      dataURL: '/stats/patients/delta.json',
      onData: function(d){
        // Hide the Spinner
        return $.map(d, function(i){ i["color"] = palette.color(); return i; });
      },
      onComplete: function(s){
		var hoverDetail = new Rickshaw.Graph.HoverDetail({
		  graph: s.graph,
		  xFormatter: function(x) { var d = new Date(x*1000); return "Week of " + d.toString("MMM d"); },
		  yFormatter: function(y) { return parseInt(y) + " patients"; }
		});
		
		var ticksTreatment = 'glow';
		
		var xAxis = new Rickshaw.Graph.Axis.Time({
		  graph: s.graph,
		  timeUnit: 'week',
		  ticksTreatment: ticksTreatment
		});
		
		var yAxis = new Rickshaw.Graph.Axis.Y({
		  graph: s.graph,
		  tickFormat: Rickshaw.Fixtures.Number.formatKMBT,
		  ticksTreatment: ticksTreatment
		});
		
		xAxis.render();
		yAxis.render();				
      }
   });
});