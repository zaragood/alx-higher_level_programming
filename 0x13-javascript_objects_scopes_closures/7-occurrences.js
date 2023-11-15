#!/usr/bin/node

// function that returns the number of occurrences in a list:

exports.nbOccurences = function (list, searchElement) {
  // use reduce method to count occurences
  const occurences = list.reduce((count, element) => {
    if (element === searchElement) {
      return count + 1;
    } else {
      return count;
    }
  }, 0);
  return occurences;
};
