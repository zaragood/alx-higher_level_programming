#!/usr/bin/node
// script that reads and prints the content of a file.

const fs = require('fs');

const filePath = process.argv[2];

fs.writeFile(filePath, process.argv[3], 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
