/*
 * Bootstrap Image Gallery JS Demo 3.0.1
 * https://github.com/blueimp/Bootstrap-Image-Gallery
 *
 * Copyright 2013, Sebastian Tschan
 * https://blueimp.net
 *
 * Licensed under the MIT license:
 * http://www.opensource.org/licenses/MIT
 */

/*jslint unparam: true */
/*global blueimp, $ */

$(function () {
    'use strict';

    // Load demo images from flickr:
    // $.ajax({
    //     url: 'https://api.flickr.com/services/rest/',
    //     data: {
    //         format: 'json',
    //         method: 'flickr.interestingness.getList',
    //         api_key: '7617adae70159d09ba78cfec73c13be3'
    //     },
    //     dataType: 'jsonp',
    //     jsonp: 'jsoncallback'
    // }).done(function (result) {
    //     var linksContainer = $('#links'),
    //         baseUrl;
    //     // Add the demo images as links with thumbnails to the page:
    //     $.each(result.photos.photo, function (index, photo) {
    //         baseUrl = 'http://farm' + photo.farm + '.static.flickr.com/' +
    //             photo.server + '/' + photo.id + '_' + photo.secret;
    //         $('<a/>')
    //             .append($('<img>').prop('src', baseUrl + '_s.jpg'))
    //             .prop('href', baseUrl + '_b.jpg')
    //             .prop('title', photo.title)
    //             .attr('data-gallery', '')
    //             .appendTo(linksContainer);
    //     });
    // });

    $("#links a").click(function(){
       console.log();
       var imgid = $(this).attr("data-imgid")
        $.ajax({
            url: '/modal/'+imgid
        }).done(function (result) {
            console.log(result);
            $(".modal-body").html(result);
            $('#myModal').modal('toggle');
            $('#btnSaveCaption').click(function(){
                $('#myModal').modal('toggle');
            });
        });
    });
});
