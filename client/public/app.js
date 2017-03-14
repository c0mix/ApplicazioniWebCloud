'use strict';

var sito = angular.module("sito", []);

angular.module('ItaliaSportApplication', [
        'appRoutes',
        'sito',
        'ngResource',
        'auth0.lock',
        'angular-jwt',
        'ui.router'
        //'appConfig',
        //'angular-storage',
        //'angular-jwt'
    ]);

angular.config(config);

  function config($stateProvider, lockProvider, $urlRouterProvider) {

    $stateProvider
      .state('sito', {
        url: '/',
        controller: 'HomeController',
        templateUrl: '/',
        controllerAs: 'vm'
      });

    lockProvider.init({
      clientID: 'TAthQ4NY8q8fY6aKXCRKnymwe1NGs0GF',
      domain: 'italiasport.eu.auth0.com'
    });

    $urlRouterProvider.otherwise('/home');
  }