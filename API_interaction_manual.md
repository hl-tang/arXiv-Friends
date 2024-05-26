API文档: http://127.0.0.1:8000/api/docs
(启动django-ninja)





### 实现细节

home就访问 `api/recommend` 获取recommendPapers的list

搜索就跳到搜索结果的页面url不再是/了，而且加上query para，获取searchedPapers的list


PaperRow作为子组件被Home和SearchResult引用，Home和SearchResult通过axios从后端获得数据，通过props传给PaperRow

在PaperRow.vue里

```ts
const props = defineProps({
  paper_id: String,
  title_en: String,
  title_ja: String,
  authors: Array,
  published: String,
  content_en: String,
  pdf_url: String,
  categories: Array
})
const { paper_id, title_en, title_ja, authors, published, content_en, pdf_url, categories } = toRefs(props);
```

---

**关于watch**

跳到搜索结果页面/search是由topbar的搜索栏里回车或点击按钮触发的

发axios访问/api/arxiv是在SearchResult做的

尽管尝试把*searchContent*做成全局的状态管理，但已经在搜索页面后在点击topbar搜索栏按钮企图跳转新url后触发axios但似乎并不会做页面跳转。(可能是因为已经在/search了，只是换了个query para，就没有跳转进而没有访问/api/arxiv)

于是把发axios包装为一个函数，使用***watch***来监听route.query.search_content这个query para，一旦变化就触发访问后端的函数。





然后点击了PaperRow跳到detailpaper页面。

由于跳到detailpaper页面需要先展示title,authors等信息，所以不能等axios（事实后端只返回摘要，不返回余計的东西了）。**那点击了一个要简化的paperRow之后，应该把这篇论文的id,title,authors等信息存为 状态管理 **以便到了detailpaper页面可以直接展示相关信息。访问/simplify endpoint应该在detailpaper组件进行(页面刷新了之后还能访问api。之前的做法在paperRow里axios发请求，导致已经跳到了detailpaper后刷新页面空白)





**状态管理 + 持久化localStorage**

除了刚才提到的choosedPaperInfo要保存点击的PaperRow的paper_id,authors等信息，以便于跳转到了detailpaper页面后利用这些信息来发请求，以及展示不需要访问后端的数据。

还需要记录isLoggedIn，没有登录的用户的topbar就不会显示avatar也不可能进入到mypage了。给@login_required的api发请求时，也可以根据isLoggedIn前端直接处理扔个alert.



注意我导入了pinia-plugin-persistedstate来把状态管理存到localStorage，避免一个页面改了某状态管理的数据，另一个页面读到的是定义pinia的初值，导致状态管理在某页面的修改丢失。





**收藏**

home或searchresult因为不知道用户到底收藏了没有，前端先统一显示灰色的星星(`const isLiked = ref(false);`)。点击收藏按钮后，post访问/like/这个接口。

然后后端判断是否已经收藏过了(userlikepaper表里有没有这条记录)，是的话就返回msg说已经收藏了，然后前端把星星变黄。如果确实没收藏过，那就数据库里加一条记录，然后前端把星星变黄。

取消收藏：前端对着一个黄色星星点击后，delete方法访问/like/接口，把数据库记录删掉。星星变灰。

用户mypage前端统一显示黄色的星星(`const isLiked = ref(true);`)，因为都是肯定已经收藏了的。



**关于emit**

然后碰到的一个问题就是，我在子组件PaperRow点击了收藏按钮想要取消收藏，之后怎么触发某个写在MyPage.vue里的handleClickFavorites函数用以重新获取likedPapers(取消收藏的删掉)和收藏数统计来重新渲染呢？

子组件里defineEmits定义事件,子组件PaperRow `axios.delete('/api/like/)`后`emit('cancel-like-at-my-page');`来通知父组件。父组件MyPAge.vue里`<PaperRow @cancel-like-at-my-page="renewFavorites" />`收到emit便会触发renewFavorites函数,访问后端`axios.get('/api/like/')`重新渲染页面.

**但子组件emit记得写在axios.then里面** *保证后端数据库写入返回了再hit get endpoint*

起初我还在父组件MyPage的触发函数里setTimeout设置0.5s延迟访问，想到PaperRow那里delete请求数据库还没做完，导致这里显示有问题(*可能数据库还没写入，就去访问api了，而这时的返回结果就不对了因为数据库还没更新*)。

后来发现是emit写在了axios的外面，导致异步先去get访问api了。就和loading的问题一样。


