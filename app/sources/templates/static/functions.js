// Figure update
function showFigure() {
    var datasetId = $("#datasets").val();
    var channel = $("#channels").val();
    var figure = $("#figures").val();
    var sliceEnd = $("#slice-end").val();
    $.ajax({
        url : '/analysis',
        type : 'POST',
        data : { datasetId: datasetId,
                 channel: channel,
                 sliceStart: 0,
                 sliceEnd: sliceEnd,
                 figure: figure },
        success: function(data) {
            var slot = document.getElementById("figure");
            slot.innerHTML = "";
            if(data.content != "empty") {
                var myFig = JSON.parse(data.content);
                Plotly.newPlot(slot, myFig);
            }
            else {
                slot.innerHTML = "<div>\
                                      <p>No data available for the selected dataset/channel.</p>\
                                  </div>";
            }
        },
        error: function() {
            console.log("Errou!");
        }
    });
}

// Figure update triggered by any dropdown change
$(document).ready(function() {
    showFigure();
    $("select").on("change", function() {
        showFigure();
    });
});

// Figure size adjustment triggered by window resizing
$(window).resize(function(){
    showFigure();
});












