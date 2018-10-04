class Main{
    frequencia = 2500;

     public start(){
        

        console.log('loop ...');
        this.status();
    }

    public status(){
        console.log("Iniciando ...");

        var os = require('os-utils');

        var cpu = 0;

        console.log("CPU:" + cpu);
        
        
        
        var memoria = os.totalmem() - os.freemem();
        console.log("Memoria:" +  memoria);
       this.save(cpu,memoria);


    }

    public save(cpu,memoria){


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

    }
}

export{Main}