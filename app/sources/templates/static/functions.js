// Alteração da figura
function showFigure() {
    var dataset = $("#datasets").val();
    var channel = $("#channels").val();
    var figure = $("#figures").val();
    $.ajax({
        url : '/analysis',
        type : 'POST',
        data : { dataset_id: dataset,
                 channel: channel,
                 slice_start: 10,
                 slice_end: 90,
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

// Alteração da figura pelo dropdown de figura
$(document).ready(function() {
    showFigure();
    $("select").on("change", function() {
        showFigure();
    });
});

// Ajuste do tamanho da figura quando a janela é redimensionada
$(window).resize(function(){
    showFigure();
});

