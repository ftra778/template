const assert = require('assert');
const { add } = require('../main.js');

// Test case
const result = add(1, 1);
assert.strictEqual(result, 2, 'add(1, 1) should equal 2');
console.log("1 + 1 = 2")