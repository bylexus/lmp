const { app, BrowserWindow } = require('electron');
const walkdir = require('walkdir');
const mime = require('mime');
const NodeId3 = require('node-id3');
const registerMainOperation = require('./src/services/ipcRegisterMainOperation').registerMainOperation;

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let win;

function createWindow() {
    // Create the browser window.
    win = new BrowserWindow({
        show: false,
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            nodeIntegrationInWorker: true,
        },
    });

    // and load the index.html of the app.
    win.loadFile('index.html');

    // Open the DevTools.
    win.webContents.openDevTools();

    win.once('ready-to-show', () => {
        win.show();
    });

    // Emitted when the window is closed.
    win.on('closed', () => {
        // Dereference the window object, usually you would store windows
        // in an array if your app supports multi windows, this is the time
        // when you should delete the corresponding element.
        win = null;
    });
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', createWindow);

// Quit when all windows are closed.
app.on('window-all-closed', app.quit);

registerMainOperation('inspect-dir', (params, success, reject) => {
    let emitter = walkdir(params.dir, { no_return: true });
    let promises = [];
    let found = [];
    emitter.on('file', (filePath, stat) => {
        let type = mime.getType(filePath);
        if (type && type.match(/^audio\//)) {
            let workingPromise = new Promise((iResolve, iReject) => {
                NodeId3.read(filePath, (err, tags) => {
                    if (!err) {
                        console.log('ID3 tags for ', filePath, tags);
                        found.push({
                            file: filePath,
                            type,
                            id3: tags,
                        });
                    }
                    iResolve();
                });
            });
            promises.push(workingPromise);
        }
    });
    emitter.on('end', () => {
        console.log('End walkdir!');
        Promise.all(promises)
            .then(() => {
                success(found);
            })
            .catch(reject);
    });
});

