$("#loginButton").click(function () {
    if ($("#checkBox").prop("checked")) {
        window.redirect.submit();
    } else {
        alert("請打勾授權");
    }
});

$("#openAgreement").click(function () {
    $("#agreementIframeDivID").show();
});

$("#closeAgreementIframeID").click(function () {
    $("#agreementIframeDivID").hide();
});

