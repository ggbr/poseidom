"use strict";
exports.__esModule = true;
var Main = /** @class */ (function () {
    function Main() {
        this.frequencia = 2500;
    }
    Main.prototype.start = function () {
        console.log('loop ...');
        this.status();
    };
    Main.prototype.status = function () {
        console.log("Iniciando ...");
        var os = require('os-utils');
        var cpu = 0;
        console.log("CPU:" + cpu);
        var memoria = os.totalmem() - os.freemem();
        console.log("Memoria:" + memoria);
        this.save(cpu, memoria);
    };
    Main.prototype.save = function (cpu, memoria) {
        var mongoose = require('mongoose');
        mongoose.connect('mongodb://mongodb:27017/monitor');
        var ObjectID = require('mongodb').ObjectID;
        var conn = mongoose.connection;
        var user = {
            _id: new ObjectID(),
            cpu: cpu,
            memoria: memoria
        };
        conn.collection('status').insert(user);
    };
    return Main;
}());
exports.Main = Main;
