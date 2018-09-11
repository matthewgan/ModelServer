(function() {
    'use strict';

    var app = angular.module('gallery.demo', ['ngRoute']);

    app.config(['$routeProvider', config]).run(['$http', GalleryRun]);
    app.controller('GalleryController',[ '$scope', '$http', '$location', 'LoginService', GalleryController ]);

    function config($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'static/html/gallery.html',
                controller: 'GalleryController',
            })
            .when('/login', {
                templateUrl: 'static/html/login.html',
                controller: 'LoginController',
            })
            .otherwise('/');
    }

    function GalleryRun($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken'
        $http.defaults.xsrfCookieName = 'csrftoken';
    }

    function GalleryController($scope, $http, $location, LoginService) {

        LoginService.redirectIfNotLoggedIn();
        $scope.logout = LoginService.logout;
        $scope.sortBy = 'story_points';
        $scope.reverse = true;
        $scope.showFilters = false;

//        $scope.add = function(list, title) {
//            var card = {
//                list: list.id,
//                title: title
//            };
//
//            $http.post('/scrumboard/cards/', card)
//            .then(
//                function(response){
//                    list.cards.push(response.data);
//                },
//                function(){ //Error handling
//                    alert('Could not create card')
//                }
//            );
//
//        };

        $scope.subcategory = function(cat_id){
            $http.get('/category/sub/'+cat_id)
            .then(
            );
        };

        $scope.data = [];
        $http.get('/category/').then(function(response){
            $scope.data.categories = response.data;
        });
    }

}());