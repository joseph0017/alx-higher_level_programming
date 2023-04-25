
const fs = require('fs');
fs.readFile(process.argv[2], (err, data) => {
  if (data) {
    console.log(data);
  } else {
    console.log(err);
  }
});
