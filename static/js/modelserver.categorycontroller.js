(function(){
    'use strict';

    angular.module('modelserver', [])
        .controller('CategoryController', [ '$scope', '$http', CategoryController ]);

    function CategoryController($scope, $http){
        $scope.categories = [];
        $http.get('/api/category/').then(function(response){
            $scope.categories = response.data;
        });

        $scope.assets = [];
        $scope.get_assets_under_category = function(assets, category){
            $http.get('api/category/'+category.id+'/assetbundles/').then(function(response){
                $scope.assets = response.data;
            })
        }

        $scope.
    }
}());