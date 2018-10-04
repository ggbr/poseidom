"use strict";
exports.__esModule = true;
var Main_1 = require("./Main");
var Rotina = /** @class */ (function () {
    function Rotina() {
    }
    Rotina.prototype.setup = function () {
        console.log("Iniciando ...");
    };
    Rotina.prototype.main = function () {
        console.log("loop");
    };
    Rotina.prototype.start = function () {
        var f1 = function () {
            var m = new Main_1.Main();
            m.start();
            setTimeout(f2, m.frequencia);
        };
        var f2 = function () {
            var m = new Main_1.Main();
            m.start();
            setTimeout(f1, m.frequencia);
        };
        f1();
    };
    return Rotina;
}());
exports.Rotina = Rotina;
