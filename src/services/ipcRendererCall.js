const ipcRenderer = window.require('electron').ipcRenderer;

/**
 * Wrapper for the Electron Render Thread's ipcRenderer send / response
 * mechanism: Wraps the ipcRenderer.send call in a Promise and waits
 * for the response. This function needs a counter-part on the
 * Main thread side (ipcRegisterMainOperation) to work properly, as it
 * makes sure the response channel is named correctly.
 *
 * Usage:
 * <code>
 * ipcRenderCall('my-operation', paramsObject)
 *   .then(response => {})
 *   .catch((error, data) => {});
 * </code>
 *
 * @param {String} operation Name of the operation
 * @param {Object} params operation-specific parameters
 */
function ipcRendererCall(operation, params) {
    params = params || {};
    let endOpIdent = `${operation}-done`,
        responsePromise = new Promise((success, reject) => {
            ipcRenderer.once(endOpIdent, (event, response) => {
                let data = (response && response.data) || null;
                let error = (response && response.error) || null;
                if (error) {
                    reject(error, data);
                } else {
                    success(data);
                }
            });
            ipcRenderer.send(operation, params);
        });

    return responsePromise;
}

export { ipcRendererCall };
