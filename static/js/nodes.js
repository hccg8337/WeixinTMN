"use strict";

function getNodesByGame(callback) {
    var gameId = $('#game').attr('gameid');
    var url = '/node/nodesflow?gameid=' + gameId;
    $.ajax({
        'url': url,
        'dataType': 'json',
        traditional: true,
        'success': function (data) {
            //alert(data.type)
            switch (parseInt(data.type)) {
                case 1:
                    listNodesTemplates(data.template, callback);
                    break;
                case 2:
                    //alert(data.changenode)
                    showFlow(data.instance, data.line, data.changenode, callback);
                    break;
                default:
                    if (callback) {
                        callback();
                    }
                    break;
            }

        },
        'error': function (XMLHttpRequest, textStatus, errorThrown) {
            if (callback) {
                callback();
            }
            alert('fail');
        }
    })
}

function clearView() {
    $.each($('#view').children(), function (i, v) {
        v.remove();
    })
}

function createNodesTemplatesSelector() {
    var $temp = $('<div id="NodesTemplatesSelector"></div>');
    $temp.append($('<h2>模板选择</h2>'));
    return $temp;
}

function createNodesTemplate(o) {
    var $gamesTemplate = $('<div class="am-panel am-panel-default" name="GamesTemplate"></div>');
    var $1 = $('<div class="am-panel-hd am-cf" data-am-collapse="{target: \'#' + o.id + '\'}"></div>');
    var $11 = $('<header class="am-comment-hd"></header>');
    var $111 = $('<div class="am-comment-meta"></div>');
    $111.append($('<p>模板名称：' + o.name + '</p>'));
    $11.append($111);
    var $112 = $('<button type="button" class="am-btn am-btn-primary">选择</button>');
    //alert(o.id);
    $112.click(function (e) {
        e.stopPropagation();
        if (confirm('确认选择此模板？')) {
            $('#my-modal-loading').modal('open');
            selectNodesTemplate($(this));
        }
    })
    $11.append($112);
    $1.append($11);
    $1.append($('<span class="am-icon-chevron-down am-fr" ></span>'));
    $gamesTemplate.append($1);
    var $2 = $('<div class="am-panel-bd am-collapse am-in am-cf" id="' + o.id + '"></div>');
    var $21 = $('<ul class="am-comments-list admin-content-comment"></ul>');
    var $211 = $('<div class="am-comment-main"></div>');
    var $2111 = $('<header class="am-comment-hd"></header>');
    var $21111 = $('<div class="am-comment-bd"></div>');
    //$21111.append($('<p>包含比赛：' + o.games + '</p>'));
    $21111.append($('<p>备注：' + o.comments + '</p>'));
    $2111.append($21111);
    $211.append($2111);
    $21.append($211);
    $2.append($21);
    $gamesTemplate.append($2);
    return $gamesTemplate;
}

function listNodesTemplates(data, callback) {
    //alert(data);
    if (data.length > 0) {
        clearView();
        var $nodesTemplatesSelector = createNodesTemplatesSelector();
        var n = 0;
        $.each(data, function (i, v) {
            //alert(v.id)
            $nodesTemplatesSelector.append(createNodesTemplate(v));
            n++;
            //alert(n);
            if (n >= data.length) {
                //alert(1);
                $('#view').append($nodesTemplatesSelector);
                if (callback) {
                    callback();
                }
            }
        })
    } else {
        $('#view').append('<h2>没有模板</h2>');
        if (callback) {
            callback();
        }
    }
}

function selectNodesTemplate(o) {
    var url = '/game/selectnodestemplate/';
    var game = parseInt($('#game').attr('gameid'));
    //alert(1)
    //alert(o.parent());
    var templateId = o.parent().parent().next().attr('id');
    $.ajax({
        'url': url,
        'data': {gameid: game, nodestemplateid: templateId},
        'dataType': 'json',
        traditional: true,
        'success': function (data) {
            alert(data.result);
            getNodesByGame(function () {
                $('#my-modal-loading').modal('close');
            })
            $('#my-modal-loading').modal('close');
        },
        'error': function (XMLHttpRequest, textStatus, errorThrown) {
            $('#my-modal-loading').modal('close');
            alert('fail');
        },
        'type': 'post'
    });
    return false;
}

