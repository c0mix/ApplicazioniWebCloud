sito.controller('sitoController', function($scope, Attivita, Test){

    Attivita.query().$promise.then(function(data) {
        $scope.attivitas = data;
    });

    Test.query().$promise.then(function(data) {
        $scope.tests = data;
    });
});

sito.controller('sportivoController', function($scope, Sportivo) {

    Sportivo.query().$promise.then(function(data) {
        $scope.sportivi = data;
    });
});