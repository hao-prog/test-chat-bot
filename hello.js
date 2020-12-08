const {spawn} = require('child_process');

const childPython = spawn('python', ['VnCoreNLP/pp.py', 'Le Van Hao']);

childPython.stdout.on('data', (data) => {
    var obj = JSON.parse(`${data}`);
    console.log(obj.nerLabel);
});

childPython.stderr.on('data', (data) => {
    console.error(`${data}`);
});

childPython.on('close', (code) => {
    console.log(`child process exited with code ${code}`)
});