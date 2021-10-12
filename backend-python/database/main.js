const fs = require('fs');
const sqlite3 = require('sqlite3');

sqlite3.verbose();


function dbExists() {
  return fs.existsSync('duodigito.db');
}

function initDb() {
  return new sqlite3.Database('./duodigito.db', sqlite3.OPEN_READWRITE | sqlite3.OPEN_CREATE, (err) => {
    if (err) {
      throw (err);
    }
  });
}

async function Create() {
  const initSql = fs.readFileSync('./init.sql').toString();
  let db = initDb();

  new Promise((resolve, reject) => {
    db.exec(initSql, (err, obj) => {
      if (err) {
        console.log(err);
        reject(err);
      } else {
        resolve(obj);
      }
    });
  });

  db.close(err => {
    if (err) {
      return console.error(err.message);
    }
  });
}

if (!dbExists()) {
  console.log('Banco não encontrado, inicializando o banco de dados');
  Create();
}