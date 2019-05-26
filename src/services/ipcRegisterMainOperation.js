const ipcMain = require('electron').ipcMain;

/**
 * Wrapper for the Electron ipcMain receive mechanism, instead of
 * using ipcMain.on() / event.reply.
 *
 * It attaches a listener to ipcMain for the given channel
 * (ipcMain.on(operation)), executes the given callback function
 * when the channel is called through ipcRenderer.send(),
 * and response to the event when the given Callback is done.
 *
 * Usage:
 * <code>
 * registerMainOperation('my-operation', (data, success, reject) {
 *     do_long_running_operation(data).then(success).catch(reject);
 * });
 * </code>
 * @param {String} operation Name of the ipc channel to listen to
 * @param {Function(Object, Function, Function)} promiseCallback This
 *   function is called with 3 parameters:
 *     - params: Object with params sent from the Renderer Thread's ipcRenderCall() function
 *     - success: The callback must call this function when its operation is done,
 *            with additional parameters as a response (e.g. success('all-done')).
 *     - reject: In case of an error, the callback must call reject with an error information.
 */
async function registerMainOperation(operation, promiseCallback) {
    let endOpIdent = `${operation}-done`;
    let result = null;
    let response = {
        error: null,
        data: null,
    };

    ipcMain.on('inspect-dir', async (event, params) => {
        let opPromise = new Promise((success, reject) => {
            return promiseCallback(params, success, reject);
        });
        try {
            result = await opPromise;
            response.data = result;
        } catch (e) {
            response.error = String(e);
        } finally {
            event.reply(endOpIdent, response);
            return response;
        }
    });
}

module.exports = { registerMainOperation };
