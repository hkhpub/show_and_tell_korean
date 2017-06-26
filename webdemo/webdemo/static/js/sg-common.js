/**
 * Created by hkh on 2017-05-18.
 */

$(document).ready(function(){
    $("#inputStdNum").keyup(function() {
        $("#inputStdNum").val(this.value.match(/[0-9]*/));
    });

    $("a.vote-submit-agree").click(function(){
        var student_num = $(this).find("data").attr("student_num");
        var cand_name = $(this).find("data").attr("cand_name");
        raiseConfirmBox(student_num, cand_name);
    });
    $("a.vote-submit-decline").click(function() {
        raiseConfirmBox(null, "반대");
    });

    var raiseConfirmBox = function(student_num, cand_name){
        bootbox.confirm({
            message: "<"+cand_name+">을(를) 선택하였습니다. 투표를 진행하면 수정할 수 없습니다. 진행하시겠습니까?",
            buttons: {
                confirm: {
                    label: '예',
                    className: 'btn-success sg-button'
                },
                cancel: {
                    label: '아니오',
                    className: 'btn-danger sg-button'
                }
            },
            callback: function (result) {
                if (result) {
                    console.log("fire post");
                    $("#voteData").attr("value", student_num);
                    console.log(student_num);
                    $("#voteForm").submit();
                }
            }
        });
    };  // end of raiseConfirmBox
 });