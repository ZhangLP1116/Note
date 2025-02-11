# 对接API三方接口

axios异步请求三方接口时会报错跨域

解决方法

- 本地开发使用vue代理解决跨域，部署后使用nginx反向代理

- 不使用axios进行异步请求，使用jsonp代替

  > 原理：动态生成一个JavaScript标签，其src由接口url、请求参数、callback函数名拼接而成，利用js标签没有跨域限制的特性实现跨域请求。

```
安装依赖
npm i vue-jsonp -S
```

```js
import { jsonp } from 'vue-jsonp'

      mounted() {
        const that = this
        // jsonp调用腾讯地图接口
        jsonp('https://apis.map.qq.com/ws/place/v1/suggestion', {
          output: 'jsonp',
          keyword: '北京',
          page_index: 2,
          page_size: 10,
          region: '中国',
          key: 'XIRBZ-TWKWD-AAX4Q-HEKFK-JGPIO-YNBTJ'
        })
          .then(function (response) {
            const arr = response.data
            arr.forEach(item => {
              item.value = item.title
            })
            that.restaurants = arr
            console.log(that.restaurants, 'that.restaurants')
          })
          .catch(function (error) {
            console.log(error)
          })
      }
```