function createFlow() {
    var flow = $('<div id="nodes"></div>');
    return flow;
}

function createRow() {
    var role = $('#game');
    var $body = $('<div style="text-align:center; "></div>');

    if(role.attr('cancel') == 'True'){
        var $del = $('<input type="button" value="✖" class="del1">');
        $del.click(function () {
            var o = $(this).parent().children('.input_list');
            if(o.length > 1){
                o = $(this).parent().children('.input_border');
                if(o.length == 0){
                    alert('请先选择当前行要删除的节点');
                    return;
                }
            }
            if(confirm('确定要删除节点' + o.val() + '？')){
                deleteNode(o);
            }
        });
        $body.append($del);
    }

    return $body;
}

function createNode(o, canChangeNode) {
    //alert(o.id)
    var role = $('#game');
    var $name = $('<input type="text" class="input_list" readonly>');

    $name.attr('nodeid', o.id);
    $name.attr('deadline', o.deadline);
    $name.attr('notifytime', o.notifytime);
    $name.attr('state', o.state);
    $name.attr('comments', o.comments);
    $name.val(o.name);
    //alert(o.state);
    switch (parseInt(o.state)) {
        case 1:
            $name.addClass('state-default');
            break;
        case 2:
            $name.addClass('state-unfinished');
            break;
        case 3:
            $name.addClass('state-broken');
            break;
        case 4:
            $name.addClass('state-done');
            break;
        default:
            $name.addClass('state-default');
            break;
    }

    if(role.attr('edit') == 'True' || (role.attr('state') == 'True' && canChangeNode.indexOf(o.id) != -1)){
        //alert(o.id);
        $name.addClass('can-change');
    }else{
        $name.addClass('no-change');
    }

    return $name;
}

var LINE = {
    singleVer: 1,
    doubleVer: 2,
    cross: 3
};

function createLine(type, o) {
    var $line = null;
    switch (type) {
        case LINE.doubleVer:
            $line = $('<div class="leftline"></div><div class="rightline"></div></div>');
            if (o[0]) {
                $line.first().attr('state', o[0].state);
                $line.first().attr('lineid', o[0].id);
            }
            if (o[1]) {
                $line.first().attr('state', o[1].state);
                $line.first().attr('lineid', o[1].id);
            }
            break;
        case LINE.cross:
            $line = $('<div class="longline"></div>');
            if (o) {
                $line.first().attr('state', o.state);
                $line.first().attr('lineid', o.id);
            }
            break;
        case LINE.singleVer:
        default:
            $line = $('<div class="line1"></div>');
            if (o) {
                $line.first().attr('state', o.state);
                $line.first().attr('lineid', o.id);
            }
            break
    }
    return $line;
}

function findLine(lines, prev, next) {
    if (!lines) {
        return null;
    }
    var t = null;
    for (var i = 0; i < lines.length; i++) {
        if (parseInt(lines[i].prev) == prev && parseInt(lines[i].next) == next) {
            t = lines[i];
            lines.splice(i, 1);
            break;
        }
    }
    return t;
}

