#!/usr/bin/node
// 6. How many completed?
const request = require('request');
const process = require('process');
const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err === null) {
    const data = JSON.parse(body);
    const users = [...new Set(data.map(todo => todo.userId))];
    const completedTasks = {};
    users.forEach((id) => {
      const completedTask = data.filter(todo => todo.userId === id && todo.completed);
      if (completedTask.length <= 0) {
        return;
      }
      completedTasks[id] = completedTask.length;
    });
    console.log(completedTasks);
  } else {
    console.log(err);
  }
});
