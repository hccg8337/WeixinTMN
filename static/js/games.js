"use strict";



function datepickerInit(id, date) {
    var dateTag = $(id);
    var s = date.substr(0, 4) + '-' + date.substr(4, 2) + '-' + date.substr(6, 2);
    dateTag.attr('value', s);
    dateTag.datepicker({
        format: 'yyyy-mm-dd'
    }).on('changeDate.datepicker.amui', function (event) {
        console.log(event.date);
    });
}

function clearView() {
    $.each($('#view').children(), function (i, v) {
        v.remove();
    })
}

function createGamesTemplatesSelector() {
    var $temp = $('<div id="GamesTemplatesSelector"></div>');
    $temp.append($('<h2>模板选择</h2>'));
    return $temp;
}

function createGamesTemplate(o) {
    var $gamesTemplate = $('<div class="am-panel am-panel-default" name="GamesTemplate"></div>');
    var $1 = $('<div class="am-panel-hd am-cf" data-am-collapse="{target: \'#'+ o.id + '\'}"></div>');
    var $11 = $('<header class="am-comment-hd"></header>');
    var $111 = $('<div class="am-comment-meta"></div>');
    $111.append($('<p>模板名称：' + o.name + '</p>'));
    $11.append($111);
    var $112 = $('<button type="button" class="am-btn am-btn-primary">选择</button>');
    //alert(o.id);
    $112.click(function (e) {
        e.stopPropagation();
        if(confirm('确认选择此模板？')){
            $('#my-modal-loading').modal('open');
            selectGamesTemplate($(this));
        }
    })
    $11.append($112);
    $1.append($11);
    $1.append($('<span class="am-icon-chevron-down am-fr" ></span>'));
    $gamesTemplate.append($1);
    var $2 = $('<div class="am-panel-bd am-collapse am-cf" id="' + o.id + '"></div>');
    var $21 = $('<ul class="am-comments-list admin-content-comment"></ul>');
    var $211 = $('<div class="am-comment-main"></div>');
    var $2111 = $('<header class="am-comment-hd"></header>');
    var $21111 = $('<div class="am-comment-bd"></div>');
    $21111.append($('<p>包含比赛：' + o.games + '</p>'));
    $21111.append($('<p>备注：' + o.comments + '</p>'));
    $2111.append($21111);
    $211.append($2111);
    $21.append($211);
    $2.append($21);
    $gamesTemplate.append($2);
    return $gamesTemplate;
}

function listGamesTemplates(data, callback){
    //alert(data);
    if(data.length > 0){
        clearView();
        var $gamesTemplatesSelector = createGamesTemplatesSelector();
        var n = 0;
        $.each(data, function (i, v) {
            //alert(v.id)
            $gamesTemplatesSelector.append(createGamesTemplate(v));
            n++;
            //alert(n);
            if(n >= data.length){
                //alert(1);
                $('#view').append($gamesTemplatesSelector);
                if(callback){
                    callback();
                }
            }
        })
    } else {
        $('#view').append('<h2>没有模板</h2>');
        if(callback){
            callback();
        }
    }
}

var GameStateType = {
    default: 1,
    done: 2,
    cancelled: 3,
    empty: 4,
    notstart: 5,
    broken: 6,
    overtime: 7,
    processing: 8
}

function createGamesList() {
    var $temp = $('<div id="GamesList"></div>');
    $temp.append($('<h2>比赛</h2>'));
    return $temp;
}

function createGamesBlock(type, title) {
    var $temp = $('<div name="GamesBlock"></div>');
    //$temp.append($('<button type="button" class="am-btn am-btn-success">' + title + '</button>'));
    $temp.attr('type', type);
    return $temp;
}

