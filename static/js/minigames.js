var getBarrel = 1;
function UpgradeBarrel() {
    $(".getbarrel").hide();
    $(".getbarrel").show();
}

$(document).ready(function() {
    UpgradeBarrel();
    setInterval(UpgradeBarrel, 3000);
});
