sito.controller('sitoController', function($scope, Test){
    Test.query().$promise.then(function(data) {
        $scope.tests = data;
    });
});

sito.controller('sportivoController', function($scope, Sportivo) {

    Sportivo.query().$promise.then(function(data) {
        $scope.sportivi = data;
    });
});

sito.controller('attivitaController', function($scope, Attivita) {

    Attivita.query().$promise.then(function(data) {
        $scope.attivita = data;
    });

});
