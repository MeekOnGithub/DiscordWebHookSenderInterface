// Application electronjs basique
const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const path = require('path');

let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            devTools: false,
        },
        title: 'Webhook sender remake with ElectronJS',
        autoHideMenuBar: true,
    });

    mainWindow.loadFile('app/index.html');
    mainWindow.webContents.openDevTools();
    mainWindow.on('closed', function() {
        mainWindow = null;
    });
}

// Quand l'application est prête, on crée la fenêtre
app.whenReady().then(createWindow);

// Quitter l'application quand toutes les fenêtres sont fermées
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') { // si n'est pas MacOS: on ne quitte pas l'application car l'utilisateur peut ouvrir une nouvelle fenêtre depuis le dock
        app.quit();
    }
});