let mix = require('laravel-mix');

mix.sass('static_common/scss/product/list.scss', 'static_common/css/list.min.css')
    .sass('static_common/scss/base.scss', 'static_common/css/product/base.min.css')
    .sass('static_common/scss/product/detail.scss', 'static_common/css/product/detail.min.css') 
    .sass('static_common/scss/cart/detail.scss', 'static_common/css/cart/detail.min.css') 
    .sass('static_common/scss/orders/create.scss', 'static_common/css/orders/create.min.css') 
    .sourceMaps(true, 'inline-source-map')
    .options({ processCssUrls: false })
    

