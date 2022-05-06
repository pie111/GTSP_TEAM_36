const mysql = require('mysql');
const connection = mysql.createConnection({
  host: 'sql353.main-hosting.eu',
  user: 'u934542817_Driver',
  password: 'Emergency123',
  database: 'u934542817_EmergencyVec',
});

connection.connect((error) => {
  if(error){
    console.log('Error connecting to the MySQL Database');
    return;
  }
  console.log('Connection established sucessfully');
});
connection.end((error) => {
});