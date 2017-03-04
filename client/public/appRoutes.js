angular.module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

    $stateProvider.state({
        name: 'sito',
        url: '/',
        templateUrl: 'public/components/sito/templates/sito.template',
        controller: 'sitoController'
    });

 //   $stateProvider.when('/sportivi', {
 //       templateUrl:'public/components/sito/templates/sportivi.template',
 //       controller : 'sitoController'
 //   });

    $urlRouterProvider.otherwise('/');
}]);
