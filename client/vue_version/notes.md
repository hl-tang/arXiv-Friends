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



## TS

src下创建**shims-vue.d.ts**文件

```
declare module '*.vue';
```

不然 router导入 import Home from "../pages/Home.vue"; 会飘红

https://stackoverflow.com/questions/54839057/vscode-showing-cannot-find-module-ts-error-for-vue-import-while-compiling-doe



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



## 暗黑模式

https://github.com/dishait/vue-dark-switch

```
import { useDark, useToggle } from '@vueuse/core'
const isDark = useDark()
const toggleDark = useToggle(isDark)
```



## i18n

https://vue-i18n.intlify.dev/guide/installation.html



## vue-cookies

https://www.npmjs.com/package/vue-cookies

```
pnpm add vue-cookies
```

main.js里

```
import VueCookies from "vue-cookies";
app.use(VueCookies);
```

使用

```
const username = ref("");
username.value = $cookies.get("username")
```



注意⚠️

```
axios.defaults.withCredentials = true;
```

main.js不加这个axios配置，浏览器不会接受后端发来set的cookie



⚠️注意⚠️

`axios.post("http://127.0.0.1:8000/api/login/"`  浏览器刷新后cookie丢失

`axios.post("http://localhost:8000/api/login/"`  浏览器刷新后cookie还在

即cookie的Domin要是localhost，不懂为什么127.0.0.1丢失了

*axios*.*defaults*.*baseURL* *=* "http://localhost:8000"; 那改成localhost就好了

就是因为node起的服务器地址是localhost:5173,同源的cookie自然好设置。127.0.0.1都跨站了就需要cookie的跨站处理，什么cookie的SameSite

---

本质原因在于cookie的SameSite属性有问题:

this set cookie didn t specify a samesite

https://andrewlock.net/understanding-samesite-cookies/

https://stackoverflow.com/questions/46288437/set-cookies-for-cross-origin-requests



## pinia持久化localStorage

pinia-plugin-persistedstate

https://prazdevs.github.io/pinia-plugin-persistedstate/guide/



## 构思

home就访问 api/recommend

搜索就跳到搜索结果的页面url不再是/了，而且加上query para

在home或searchresult页面点击了paperRow组件后，由于跳到detailpaper页面需要先展示title,authors等信息，所以不能等axios（事实后端只返回摘要，不返回余計的东西了）。**那点击了一个要简化的paperRow之后，应该把这篇论文的id,title,authors等信息存为 状态管理 **以便到了detailpaper页面可以直接展示相关信息。访问/simplify endpoint应该在detailpaper组件进行(页面刷新了之后还能访问api。之前的做法在paperRow里axios发请求，导致已经跳到了detailpaper后刷新页面空白)





## 注意点

topbar `h-[60px]`定长之后，下面的div要`pt-[60px]`设置与topbar高度相同的上边距，不然会被topbar挡住





## 問題点

```html
<p class="font-japanese">会員登録がお済みのお客様</p> <!-- 不知道怎么精细地调日语字体 -->
```

而且Font Weight的设置对日语字体无效



## 难点

用户登录 JWT 权限控制
