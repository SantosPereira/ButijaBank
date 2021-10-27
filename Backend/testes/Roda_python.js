let {PythonShell} = require('python-shell');

PythonShell.run('C:/Git/SistemaBancoButija/GUI.py', null, function (err) {
  if (err) throw err;
  console.log('finished');
});
