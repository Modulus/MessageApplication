/**
 * Created by johska on 10.11.2014.
 */
'use strict';

describe('Controller: UserController', function () {

  // load the controller's module
  beforeEach(module('webApp'));

  var MainCtrl,
    scope;


  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    MainCtrl = $controller('UserController', {
      $scope: scope
    });
  }));

  it('Should have createUser function', function () {
    expect(scope.createUser).toBeDefined();
  });

  it('Should have getUser function', function(){
    expect(scope.getUser).toBeDefined();
  });

  it('Should have empty object on fresh instance', function(){
    expect(scope.user).toEqual({})
  });

});
