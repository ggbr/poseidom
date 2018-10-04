// app.js
const express = require('express');
const bodyParser = require('body-parser');
// initialize our express app
const app = express();

let port = 3000;
var mongoose = require('mongoose');

mongoose.connect('mongodb://mongodb:27017/');
var ObjectID = require('mongodb').ObjectID;
var conn = mongoose.connection;

var user = {
  a: 'abc',
  _id: new ObjectID()
};

conn.collection('aaa').insert(user);

