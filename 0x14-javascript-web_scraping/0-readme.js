#!/usr/local/bin/node
// script that reads and prints the content of a file.

const fs = require('fs');

filePath = process.argv[2]

fs.readFile(filePath, 'utf8', (error, data) => {
    if (error) {
        console.log(error);
        return;
    }
    else {
        // log the content of the file
        console.log(data);
    }
});