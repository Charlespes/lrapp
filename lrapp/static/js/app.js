/**
 * Created by dell on 2016/12/2.
 */

$(document).ready(function() {
    $('#suggestion').keyup(function() {
        var query;
        query = $(this).val();
        $.get('/suggest_category/', {suggestion: query}, function(data) {
            $('#cats').html(data);
        });
    });

    var query = $('div');
    if(query.hasClass('index')) {
        $('.header .left.first').addClass('active');
    } else if(query.hasClass("create-category")) {
        $(".header .right.create-category").addClass("active");
    } else if(query.hasClass('signup')) {
        $('.header .right.signup').addClass('active');
    } else if(query.hasClass('register')) {
        $('.header .last.register').addClass('active');
    } else {}

    if($("span").hasClass("personal-homepage")) {
        $(".header .right.homepage").addClass("active");
    }

    //用ajax实现收藏或取消收藏
    //$("#fc-or-not").click(function(e) {
    //    e.preventDefault();
    //    var slug_name = $(this).attr("data-var");
    //    $.get('/account/add_or_remove_favorite_category/' + slug_name + '/',
    //        {category_slug_name: slug_name}, function(data){
    //        $("#fc-or-not").html(data);
    //    });
    //});

});