function showFlow(nodes, lines, canChangeNode, callback) {
    clearView();
    //alert(1);
    var $flow = createFlow();
    var nodesList = [];
    if (nodes && nodes.length > 0) {
        //alert(2);
        var object, o, x;
        var tag;
        var i, j, k;
        var parents;
        var ids = {};
        var root = [];
        var flag;
        //alert(nodes.length);
        while (nodes.length > 0) {
            //alert(nodes.length);
            object = nodes.shift();
            //alert(nodes.length);
            //alert(object.parentnode);
            tag = createNode(object, canChangeNode);
            tag.click(function () {
                $('.input_border').removeClass('input_border');
                $(this).addClass('input_border');
                //alert($(this).attr('comments'));
                $(this).parent().children('.input_comments').val($(this).attr('comments'));
                //alert($(this).next('.input_comments').length);
            });
            //alert(object.id);
            parents = object.parentnode.split(',');
            //alert(parents);
            try {
                nodesList.push({id: object.id, node: tag});
            } catch (e) {
                alert(e.message);
                return;
            }
            //alert('bb');
            flag = false;
            //alert(parents);
            for (x in parents) {
                x = parents[x]
                //alert(object.id);
                if (x in ids) {
                    if (!((nodesList.length - 1) in ids[x])) {
                        ids[x].push(nodesList.length - 1);
                    }
                } else {
                    ids[x] = [nodesList.length - 1];
                }
                flag = parseInt(x) == 0 ? true : flag;
            }
            if (flag) {
                root.push((nodesList.length - 1));
            }

        }
        //alert(root);
        var old_root = [];
        var queue;
        var temp;
        while (root.length > 0) {
            object = createRow();
            queue = [];
            temp = [];
            try {
                //alert(old_root.length);
                //alert(root.length);
                if (old_root.length > 0) {
                    if (old_root.length == 1) {
                        if (root.length == 1) {
                            k = createLine(LINE.singleVer, findLine(lines, nodesList[old_root[0]].id, nodesList[root[0]].id));
                            queue.push(k)
                        } else {
                            k = createLine(LINE.singleVer, null);
                            queue.push(k);
                            k = createLine(LINE.cross, null);
                            queue.push(k);
                            j = [];
                            j.push(findLine(lines, nodesList[old_root[0]].id, nodesList[root[0]].id));
                            j.push(findLine(lines, nodesList[old_root[0]].id, nodesList[root[1]].id));
                            k = createLine(LINE.doubleVer, j);
                            queue.push(k);
                        }
                    } else {
                        //alert(root);
                        if (root.length == 1) {
                            //alert(1);
                            j = [];

                            j.push(findLine(lines, nodesList[old_root[0]].id, nodesList[root[0]].id));
                            j.push(findLine(lines, nodesList[old_root[1]].id, nodesList[root[0]].id));
                            k = createLine(LINE.doubleVer, j);
                            queue.push(k);
                            k = createLine(LINE.cross, null);
                            queue.push(k);
                            k = createLine(LINE.singleVer, null);
                            queue.push(k);
                            //alert(queue[queue.length - 2].attr('class'));
                        } else {
                            //alert('t');
                            j = [];
                            j.push(findLine(lines, nodesList[old_root[0]].id, nodesList[root[0]].id));
                            j.push(findLine(lines, nodesList[old_root[1]].id, nodesList[root[1]].id));
                            k = createLine(LINE.doubleVer, j);
                            //alert(k.first().attr('class'));
                            //alert(k.last().attr('class'));
                            queue.push(k);
                            //alert('f');
                        }
                    }
                }
            } catch (e) {
                alert(e.message);
                return;
            }

            //alert(2);
            try {
                old_root = [];
                //alert(root);
                for (o in root) {
                    o = root[o];
                    queue.push(nodesList[o].node);
                    old_root.push(o);
                    temp.push(nodesList[o].id);
                }
                for (i = queue.length - 1; i >= 0; i--) {
                    //alert(queue[i].attr('class'));
                    object.prepend(queue[i]);
                }

                var role = $('#game');
                if (role.attr('add') == 'True') {
                    if (root.length == 1) {
                        var $add = $('<input type="button" value="➕" class="add1">');
                        $add.click(function () {
                            showAddNode($(this).parent().children('.input_list').first(), null);
                        });
                        object.append($add);
                    }
                }

                var $rightblock = $('<input name="rightinfo" readonly="readonly" class="input_comments rightblock testTxt green">');
                if (root.length == 1) {
                    $rightblock.val(nodesList[root[0]].node.attr('comments'));
                } else {
                    i = nodesList[root[0]].node.attr('nodeid') >= nodesList[root[1]].node.attr('nodeid') ? 0 : 1;
                    if (parseInt(nodesList[root[i]].node.attr('state')) == 0) {
                        if (parseInt(nodesList[root[1 - i]].node.attr('state')) == 0) {
                            $rightblock.val(nodesList[root[i]].node.attr('comments'));
                        } else {
                            $rightblock.val(nodesList[root[1 - i]].node.attr('comments'));
                        }
                    } else {
                        $rightblock.val(nodesList[root[i]].node.attr('comments'));
                    }
                }
                $rightblock.click(function () {
                    var role = $('#game');
                    if (role.attr('edit') == 'True') {
                        var o = $(this).parent().children('.input_list');
                        if(o.length > 1){
                            o = $(this).parent().children('.input_border');
                            if(o.length == 0){
                                alert('请先选择当前行要修改信息的节点');
                                return;
                            }
                        }
                        if(!o.hasClass('can-change')){
                            return;
                        }
                        showEditNode(o);
                    }
                    if (role.attr('state') == 'True') {
                        var o = $(this).parent().children('.input_list');
                        if(o.length > 1){
                            o = $(this).parent().children('.input_border');
                            if(o.length == 0){
                                alert('请先选择当前行要修改状态的节点');
                                return;
                            }
                        }
                        if(!o.hasClass('can-change')){
                            return;
                        }
                        showStateNode(o);
                    }
                })
                //alert($rightblock.val())
                object.append($rightblock);

                root = [];
                for (o in temp) {
                    o = temp[o];
                    i = ids[o.toString()];
                    if (i) {
                        //alert(i);
                        for (j in i) {
                            j = i[j];
                            if (function () {
                                    for (var x in root) {
                                        if (root[x] == j) {
                                            return x;
                                        }
                                    }
                                    return -1;
                                }() == -1) {
                                //alert(typeof j);
                                //alert(j);
                                root.push(j);
                                //alert(root);
                            }
                        }
                    }
                }
                $flow.append(object);
            } catch (e) {
                alert(e);
                return;
            }
        }
    } else {
        $flow.append($('<h2>没有节点</h2>'))
    }
    $('#view').append($flow);
    if (callback) {
        callback();
    }
}

