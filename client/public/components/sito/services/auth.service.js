/**
 * Created by Lory on 14/03/17.
 */
'use strict';

sito.factory('Auth', function($resource) {
        return $resource(
            'http://127.0.0.1:8000/auth/locals/',
            {},
            {
                'query': {
                    method: 'POST',
                    isArray: true,
                    headers: {
                        'Content-Type':'application/json'
                    }
                }
            },
            {
                stripTrailingSlashes: true
            }
        );
    });