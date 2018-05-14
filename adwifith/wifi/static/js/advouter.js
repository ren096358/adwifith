var whRate = 3 / 2;
var loadCom = false;

$("#advIframe").attr("src", adUrl);
$("#advIframe").height($("#advIframe").width() * whRate);
if (window.addEventListener) {
    window.addEventListener("message", postMessageHandler, false);
} else {
    window.attachEvent("onmessage", postMessageHandler);
}

function postMessageHandler(event) {
    //console.log(event.data);
    switch (event.data.method) {
        case "adwifi_DispalyLayout":
            //whRate = obj.height / obj.width;
            $("#advIframe").height($("#advIframe").width() * whRate);
            loadCom = true;
            break;
        case "adwifi_EventTrigger":
            if (event.data.action == "auth") {
                $.ajax({
                    url: "inurl",
                    type: 'POST',
                    data: {
                        rid: rid,
                        mac_: mac_,
                        url: event.data.url
                    },
                    error: function (xhr) {
                        console.log(xhr);
                    },
                    success: function (response) {
                        if (response.result) {
                            //alert("登入成功");
                            window.redirect.submit();
                        } else {
                            console.log(response);
                        }
                    }
                });
            }
            break;
    }
}

$(window).on("resize", function () {
    $("#advIframe").height($("#advIframe").width() * whRate);
});