function getNodePermit(nodeId, callback) {
    var url = '/node/nodepermits?nodeid=' + nodeId;
    $.ajax({
        'url': url,
        //'data': {game: JSON.stringify(game)},
        'dataType': 'json',
        traditional: true,
        'success': function (data) {
            //alert(data.result);
            callback(data);
        },
        'error': function (XMLHttpRequest, textStatus, errorThrown) {
            callback(null);
        },
        //'type': 'post'
    });
}

function getGroups(callback) {
    var url = '/usersgroup/usersgroupslist';
    $.ajax({
        'url': url,
        //'data': {game: JSON.stringify(game)},
        'dataType': 'json',
        traditional: true,
        'success': function (data) {
            //alert(data.result);
            callback(data.groups);
        },
        'error': function (XMLHttpRequest, textStatus, errorThrown) {
            callback(null);
        },
        //'type': 'post'
    });
}

function getUsers(callback) {
    var url = '/customuser/userslist';
    $.ajax({
        'url': url,
        //'data': {game: JSON.stringify(game)},
        'dataType': 'json',
        traditional: true,
        'success': function (data) {
            //alert(data.result);
            callback(data.users);
        },
        'error': function (XMLHttpRequest, textStatus, errorThrown) {
            callback(null);
        },
        //'type': 'post'
    });
}

