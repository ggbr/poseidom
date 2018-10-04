import {Main} from "./Main";
class Rotina{

    local:any;
    
    public setup(){
       console.log("Iniciando ...");
    }

    public main(){
        console.log("loop")
    }

    public start(){

        var f1 = function(){
            var m = new  Main();
            m.start();
            setTimeout(f2, m.frequencia);

        }


        var f2 = function(){
            var m = new  Main();
            m.start();
            setTimeout(f1, m.frequencia);
            
        }

        f1();
        
    }
}
export {Rotina}