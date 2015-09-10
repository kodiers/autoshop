$(document).ready(function () {
//function test_button (id) {
    $('a[name=modal]').click(function (e) {
        e.preventDefault();
        var id = $(this).attr('href');
        var maskHeight = $(document).height();
        var maskWidth = $(window).width();
        var good_url = '/modal_good/' + $(this).parent().parent().find("td[id='td_pp']").find('input').val();
        //var good_url = '/dict/' + id
        console.log(good_url);
        $('#mask').css({'width': maskWidth, 'height': maskHeight});
        $('#mask').fadeIn(1000);
        $('#mask').fadeTo("slow", 0.8);
        var winH = $(window).height();
        var winW = $(window).width();
        $(id).css('top', winH / 2 - $(id).height() / 2);
        $(id).css('left', winW / 2 - $(id).width() / 2);
        $(id).fadeIn(2000);

        $.getJSON(good_url)
            .success(function (data) {
                $.each(data, function (key, val) {
                    $("#ajaxPartnumber").html("Артикул: "+data.partnumber);
                    $("#ajaxTitle").html(data.title);
                    $("#ajaxDescription").html(data.description);
                    $("#ajaxPrice").html("Цена: "+data.price+" руб.");
                    $("#ajaxImage").html("<img src=" +data.image+ " style=\"max-width: 100%; max-height: 100%;\">");
                    $("#ajaxPk").html("<input type='hidden' name='good_id' value='"+data.pk+"'>")
                });

            })
            .error(function () {
                alert("Error !");
            })

    });

    $('.window .close').click(function (e) {
        e.preventDefault();
        $('#mask, .window').hide();
    });
    $('#mask').click(function () {
        $(this).hide();
        $('.window').hide();
    });
//}
});