function createGame(o) {
    var role = $('#currentuser')

    var $game = $('<div class="am-panel am-panel-default" name="Game"></div>');
    var $1 = $('<div class="am-panel-hd am-cf" data-am-collapse="{target: \'#'+ o.id + '\'}"></div>');
    var $11 = $('<header class="am-comment-hd"></header>');
    var $111 = $('<div class="am-comment-meta"></div>');
    var state = $('<div></div>');
    switch (parseInt(o.state)){
        case 2:
            state.addClass('state-finished');
            break;
        case 4:
        case 6:
        case 7:
            state.addClass('state-warning');
            if(o.nodename){
                state.append($('<span>' + o.nodename + '</span>').addClass('node'));
            }
            //alert(o.nodename);
            break;
        case 8:
            state.addClass('state-processing');
            break;
        case 3:
            state.addClass('state-cancelled');
            break;
        case 1:
        case 5:
        default:
            state.addClass('state-default');
            break;
    }
    //alert(o.state);
    $game.attr('state', o.state);
    $111.append(state);
    $111.append($('<p>比赛名称：' + o.name + '</p>'));
    var start = o.workstarttime.substr(8, 2) + ':' + o.workstarttime.substr(10, 2) + ':00';
    var end = o.workendtime.substr(8, 2) + ':' + o.workendtime.substr(10, 2) + ':00';
    $111.append($('<time>' + start + '--' + end + '</time>'));
    if(o.workextratime > 0){
        $111.append($('<p>(预留' + o.workextratime + '分钟)</p>'));
    }else {
        $111.append($('<p>（无预留）</p>'));
    }
    $11.append($111);
    //alert(role.attr('cancel'))
    if(role.attr('process') == 'True'){
        var $112 = $('<button type="button" class="am-btn am-btn-primary">进度</button>');
        //alert(o.id);
        $112.click(function (e) {
            e.stopPropagation();
            window.location.href="/node/flowindex?gameid=" + $(this).parent().parent().next().attr('id');
        });
        $11.append($112);
    }

    if(role.attr('cancel') == 'True'){
        var $113 = $('<button type="button" class="am-btn am-btn-danger">取消</button>');
        $113.click(function (e) {
            e.stopPropagation();
            var name = $(this).prev().prev().children('p:first').text().split('：')[1];
            //alert(name);
            if(confirm('确认取消'+ name + '？')){
                $('#my-modal-loading').modal('open');
                cancelGame($(this).parent().parent().next().attr('id'));
            }
        });
        $11.append($113);
    }

    $1.append($11);
    $1.append($('<span class="am-icon-chevron-down am-fr" ></span>'));
    $game.append($1);
    var $2 = $('<div class="am-panel-bd am-collapse am-cf" id="' + o.id + '"></div>');
    var $21 = $('<ul class="am-comments-list admin-content-comment"></ul>');
    var $211 = $('<div class="am-comment-main"></div>');
    var $2111 = $('<header class="am-comment-hd"></header>');
    var $21111 = $('<div class="am-comment-bd"></div>');
    //alert(o.place == 'null' ? o.place : '');
    var t = o.place != '' ? o.place : '';
    //alert(t);
    $21111.append($('<p>场地：' + t + '</p>'));
    t = o.gamestarttime != '' ? o.gamestarttime.substr(8, 2) + ':' + o.gamestarttime.substr(10, 2) : '';
    $21111.append($('<time>比赛开始时间：' + t + '</time>'));
    t = o.comments != '' ? o.comments : '';
    $21111.append($('<p>备注：' + t + '</p>'));
    $2111.append($21111);
    if(role.attr('edit') == 'True'){
        var $21112 = $('<button type="button" class="am-btn am-btn-danger">编辑</button>');
        $21112.click(function (e) {
            e.stopPropagation();
            showEditGame(o, o.id);
        });
        $2111.append($21112);
    }

    $211.append($2111);
    $21.append($211);
    $2.append($21);
    $game.append($2);
    return $game;
}

function listGames(data, callback){
    clearView();
    if(data && data.length > 0){
        var $gamesList = createGamesList();
        var $gamesListDefault = createGamesBlock(GameStateType.default, '默认');
        var $gamesListFinished = createGamesBlock(GameStateType.finished, '已完成');
        var $gamesListProcessing = createGamesBlock(GameStateType.processing, '进行中');
        var $gamesListWarning = createGamesBlock(GameStateType.warning, '故障');
        var $gamesListCancelled = createGamesBlock(GameStateType.cancelled, '已取消');
        var n = 0;
        //alert(data.length);
        $.each(data, function (i, v) {
            var t = createGame(v);
            //alert(t.attr('state'));
            switch (parseInt(t.attr('state'))){
                case 2:
                    $gamesListFinished.append(t);
                    break;
                case 4:
                case 6:
                case 7:
                    $gamesListWarning.append(t);
                    break;
                case 8:
                    $gamesListProcessing.append(t);
                    break;
                case 3:
                    $gamesListCancelled.append(t);
                    break;
                case 1:
                case 5:
                default:
                    $gamesListDefault.append(t);
                    break;
            }
            n++;
            //alert(n);
            if(n >= data.length){
                //alert(1);
                $gamesList.append($gamesListWarning);
                $gamesList.append($gamesListProcessing);
                $gamesList.append($gamesListDefault);
                $gamesList.append($gamesListFinished);
                $gamesList.append($gamesListCancelled);
                $('#view').append($gamesList);
                if(callback){
                    callback();
                }
            }
        })
    }else {
        //alert(1)
        $('#view').append('<h2>没有比赛</h2>');
        if(callback){
            callback();
        }
    }
}