function showAddNode(left, callback) {
    //alert(1);
    getGroups(function (data) {
        var i;

        if (!data) {
            alert('fail');
            callback();
            return;
        }

        var $group = $('#nodePermit').children().first();
        $group.children().remove();
        for (i = 0; i < data.length; i++) {
            $group.append($('<option value="' + 'group:' + data[i].id + '">' + data[i].name + '</option>'))
        }

        getUsers(function (data) {
            var i;

            if (!data) {
                alert('fail');
                callback();
                return;
            }

            var $user = $('#nodePermit').children().first().next();
            $user.children().remove();

            for (i = 0; i < data.length; i++) {
                $user.append($('<option value="' + 'user:' + data[i].id + '">' + data[i].nickname + '</option>'))
            }

            if (left) {
                $('#nodeid').attr('left', left.attr('nodeid'));
            } else {
                $('#nodeid').attr('left', 0);
            }

            try {
                $('#nodeid').val(id);//$('#nodeModal').modal('show');
                //alert(123);
            } catch (e) {
                alert(e.message);
            }
            $('#nodePermit').multipleSelect({
                width: '100%',
                multiple: true,
                multipleWidth: 55,
                filter: true
            });

            var prev;
            var next;
            var t, n;
            try {
                if (left) {
                    t = left.parent().prev();
                    if (t.length > 0) {
                        t = t.children('.input_list');
                        switch (t.length) {
                            case 2:
                                prev = t.last().attr('nodeid');
                                break;
                            case 1:
                            default:
                                prev = t.first().attr('nodeid');
                                break;
                        }
                    } else {
                        prev = '0';
                    }
                    t = left.parent().next();
                    if (t.length > 0) {
                        t = t.children('.input_list');
                        switch (t.length) {
                            case 2:
                                next = t.last().attr('nodeid');
                                break;
                            case 1:
                            default:
                                next = t.first().attr('nodeid');
                                break;
                        }
                    } else {
                        next = '0';
                    }
                } else {
                    var selected = $('.input_border');
                    //alert(1);
                    if (selected.length > 0) {
                        n = [];
                        i = selected.parent().children('.input_list').first();
                        n.push(i.attr('nodeid'));
                        i = i.next('.input_list');
                        if (i.length > 0) {
                            n.push(i.attr('nodeid'));
                        }
                        prev = n.join(',');
                        t = selected.parent().next('div');
                        if (t.length > 0) {
                            t = t.children('.input_list');
                            n = [];
                            switch (t.length) {
                                case 2:
                                    n.push(parseInt(t.first().attr('nodeid')));
                                    n.push(parseInt(t.last().attr('nodeid')));
                                    break;
                                case 1:
                                default:
                                    n.push(parseInt(t.first().attr('nodeid')));
                                    break;
                            }
                            next = n.join(',');
                        } else {
                            next = '0';
                        }
                        //alert(prev);
                        //alert(next);
                    } else {
                        t = $('#nodes').children();
                        if (t.length > 0) {
                            t = t.last().children('.input_list');
                            n = [];
                            //alert(t.length);
                            switch (t.length) {
                                case 2:
                                    n.push(t.first().attr('nodeid'));
                                    n.push(t.last().attr('nodeid'));
                                    break;
                                case 1:
                                default:
                                    n.push(t.first().attr('nodeid'));
                                    break;
                            }
                            prev = n.join(',');
                        } else {
                            prev = '0';
                        }
                        next = '0';
                    }
                }
            } catch (e) {
                alert(e.message);
                return;
            }

            var id = 0;

            $('#nodeid').attr('prev', prev).attr('next', next).val(id);
            //alert($('#nodeid').attr('prev'))
            $('#nodeName').val('');
            $('#nodeDeadline').val('');
            $('#nodeNotifytime').val('5');
            $('#nodeComments').val('');

            $('#nodeModal').modal({
                closeViaDimmer: false,
                closeOnConfirm: false,
                onConfirm: submitNode,
                onCancel: function (e) {
                    //alert('不想说!');
                }
            });
        });
    });
}

