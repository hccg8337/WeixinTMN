/* 设置自适应宽度 */
/*$(window).resize(function(){
    var deviceWidth=$(window).width();
    alert(deviceWidth);
    if(deviceWidth>640){
        $("html").css("font-size","85px");
    }else{
        $("html").css("font-size",100*(deviceWidth/750)+'px');
    }
}).resize();*/

/* 关闭公告 */
$(function(){
    $(".notice-close").click(function(){
        $(this).parents(".notice-box").removeClass("notice-in");
    });
});