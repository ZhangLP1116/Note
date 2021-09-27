> class与内联style都属于attribute所以我们可以使用v-bind处理，只需要通过表达式计算出字符串结果即可，由于class和style的特殊性其结果的字符串过于复杂vue再使用v-bind处理它们时做了增强`表达式结果的类型除了字符串之外，还可以是对象或数组。`
>
> v-bind处理非class、style属性时返回的结果不是字符串对象则不会解析对象内容

### 绑定Html Class

#### 1、表达式结果为对象

vue解析结果：对象的键作为class名，键值决定是否使用该类

##### 示例1

```html
<div v-bind:class="{ active: isActive }"></div>
```

```js
data: {
  isActive: true,
}
```

渲染结果

```html
<div v-bind:class="active"></div>
```

##### 示例2

vue会自动拼接已存在的class属性

```html
<div
  class="static"
  v-bind:class="{ active: isActive, 'text-danger': hasError }"
></div>
```

```js
data: {
  isActive: true,
  hasError: false
}
```

渲染结果

```html
<div class="static active"></div>
```

##### 示例3

使用一个对象统一编写class

```html
<div v-bind:class="classObject"></div>
```

```js
data: {
  classObject: {
    active: true,
    'text-danger': false
  }
}
```

渲染结果

```html
<div class="active"></div>
```

##### 示例4

使用计算属性

```html
<div v-bind:class="classObject"></div>
```

```js
data: {
  isActive: true,
  error: null
},
computed: {
  classObject: function () {
    return {
      active: this.isActive && !this.error,
      'text-danger': this.error && this.error.type === 'fatal'
    }
  }
}
```

渲染结果

```html
<div class="active"></div>
```

#### 2、表达式结果为数组

vue解析结果：每个元素的表达式结果作为类

##### 示例1

```html
<div v-bind:class="[activeClass, errorClass]"></div>
```

```js
data: {
  activeClass: 'active',
  errorClass: 'text-danger'
}
```

渲染结果

```html
<div class="active text-danger"></div>
```

##### 示例2

可以使用三元表达式作为数组元素

```html
<div v-bind:class="[isActive ? activeClass : '', errorClass]"></div>
```

```js
data: {
  activeClass: 'active',
  errorClass: 'text-danger'
}
```

渲染结果

```html
<div class="active text-danger"></div>
```

##### 示例3

可以嵌套对象语法

```html
<div v-bind:class="[{ active: isActive }, errorClass]"></div>
```

```js
data: {
  activeClass: 'active',
  errorClass: 'text-danger'
}
```

```html
<div class="active text-danger"></div>
```

#### 3、作用再组件上

不会覆盖组件上原有的样式，会以附加形式出现

```js
Vue.component('my-component', {
  template: '<p class="foo bar">Hi</p>'
})
```

```html
<my-component class="baz boo"></my-component>
```

渲染结果

```js
<p class="foo bar baz boo">Hi</p>
```

### 绑定内联样式

#### 1、表达式结果为对象

vue解析：对象键作为style键，对象值作为style值

##### 示例1

```html
<div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
```

```js
data: {
  activeColor: 'red',
  fontSize: 30
}
```

渲染结果

```html
<div v-bind:style="color: red; font-size: 30px;"></div>
```

##### 示例2

使用对象统一编写

```html
<div v-bind:style="styleObject"></div>
```

```js
data: {
  styleObject: {
    color: 'red',
    fontSize: '13px'
  }
}
```

渲染结果

```html
<div v-bind:style="color: red; font-size: 30px;"></div>
```

#### 2、表达式结果为数组

vue解析：数组元素必须为对象，将多个对象的结果解析到一起

示例

```html
<div id="app" v-bind:style="[styleObject, fontStyle]"></div>
```

```js
data: {
	styleObject: {
		color: 'red',
	},
	fontStyle:{
		fontSize: '13px',
	}
}
```

渲染结果

```html
<div v-bind:style="color: red; font-size: 30px;"></div>
```

#### 3、自动为style添加前缀

当 `v-bind:style` 使用需要添加[浏览器引擎前缀](https://developer.mozilla.org/zh-CN/docs/Glossary/Vendor_Prefix)的 CSS property 时，如 `transform`，Vue.js 会自动侦测并添加相应的前缀。

#### 4、多重值

从 2.3.0 起你可以为 `style` 绑定中的 property 提供一个包含多个值的数组，常用于提供多个带前缀的值，例如：

```html
<div :style="{ display: ['-webkit-box', '-ms-flexbox', 'flex'] }"></div>
```



