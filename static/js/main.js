var $jq = jQuery.noConflict();

$jq.ajaxSetup({
  contentType: "application/json; charset=utf-8"
});

function reloadPage(){
        location.reload(true);
    }

$jq(function() {
    $jq("button.btn-lg").click(function() {
        console.log($jq("button.btn-lg").html())
        var sentObj
        sentObj = {
            "app_code": document.getElementById("appcode").value,
            "os_version_int": document.getElementById("osversion").value,
            "is_4G": document.getElementById("is4g").value
        }
        $jq.post("localhost:5000", JSON.stringify({"answer": sentObj}), function( data ) {
            console.log("masuk dia")
            $jq("p").html(data);
        }, "json" )
    });
});
