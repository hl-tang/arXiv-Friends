## 初期化

vite pnpm创建项目



### 删掉没用的东西

`src/components`下的`HelloWorld.vue` 删掉

`App.vue`里面东西删光

`style.css`里面东西删光



### 配置router

导入`vue-router`

```
pnpm add vue-router@4
```



`App.vue`写入

```vue
<template>
  <router-view />
</template>
```



src/下建个pages目录放page(以前的习惯叫views)

src/下建个router目录，下面创建index.js定义路由

pages下创个Play.vue，配好router，随便在里面尝试 (最后.gitignore里加上`/src/pages/Play.vue`)



参考以前做的项目，修改main.js (导入vue-router)，将路由应用到跟实例上 (别忘了`import router from "./router";`)



### Tailwind CSS

参考 https://tailwindcss.com/docs/guides/vite#vue

```
pnpm add -D tailwindcss postcss autoprefixer
```



### Vuetify

```
pnpm i vuetify
```



### 关于Icon

https://www.npmjs.com/package/vue-material-design-icons



## 注意点

topbar `h-[60px]`定长之后，下面的div要`pt-[60px]`设置与topbar高度相同的上边距，不然会被topbar挡住



## 問題点

```html
<p class="font-japanese">会員登録がお済みのお客様</p> <!-- 不知道怎么精细地调日语字体 -->
```

而且Font Weight的设置对日语字体无效



## 难点

用户登录 JWT 权限控制