function showEditNode(o) {
    var id = o.attr('nodeid');
    //alert(id);
    getNodePermit(id, function (data) {
        if (!data) {
            alert('fail');
            return;
        }

        var prev = '';//
        var next = '';//

        $('#nodeid').val(o.attr('nodeid'));//
        $('#nodeName').val(o.val());//
        var deadline = o.attr('deadline');
        //alert(deadline);
        if(deadline){
            deadline = deadline.substr(8,2) + ":" + deadline.substr(10,2);
        }
        $('#nodeDeadline').val(deadline);//
        $('#nodeNotifytime').val(o.attr('notifytime'));//
        $('#nodeComments').val(o.attr('comments'));//

        if($('#nodePermit').length > 0){
            var $group = $('#nodePermit').children().first();
            $group.children().remove();
            var i = 0;
            for (i = 0; i < data.groups.length; i++) {
                var t = $('<option value="' + 'group:' + data.groups[i].id + '">' + data.groups[i].name + '</option>');
                if(data.groups[i].select){
                    t.attr('selected', 'true');
                }
                $group.append(t);
            }

            var $user = $('#nodePermit').children().first().next();
            $user.children().remove();
            for (i = 0; i < data.users.length; i++) {
                //alert(data.users[i].id);
                var t = $('<option value="' + 'user:' + data.users[i].id + '">' + data.users[i].nickname + '</option>');
                if(data.users[i].select){
                    t.attr('selected', 'true');
                }
                $user.append(t);
            }
        }
        $('#nodeModal').modal({
            closeViaDimmer: false,
            closeOnConfirm: false,
            onConfirm: submitNode,
            onCancel: function (e) {
                    //alert('不想说!');
            }
        });
    });
}

function submitNode() {
    //alert(1);
    //$('#nodeModal').modal('close');
    //return;
    /*$('#my-modal-loading').modal({
     dimmer: false
     });*/
    //alert('2');

    var i, o;
    var node = {};

    node.name = $('#nodeName').val().trim();
    //alert(node.name);
    if (node.name.length == 0) {
        //alert(2);
        alert('节点名称不能为空');
        $('#my-modal-loading').modal('close');
        //$('#nodeModal').modal('open');
        return false;
    }
    //alert($('#nodeDeadline').val());
    node.deadline = $('#nodeDeadline').val().trim() ? $('#nodeDeadline').val().trim().split(':').join('') + '00' : '';
    node.notifytime = $('#nodeNotifytime').val().trim();
    if (!(/^[0-9]*$/.test(node.notifytime))) {
        alert('提前通知时间必须为数字');
        //$('#my-modal-loading').modal('close');
        return false;
    }
    node.comments = $('#nodeComments').val().trim();
    //alert(3)
    var url = '/node/';

    var id = $('#nodeid').val().trim();
    if (id && parseInt(id) > 0) {
        node.id = id;
        url += 'nodedetail/'
    } else {
        url += 'addnode/';
        node.left = $('#nodeid').attr('left').trim();
    }
    //alert(6);
    node.prev = $('#nodeid').attr('prev');
    node.next = $('#nodeid').attr('next');
    //alert(node.id);
    //alert(node.prev);
    //alert(node.next)
    //alert(1);
    node.groups = [];
    node.users = [];
    //alert(selects);
    //selects = selects.toString().split(',');
    //alert($("#nodePermit").length);
    if($("#nodePermit").length > 0){
        var selects = $("#nodePermit").val();
        //alert(1);
        try{
            //selects = selects.split(',');
        }catch(e){
            alert(e.message);
        }
        //alert(1);
        for (i in selects) {
            o = selects[i];
            //alert(o);
            o = o.split(':');
            switch (o[0]) {
                case 'group':
                    node.groups.push(o[1]);
                    break;
                case 'user':
                    node.users.push(o[1]);
                    break;
                default:
                    break;
            }
        }
    }
    //alert(node.users);
    node.gameid = $('#game').attr('gameid');
    $.ajax({
        'url': url,
        'data': {node: JSON.stringify(node)},
        'dataType': 'json',
        traditional: true,
        'success': function (data) {
            //alert(3);
            alert(data.result);
            if (data.result == 'fail') {
                //alert(data.msg);
                //$('#my-modal-loading').modal('close');
            } else {
                $('#nodeModal').modal('close');
                getNodesByGame(function () {
                    //$('#my-modal-loading').modal('close');
                });
            }

        },
        'error': function (XMLHttpRequest, textStatus, errorThrown) {
            //$('#my-modal-loading').modal('close');
            alert('fail');
        },
        'type': 'post'
    })
}

