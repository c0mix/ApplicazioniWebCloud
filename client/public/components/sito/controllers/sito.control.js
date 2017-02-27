sito
    .controller('sitoController', function($scope, Sportivo, Attivita, Test)
    {
        Sportivo.query().$promise.then(function(data) {
            $scope.sportivi = data;
        });

        Attivita.query().$promise.then(function(data) {
            $scope.attivitas = data;
        });

        Test.query().$promise.then(function(data) {
            $scope.tests = data;
        });

});
