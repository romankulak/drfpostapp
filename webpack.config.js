const path = require('path');

module.exports = {
    entry: {
        app: './frontend/index.jsx',
    },
    output: {
        path: path.join(__dirname, '/posts/static/js'),
        publicPath: '/static/js/',
        filename: '[name]/bundle.js',
        chunkFilename: 'chunks/[name].js',
    },
    resolve: {
        extensions: ['.js', '.jsx'],
        modules: [
            './frontend',
            './node_modules',
        ]
    },
    module: {
        rules: [
            {
                enforce: 'pre',
                test: /\.jsx?$/,
                loader: 'eslint-loader',
                options: {
                    quiet: true,
                    failOnError: false,
                    failOnWarning: false,
                    emitError: false,
                    emitWarning: false,
                    configFile: '.eslintrc',
                  }
                
            },
            {
                test: /\.jsx?$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: 'babel-loader',
                    options: { presets: ['react', 'env','stage-0'] }
                }
            },
            {
                test: /\.scss/,
                exclude: /(node_modules|bower_components)/,
                use: ['style-loader', 'css-loader', 'sass-loader']
            }
        ]
    },
    devServer: {
        contentBase: './src',
        publicPath: '/output'
     }
};