var STATES =[{id:2, name:'state-unfinished', info:'未完成'},
    {id:4,name:'state-done', info:'已完成'},
    {id:3, name:'state-broken', info:'故障'}];

function showStateNode(o) {
    var modal = $('#stateModal');
    modal.find('input[name="nodeid"]').first().val(o.attr('nodeid'));
    modal.find('input[name="nodeName"]').first().val(o.val());
    var select = modal.find('select[name="nodeState"]').first();
    select.children().remove();
    for (var i in STATES){
        if(o.hasClass(STATES[i].name)){
            modal.find('input[name="nodeid"]').first().attr('oldstate', STATES[i].id);
            select.append($('<option selected>' + STATES[i].info + '</option>').attr('value', STATES[i].id))
        }else{
            select.append($('<option>' + STATES[i].info + '</option>').attr('value', STATES[i].id))
        }
    }

    select.multipleSelect({
        single: true,
        width: '100%',
        filter: false
    });

    $('#stateModal').modal({
        closeViaDimmer: false,
        closeOnConfirm: false,
        onConfirm: stateNode,
        onCancel: function (e) {
            //alert('不想说!');
        }
    });
}

function stateNode() {
    //alert(1);
    var modal = $('#stateModal');
    var id = modal.find('input[name="nodeid"]').first().val();
    var state = modal.find("select[name='nodeState']").multipleSelect("getSelects")[0];
    //alert(state);
    if(parseInt(state) == parseInt(modal.find('input[name="nodeid"]').first().attr('oldstate'))){
        $('#stateModal').modal('close');
        //alert('无修改');
        return;
    }
    var comments = modal.find('textarea[name="nodeComments"]').first().val();
    var url = '/node/nodestate/';
    //alert(id);
    $.ajax({
        'url': url,
        'data': {node: JSON.stringify({id: id, state: state, comments: comments})},
        'dataType': 'json',
        traditional: true,
        'success': function (data) {
            //alert(3);
            alert(data.result);
            if (data.result == 'fail') {
                alert(data.msg);
                //$('#my-modal-loading').modal('close');
            } else {
                getNodesByGame(function () {
                    $('#stateModal').modal('close');
                });
            }

        },
        'error': function (XMLHttpRequest, textStatus, errorThrown) {
            //$('#my-modal-loading').modal('close');
            alert('fail');
        },
        'type': 'post'
    })
}

function deleteNode(o) {
    var url = '/node/delnode/';
    var id = o.attr('nodeid');
    $.ajax({
        'url': url,
        'data': {nodeid: id},
        'dataType': 'json',
        traditional: true,
        'success': function (data) {
            //alert(3);
            alert(data.result);
            if (data.result == 'fail') {
                alert(data.msg);
                //$('#my-modal-loading').modal('close');
            } else {
                getNodesByGame(null);
            }

        },
        'error': function (XMLHttpRequest, textStatus, errorThrown) {
            //$('#my-modal-loading').modal('close');
            alert('fail');
        },
        'type': 'post'
    })
}

/*function canChangeNode(nodeid, callback){
    var url = '/nodes/canChangeNode?node_id=' + nodeid;
    $.ajax({
        'url': url,
        //'data': {node_id: id},
        'dataType': 'json',
        traditional: true,
        'success': function (data) {
            if(data.result == 'ok'){
                callback();
            }
        },
        'error': function (XMLHttpRequest, textStatus, errorThrown) {
            //$('#my-modal-loading').modal('close');
            alert('fail');
        },
        //'type': 'post'
    })
}*/