function getGamesByDate(date, callback) {
    var url = '/game/gameslist?date=' + date;
    $.ajax({
        'url': url,
        'dataType': 'json',
        traditional: true,
        'success': function (data) {
            //alert(data.type);
            switch(data.type){
                case 1:
                    listGamesTemplates(data.template, callback);
                    break;
                case 2:
                    listGames(data.instance, callback);
                    break;
                default:
                    if(callback){
                        callback();
                    }
                    break;
            }
        },
        'error': function (XMLHttpRequest, textStatus, errorThrown) {
            if(callback){
                callback();
            }
            alert('fail');
        }
        //'type': 'post',
    })
}

function searchGames() {
    $('#my-modal-loading').modal('open');
    cancelAddGame();
    cancelEditGame();
    var date = $('#datepicker').val();
    date = date.split('-').join('');
    //alert(2)
    getGamesByDate(date, function () {
        $('#my-modal-loading').modal('close');
    })
}

function selectGamesTemplate(o) {
    var url = '/game/selectgamestemplate/';
    var date = $('#datepicker').val().split('-').join('');
    //alert(1)
    //alert(o.parent());
    var gamesTemplateId = o.parent().parent().next().attr('id');
    //alert(gamesTemplateId)
    $.ajax({
        'url': url,
        'data': {date: date, gamestemplateid: gamesTemplateId},
        'dataType': 'json',
        traditional: true,
        'success': function (data) {
            alert(data.result);
            getGamesByDate(date, function () {
                $('#my-modal-loading').modal('close');
            })
        },
        'error': function (XMLHttpRequest, textStatus, errorThrown) {
            $('#my-modal-loading').modal('close');
            alert('fail');
        },
        'type': 'post'
    });
    return false;
}

function cancelAddGame() {
    $('#addGame').hide();
    $('#view').show();
}

function showAddGame() {
    $('#addname').val('');
    $('#addworkstarttime').val('');
    $('#addworkendtime').val('');
    $('#addworkextratime').val('');
    $('#addplace').val('');
    $('#addgamestarttime').val('');
    $('#addcomments').val('');

    $('#view').hide();
    $('#editGame').hide();
    $('#addGame').show();
}

function myPopOver(o, text) {
    $(o).popover({
        content: text
    });
    $(o).popover('open');
    setTimeout(function () {
        $(o).popover('close');
    }, 3000);
}

function addGame() {
    $('#my-modal-loading').modal('open');
    var game = Object();
    game.name = $('#addname').val();
    if(!game.name){
        $('#my-modal-loading').modal('close');
        myPopOver('#addname', '请填写比赛名称');
        return false;
    }
    if(!$('#addworkstarttime').val()){
        $('#my-modal-loading').modal('close');
        myPopOver('#addworkstarttime', '请选择工作开始时间');
        return false;
    }
    if(!$('#addworkendtime').val()){
        $('#my-modal-loading').modal('close');
        myPopOver('#addworkendtime', '请选择工作结束时间');
        return false;
    }
    var date = $('#datepicker').val().split('-').join('');
    game.workstarttime = date + $('#addworkstarttime').val().split(':').join('') + '00';
    game.workendtime = date + $('#addworkendtime').val().split(':').join('') + '00';
    if (game.workstarttime >= game.workendtime){
        $('#my-modal-loading').modal('close');
        myPopOver('#addworkendtime', '工作结束时间须大于开始时间');
        return false;
    }
    game.workextratime = $('#addworkextratime').val();
    if(!game.workextratime){
        game.workextratime = 0
    }else{
        if(!/^[0-9]+$/.test(game.workextratime)){
            $('#my-modal-loading').modal('close');
            myPopOver('#addworkextratime', '预留时间须为整数');
            return false;
        }
    }
    game.place = $('#addplace').val();
    game.gamestarttime = $('#addgamestarttime').val() != '' ? date + $('#addgamestarttime').val().split(':').join('') + '00' : '';
    game.comments = $('#addcomments').val();
    var url = '/game/addgame/';
    $.ajax({
        'url': url,
        'data': {game: JSON.stringify(game)},
        'dataType': 'json',
        traditional: true,
        'success': function (data) {
            alert(data.result);
            cancelAddGame();
            getGamesByDate(date, function () {
                $('#my-modal-loading').modal('close');
            })
        },
        'error': function (XMLHttpRequest, textStatus, errorThrown) {
            $('#my-modal-loading').modal('close');
            alert('fail');
        },
        'type': 'post'
    });

    return false;
}

