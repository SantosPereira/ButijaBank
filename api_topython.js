let {PythonShell} = require('python-shell');

/*
        APENAS RODA O SCRIPT PYTHON

PythonShell.run('GUI.py', null, function (err) {
  if (err) throw err;
  console.log('finished');
});*/




/*
      ENVIA INFORMAÇÕES PRO PYTHON
*/
/*
var dados = {
  'msg':'Funciona',
  'outro dado':'vazio'
}*/

let options = {
  mode: 'text',
  pythonOptions: ['-u'], // get print results in real-time
  //args: [dados['msg']]
  args: ['FUNCIONA!!!']
};

PythonShell.run('GUI.py', options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log('results: %j', results);
});





/*
let pyshell = new PythonShell('GUI.py');

// sends a message to the Python script via stdin
pyshell.send('hello');

pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  console.log(message);
});

// end the input stream and allow the process to exit
pyshell.end(function (err,code,signal) {
  if (err) throw err;
  console.log('The exit code was: ' + code);
  console.log('The exit signal was: ' + signal);
  console.log('finished');
});*/