#!/usr/bin/node
const request = require('request')
const urlRequest = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${urlRequest}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const urlCharacters = JSON.parse(body).characters;
    const nameCharacters = urlCharacters.map( url => new Promise (
      (resolve, reject) => {
        request(url, (promiseErr, __, charactersReqBody) => {
		if (promiseErr) {
			reject(promiseErr);
                }
                resolve(JSON.parse(charactersReqBody).name);
        });
      }));
      promise.all(nameCharacters).then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