function cancelGame(id){
    //alert(id);
    var url = '/game/cancelgame/';
    $.ajax({
        'url': url,
        'data': {gameid: id},
        'dataType': 'json',
        traditional: true,
        'success': function (data) {
            alert(data.result);
            //alert(2);
            var  date = $('#datepicker').val();
            date = date.split('-').join('');
            getGamesByDate(date, function () {
                $('#my-modal-loading').modal('close');
            })
        },
        'error': function (XMLHttpRequest, textStatus, errorThrown) {
            $('#my-modal-loading').modal('close');
            alert('fail');
        },
        'type': 'post'
    });
}

function editGame(){
    $('#my-modal-loading').modal('open');
    var game = Object();
    game.id = $('#editid').val();
    if(!game.id){
        $('#my-modal-loading').modal('close');
        myPopOver('#game_id', '无法获取比赛ID');
        return false;
    }
    game.name = $('#editname').val();
    if(!game.name){
        $('#my-modal-loading').modal('close');
        myPopOver('#editname', '请填写比赛名称');
        return false;
    }
    if(!$('#editworkstarttime').val()){
        $('#my-modal-loading').modal('close');
        myPopOver('#editworkstarttime', '请选择工作开始时间');
        return false;
    }
    if(!$('#editworkendtime').val()){
        $('#my-modal-loading').modal('close');
        myPopOver('#addworkendtime', '请选择工作结束时间');
        return false;
    }
    var date = $('#datepicker').val().split('-').join('');
    game.workstarttime = date + $('#editworkstarttime').val().split(':').join('') + '00';
    game.workendtime = date + $('#editworkendtime').val().split(':').join('') + '00';
    if (game.workstarttime >= game.workendtime){
        $('#my-modal-loading').modal('close');
        myPopOver('#editworkendtime', '工作结束时间须大于开始时间');
        return false;
    }
    game.workextratime = $('#editworkextratime').val();
    if(!game.workextratime){
        game.workextratime = 0
    }else{
        if(!/^[0-9]+$/.test(game.workextratime)){
            $('#my-modal-loading').modal('close');
            myPopOver('#editworkextratime', '预留时间须为整数');
            return false;
        }
    }
    game.place = $('#editplace').val();
    game.gamestarttime = $('#editgamestarttime').val() != '' ? date + $('#editgamestarttime').val().split(':').join('') + '00' : '';
    game.comments = $('#editcomments').val();
    var url = '/game/gamedetail/';
    $.ajax({
        'url': url,
        'data': {game: JSON.stringify(game)},
        'dataType': 'json',
        traditional: true,
        'success': function (data) {
            alert(data.result);
            cancelEditGame();
            getGamesByDate(date, function () {
                $('#my-modal-loading').modal('close');
            })
        },
        'error': function (XMLHttpRequest, textStatus, errorThrown) {
            $('#my-modal-loading').modal('close');
            alert('fail')
        },
        'type': 'post'
    });

    return false;

}


function cancelEditGame() {
    $('#editGame').hide();
    $('#view').show();
}


function showEditGame(o,id) {
    $('#view').hide();
    $('#editGame').show();
    document.getElementById("editid").value=id;
    document.getElementById("editname").value=o.name;
    document.getElementById("editworkstarttime").value=short_time(o.workstarttime);
    document.getElementById("editworkendtime").value=short_time(o.workendtime);
    document.getElementById("editworkextratime").value=o.workextratime;
    document.getElementById("editplace").value=o.place;
    document.getElementById("editgamestarttime").value=short_time(o.gamestarttime);
    document.getElementById("editcomments").value=o.comments;

}


function short_time(gettime){
    var shortlentime = gettime.substr(8,2)+":"+gettime.substr(10,2);
    return shortlentime;
}