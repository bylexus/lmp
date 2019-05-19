const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
    mode: process.env.NODE_ENV === 'development' ? 'development' : 'production',
    entry: {
        app: './src/app.js'
    },
    output: {
        path: __dirname,
        filename: '[name].bundle.js'
    },
    resolve: { modules: [path.resolve(__dirname, 'src'), 'node_modules'] },
    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.scss$/,
                use: ['vue-style-loader', 'css-loader', 'sass-loader']
            },
            {
                test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: '[name].[ext]',
                            outputPath: 'resources/fonts/bundled'
                        }
                    }
                ]
            }
        ]
    },
    plugins: [new VueLoaderPlugin()]
};
