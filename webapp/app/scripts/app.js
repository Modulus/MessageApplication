'use strict';

/**
 * @ngdoc overview
 * @name webApp
 * @description
 * # webappApp
 *
 * Main module of the application.
 */
angular
  .module('webApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      }).
      when('/user', {
        templateUlr: '/views/createUser',
        controller: 'UserController'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
