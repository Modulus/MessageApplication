/**
 * Created by johska on 10.11.2014.
 */


(function(){
  var UserController = function($scope, $http, $log){

    $scope.createUser = function(username, password){
      $http.post('/api/user', {'username': username, 'password': password})
        .success(function(data, status, headers, config){
      })
      .error(function(data, status, headers, config){
      });
    };

    $scope.getUser = function(id){
      $http.get('/api/user', function(id){

      })
        .success(function(data, status, header, config){
        })
        .erro(function(data, status, header, config){

        });
    };

  };
  //UserController.$inject['$http','$log', '$routeProvider'];


  angular.module('webApp').controller("UserController", UserController)
}());


/*angular.module('webApp')
  .controller('MainCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
*/
